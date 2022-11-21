from tkinter import *


def shift():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if (x2 < 0 or y1 < 0):  # reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps, shift)


############# Main program ###############
root = Tk()
root.title('Move Text')
canvas = Canvas(root, bg='black')
canvas.pack(fill=BOTH, expand=1)
text_var = "WELCOME TO THE DEPARTMENT OF COMPUTER SCIENCE. UNIVERSITY OF LAGOS."
text = canvas.create_text(0, -2000, text=text_var, font=('Ariel',
                          20, 'bold'), fill='red', tags=("marquee",), anchor='w')
x1, y1, x2, y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width'] = width
canvas['height'] = height
fps = 40  # Change the fps to make the animation faster/slower
shift()
root.mainloop()
