
    
import tkinter as tk
import random   #FOR GENERATING RANDOM PUZZLE
import pygame
from tkinter import *
from tkinter import font
from tkinter import messagebox
hint_count=3
pygame.mixer.init()

#MAIN WINDOW
first_window = tk.Tk()
first_window.title("FUTOSHIKI PUZZLE")
first_window.geometry("700x500")
bg = tk.PhotoImage(file='classic.png')
label1= tk.Label( first_window , image=bg)
label1.place(x=0,y=0)

wakari_font = font.Font(family="Courier bold 700", size=32)
# PUZZLE LABEL
#label = tk.Label(root, text="Welcome to the Puzzle Game", font=poppins_font)
puzzle_label = tk.Label(first_window,text="Futoshiki Puzzle", font=wakari_font)
puzzle_label.place(relx=0.5, rely=0.15, anchor='center')
puzzle_label.config(bg='#AEE2FF', fg="black")

#HIDE MAIN WINDOW I.E FOR SECOND WINDOW
def hide_main_window():
    first_window.withdraw()
#OPEN MAIN WINDOW
def open_second_window():
    pygame.mixer.music.load("game latch.mp3")
    pygame.mixer.music.play(loops=0)
    global second_window
    hide_main_window()  # CALLS FUNCTION TO HIDE WINDOW
    second_window = tk.Toplevel()  #SECOND WINDOW AS A TOP LEVEL WIDGET
    second_window.title("Futoshiki Rules and Choose")
    second_window.geometry("700x500")
    second_window.config(bg='#ffb7c5')
    #RULES BUTTON
    rules_button = tk.Button(second_window, text="Rules", command=open_rules_window, font=("Arial", 20), bg="#ffeffe", fg="black")
    rules_button.place(x=270, y=100)

    #CHOOSE BUTTON
    choose_button = tk.Button(second_window, text="Choose", command=lambda:[open_choose_window(),second_window.withdraw()], font=("Arial", 20), bg="#ffeffe", fg="black")
    choose_button.place(x=268, y=300)

    def play():
        pygame.mixer.music.load("game latch.mp3")
        pygame.mixer.music.play(loops=0)
    #MENU BUTTON
    menu_button = tk.Button(second_window, text="Menu", command=lambda:[play,second_window.withdraw(),first_window.deiconify()], font=("Arial", 20), bg="#ffeffe", fg="black")
    menu_button.place(x=600, y=400)

#OPEN THIRD WINDOW I.E FOR RULES
def open_rules_window():
    pygame.mixer.music.load("game latch.mp3")
    pygame.mixer.music.play(loops=0)
    global second_window
    second_window.withdraw()  # HIDE SECOND WINDOW

    rules_window = tk.Toplevel()  # TOPLEVEL WIDGET
    rules_window.title("Futoshiki Puzzle Rules")
    rules_window.geometry("700x500")
    rules_window.config(bg='#ffb7c5')

    #DISPLAY REULES
    rules = """
    Futoshiki is a logic puzzle game played on a square grid.
    The objective is to place numbers from 1 to N on the grid, 
    with each row and column containing unique numbers. 
    Additionally, some cells contain inequality signs (< or >) 
    which must be satisfied.

    Rules:
    1. Each row and column must contain numbers from 1 to N.
    2. Numbers cannot be repeated in any row or column.
    3. The inequality signs (< or >) must be satisfied.
    
    Have fun playing Futoshiki!
    """
    rules_text= tk.Text(rules_window, font=("Arial", 14))
    rules_text.insert(tk.END, rules)
    rules_text.config(bg='#ffb7c5')
    rules_text.pack()

    #DONE BUTTON
    done_button = tk.Button(rules_window, text="Done", command=lambda: [rules_window.destroy(), second_window.deiconify()], font=("Arial", 20), bg="#ffeffe", fg="black")
    done_button.place(x=250, y=400)
    
def open_choose_window():
    pygame.mixer.music.load("game latch.mp3")
    pygame.mixer.music.play(loops=0)
    button_window = tk.Tk()
    button_window.title("Futoshiki Puzzle")
    button_window.geometry("700x500")
    button_window.config(bg='#ffb7c5')

    label2 = tk.Label(button_window, text="Futoshiki Puzzle", font=("Arial", 24))
    label2.place(relx = 0.5, rely = 0.25,anchor = 'center')
    label2.config(bg='#ffb7c5',fg="black")

    # Center the buttons just below the label
    button_frame =tk.Frame(button_window)
    button_frame.place(x=220, y=250)
    button_frame.config(bg='#ffb7c5')


    fourbutton = tk.Button(button_frame, text="4x4", font=("Helvetica", 20), command=lambda:[button_window.withdraw(),on_play(4)])
    fourbutton.grid(row=0, column=0, padx=10, pady=10)
    fourbutton.config(bg='#ffeffe')

    fivebutton = tk.Button(button_frame,text="5x5", font=("Helvetica", 20), command=lambda: [button_window.withdraw(),on_play(5)])
    fivebutton.grid(row=0,column=1,padx=10,pady=10)
    fivebutton.config(bg='#ffeffe')

    sixbutton=tk.Button(button_frame,text="6x6",font=("Helvetica",20),command=lambda:[button_window.withdraw(),on_play(6)])
    sixbutton.grid(row=0,column=2,padx=10,pady=10)
    sixbutton.config(bg='#ffeffe')

    back_button=tk.Button(button_window,text="BACK",command=lambda:[button_window.withdraw(),second_window.deiconify()], font=("Arial", 20), bg="#ffeffe", fg="black")
    back_button.place(x=600,y=400)


def on_play(n):
    pygame.mixer.music.load("game latch.mp3")
    pygame.mixer.music.play(loops=0)
    global question_window
    question_window = tk.Toplevel()
    question_window.title("Futoshiki Puzzle Rules")
    question_window.geometry("700x700")
    question_window.config(bg='#ffb7c5')
    p,q=answer(n)

    def get_entry_coordinates(focused_entry):
        for i in range(len(entry_grid)):
            for j in range(len(entry_grid[i])):
                if entry_grid[i][j] == focused_entry:
                   return i, j
        return None, None  

    def activate_hint():
        global hint_count

        focused_entry = question_window.focus_get()  # CURSER WIDGET
        if focused_entry:
            i, j = get_entry_coordinates(focused_entry) #ROW COL INDICES
            if i is not None and j is not None:
                if hint_count > 0:
                   hint_count -= 1
                   focused_entry.delete(0, END)
                   focused_entry.insert(0, str(p[i][j]))
                else:
                   messagebox.showinfo("Hint Limit", "You have used all your hints")
        else:
            print("")
 
    hint_button = Button(question_window, text="HINT", font=("Helvetica", 14), command=activate_hint)
    hint_button.grid(row=2, column=n + 150)
    hint_button.config(bg="#ffeffe")
    
    def show_solution():
        pygame.mixer.music.load("game latch.mp3")
        pygame.mixer.music.play(loops=0)
        result=messagebox.askquestion("Yes/No", "Do you want to see solution?")
        if result == "yes":
            for i in range(len(entry_grid)):
                for j in range(len(entry_grid[i])):
                    if entry_grid[i][j] is not None:
                       entry_grid[i][j].delete(0, END)  # REMOVE WHAT USER HAS WRITTEN
                       entry_grid[i][j].insert(0, str(p[i][j]))
        else:
           print("User chose not to proceed.")
    def clear_puzzle(n):
        pygame.mixer.music.load("game latch.mp3")
        pygame.mixer.music.play(loops=0)
        global entry_grid
        result=messagebox.askquestion("Yes/No", "Do you want to clear input?")
        if result=="yes":
            for i in range(len(entry_grid)):
                for j in range(len(entry_grid[i])):
                    if entry_grid[i][j] is not None:
                        entry_grid[i][j].delete(0, END)
                        if q[i][j] == "" or q[i][j] == "_":
                           entry_grid[i][j].insert(0,"")
                        else:
                           entry_grid[i][j].insert(0,str(q[i][j]))
        else:
            print("User choose not to proceed")
    
                       
    solution_button = Button(question_window, text="Show Solution", font=("Helvetica", 14), command=show_solution)
    solution_button.grid(row=5, column=n + 150)
    solution_button.config(bg="#ffeffe")
   
    clear_button = Button(question_window, text="Clear", font=("Helvetica", 14), command=lambda: clear_puzzle(n))
    clear_button.grid(row=3, column=n + 150)
    clear_button.config(bg="#ffeffe")

    global entry_grid
    entry_grid = []
    for i in range(len(q)):
        row_entries = []
        for j in range(len(q[i])):
            if q[i][j] == "_":
                entry = Entry(question_window, font=("Helvetica", 16), width=2,borderwidth=3,relief="sunken", justify='center')
                entry.grid(row=i + 2, column=j)
                row_entries.append(entry)
               
            elif q[i][j] == "*":
                label = Label(question_window, text=q[i][j], font=("Helvetica", 16), width=3, height=2)
                label.grid(row=i + 2, column=j)
            else:
                label = Label(question_window, text=q[i][j], font=("Helvetica", 16), width=3, height=2)
                label.grid(row=i + 2, column=j)
                label.config(bg='#ffb7c5')
                row_entries.append(None)
        entry_grid.append(row_entries)

    def play():
        pygame.mixer.music.load("game latch.mp3")
        pygame.mixer.music.play(loops=0)
    new_button = Button(question_window, text="NewGame", command=lambda:[play,question_window.withdraw(),open_choose_window()], font=("Arial", 20), bg='#AEE2FF', fg="black")
    new_button.place(x=500,y=400)
    new_button.config(bg="#ffeffe")
    
def answer(n):
    def is_valid(puzzle, row, col, num):
        for i in range(len(puzzle)):
            if puzzle[row][i]==num or puzzle[i][col]==num:
                return False
        return True
    def count_valid_entries():
        total_valid = 0 
        for row in entry_grid:
            for entry in row:
                if entry:
                    total_valid += 1 
        return total_valid  
    def check_solution():
        focused_entry = question_window.focus_get()  #ENTRY WIDGET WHERE THE CURSER IS PRESENT 
        for i in range(len(entry_grid)):
            for j in range(len(entry_grid[i])):
                entry = entry_grid[i][j]
                if entry == focused_entry:
                   user_input = entry.get()  # GET USER INPUT
                   correct_number = puzzle[i][j]  # GET CORRECT NUMBER FROM THAT ROW AND COLUMN
                   if user_input.isdigit() and int(user_input) == correct_number:
                      entry.config(bg='white')
                   else:
                      entry.config(bg='red')

    check_button = tk.Button(question_window, text="Check",font=("Helvetica", 14), command=check_solution)
    check_button.grid(row=6, column=n+150)
    check_button.config(bg="#ffeffe")
 
    def submit_solution():
       correct_entries = 0

       for i in range(len(entry_grid)):
         for j in range(len(entry_grid[i])):
            entry = entry_grid[i][j]
            if entry:
                user_input = entry.get()
                correct_number = puzzle[i][j]

                if user_input.isdigit() and int(user_input) == correct_number:
                    entry.config(bg='white')
                    correct_entries += 1
                else:
                    entry.config(bg='red')

       total_valid_entries = count_valid_entries()
       if correct_entries == total_valid_entries:
         pygame.mixer.music.load('yay.mp3')
         pygame.mixer.music.play(loops=0)
         result = messagebox.askquestion("Congratulations!", "All entries are correct!\nDo you want to play again?")
         if result == "yes":
            open_choose_window()
            question_window.destroy()

         elif result == "no":
            question_window.destroy()
       else:
           result=messagebox.askquestion("You loose!","GAME OVER!!,Do you want to play again?")
           if result=="yes":
              question_window.destroy()
              open_choose_window()
           elif result=="No":
              question_window.destroy()
    submit_button = tk.Button(question_window, text="Submit Solution",font=("Helvetica", 14), command=submit_solution)
    submit_button.grid(row=4, column=n+150)
    submit_button.config(bg="#ffeffe")
    

    def solve_puzzle(puzzle, numbers, row=0, col=0):
        if row == len(puzzle):
            return True

        next_row, next_col = row, col + 1
        if next_col == len(puzzle):
            next_row, next_col = row + 1, 0

        if puzzle[row][col] == 0:
            for num in numbers:
                if is_valid(puzzle, row, col, num):
                    puzzle[row][col] = num
                    if solve_puzzle(puzzle, numbers, next_row, next_col):
                        return True
                    puzzle[row][col] = 0

        else:
            if solve_puzzle(puzzle, numbers, next_row, next_col):
                return True

        return False
    row, col = ((2*n)-1, (2*n)-1)
    puzzle = []
    for i in range(row):
        x = []
        for j in range(col):
            if i % 2 == 0 and j % 2 == 0:
                x.append(0)
            elif i % 2 == 0 or j % 2 == 0:
                x.append("*")
            else:
                x.append(" ")
        puzzle.append(x)
    numbers = list(range(1, n+1))
    random.shuffle(numbers)
    if solve_puzzle(puzzle, numbers):
        print("")
    else:
        print("")

    for i in range(row):
        for j in range(col):
            if puzzle[i][j] == "*":
                if i % 2 != 0 and j % 2 == 0:
                    if puzzle[i - 1][j] > puzzle[i + 1][j]:
                        puzzle[i][j] = 'v'
                    else:
                        puzzle[i][j] = '^'
                else:
                    if puzzle[i][j - 1] > puzzle[i][j + 1]:
                        puzzle[i][j] = '>'
                    else:
                        puzzle[i][j] = '<'

    probability = 0.2
    question = [[" " for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            if random.random() < probability:
                question[i][j] = puzzle[i][j]
            elif i % 2 == 0 and j % 2 == 0:
                question[i][j] = "_"
            else:
                question[i][j] = " "
    return puzzle,question

#PLAY BUTTON IN THE FIRST WINDOW
play_button = tk.Button(first_window, text="Play", command=open_second_window, font=("Arial", 22), bg='#AEE2FF', fg="black")
play_button.place(x=295, y=295)
first_window.mainloop()
