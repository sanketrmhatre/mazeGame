from tkinter import *
from tkinter import messagebox


class Player():
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="red")
        self.x, self.y = x, y
        self.nx, self.ny = x, y

    def move(self, direction):
        # Movement according to the key pressed on the keyboard
        if direction == 'w':
            self.nx, self.ny = self.x, self.y - 1
        elif direction == 'a':
            self.nx, self.ny = self.x - 1, self.y
        elif direction == 's':
            self.nx, self.ny = self.x, self.y + 1
        elif direction == 'd':
            self.nx, self.ny = self.x + 1, self.y

        # If the moved location is not a wall, move it and update x and y.
        if not self.is_collide():
            self.canvas.move(self.id, (self.nx - self.x) * 30, (self.ny - self.y) * 30)
            self.x, self.y = self.nx, self.ny

        # When you reach the goal point
        if map[self.y][self.x] == 3:
            messagebox.showinfo(title="success", message="You have succeeded in finding the maze.")

    # Determine whether the moved area is a wall or not
    def is_collide(self):
        if map[self.ny][self.nx] == 1:
            return True
        else:
            return False


# Key listener event
def keyEvent(event):
    player.move(repr(event.char).strip("'"))


root = Tk()
root.title("maze game")
root.resizable(False, False)

# Set window width, height, and position
width, height = 540, 540
x, y = (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

# Add a canvas and attach a key event
canvas = Canvas(root, width=width, height=height, bg="white")
canvas.bind("<Key>", keyEvent)
canvas.focus_set()
canvas.pack()

# 1: Wall, 2: Player starting point, 3: Goal point
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Draw a map on a canvas
for y in range(len(map[0])):
    for x in range(len(map[y])):
        if map[y][x] == 1:
            canvas.create_rectangle(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="black")
        elif map[y][x] == 2:
            player = Player(canvas, x, y)
        elif map[y][x] == 3:
            canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="blue")

root.mainloop()