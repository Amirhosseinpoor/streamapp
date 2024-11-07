import cv2

# Open the input video file
input_path = "input_video.mp4"  # Replace with your video file path
cap = cv2.VideoCapture(input_path)

# Check if the video opened successfully


# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object to save the output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("output_video_with_large_rectangle.avi", fourcc, fps, (frame_width, frame_height))

# Define rectangle properties
top_left = (30, 30)  # Adjusted top-left corner for larger rectangle
bottom_right = (300, 300)  # Adjusted bottom-right corner for larger rectangle
rectangle_color = (0, 255, 0)  # Rectangle color (green in BGR)
thickness = 4  # Increased thickness for a bolder rectangle

# Define text properties
name = "Amirrrrrr"  # Replace with your name
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.0  # Font scale for larger text
text_color = (255, 255, 255)  # Text color (white in BGR)
text_thickness = 2  # Thickness for larger text

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Draw the larger rectangle on each frame
    cv2.rectangle(frame, top_left, bottom_right, rectangle_color, thickness)

    # Calculate text position (bottom of the larger rectangle)
    text_position = (top_left[0], bottom_right[1] + 40)  # Adjust position for larger rectangle and text

    # Add the name text below the rectangle
    cv2.putText(frame, name, text_position, font, font_scale, text_color, text_thickness, cv2.LINE_AA)

    # Write the modified frame to the output video
    output.write(frame)

# Release resources
cap.release()
output.release()


