from PIL import Image

def convert_to_grayscale_and_save(input_path, output_path):
    # Open an image file
    img = Image.open(input_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Save the grayscale image
    img_gray.save(output_path)

# Replace 'input_image.jpg' with the path to your input image file
# Replace 'output_image_gray.jpg' with the desired output path for the grayscale image
input_path = 'test.jpeg'
output_path = 'output_image_gray.jpg'

# Call the function to convert to grayscale and save the image
convert_to_grayscale_and_save(input_path, output_path)
