from PIL import Image, ImageTk
from tkinter import *
import random


width = 30
height = 30
size = 10


class Snake():
    def __init__(self):
        self.snakeX = [20, 20, 20]
        self.snakeY = [21, 21, 22]
        self.snakeL = 3
        self.key = 'w'
        self.points = 0

    def move(self):
        for i in range(self.snakeL - 1, 0, -1):
            self.snakeX[i] = self.snakeX[i-1]
            self.snakeY[i] = self.snakeY[i-1]

        if self.key == 'w':
            self.snakeY[0] = self.snakeY[0] - 1
        elif self.key == "s":
            self.snakeY[0] = self.snakeY[0] + 1

        elif self.key == "a":
            self.snakeX[0] = self.snakeX[0] - 1

        elif self.key == "d":
            self.snakeX[0] = self.snakeX[0] + 1

    def GameOver(self):
        '''
        for i in range(1, self.snakeL, 1):
            if self.snakeY[0] == self.snakeY[i] and self.snakeX[0] == self.snakeX[i]:
                return True
        if self.snakeX[0] < 1 or self.snakeY > 1 or self.snakeY >= height-1:
            return True
        '''
        return False

    def getKey(self, event):

        if event.char == "w" or event.char == "d" or event.char == "s" or event.char == "a" or event.char == " ":
            self.key = event.char

    def getSnakeX(self, index):
        return self.snakeX[index]

    def getSnakeY(self, index):
        return self.snakeY[index]

    def getSnakeLength(self):
        return self.snakeL


def startGame():
    if snake.GameOver == False:
        print('hek')
        canvas.after(200, startGame())
    if snake.GameOver == False:
        print('hej')
        snake.move()
        snake.GameOver()
        canvas.create_rectangle(snake.getSnakeX(0) * size, snake.getSnakeY(0) * size,
                                snake.getSnakeX(0) * size + size,
                                snake.getSnakeY(0) * size + size, fill="red")
        for i in range(1, snake.getSnakeLength(), 1):
            canvas.create_rectangle(snake.getSnakeX(i) * size, snake.getSnakeY(i) * size,
                                    snake.getSnakeX(i) * size + size,
                                    snake.getSnakeY(i) * size + size, fill="blue")
    else:
        canvas.delete(ALL)


root = Tk()
root.title('Snake Game')
root.resizable(False, False)
canvas = Canvas(root, width=700, height=500, background='yellow')
canvas.pack()
snake = Snake()
print(snake.GameOver())
startGame()
root.bind('<KeyPress>', snake.getKey)
root.mainloop()
