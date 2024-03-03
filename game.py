import random
import tkinter as tk
from PIL import Image, ImageTk
import data_loader

# Game state variables
current_round = 1
score = 0
num_negative_images = 15

# Initialize the Tkinter window
window = tk.Tk()
window.title("Happy Face Finder")

def display_grid(image_tuples):
    global window
    for i, (img, emotion) in enumerate(image_tuples):
        img = img.resize((144, 144))  # Resize the image
        img = ImageTk.PhotoImage(img)
        btn = tk.Button(window, image=img, command=lambda i=i: check_selection(i, image_tuples))
        btn.grid(row=i // 4, column=i % 4)  # Arrange buttons in a 4x4 grid
        btn.image = img  # Keep a reference to the image

def check_selection(index, image_tuples):
    global current_round, score
    selected_emotion = image_tuples[index][1]
    if selected_emotion == "happy":
        print("Correct! Moving to the next round.")
        score += 1
        current_round += 1
        start_round()  # Start the next round
    else:
        print(f"Incorrect. You selected {selected_emotion}. Try again.")

def start_round():
    global current_round, window
    print(f"Round {current_round}")
    positive_image_tuple, negative_image_tuples = data_loader.get_random_images("./data", num_negative_images)
    image_tuples = [positive_image_tuple] + negative_image_tuples
    random.shuffle(image_tuples)  # Shuffle the images
    image_tuples = data_loader.load_images(image_tuples)  # Load the images
    display_grid(image_tuples)

def play_game():
    start_round()
    window.mainloop()

if __name__ == "__main__":
    play_game()
