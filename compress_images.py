from PIL import Image
import os

# Path to your Images folder
image_folder = "Images"

# Target quality (lower = more compression, 85 is a good balance)
quality = 85

for filename in os.listdir(image_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        filepath = os.path.join(image_folder, filename)

        try:
            img = Image.open(filepath)
            # Convert PNGs to JPEG to reduce size (optional)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.save(filepath, "JPEG", optimize=True, quality=quality)
            print(f"Compressed and saved: {filename}")
        except Exception as e:
            print(f"Error compressing {filename}: {e}")

print("All images compressed successfully!")

