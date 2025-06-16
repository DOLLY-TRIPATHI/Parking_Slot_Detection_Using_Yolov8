import cv2
import numpy as np
import json

img = cv2.imread(r"D:\Minor project\Car Traffic 2\frame.png")
clone = img.copy()

parking_spots = []
current_points = []

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        current_points.append((x, y))
        print(f"Point added: ({x}, {y})")

cv2.namedWindow("Define Parking Spots")
cv2.setMouseCallback("Define Parking Spots", mouse_callback)

while True:
    temp_img = clone.copy()

    # Draw current polygon
    if len(current_points) > 1:
        cv2.polylines(temp_img, [np.array(current_points)], False, (0, 255, 0), 2)

    # Draw completed polygons
    for spot in parking_spots:
        cv2.polylines(temp_img, [np.array(spot)], True, (0, 0, 255), 2)

    cv2.imshow("Define Parking Spots", temp_img)

    key = cv2.waitKey(1) & 0xFF

    if key == 13:  # ENTER key to finish a polygon
        if len(current_points) >= 3:
            parking_spots.append(current_points.copy())
            print(f"Polygon saved: {current_points}")
        current_points = []

    elif key == ord("z"):  # undo last point
        if current_points:
            current_points.pop()
            print("Last point removed.")

    elif key == ord("q"):  # Quit and save
        break

cv2.destroyAllWindows()

with open("parking_spotsf.json", "w") as f:
    json.dump(parking_spots, f, indent=2)

print("Saved parking spot coordinates to parking_spots.json")
