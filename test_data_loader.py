import matplotlib.pyplot as plt
from data_loader import get_random_images, load_images

# Set the path to your data directory
data_dir = './data'

# Get random image tuples
positive_image_tuple, negative_image_tuples = get_random_images(data_dir, num_negative=5)

# Load the images
image_tuples = load_images([positive_image_tuple] + negative_image_tuples)
images = [img for img, emotion in image_tuples]

# Display the images
fig, axes = plt.subplots(1, 6, figsize=(15, 5))
for ax, img in zip(axes, images):
    ax.imshow(img)
    ax.axis('off')
plt.show()
