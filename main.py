from tkinter import*

calculation  = ""

def add_To_Calculation(symbol):
    global calculation 
    calculation += str(symbol)
    text_Result.delete(1.0, "end")
    text_Result.insert(1.0, calculation)

def evaluate_Calculation():
    global calculation
    try:
        calculation = str(eval(calculation))

        text_Result.delete(1.0 , "end")
        text_Result.insert(1.0 , calculation)
    except:
        clear()
        text_Result.insert(1.0 , "Error")
       

def clear():
   global calculation
   calculation = ""
   text_Result.delete(1.0, "end")

window = Tk()
window.title("Simple Calculator")
window.geometry("300x275")


text_Result = Text(window, height=2 , width=20 , font=("times" , 24))
text_Result.grid(columnspan=5)

button_1 = Button(window , text="1" , command=lambda: add_To_Calculation(1) , width = 5 , font=("Times" , 12))
button_1.grid(row = 2 , column = 0)

button_2 = Button(window , text="2" , command=lambda: add_To_Calculation(2) , width = 5 , font=("Times" , 12))
button_2.grid(row = 2 , column = 1)

button_3 = Button(window , text="3" , command=lambda: add_To_Calculation(3) , width = 5 , font=("Times" , 12))
button_3.grid(row = 2 , column =2)

button_4 = Button(window , text="4" , command=lambda: add_To_Calculation(4) , width = 5 , font=("Times" , 12))
button_4.grid(row = 3 , column = 0)

button_5 = Button(window , text="5" , command=lambda: add_To_Calculation(5) , width = 5 , font=("Times" , 12))
button_5.grid(row = 3 , column = 1)

button_6 = Button(window , text="6" , command=lambda: add_To_Calculation(6) , width = 5 , font=("Times" , 12))
button_6.grid(row = 3 , column = 2)

button_7 = Button(window , text="7" , command=lambda: add_To_Calculation(7) , width = 5 , font=("Times" , 12))
button_7.grid(row = 4 , column = 0)

button_8 = Button(window , text="8" , command=lambda: add_To_Calculation(8) , width = 5 , font=("Times" , 12))
button_8.grid(row = 4 , column = 1)

button_9 = Button(window , text="9" , command=lambda: add_To_Calculation(9) , width = 5 , font=("Times" , 12))
button_9.grid(row = 4 , column = 2)

button_0 = Button(window , text="0" , command=lambda: add_To_Calculation(0) , width = 5 , font=("Times" , 12))
button_0.grid(row = 5 , column =1)


button_Plus = Button(window , text="+" , command=lambda: add_To_Calculation("+") , width = 5 , font=("Times" , 12))
button_Plus.grid(row = 2 , column = 3)

button_Minus = Button(window , text="-" , command=lambda: add_To_Calculation("-") , width = 5 , font=("Times" , 12))
button_Minus.grid(row = 3 , column = 3)

button_Mult = Button(window , text="x" , command=lambda: add_To_Calculation("*") , width = 5 , font=("Times" , 12))
button_Mult.grid(row = 4 , column = 3)

button_Div = Button(window , text="/" , command=lambda: add_To_Calculation("/") , width = 5 , font=("Times" , 12))
button_Div.grid(row = 5 , column = 3)


button_Open = Button(window , text="(" , command=lambda: add_To_Calculation("(") , width = 5 , font=("Times" , 12))
button_Open.grid(row = 5 , column = 0)


button_Close = Button(window , text=")" , command=lambda: add_To_Calculation(")") , width = 5 , font=("Times" , 12))
button_Close.grid(row = 5 , column = 2)

button_Equal = Button(window , text="=" , command=evaluate_Calculation , width = 11 , font=("Times" , 12))
button_Equal.grid(row = 6 , column = 2 , columnspan=2)

button_Clear = Button(window , text="C" , command=clear , width = 11 , font=("Times" , 12))
button_Clear.grid(row = 6 , column = 0 , columnspan=2)

window.mainloop()