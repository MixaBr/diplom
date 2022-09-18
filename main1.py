import random
from tkinter import *
from tkinter import ttk
field = []
check = []
row = 0
col = 0
root = Tk()
#frm = ttk.Frame(root,border=0,borderwidth=0, padding=10,relief="raised")
#frm.grid()
#ttk.Label(frm, text="Hello World!").grid(column=0, row=10)
#ttk.Button(frm, text="Quit", width=100, command=root.destroy).grid(column=1, row=0)
def new_game():
    for row in range(5):
        for col in range(5):
            field[row][col]['text'] = str(random.randint(1,100))
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0
    global check
    check = []
def click(row, col):
    if game_run and field[row][col]['text'] != ' ':
        check.append(field[row][col]['text'])
        print(check)
        field[row][col]['text'] = 'X'
        field[row][col]['background'] = 'Red'
        global cross_count
        cross_count += 1
        if cross_count == 25:
            new_game()
#        check_win('X')
#        if game_run and cross_count < 5:
#            computer_move()
#            check_win('O')

for row in range(5):
    line = []
    for col in range(5):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=5, column=0, columnspan=3, sticky='nsew')

new_game()

root.mainloop()