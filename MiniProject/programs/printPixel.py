import tkinter as tk
import getPixel
import coordsData
import numpy as np

def draw_coordinates(canvas, coordinates, sx=1, sy=1):
    # Draw a single pixel at each coordinate using create_line
    coordinates = coordinates*np.array([sx,sy])
    for (x, y) in coordinates:
        canvas.create_line(x-1, y, x, y, fill='black')

def main(coordinates):
    # Create the main window
    root = tk.Tk()
    root.title("Black Pixel Coordinates")

    # Create a canvas widget
    canvas = tk.Canvas(root, width=500, height=500, bg='white')
    canvas.pack()

    # Draw the coordinates on the canvas
    draw_coordinates(canvas, coordinates,0.3,0.3)

    # Start the Tkinter main loop
    root.mainloop()

# Example list of coordinates
image_path = "C:\\Users\\piyus\\OneDrive\\Desktop\\MiniProject\\database\\alphabets_config\\alphabets.jpg"  # Path to your input image
left = 50  # x-coordinate of the left side of the box
top = 50  # y-coordinate of the top side of the box
right = 300  # x-coordinate of the right side of the box
bottom = 330  # y-coordinate of the bottom side of the box

coordinates = coordsData.getData(image_path)
print((coordinates))

main(coordinates[4])
