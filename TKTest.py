from tkinter import *


class Application(Frame):

    def __init__(self, masster=None):
        Frame.__init__(self, masster)
        self.quitButton = Button(self, text='退出', command=self.quit)
        self.helloLabel = Label(self, text='Hello world')
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel.pack()
        self.quitButton.pack()

    # def quit(self):
    #     print('退出')


app = Application()
app.master.title('Hello world')
app.mainloop()
