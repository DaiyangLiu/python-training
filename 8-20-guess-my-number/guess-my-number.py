from tkinter import *
import random

class Application(Frame):
    """ A GUI application with three buttons. """ 
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)    
        self.grid()
        self.create_widgets()
        self.the_number = random.randint(1,100)


    def create_widgets(self):
        Label(self,
              text = "I'm thinking a number between 1 and 100.\n"
                     "Try to guess it in as few attempts as possible.").grid(row = 0, column = 0,  columnspan = 2 ,sticky = W)
        # rowspan = 2, columnspan = 3,

        Label(self,
              text = "Your Guess Number: ").grid(row = 3, column = 0,columnspan = 1, sticky = W)

        self.num_ent = Entry(self)

        self.num_ent.grid(row = 3, column = 1 , sticky = W)

        self.submit_button = Button(self,text = "submit", command = self.check)
        self.submit_button.grid(row = 3, column = 3, sticky = E)

        self.answer = Text(self,width = 35, height = 5, wrap = WORD)
        self.answer.grid(row = 5, column = 0, columnspan = 4, sticky= W)

    def check(self):
        try:
            numb = int(self.num_ent.get())
        except:
            message = "please input a number"
        else:
            if numb > self.the_number:
                message = "larger..."
            elif numb < self.the_number:
                message = "lower..."
            elif numb == self.the_number:
                message = "YOU WIN"

        self.answer.delete(0.0, END)
        self.answer.insert(0.0, message)


# main
root = Tk()
root.title("guess my number")
root.geometry("400x150")
app = Application(root)
root.mainloop()
