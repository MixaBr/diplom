import random
from tkinter import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

class Playing_field:
    def __init__(self, field, row_g, game_run, sum_pl_1, sum_pl_2, cross_count, turn, plaer):
        self.field = field
        self.row_g = row_g
        self.game_run = game_run
        self.sum_pl_1 = sum_pl_1
        self.sum_pl_2 = sum_pl_2
        self.cross_count = cross_count
        self.turn = turn
        self.plaer = plaer


    def new_game(self):
        for row_v in range(self.row_g):
            for col_v in range(self.row_g):
                self.field[row_v][col_v]['text'] = str(random.randint(0,9))
        self.sum_pl_1 = 0
        self.sum_pl_2 = 0
        self.game_run = True
        self.cross_count = 0
        row = random.randint(0,self.row_g)
        col = random.randint(0,self.row_g)
        if self.turn == 1:
            self.row_2()
            self.row_1(row, col)
            self.turn = 0
        else:
            self.row_2()
            self.col_1(row)
            self.turn = 1
        ttk.Label(frame1, text="Игрок 1 -   " + str(self.sum_pl_1), background='lavender').grid(column=0, row=4 * 10)
        ttk.Label(frame2, text="Игрок 2 -   " + str(self.sum_pl_2), background='lavender').grid(column=0, row=8 * 10)
        if self.plaer == 0:
            ttk.Label(frame2, background='lavender').grid(column=0, row=8 * 10)
            ttk.Label(frame1, text="Игрок 1 - " + str(self.sum_pl_1), background='red').grid(column=0, row=4 * 10)
        else:
            ttk.Label(frame1, background='lavender').grid(column=0, row=4 * 10)
            ttk.Label(frame2, text="Игрок 2 - " + str(self.sum_pl_2), background='red').grid(column=0, row=8 * 10)

    def click(self,row, col):
        if self.game_run and self.field[row][col]['text'] != ' ' and self.field[row][col]['text'] != 'X' and self.field[row][col]['background'] == 'red' and self.cross_count != row_g * row_g:
            if self.plaer == 0:
                self.sum_pl_1 += int(self.field[row][col]['text'])
                ttk.Label(frame2,  text="Игрок 2 - " + str(self.sum_pl_2), background='red').grid(column=0, row=8 * 10)
                ttk.Label(frame1, text="Игрок 1 - " + str(self.sum_pl_1), background='lavender').grid(column=0, row=4 * 10)
                print(self.cross_count, " sum_pl_1", self.sum_pl_1)
                self.plaer = 1
            else:
                self.sum_pl_2 += int(self.field[row][col]['text'])
                ttk.Label(frame1, text="Игрок 1 - " + str(self.sum_pl_1), background='red').grid(column=0, row=4 * 10)
                ttk.Label(frame2, text="Игрок 2 - " + str(self.sum_pl_2), background='lavender').grid(column=0, row=8 * 10)
                print(self.cross_count, " sum_pl_2", self.sum_pl_2)
                self.plaer = 0
            self.field[row][col]['text'] = 'X'
            if self.turn == 1:
                self.row_2()
                self.row_1(row,col)
                self.turn = 0
            else:
                self.row_2()
                self.col_1(row)
                self.turn =1
            self.cross_count += 1
        else:
            print("Конец игре")

    def row_1 (self,row,col):
        for row_v in range(row_g):
            self.field[row_v][col]['background'] = 'red'

    def row_2 (self):
        for row_v in range(self.row_g):
            for col_v in range(self.row_g):
                self.field[row_v][col_v]['background'] = 'lavender'

    def col_1 (self,row):
        for col_v in range(self.row_g):
            self.field[row][col_v]['background'] = 'red'
    def col_2 (self,row):
        for col_v in range(self.row_g):
            self.field[row][col_v]['background'] = 'lavender'
#определение игрового поля
row_g = 5

pole = Playing_field([],row_g,True,0,0,0,random.randint(0,1),random.randint(0,1))

for row_v in range(row_g):
    line = []
    for col_v in range(row_g):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row_v=row_v, col_v=col_v: pole.click(row_v,col_v))
        button.grid(row=row_v, column=col_v, sticky='nsew')
        line.append(button)
    pole.field.append(line)

new_button = Button(root, text='new game', background='lavender',command=pole.new_game)
new_button.grid(row=row_g+1, column=0, columnspan=row_g, sticky='nsew')

frame1 = ttk.Frame(root,border=0,borderwidth=0, padding=10,relief="raised")
frame1.grid(row=0, column=8)
frame2 = ttk.Frame(root,border=0,borderwidth=0, padding=10,relief="raised")
frame2.grid(row=1, column=8)

ttk.Label(frame1, text="Игрок 1 - " + str(pole.sum_pl_1)).grid(column=0, row=4*10)
ttk.Label(frame2, text="Игрок 2 - " + str(pole.sum_pl_2)).grid(column=0, row=8*10)


pole.new_game()

root.mainloop()