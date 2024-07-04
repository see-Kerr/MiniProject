from PIL import Image

def select_portion(image_path, left, top, right, bottom, output_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Define the coordinates for the portion to be selected
        box = (left, top, right, bottom)
        # Crop the image using the defined box
        cropped_image = img.crop(box)
        # Save the cropped image
        cropped_image.save(output_path)
        print(f'Cropped image saved to {output_path}')

# Path to save the cropped image
left = 650  # x-coordinate of the left side of the box
top = 20  # y-coordinate of the top side of the box
right = 900  # x-coordinate of the right side of the box
bottom = 330  # y-coordinate of the bottom side of the box

image_path = "C:\\Users\\piyus\\OneDrive\\Desktop\\MiniProject\\database\\alphabets_config\\alphabets.jpg"
output_path = "C:\\Users\\piyus\\OneDrive\\Desktop\\MiniProject\\database\\alphabets_config\\c.jpg"
select_portion(image_path, left, top, right, bottom, output_path)
