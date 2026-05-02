import cv2
import numpy as np
import pydobot

last_print = 0

def detect_squares(frame):
    results = []

    img = frame.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11, 2
    )

    # morfologie (lepší kontury)
    kernel = np.ones((3,3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detected_centers = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 1000:
            continue

        rect = cv2.minAreaRect(contour)
        (cx, cy), (w, h), angle = rect

        if w == 0 or h == 0:
            continue

        ratio = w / h if w > h else h / w

        if ratio < 1.2:
            cx, cy = int(cx), int(cy)

            # odstranění duplicit
            duplicate = False
            for (px, py) in detected_centers:
                dist = np.sqrt((cx - px)**2 + (cy - py)**2)
                if dist < 50:
                    duplicate = True
                    break

            if duplicate:
                continue

            detected_centers.append((cx, cy))

            # 🎨 barva ve středu (BGR)
            b, g, r = img[cy, cx]

            # 🟥🟩🟦 klasifikace barvy
            if r > g and r > b:
                color = "red"
            elif g > r and g > b:
                color = "green"
            elif b > r and b > g:
                color = "blue"
            else:
                color = "unknown"

            results.append({
                "position": (cx, cy),
                "color": color,
                "rgb": (int(r), int(g), int(b))
            })

    return results, thresh

# pripojeni robota

port = "COM3"

try:
    device = pydobot.Dobot(port=port, verbose=True)
except Exception as e:
    print(f"Chyba pripojenia: {e}")
    exit()

# Kalibrace a start

(home_x, home_y, home_z, home_r, *_) = device.pose()
print(f"Domovská poloha nastavená na: {home_x}, {home_y}, {home_z}")
home_r = -120

 # Zistenie štartovacej pozície
(x0, y0, z0, r0, *_ ) = device.pose()
print(f"Robot pripravený na súradniciach: {x0}, {y0}, {z0}")

# Nulova pozice kamery
pos_0_x = 172
pos_0_y = -94

# Limity ramena
X_MIN, X_MAX = 150, 300
Y_MIN, Y_MAX = -150, 150

# Pohyb nad plochu
device.move_to(220, 0, 120, home_r, wait=True)

#Vypnutí přísavky
device._set_end_effector_suction_cup(False)

#nacteni kamery
cap = cv2.VideoCapture(0)

#pocet kostek v sloupu
kostek_red = 0
kostek_blue = 0

while True:
    #nacteni fotky z kamery
    ret, frame = cap.read()
    if not ret:
        break
    #otoceni fotky
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    #najiti kostek pres funkci
    squares, mono = detect_squares(frame)

    h, w = frame.shape[:2]
    cx, cy = w // 2, h // 2

    

    # vykreslení výsledků
    
    for sq in squares:
        
        x, y = sq["position"]
        color = sq["color"]
        print(sq["position"])

        #oznaceni kostky v obrazu
        cv2.circle(frame, (x, y), 5, (0, 255, 255), -1)
        cv2.putText(frame, color, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (255, 255, 255), 2)
        
        #sebrani kostky z plochy 
        device.move_to(pos_0_x + (y * 179/480),pos_0_y + (x * 240/640), -40, 0, wait=True)
        device._set_end_effector_suction_cup(True)
        device.move_to(pos_0_x + (y * 179/480),pos_0_y + (x * 240/640), 0, 0, wait=True)
        device.move_to(175, 190, 120, 0, wait=True)

        print(color)
        #umisteni do sloupu
        if color == "red":
            device.move_to(175, 220, -40 + (kostek_red * 27 ), 0, wait=True)
            kostek_red = kostek_red + 1
            device._set_end_effector_suction_cup(False)
            device.move_to(175, 220, -40 + (kostek_red * 27 ) + 20, 0, wait=True)
        #umisteni do sloupu
        elif color == "blue":
            device.move_to(175, 160, -40 + (kostek_blue * 27 ), 0, wait=True)
            kostek_blue = kostek_blue + 1
            device._set_end_effector_suction_cup(False)
            device.move_to(175, 160, -40 + (kostek_blue * 27 ) + 20, 0, wait=True)         
        #presun do horni polohy
        device.move_to(220, 0, 120, home_r, wait=True)

   #vykresleni obrazů z kamery
    cv2.imshow("Normal Feed", frame)
    cv2.imshow("Monochrome", mono)
    #exit key ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break
#vypsani poctu kostek ve vezich
print("vyska red veze = ", kostek_red)
print("vyska blue veze = ", kostek_blue)
#x=172,5 y=94
cap.release()
cv2.destroyAllWindows()