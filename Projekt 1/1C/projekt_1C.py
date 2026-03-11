import math
from svgpathtools import svg2paths
import pydobot

# -----------------------------
# připojení robota
# -----------------------------

port = "COM3"

try:
    device = pydobot.Dobot(port=port, verbose=True)
except Exception as e:
    print("Dobot connection failed:", e)
    exit()

# -----------------------------
# bezpečný pohyb
# -----------------------------

def safe_move(x, y, z, r):
    try:
        device.move_to(x, y, z, r, wait=True)
    except:
        print("Move failed, retrying...")
        try:
            device.move_to(x, y, z, r, wait=True)
        except:
            print("Move skipped")

# -----------------------------
# domovská pozice
# -----------------------------

(home_x, home_y, home_z, home_r, *_) = device.pose()
print("Home position:", home_x, home_y, home_z)

try:

    # -----------------------------
    # aktuální pozice
    # -----------------------------

    (x0, y0, z0, r0, *_ ) = device.pose()
    print("Robot position:", x0, y0, z0)

    # -----------------------------
    # parametry kreslení
    # -----------------------------

    DRAW_SIZE = 60
    POINTS = 40   # méně bodů = rychlejší

    z_up = z0 - 20
    z_draw = z0 - 55

    # pracovní prostor Dobota
    X_MIN = 150
    X_MAX = 300
    Y_MIN = -150
    Y_MAX = 150

    # -----------------------------
    # načtení SVG
    # -----------------------------

    paths, attributes = svg2paths("camera-svgrepo-com.svg")

    # -----------------------------
    # zjištění velikosti SVG
    # -----------------------------

    min_x = 1e9
    max_x = -1e9
    min_y = 1e9
    max_y = -1e9

    for path in paths:
        for i in range(POINTS):
            p = path.point(i/POINTS)

            x = p.real
            y = p.imag

            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

    svg_width = max_x - min_x
    svg_height = max_y - min_y

    scale = DRAW_SIZE / max(svg_width, svg_height)

    print("SVG size:", svg_width, svg_height)
    print("Scale:", scale)

    # -----------------------------
    # kreslení
    # -----------------------------

    for path in paths:

        points = []

        for i in range(POINTS+1):

            t = i / POINTS
            p = path.point(t)

            x = (p.real - min_x) * scale
            y = (p.imag - min_y) * scale

            xr = x0 + x - DRAW_SIZE/2
            yr = y0 + y - DRAW_SIZE/2

            # kontrola pracovního prostoru
            if xr < X_MIN or xr > X_MAX:
                continue

            if yr < Y_MIN or yr > Y_MAX:
                continue

            points.append((xr, yr))

        if len(points) == 0:
            continue

        # přesun nad start
        safe_move(points[0][0], points[0][1], z_up, r0)

        # pero dolů
        safe_move(points[0][0], points[0][1], z_draw, r0)

        # kreslení
        for x, y in points:
            safe_move(x, y, z_draw, r0)

        # pero nahoru
        safe_move(points[-1][0], points[-1][1], z_up, r0)

finally:

    # -----------------------------
    # návrat domů
    # -----------------------------

    print("Returning to home position...")
    safe_move(home_x, home_y, home_z, home_r)

    device.close()

    print("Hotovo")