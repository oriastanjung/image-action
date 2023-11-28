from PIL import Image

def sobel_operator(image_path, output_path):
    # Open an image file
    img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Get the image size
    width, height = img_gray.size

    # Sobel operator kernels
    sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    # Initialize an array for the Sobel result
    sobel_result = [[0] * width for _ in range(height)]

    # Apply Sobel operator to each pixel
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            pixel_x = sum(img_gray.getpixel((min(width-1, max(0, x + i)), min(height-1, max(0, y + j)))) * sobel_x[i][j] for i in range(3) for j in range(3))
            pixel_y = sum(img_gray.getpixel((min(width-1, max(0, x + i)), min(height-1, max(0, y + j)))) * sobel_y[i][j] for i in range(3) for j in range(3))
            sobel_result[y][x] = int((pixel_x**2 + pixel_y**2)**0.5)

    # Create a new image from the Sobel result
    sobel_image = Image.new('L', (width, height))
    sobel_image.putdata([pixel for row in sobel_result for pixel in row])

    # Save the Sobel-filtered image
    sobel_image.save(output_path)

# Replace 'your_image.jpg' with the path to your image file
image_path = 'output_image_gray_resized.jpg'
# Replace 'output_sobel_image.jpg' with the desired output path for the Sobel-filtered image
output_path = 'output_sobel_image.jpg'
sobel_operator(image_path, output_path)
