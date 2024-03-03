import os
import random
from typing import List, Tuple
from PIL import Image

def list_image_files(directory: str) -> List[str]:
    """
    List all image files in a given directory.

    :param directory: Path to the directory containing image files.
    :return: List of file paths to the images.
    """
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.jpg')]

def get_random_images(data_dir: str, num_negative: int) -> Tuple[Tuple[str, str], List[Tuple[str, str]]]:
    """
    Get file paths for one random positive emotion image and a list of
    random negative emotion images, along with their emotions.

    :param data_dir: Root directory containing emotion subdirectories.
    :param num_negative: Number of negative images to select.
    :return: Tuple containing a tuple of the positive image path and its emotion, and a list of tuples of negative image paths and their emotions.
    """
    # Define the subdirectories for positive and negative emotions
    positive_emotion = 'happy'
    positive_dir = os.path.join(data_dir, positive_emotion)
    negative_emotions = ['angry', 'disgust', 'fear', 'sad', 'surprise', 'neutral']
    
    # List image files in the positive directory and randomly select one
    positive_images = list_image_files(positive_dir)
    positive_image = random.choice(positive_images)
    positive_tuple = (positive_image, positive_emotion)
    
    # List image files in the negative directories and randomly select
    negative_tuples = []
    for emotion in negative_emotions:
        neg_dir = os.path.join(data_dir, emotion)
        neg_images = list_image_files(neg_dir)
        selected_negatives = random.sample(neg_images, num_negative // len(negative_emotions))
        negative_tuples.extend([(img, emotion) for img in selected_negatives])
    
    # If we need more negative images due to rounding, add them from a random emotion
    while len(negative_tuples) < num_negative:
        extra_emotion = random.choice(negative_emotions)
        extra_dir = os.path.join(data_dir, extra_emotion)
        extra_images = list_image_files(extra_dir)
        extra_image = random.choice(extra_images)
        negative_tuples.append((extra_image, extra_emotion))
    
    return positive_tuple, negative_tuples


def load_images(image_tuples: List[Tuple[str, str]]) -> List[Tuple[Image.Image, str]]:
    """
    Load images from the provided list of tuples containing file paths and emotions.

    :param image_tuples: List of tuples containing image file paths and their corresponding emotions.
    :return: List of tuples containing loaded PIL Image objects and their corresponding emotions.
    """
    return [(Image.open(path), emotion) for path, emotion in image_tuples]
