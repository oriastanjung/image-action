from PIL import Image

def resize_and_convert_to_grayscale_and_save(input_path, output_path, target_size=(256, 256)):
    # Open an image file
    img = Image.open(input_path)

    # Resize the image to the target size
    img_resized = img.resize(target_size)

    # Convert the resized image to grayscale
    img_gray = img_resized.convert('L')

    # Save the grayscale image
    img_gray.save(output_path)

# Replace 'input_image.jpg' with the path to your input image file
# Replace 'output_image_gray_resized.jpg' with the desired output path for the grayscale and resized image
input_path = 'test.jpeg'
output_path = 'output_image_gray_resized.jpg'

# Call the function to resize, convert to grayscale, and save the image
resize_and_convert_to_grayscale_and_save(input_path, output_path)
