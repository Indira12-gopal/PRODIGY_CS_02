from PIL import Image

def encrypt_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        pixels = img.load()

        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # swapping red and blue channels
                encrypted_pixel = (b, g, r)

                pixels[i, j] = encrypted_pixel

        img.save(output_path)
        print("Image encrypted successfully! Saved at:", output_path)
    except Exception as e:
        print("Error during encryption:", e)

def decrypt_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        pixels = img.load()

        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # swapping red and blue channels back
                decrypted_pixel = (b, g, r)

                pixels[i, j] = decrypted_pixel

        img.save(output_path)
        print("Image decrypted successfully! Saved at:", output_path)
    except Exception as e:
        print("Error during decryption:", e)

# Get user input for paths
input_image =input("Enter input image path: ")
encrypted_image =input("Encrypted img will be saved at and as: ")
decrypted_image =input("Decrypted img will be saved at and as: ")

# Encrypt the image
encrypt_image(input_image, encrypted_image)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image)
