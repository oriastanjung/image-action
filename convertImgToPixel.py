from PIL import Image

def get_specific_pixels(image_path, coordinates):
    # Open an image file
    img = Image.open(image_path)

    # Get the pixel values as a 2D list (matrix)
    pixel_matrix = list(img.getdata())

    # Reshape the matrix to match the image size
    width, height = img.size
    pixel_matrix = [pixel_matrix[i * width:(i + 1) * width] for i in range(height)]

    # Extract specific pixels based on the provided coordinates
    specific_pixels = [(row, col, pixel_matrix[row][col]) for row, col in coordinates]

    return specific_pixels

# Replace 'your_image.jpg' with the path to your image file
image_path = 'test.jpeg'

# Specify the coordinates of the pixels you want to extract
pixel_coordinates = [
    (0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(0, 255),
    (1, 0),(1, 1),(1, 2),(1, 3),(1, 4),(1, 255),
    (2, 0),(2, 1),(2, 2),(2, 3),(2, 4),(2, 255),
    (3, 0),(3, 1),(3, 2),(3, 3),(3, 4),(3, 255),
    (4, 0),(4, 1),(4, 2),(4, 3),(4, 4),(4, 255),
    (255, 0),(255, 1),(255, 2),(255, 3),(255, 4),(255, 255),
                     ]

# Get and print the specific pixels with grayscale values
specific_pixels = get_specific_pixels(image_path, pixel_coordinates)
for pixel in specific_pixels:
    # Extract the grayscale value from the RGB tuple with two decimal places
    grayscale_value = round(sum(pixel[2]) / len(pixel[2]), 2) if isinstance(pixel[2], tuple) else round(pixel[2], 2)
    print(f"Pixel at ({pixel[0]}, {pixel[1]}): {pixel[2]} grayscale : {grayscale_value}")
