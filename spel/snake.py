from tkinter import *
import random


width = 40
height = 40
size = 10


class Snake():
    def __init__(self):
        self.snakeX = [20, 20, 20]
        self.snakeY = [21, 22, 23]
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

        self.eat()

    def eat(self):
        if self.snakeX[0] == apple.getAppleX() and self.snakeY[0] == apple.getAppleY():
            self.snakeL = self.snakeL + 1

            x = self.snakeX[len(self.snakeX)-1]
            y = self.snakeY[len(self.snakeY) - 1]
            self.snakeX.append(x+1)
            self.snakeY.append(y)
            self.points = self.points + 1
            global scoreLable
            scoreLable["text"] = self.points
            apple.createNewApple()

    def GameOver(self):
        for i in range(1, self.snakeL, 1):

            if self.snakeY[0] == self.snakeY[i] and self.snakeX[0] == self.snakeX[i]:
                return True

        if self.snakeX[0] < 1 or self.snakeX[0] >= width-1 or self.snakeY[0] < 1 or self.snakeY[0] >= height-1:
            return True

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

    def getPoints(self):
        return self.points


class Apple:
    def __init__(self):
        self.appleX = random.randint(1, width - 2)
        self.appleY = random.randint(1, height - 2)

    def getAppleX(self):
        return self.appleX

    def getAppleY(self):
        return self.appleY

    def createNewApple(self):
        self.appleX = random.randint(1, width - 2)
        self.appleY = random.randint(1, height - 2)


class GameLooop:

    def repaint(self):
        canvas.after(200, self.repaint)
        canvas.delete(ALL)
        if snake.GameOver() == False:

            snake.move()
            snake.GameOver()
            canvas.create_rectangle(snake.getSnakeX(0) * size, snake.getSnakeY(0) * size,
                                    snake.getSnakeX(0) * size + size,
                                    snake.getSnakeY(0) * size + size, fill="red")

            for i in range(1, snake.getSnakeLength(), 1):
                canvas.create_rectangle(snake.getSnakeX(i) * size, snake.getSnakeY(i) * size,
                                        snake.getSnakeX(i) * size + size,
                                        snake.getSnakeY(i) * size + size, fill="blue")

                canvas.create_rectangle(apple.getAppleX() * size, apple.getAppleY() * size,
                                        apple.getAppleX() * size + size,
                                        apple.getAppleY() * size + size, fill="green")

        else:
            canvas.delete(ALL)


snake = Snake()
apple = Apple()
root = Tk()

canvas = Canvas(root, width=400, height=400, background='yellow')
canvas.pack()


root.title('Snake Game')
root.resizable(False, False)
root.bind('<KeyPress>', snake.getKey)


scoreLable = Label(root, text=snake.points, anchor=W).pack(fill='both')


def updateLabel():
    pass


gameStart = GameLooop()
gameStart.repaint()
root.mainloop()
