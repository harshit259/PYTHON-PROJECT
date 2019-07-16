from tkinter import*
import pyttsx3          # pyttsx3 is a text-to-speech conversion library in Python


e = pyttsx3.init('sapi5')   #sapi5 work only in windows
v = e.getProperty('voices')     #to access voice
e.setProperty('voice',v[1].id)  #here you select voice with 0 or 1

def speak(audio):                    # anything pass in speak function with argument audio is speak by sapi5
    if audio == "*":
        audio = "multiply"
    elif audio == "/":
        audio = "divide"
    elif audio == ".":
        audio = "dot"
    elif audio == "+/-":
        audio = "ADDITION OR SUBTRACTION"
    elif audio == "+":
        audio = "addtion"
    elif audio == "%":
        audio = "modooules"
    elif audio == "**(1/2)":
        audio = "squareroot"
    elif audio == "**2":
        audio = "square"
    elif audio == "**3":
        audio = "cube"
    elif audio == "-":
        audio = "subtraction"
    elif audio == "1/x":
        audio = "ONE Divide BY X"
    e.say(audio)                      
    e.runAndWait()
    
    
#btnclick function collect all number and operator in operator variable


def btnclick(number):
    speak(number)
    global operator
    operator=operator + str(number)
    t1.set(operator)
    
#btnclear fuction clean the whole screen


def btnclear():
    global operator
    speak("clear")
    operator=""
    t1.set("")
   
#btnequal function evaluate operator variable



def btnequal():
    global operator
    speak("equal")
    res=str(eval(operator))
    speak(res)
    t1.set(res)
    operator=""


win = Tk()
win.title("CALCULATOR")
operator=""
t1 =StringVar()

#layout or physical structure


txtdisplay = Entry(win, font=('arial', 26, 'bold'), textvariable= t1, insertwidth=5 ).grid(columnspan=5)
btn0 = Button(win, text="%", command=lambda:btnclick("%"), height=5, width=10).grid(row=1,column=0)
btn1 = Button(win, text="ce", command=btnclear,  height=5, width=10).grid(row=1,column=1)
btn2 = Button(win, text="c", command=btnclear, height=5, width=10).grid(row=1,column=2)
btn3 = Button(win, text="xx", command=btnclear, height=5, width=10).grid(row=1,column=3)
btn5 = Button(win, text="/", command=lambda:btnclick("/"), height=5, width=10).grid(row=1,column=4)
btn6 = Button(win, text="x^1/2", command=lambda:btnclick("**(1/2)"), height=5, width=10).grid(row=2,column=0)
btn7 = Button(win, text="7", command=lambda:btnclick(7), height=5, width=10).grid(row=2,column=1)
btn8 = Button(win, text="8", command=lambda:btnclick(8), height=5, width=10).grid(row=2,column=2)
btn9 = Button(win, text="9", command=lambda:btnclick(9), height=5, width=10).grid(row=2,column=3)
btn10 = Button(win, text="x", command=lambda:btnclick("*"), height=5, width=10).grid(row=2,column=4)
btn11 = Button(win, text="x^2", command=lambda:btnclick("**2"), height=5, width=10).grid(row=3,column=0)
btn12 = Button(win, text="4",  command=lambda:btnclick(4), height=5, width=10).grid(row=3,column=1)
btn13 = Button(win, text="5", command=lambda:btnclick(5), height=5, width=10).grid(row=3,column=2)
btn14 = Button(win, text="6", command=lambda:btnclick(6), height=5, width=10).grid(row=3,column=3)
btn15 = Button(win, text="-", command=lambda:btnclick("-"), height=5, width=10).grid(row=3,column=4)
btn16 = Button(win, text="x^3", command=lambda:btnclick("**3"), height=5, width=10).grid(row=4,column=0)
btn17 = Button(win, text="1", command=lambda:btnclick(1), height=5, width=10).grid(row=4,column=1)
btn18 = Button(win, text="2", command=lambda:btnclick(2), height=5, width=10).grid(row=4,column=2)
btn19 = Button(win, text="3", command=lambda:btnclick(3), height=5, width=10).grid(row=4,column=3)
btn20 = Button(win, text="+",  command=lambda:btnclick("+"), height=5, width=10).grid(row=4,column=4)
btn21 = Button(win, text="1/x",  command=lambda:btnclick("1/x"), height=5, width=10).grid(row=5,column=0)
btn22 = Button(win, text="+/-",  command=lambda:btnclick("+/-"), height=5, width=10).grid(row=5,column=1)
btn23 = Button(win, text="0",  command=lambda:btnclick(0), height=5, width=10).grid(row=5,column=2)
btn24 = Button(win, text=".",  command=lambda:btnclick("."), height=5, width=10).grid(row=5,column=3)
btn25 = Button(win, text="=", command=btnequal, height=5, width=10).grid(row=5,column=4)



win.mainloop()
