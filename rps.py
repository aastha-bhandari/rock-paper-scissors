import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors Game")
choices = ["rock","paper","scissors"]

def play(user_choice):
    comp_choice = random.choice(choices)
    
    if user_choice == comp_choice : result = "it is a draw!"
    elif (
        (user_choice=="rock" and comp_choice=="scissors") or (user_choice=="paper" and comp_choice=="rock") or 
        (user_choice=="scissors" and comp_choice=="paper")):
            result = "You Win!"
    
    else : result = "You Lose!"

    result_label.config(text=f"You Chose : {user_choice}\n" f"Computer Chose : {comp_choice}\n\n"f"{result}")

def reset():
      result_label.config(text="")

heading = tk.Label(window, text="rock paper scissors", font=("Arial",16)) 
heading.pack(pady=10)

rock_button = tk.Button(window, text="rock", width=10, command=lambda:play("rock"))
paper_button = tk.Button(window,text="paper", width=10, command=lambda:play("paper"))
scissors_button = tk.Button(window, text="scissors", width=10, command=lambda:play("scissors"))
reset_button = tk.Button(window, text="Try Again", command=reset)
rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)
reset_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial",12))
result_label.pack(pady=20)

window.mainloop()




    

