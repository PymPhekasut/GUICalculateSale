from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#function for store program

def calprofit():
    at = int(allcoffee.get())
    # .get() is to gather data from box
    cal_sale = at * 40
    cal_cost = at * 20
    profit = cal_sale - cal_cost
    supplier = (profit * 10) // 500
    textshow = 'Coffee sale profit: {:,d} AUD\n'.format(profit)
    textshow2 = 'You have to pay for supplier: {:,d} AUD'.format(supplier)
    messagebox.showinfo('My profit',textshow+textshow2)


    
    
GUI = Tk()
GUI.geometry('500x500+100+100') #size
GUI.title('Coffee Beans profit calculation')

#Box for enter value
#StringVar = box that can fix value

bg = PhotoImage(file='coffeebean.png').subsample(2) #adjust size and only png

coffeepic = ttk.Label(GUI, image=bg)
coffeepic.pack(pady=20)

#text show for user
coffeetext = ttk.Label(GUI, text = 'Please entry the number of bag (40 AUD/bag)',font=('Browallia New',20))
coffeetext.pack(pady=10)

allcoffee = StringVar()

ECoffee = ttk.Entry(GUI,textvariable = allcoffee,font=('Browallia New',20))
ECoffee.pack(pady=20)


#add ttk to get better button
BCal = ttk.Button(GUI,text='Calculate',command=calprofit) #when press calculate it will run command 'calprofit in def function
BCal.pack(ipadx=20,ipady=10)

GUI.mainloop()
