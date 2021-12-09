import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window - Center')

window_width = 1000
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# message = tk.Label(root, text="Hello, World!")
# message.pack()

root.mainloop()
