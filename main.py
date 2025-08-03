from tkinter import *
import webbrowser 




myframe =Tk()



myframe.title("trt")
# لحجم اللوحه 
myframe.geometry("1500x1000")
# 
def tht():
    link = tx.get()
    webbrowser.open(link)



def ttt ():
    exit()


lll= Label (myframe, text="Ahmed ",font= "tahoma 30 bold")
lll.pack(pady=30)

tx = Entry(myframe,width=80)
tx.pack(pady=10)


botto =Button(myframe, text="Ahmed ",fg="blue",bg="yellow",font="Helvatica 20 bold",padx=10,pady=3, command=exit)
botto.pack(pady=30)



botto =Button(myframe, text="Go to link",fg="blue",bg="yellow",font="Helvatica 20 bold",padx=10,pady=3, command=tht)
botto.pack()












myframe.mainloop()

