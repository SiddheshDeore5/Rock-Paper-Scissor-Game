import tkinter as tk
import random

# Define the main game logic
def play_game(user_choice):
    item_list = ["Rock", "Paper", "Scissor"]
    comp_choice = random.choice(item_list)
    
    result_text.set(f"User choice: {user_choice}\nComputer choice: {comp_choice}")
    
    if user_choice == comp_choice:
        result_text.set(result_text.get() + "\nBoth choose same: Match Tie")
    elif user_choice == "Rock":
        if comp_choice == "Paper":
            result_text.set(result_text.get() + "\nPaper covers Rock: Computer Wins")
        else:
            result_text.set(result_text.get() + "\nRock smashes Scissor: You Win")
    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            result_text.set(result_text.get() + "\nScissor cuts Paper: Computer Wins")
        else:
            result_text.set(result_text.get() + "\nPaper covers Rock: You Win")
    elif user_choice == "Scissor":
        if comp_choice == "Paper":
            result_text.set(result_text.get() + "\nScissor cuts Paper: You Win")
        else:
            result_text.set(result_text.get() + "\nRock smashes Scissor: Computer Wins")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Create a text variable to store the result
result_text = tk.StringVar()
result_text.set("Make your choice!")

# Create a label to display the result
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14))
result_label.pack(pady=20)

# Create buttons for user choices
button_rock = tk.Button(root, text="Rock", command=lambda: play_game("Rock"), font=("Arial", 12))
button_paper = tk.Button(root, text="Paper", command=lambda: play_game("Paper"), font=("Arial", 12))
button_scissor = tk.Button(root, text="Scissor", command=lambda: play_game("Scissor"), font=("Arial", 12))

# Pack the buttons into the window
button_rock.pack(side=tk.LEFT, padx=20, pady=20)
button_paper.pack(side=tk.LEFT, padx=20, pady=20)
button_scissor.pack(side=tk.LEFT, padx=20, pady=20)

root.mainloop()