import matplotlib.pyplot as plt
# Sources used W3 School.
def show_images(original, compressed, upscaled):
    plt.figure(figsize=(12,4))

    plt.subplot(1,3,1)
    plt.title("Original")
    plt.imshow(original)
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.title("Compressed (200x120)")
    plt.imshow(compressed)
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.title("Upscaled")
    plt.imshow(upscaled)
    plt.axis("off")

    plt.show()
