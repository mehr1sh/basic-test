# file: smile.py

from PIL import Image, ImageDraw

# Create a blank image (RGB) with white background
img = Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(img)

# Draw face (yellow circle)
draw.ellipse((20, 20, 180, 180), fill="yellow", outline="black")

# Draw eyes (black circles)
draw.ellipse((60, 60, 90, 90), fill="black")  # left eye
draw.ellipse((110, 60, 140, 90), fill="black")  # right eye

# Draw smile (arc)
draw.arc((50, 80, 150, 150), start=0, end=180, fill="black", width=3)

# Save the image
img.save("smile.png")

print("Smiley saved as smile.png!")
