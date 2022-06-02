#GUI calculator written by Shubham Rachha aka Titan Spy
from tkinter import *
expression = ""    

#This function will get the operation on screen when user press the button of our GUI screen
def press(num): 
    global expression                  #This is the global variable used by the program
    expression = expression + str(num)
    var.set(expression)
    expression = entry.get()

#This function will execute and return the result to the user
def evaluate():
    try:
        global expression

        total = str(eval(expression))           #This will evaluate the input
        var.set(total)                          #This will show the output on the entry widget

        expression = ""
    except ZeroDivisionError:                   #If calulation is done by 0 then this will raise the error
        var.set("Error: division by 0 is not allowed")
        expression = ""
    except:                                     #This will handle when any other wrong calculation done by user
        var.set("error")
        expression = ""

#This will used to clear the contents of GUI screen
def buttonC():
    """This function is created to clear the of entry widget when user will click on clear button"""
    global expression
    expression = ""
    var.set("")

#The main window of calculator/GUI of calculator
if __name__ == "__main__":
    root=Tk()
    root.geometry("210x296")
    root.title("Calculator")
    root.minsize(210,296)
    root.maxsize(210,296)
    var = StringVar()

    #This is the entry widget which will used to get and show the result and this entry is in readonly which
    #means user cannot enter any character/number in this field, the input can only get by buttons
    entry = Entry(root,borderwidth = 10,relief = SUNKEN,textvariable= var,justify= RIGHT, state= "readonly")
    entry.pack(fill = X)

    #Clear Button
    C = Button(root,text="C",border = 3,padx = 11,pady = 7,bg = "gray",font = "helvetica 14 bold",command=buttonC)
    C.place(x=0, y=35)

    #Button to find square root
    sqrt = Button(root,text="sqrt",border = 3,padx = 4,pady = 10,bg = "gray",font = "helvetica 12 bold",command=lambda:press("** 0.5"))
    sqrt.place(x=53, y=35)

    #Button to find power of number
    power = Button(root,text="x^y",border = 3,padx = 6,pady = 10,bg = "gray",font = "helvetica 12 bold",command=lambda:press("**"))
    power.place(x=105,y=35)

    # button to percentage of number
    percent = Button(root,text="%",border = 3,padx = 8,pady = 5,bg = "gray",font = "helvetica 15 bold",command=lambda:press("%"))
    percent.place(x=159,y=35)

    #Button which will hold value 1
    one = Button(root,text="1",border = 3,padx = 12,pady = 5, bg = "gray70",font = "helvetica 15 bold",command=lambda: press(1))
    one.place(x=0,y=88)

    #Button which will hold value 2
    two = Button(root,text="2",border = 3,padx = 12,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press(2))
    two.place(x=53,y=88)

    #Button which will hold value 3
    three = Button(root,text="3",border = 3,padx = 12,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press(3))
    three.place(x=106,y=88)

    #Button which will hold value of + operator
    plus = Button(root,text="+",border = 3,padx = 11,pady = 5,bg = "gray",font = "helvetica 15 bold",command= lambda: press("+"))
    plus.place(x=159,y=88)

    #Button which will hold value 4
    four = Button(root,text="4",border = 3,padx = 12,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press(4))
    four.place(x=0,y=140)

    #Button which will hold value 5
    five = Button(root,text="5",border = 3,padx = 12,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press(5))
    five.place(x=53,y=140)

    #Button which will hold value 6
    six = Button(root,text="6",border = 3,padx = 12,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press(6))
    six.place(x=106,y=140)

    #Button which will hold value of - operator
    minus = Button(root,text="-",border = 3,padx = 13,pady = 5,bg = "gray",font = "helvetica 15 bold",command= lambda: press("-"))
    minus.place(x=159,y=140)

    #Button which will hold value 7
    seven = Button(root,text="7",border = 3,padx = 12,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press(7))
    seven.place(x=0,y=192)

    #Button which will hold value 8
    eight = Button(root,text="8",border = 3,padx = 12,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press(8))
    eight.place(x=53,y=192)

    #Button which will hold value 9
    nine = Button(root,text="9",border = 3,padx = 12,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press(9))
    nine.place(x=106,y=192)

    #Button which will hold value of * operator
    multiply = Button(root,text="*",border = 3,padx = 13,pady = 5,bg = "gray",font = "helvetica 15 bold",command= lambda: press("*"))
    multiply.place(x=159,y=192)

    #Button which will hold value 0
    zero = Button(root,text="0",border = 3,padx = 12,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press(0))
    zero.place(x=0,y=244)

    #Button which will hold value .(decimal point)
    point = Button(root,text=".",border = 3,padx = 14,pady = 5,bg = "gray70",font = "helvetica 15 bold",command= lambda: press("."))
    point.place(x=53,y=244)

    #Button which will hold value = (equalto)
    equal2 = Button(root,text="=",border = 3,padx = 12,pady = 5,bg = "orange",font = "helvetica 15 bold",command= evaluate)
    equal2.place(x=106,y=244)

    #Button which will hold value of / (divide) operator
    divide = Button(root,text="/",border = 3,padx = 14,pady = 5,bg = "gray",font = "helvetica 15 bold",command= lambda: press("/"))
    divide.place(x=159,y=244)


    mainloop()


#Author: Shubham Rachha aka Titan Spy
#Follow us on Instagram: https://www.instagram.com/titan_spy04/
#Subsribe our channel for more programming and hacking related content: 
#Visit our website: https://titanspy.blogspot.com/