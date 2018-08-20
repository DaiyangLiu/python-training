from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.food_all = [
            ['food1', 1, None], ['food2', 2, None],
            ['food3', 3, None], ['food4', 4, None],
            ['food5', 5, None], ['food6', 6, None]
        ]
        self.value = 0
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Welcome to Happy Restaurant!"
              ).grid(row= 0, column=2, columnspan = 3,sticky=W)

        Label(self,
              text="Menu"
              ).grid(row=1, column=3, sticky=W)

        for index,food in enumerate(self.food_all):
            food[2] = BooleanVar()
            Checkbutton(self,
                        text=food[0]+ " $"+str(food[1]),
                        variable=food[2],
                        command=self.update_the_bill
                        ).grid(row=int(2 + (index/2)), column = 1 if index%2 ==0 else 4, sticky=W)

        Label(self,text="Bill").grid(row=10, column=3, sticky=W)
        self.bill = Text(self, width = 8, height = 1, wrap = WORD)
        self.bill.grid(row = 10, column = 4)

    def update_the_bill(self):
        self.value = 0
        for food in self.food_all:
            if food[2].get():
                self.value += food[1]

        self.bill.delete(0.0, END)
        self.bill.insert(0.0, str(self.value))



# main
root = Tk()
root.title("Order Up!")
root.geometry("330x500")

app = Application(root)
root.mainloop()
