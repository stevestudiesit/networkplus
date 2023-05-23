import os
import time
import random

layers = {
    1: "Physical Layer",
    2: "Data Link Layer",
    3: "Network Layer",
    4: "Transport Layer",
    5: "Session Layer",
    6: "Presentation Layer",
    7: "Application Layer"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    clear_screen()
    print("Welcome to the OSI Layer guessing game!\n")
    print("In this game, you will be shown a layer name \nand asked to guess its corresponding number.\n")
    print("Let's see how many you can get right!\n") # added new line
    num_plays = int(input("How many times do you want to play? "))
    total_time = 0.0
    for i in range(num_plays):
        layer_number, layer_name = random.choice(list(layers.items()))
        clear_screen()
        print("==============================")
        print(f"Layer to guess: {layer_name}")
        print("==============================")
        start_time = time.time()
        while True:
            guess = input("What is the number of this layer? ")
            clear_screen()
            print("==============================")
            print(f"Layer to guess: {layer_name}")
            print("==============================")
            if guess.isnumeric():
                guess = int(guess)
                if guess == layer_number:
                    print("Correct!")
                    break
            print("Incorrect. Try again.")
        end_time = time.time()
        total_time += end_time - start_time
        print("==============================")
        print(f"Total time taken: {end_time - start_time:.1f} seconds.")
        print("==============================")
    clear_screen()
    print("==============================")
    print(f"Total time taken: {total_time:.1f} seconds.")
    if num_plays > 0:
        print(f"Average time per question: {total_time/num_plays:.1f} seconds.")
    else:
        print("No games played, average time per question not applicable.")
    print("==============================")
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again.startswith("y"):
        play_game()
    else:
        print("Thanks for playing!")

play_game()
