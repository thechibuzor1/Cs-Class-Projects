import json
import tkinter as tk
from tkinter import StringVar, ttk


LARGEFONT = ("Verdana", 20)


class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp

    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk

        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True,
                       padx=20, pady=20, anchor='center')

        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)
        self.var = StringVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()

        self.Database = StringVar()

        self.scores = []  # list of scores extracted from list of students
        self.matricNos = []  # list of matric numbers extracted from list of students
        self.names = []  # list of names extracted from list of students
        self.above70 = []
        fname = 'studentData.json'

        self.student = []
        try:
            with open(fname, "r") as f:
                self.student = json.load(f)
                f.close()
        except:
            # may complain to user as well
            with open(fname, "w") as f:
                json.dump(self.student, f)
                print("The json file is created")
                print(self.student)

        self.anaData = []
        self.anaData = self.analytics()

        # initializing frames to an empty array

        self.frames = {}

        # iterating through a tuple consisting

        # of the different page layouts

        for F in (StartPage, Page1, Page2):

            frame = F(container, self)

            # initializing frame of that object from

            # startpage, page1, page2 respectively with

            # for loop

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as

    # parameter

    def show_frame(self, cont):

        frame = self.frames[cont]

        frame.tkraise()

    def loadData(self):
        if len(self.student) != 0:
            for i in self.student:
                self.scores.append(i['score'])
                self.matricNos.append(i['matricNo'])
                self.names.append(i['fname']+i['lname'])

    def check(self, fname, lname, matricNo, score):
        self.loadData()
        res = ''
        if len(fname) != 0 and len(lname) != 0 and len(matricNo) != 0 and len(str(score)) != 0:
            if fname+lname not in self.names:
                if matricNo not in self.matricNos:
                    if len(matricNo) == 9:
                        if score >= 0 and score <= 100:
                            res = 'Valid'
                            return res
                        else:
                            res = 'Invalid score! (Scores should be within the range 0-100)'
                            return res
                    else:
                        res = "Length of student's matric number should be 9!"
                        return res
                else:
                    res = 'Matric number aleady exists!'
                    return res
            else:
                res = 'Name aleady exists'
                return res
        else:
            res = 'Fill all fields!'
            return res

    def save(self, fname, lname, matricNo, score):
        self.loadData()
        data = {
            'fname': fname,
            'lname': lname,
            'matricNo': matricNo,
            'score': score,
        }
        self.student.append(data)
        with open('studentData.json', 'w') as f:
            json.dump(self.student, f)
        self.loadData()

    def analytics(self):
        self.loadData()
        if (len(self.student) != 0):
            mean = round(sum(self.scores)/len(self.scores))
            for i in self.student:
                if i['score'] == max(self.scores):
                    highest = i['fname'], i['lname'] + '(', i['score'], ')'

                    self.var1.set(highest)
                if i['score'] >= 70:
                    self.above70.append(i)
                if i['score'] == min(self.scores):
                    low = i['fname'], i['lname'] + '(', i['score'], ')'

                    self.var3.set(low)
            self.var2.set(mean)


# first window frame startpage


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # label of frame Layout 2

        label = ttk.Label(
            self, text="CSC Group 11 Class Project", font=LARGEFONT)

        # putting the grid in its place by using

        # grid

        label.grid(row=0, column=5, padx=10, pady=10)

        button1 = ttk.Button(self, text="Add A New Student's Details",

                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by

        # using grid

        button1.grid(row=1, column=5, padx=10, pady=10)

        # button to show frame 2 with text layout2

        button2 = ttk.Button(self, text="View Analytics",

                             command=lambda:  [controller.analytics(), controller.show_frame(Page2)])

        # putting the button in its place by

        # using grid

        button2.grid(row=2, column=5, padx=10, pady=10)

        # second window frame page1


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        text = controller.var

        def goBack():
            a1.delete(0, "end")
            b1.delete(0, "end")
            c1.delete(0, "end")
            d1.delete(0, "end")
            text.set("")

        def handleSave():

            fname = a1.get().rstrip()
            lname = b1.get().rstrip()
            matricNo = c1.get().rstrip()
            try:
                score = int(d1.get().rstrip())
                res = (controller.check(fname, lname, matricNo, score))
                if (res == 'Valid'):
                    text.set('Student Details Saved!')
                    controller.save(fname, lname, matricNo, score)
                    a1.delete(0, "end")
                    b1.delete(0, "end")
                    c1.delete(0, "end")
                    d1.delete(0, "end")
                else:
                    text.set(res)

            except Exception:
                text.set("Enter a valid score (between 1 and 100).")

            responseText = ttk.Label(self, textvariable=text,
                                     )
            responseText.grid(row=5, column=2, pady=20,)

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Enter Student's Details", font=LARGEFONT)

        label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, )

        a = ttk.Label(self, text="Surname Name").grid(row=1, column=1)
        b = ttk.Label(self, text="First Name").grid(row=2, column=1)
        c = ttk.Label(self, text="Matric Number").grid(row=3, column=1)
        d = ttk.Label(self, text="Score").grid(row=4, column=1)
        a1 = ttk.Entry(self)
        a1.grid(row=1, column=2)
        b1 = ttk.Entry(self)
        b1.grid(row=2, column=2)
        c1 = ttk.Entry(self)
        c1.grid(row=3, column=2)
        d1 = ttk.Entry(self)
        d1.grid(row=4, column=2)
        # button to show frame 2 with text

        # layout2

        button1 = ttk.Button(self, text="Go Back",
                             command=lambda: [goBack(), controller.show_frame(StartPage)])

        # putting the button in its place

        # by using grid

        button1.grid(row=7, column=1, padx=10, pady=10)

        # button to show frame 2 with text

        # layout2

        button2 = ttk.Button(self, text="Save Details",
                             command=lambda: [handleSave(), controller.loadData()])

        # putting the button in its place by

        # using grid

        button2.grid(row=7, column=2, padx=10, pady=10)


# third window frame page2

class Page2(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = ttk.Label(
            self, text="Student's Analytics", font=LARGEFONT)

        label.grid(row=0, column=0, columnspan=3,
                   padx=10, pady=10, )

        ttk.Label(self, text="The highest scoring student is: ", foreground='green').grid(
            row=1, column=0, padx=10, pady=10, )

# set the text
        varStr = controller.var1
        a = ttk.Label(self, textvariable=varStr, foreground='black')
        a.grid(row=1, column=1, padx=10, pady=10, )

        ttk.Label(self, text="The mean score:", foreground='blue').grid(
            row=2, column=0, padx=10, pady=10, )

        mean = controller.var2
        mt = ttk.Label(self, textvariable=mean, foreground='black')
        mt.grid(
            row=2, column=1, padx=10, pady=10, )

        ttk.Label(self, text="Students who scored above 70:", foreground='blue').grid(
            row=3, column=0, padx=10, pady=10, )
        above70 = controller.above70
        for i in above70:
            text = i['fname'], i['lname'] + '(', i['score'], ')'
            ab = ttk.Label(self, text='', foreground='black')
            ab.grid(
                row=3+above70.index(i), column=1, padx=10, pady=10, )
            ab.configure(text=text)

        ttk.Label(self, text="The lowest scoring student:", foreground='red').grid(
            row=len(above70)+4, column=0, padx=10, pady=10, )
        low = controller.var3
        l = ttk.Label(self, textvariable=low, foreground='black')
        l.grid(
            row=len(above70)+4, column=1, padx=10, pady=10, )

        button2 = ttk.Button(self, text="Back",

                             command=lambda:   controller.show_frame(StartPage))

    # putting the button in its place by
        button2.grid(row=len(above70)+6, column=2, padx=10, pady=10)

        ''' else:
            ttk.Label(self, text="Database is empty").grid(
                row=1, column=0, padx=10, pady=10, )
            button2 = ttk.Button(self, text="Back",

                                 command=lambda:   controller.show_frame(StartPage))

        # putting the button in its place by
            button2.grid(row=6, column=2, padx=10, pady=10) '''

    # using grid

        # button to show frame 2 with text

        # layout2

        # button1 = ttk.Button(self, text="Page 1",command=lambda: controller.show_frame(Page1))

        # putting the button in its place by

        # using grid

        # button1.grid(row=7, column=1, padx=10, pady=10)

        # button to show frame 3 with text

        # layout3


# Driver Code


app = tkinterApp()
app.resizable(False, False)
app.mainloop()


''' while (res):
    loadData()
    name = str(input("Enter the student's name: "))
    matricNo = str(input("Enter the matric number: "))
    score = int(input("Score: "))
    if (check(name, matricNo, score) == 'Valid'):
        save(name, matricNo, score)
    else:
        print(check(name, matricNo, score))

    res = str(input("Enter 'y' to save another student's details: "))
    if res == 'y':
        continue
    else:
        break
 '''
'''
loadData()
mean = sum(scores)/len(scores)
for i in student:
    if i['score'] == max(scores):
        print("The highest scoring student is: ",
              i['name'], '(', i['score'], ')')
print('Students who scored above 70 are: ')
for i in student:
    if i['score'] >= 70:
        print(i['name'], '(', i['score'], ')')
for i in student:
    if i['score'] == min(scores):
        print('The lowest scoring student is: ',
              i['name'], '(', i['score'], ')')  '''
