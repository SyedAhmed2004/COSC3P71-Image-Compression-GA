import cv2
from compression import GeneticCompressor
from visualize import show_images

image_files = ["input1.jpg", "input2.jpg", "input3.jpg"]

for file in image_files:
    original = cv2.imread(file)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

    compressor = GeneticCompressor(original, pop_size=20, generations=30)
    compressed = compressor.run()

    upscaled = cv2.resize(compressed, (original.shape[1], original.shape[0]))

    show_images(original, compressed, upscaled)
