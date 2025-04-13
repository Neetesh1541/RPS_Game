import tkinter as tk
import random

# Game state
player1_score = 0
player2_score = 0
is_two_player = False
player1_choice = None

# Toggle game mode
def toggle_mode():
    global is_two_player, player1_score, player2_score
    is_two_player = not is_two_player
    mode_btn.config(text="Mode: 2 Player" if is_two_player else "Mode: Single Player")
    result_label.config(text="Mode switched. Let's play!")
    reset_game()

# Reset scores
def reset_game():
    global player1_score, player2_score, player1_choice
    player1_score = 0
    player2_score = 0
    player1_choice = None
    update_scores()
    result_label.config(text="Scores reset. Start fresh!")

# Update score label
def update_scores():
    score_label.config(text=f"Player 1: {player1_score}   Player 2: {player2_score}")

# Animate button (simple flash effect)
def animate_button(btn):
    original_color = btn.cget("bg")
    btn.config(bg="yellow")
    btn.after(150, lambda: btn.config(bg=original_color))

# Game logic
def play(choice, btn):
    global player1_choice, player1_score, player2_score

    animate_button(btn)

    if is_two_player:
        if player1_choice is None:
            player1_choice = choice
            result_label.config(text="Player 1 selected.\nNow Player 2, make your move.")
        else:
            player2_choice = choice
            if player1_choice == player2_choice:
                result = "It's a Tie!"
            elif (
                (player1_choice == "Rock" and player2_choice == "Scissors") or
                (player1_choice == "Paper" and player2_choice == "Rock") or
                (player1_choice == "Scissors" and player2_choice == "Paper")
            ):
                result = "Player 1 Wins! 🎉"
                player1_score += 1
            else:
                result = "Player 2 Wins! 🎉"
                player2_score += 1

            result_label.config(
                text=f"Player 1 chose: {player1_choice}\nPlayer 2 chose: {player2_choice}\n\n{result}"
            )
            player1_choice = None
            update_scores()
    else:
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        if choice == computer_choice:
            result = "It's a Tie!"
        elif (
            (choice == "Rock" and computer_choice == "Scissors") or
            (choice == "Paper" and computer_choice == "Rock") or
            (choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You Win! 🎉"
            player1_score += 1
        else:
            result = "Computer Wins 😞"
            player2_score += 1

        result_label.config(
            text=f"You chose: {choice}\nComputer chose: {computer_choice}\n\n{result}"
        )
        update_scores()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Rock Paper Scissors - Animated")
root.geometry("500x600")
root.config(bg="#e6f2ff")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#e6f2ff")
title.pack(pady=10)

mode_btn = tk.Button(root, text="Mode: Single Player", font=("Arial", 12), command=toggle_mode)
mode_btn.pack(pady=5)

score_label = tk.Label(root, text="Player 1: 0   Player 2: 0", font=("Arial", 14), bg="#e6f2ff")
score_label.pack(pady=5)

button_frame = tk.Frame(root, bg="#e6f2ff")
button_frame.pack(pady=10)

# Buttons with animation
rock_btn = tk.Button(button_frame, text="🪨 Rock", width=12, font=("Arial", 14),
                     bg="#ffffff", command=lambda: play("Rock", rock_btn))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", width=12, font=("Arial", 14),
                      bg="#ffffff", command=lambda: play("Paper", paper_btn))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=12, font=("Arial", 14),
                         bg="#ffffff", command=lambda: play("Scissors", scissors_btn))
scissors_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#e6f2ff", justify="center")
result_label.pack(pady=20)

reset_btn = tk.Button(root, text="🔄 Reset Game", font=("Arial", 12), command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
