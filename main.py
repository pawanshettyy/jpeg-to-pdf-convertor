from PIL import Image
import os

def jpeg_to_pdf(input_folder, output_pdf):
    image_list = []
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.jpeg') or file_name.endswith('.jpg'):
            img_path = os.path.join(input_folder, file_name)
            img = Image.open(img_path).convert('RGB')
            image_list.append(img)
    
    if image_list:
        image_list[0].save(output_pdf, save_all=True, append_images=image_list[1:])
        print(f"PDF created successfully: {output_pdf}")
    else:
        print("No JPEG images found in the folder.")

# Example usage
input_folder = 'path/to/jpeg/folder'
output_pdf = 'output.pdf'
jpeg_to_pdf(input_folder, output_pdf)
