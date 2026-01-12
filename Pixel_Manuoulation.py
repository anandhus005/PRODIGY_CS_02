from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key=123):
    img = Image.open(input_path).convert("RGB")
    data = np.array(img)

    flat = data.reshape(-1, 3)

    # Shuffle pixels using key
    np.random.seed(key)
    indices = np.arange(flat.shape[0])
    np.random.shuffle(indices)
    shuffled = flat[indices]

    # XOR encryption
    encrypted = shuffled ^ key

    encrypted_img = encrypted.reshape(data.shape)
    Image.fromarray(encrypted_img.astype(np.uint8)).save(output_path)
    print("✅ Encryption complete:", output_path)


def decrypt_image(input_path, output_path, key=123):
    img = Image.open(input_path).convert("RGB")
    data = np.array(img)

    flat = data.reshape(-1, 3)

    # XOR decrypt first (same key)
    unxor = flat ^ key

    # Unshuffle pixels using same key
    np.random.seed(key)
    indices = np.arange(unxor.shape[0])
    np.random.shuffle(indices)

    original = np.zeros_like(unxor)
    original[indices] = unxor

    decrypted_img = original.reshape(data.shape)
    Image.fromarray(decrypted_img.astype(np.uint8)).save(output_path)
    print("✅ Decryption complete:", output_path)


if __name__ == "__main__":
    print("=== IMAGE ENCRYPTION TOOL ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Enter your choice (1/2): ").strip()
    key = int(input("Enter secret key (number): "))

    if choice == "1":
        input_img = input("Enter input image path: ")
        output_img = input("Enter output encrypted image path: ")
        encrypt_image(input_img, output_img, key)

    elif choice == "2":
        input_img = input("Enter encrypted image path: ")
        output_img = input("Enter output decrypted image path: ")
        decrypt_image(input_img, output_img, key)

    else:
        print("❌ Invalid choice!")