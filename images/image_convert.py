import os
from PIL import Image

# 👉 Set your folder path here
folder_path = r"C:\Users\JANMEJAY\Downloads\My_Lab_Website\New\images"

# Supported extensions
valid_extensions = ('.png', '.PNG', '.jpeg', '.JPEG', '.jpg', '.JPG')

for filename in os.listdir(folder_path):
    if filename.endswith(valid_extensions):
        file_path = os.path.join(folder_path, filename)
        
        try:
            with Image.open(file_path) as img:
                
                # Convert RGBA (PNG with transparency) → RGB
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new("RGB", img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    img = background
                else:
                    img = img.convert("RGB")
                
                # Create new filename
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_file_path = os.path.join(folder_path, new_filename)
                
                # Save as JPG
                img.save(new_file_path, "JPEG", quality=95)
                
                print(f"Converted: {filename} → {new_filename}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("\n✅ Conversion complete!")