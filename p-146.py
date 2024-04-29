from tkinter import *

root=Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci series")
label_sum = Label(root, text="82")

def Fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
       
        
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
label_sum["text"] = "Fibonacci Sum : " + str(82)
btn.pack()
label_series.pack()
label_sum.pack()
root.mainloop()

