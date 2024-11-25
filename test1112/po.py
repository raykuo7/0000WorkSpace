import cv2
import pandas as pd
import glob

# Initialize an empty list to store the data
data = []

# Callback function to record points
def select_point(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Append the image path and selected coordinates
        data.append((param, x, y))
        print(f"Point selected at: x={x}, y={y}")

# Load images from a directory (replace 'your_image_folder_path' with your folder path)
image_files = glob.glob('./pic/*.jpg')  # Adjust file extension as needed

# Process each image
for img_path in image_files:
    # Read and display the image
    img = cv2.imread(img_path)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", select_point, img_path)
    
    print("Click on the image to select a point, press 'n' for next image.")
    key = cv2.waitKey(0)
    if key == ord('n'):
        continue
    elif key == ord('q'):  # Optional: press 'q' to quit early
        break

cv2.destroyAllWindows()

# Save the data to a CSV file
df = pd.DataFrame(data, columns=["image_path", "x", "y"])
df.to_csv("selected_points.csv", index=False)
print("Data saved to selected_points.csv")