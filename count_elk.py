import cv2
import numpy as np

# Load the image
img = cv2.imread('Elk-Count.jpg')
if img is None:
    print("Error: Could not load image")
    exit()

# Create a copy for annotation
annotated = img.copy()

# Convert to HSV color space for better color segmentation
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range for brown/tan colors (elk)
# Elk appear as brown/tan against white snow
# HSV ranges: Hue (0-180), Saturation (0-255), Value (0-255)
lower_brown = np.array([5, 30, 80])  # Lower bound for brown/tan
upper_brown = np.array([30, 255, 255])  # Upper bound for brown/tan

# Create mask for elk colors
mask = cv2.inRange(hsv, lower_brown, upper_brown)

# Apply morphological operations to clean up the mask
kernel = np.ones((5, 5), np.uint8)

# Remove noise
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

# Fill gaps
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

# Find contours (potential elk)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours by size to get individual elk
min_area = 200  # Minimum area to be considered an elk
max_area = 15000  # Maximum area for a single elk

elk_count = 0

for contour in contours:
    area = cv2.contourArea(contour)
    
    # Filter by area
    if min_area < area < max_area:
        elk_count += 1
        
        # Draw bounding box around each detected elk
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(annotated, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Draw contour
        cv2.drawContours(annotated, [contour], -1, (0, 255, 255), 2)
        
        # Add number label
        cv2.putText(annotated, str(elk_count), (x, y-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Add count text to image
text = f'Elk Count: {elk_count}'
cv2.putText(annotated, text, (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)

# Save the results
cv2.imwrite('elk_mask.jpg', mask)
cv2.imwrite('elk_annotated.jpg', annotated)

print(f"\n{'='*50}")
print(f"  ELK COUNT: {elk_count}")
print(f"{'='*50}\n")
print(f"Annotated image saved as: elk_annotated.jpg")
print(f"Mask image saved as: elk_mask.jpg")
