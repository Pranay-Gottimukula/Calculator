from tkinter import *
from tkinter.ttk import *
from tkinter import font

disExp = ''
mathExp = ''
mode = 'a'
temploghold = ''
tempsinhold = ''
tempcoshold = ''
temptanhold = ''

# Factorial function to return factorial of a number,it is used in sin, cos, tan functions
def fact(n):
    if n > 1:
        return n * fact(n-1)    # Passing recursion
    elif n == 1:
        return 1
    elif n == 0:
        return 1
    elif n < 0:
        print("factorial cant be negetive error")


# Logarithm funtion
def log(a):

    # Converting value of input into form of A*(10^n)
    '''
    Here A is a number whose value is between 1 and 0.1,
    it is done because taylor series is only for small numbers,
    we pass A through taylor series and add it to n to get result
    '''
    if a > 0:
        n = 0
        while (a > 1) | (a < 0.1):
            if a > 1:
                a = a / 10
                n += 1

            elif a < 0.1:
                a = a * 10
                n -= 1

        # Using Taylor series to find logarithm of small values
        val = 0
        for i in range(1, 500, 1):
            val = val + ((float(a) - 1) ** i) * ((-1) ** (i + 1)) / i  # Expansion for natural logarithm

        return format(n + (val / 2.30258509299), ".6f")  # Converting into value of logarithm with base 10
    
    else:
        return "Not a number"


# Sine function works on Taylor series
def sin(a):
    a = a / 180 * 3.14159265359
    val = 0
    for i in range(1, 50, 1):
        val = val + (float(a) ** (2*i - 1)) * ((-1) ** (i + 1)) / fact(2*i - 1)

    return format(val, ".6f")


# Cosine function works on Taylor series
def cos(a):
    a = a / 180 * 3.14159265359
    val = 0
    for i in range(0, 50, 1):
        val = val + (float(a) ** (2*i)) * ((-1) ** i) / fact(2*i)

    return format(val, ".6f")


# Use sine and cosine functions to fin tan value
def tan(a):

    try:
        val = float(sin(a)) / float(cos(a))

    except ZeroDivisionError:   # trying to catch zero error
        return "Undefined"

    return format(val, ".6f")


def intake(char):
    global mathExp
    global disExp
    global mode
    global temploghold

    if mode == "a": 
        disExp = disExp + str(char)
        mathExp = mathExp + str(char)
        equ.set(disExp)

    elif mode == "log":
        if str(char) == ")" :
            logval = log(int(eval(temploghold)))
            mathExp = mathExp + str(logval)
            disExp = disExp + str(char)
            equ.set(disExp)
            temploghold = ''
            mode = 'a'

        
        else:
            temploghold = temploghold + str(char)
            disExp = disExp + str(char)
            equ.set(disExp)

    elif mode == "sin":
        global tempsinhold
        if str(char) == ")" :
            sinval = sin(int(eval(tempsinhold)))
            mathExp = mathExp + str(sinval)
            disExp = disExp + str(char)
            equ.set(disExp)
            tempsinhold = ''
            mode = 'a'

        
        else:
            tempsinhold = tempsinhold + str(char)
            disExp = disExp + str(char)
            equ.set(disExp)

    
    elif mode == "cos":
        global tempcoshold
        if str(char) == ")" :
            cosval = cos(int(eval(tempcoshold)))
            mathExp = mathExp + str(cosval)
            disExp = disExp + str(char)
            equ.set(disExp)
            tempcoshold = ''
            mode = 'a'

        
        else:
            tempcoshold = tempcoshold + str(char)
            disExp = disExp + str(char)
            equ.set(disExp)


    elif mode == "tan":
        global temptanhold
        if str(char) == ")" :
            tanval = tan(int(eval(temptanhold)))
            mathExp = mathExp + str(tanval)
            disExp = disExp + str(char)
            equ.set(disExp)
            temptanhold = ''
            mode = 'a'

        
        else:
            temptanhold = temptanhold + str(char)
            disExp = disExp + str(char)
            equ.set(disExp)





def enter():
    try:
        global mathExp
        global disExp
        val = str(eval(str(mathExp)))
        equ.set(val)
        mathExp = ''
        disExp = ''


    except SyntaxError or ZeroDivisionError:
        mathExp = ''
        disExp = ''
        equ.set('ERROR')


def allClear():    # String slicing learn
    global mathExp
    global disExp
    mathExp = ''
    disExp = ''
    equ.set("")


def clear():    # String slicing learn
    global mathExp
    global disExp
    mathExp = mathExp[0:-1]
    disExp = disExp[0:-1]
    equ.set(disExp)


def takelog():
    global mathExp
    global disExp
    global mode
    mode = 'log'
    disExp = disExp + "log("
    equ.set(disExp)


def takesin():
    global mathExp
    global disExp
    global mode
    mode = 'sin'
    disExp = disExp + "sin("
    equ.set(disExp)


def takecos():
    global mathExp
    global disExp
    global mode
    mode = 'cos'
    disExp = disExp + "cos("
    equ.set(disExp)


def taketan():
    global mathExp
    global disExp
    global mode
    mode = 'tan'
    disExp = disExp + "tan("
    equ.set(disExp)


if __name__ == "__main__":

    root = Tk()
    root.maxsize(565, 555)
    root.minsize(565, 555)
    root.configure(background='#070714')
    print(font.families())
    style = Style()

    style.configure('W.TButton', font=('Cambri math', 10, 'bold'), foreground='black')
    equ = StringVar()
    canvas = Canvas(root, height='555', width='565', bg='#070714')
    canvas.pack()

    frame = Frame(root)
    frame.place(relx=0.035, rely=0.034, relwidth=0.93, relheight=0.2)

    label = Label(frame, textvariable=equ, font=('Bahnschrift SemiBold', 30))
    label.pack()

    numpad = Frame(root)
    numpad.place(relx=0.035, rely=0.25, relwidth=0.93, relheight=0.72)

    ac = Button(numpad, text='AC', style="W.TButton", command=(lambda: allClear()))
    ac.grid(row=0, column=0, ipadx=9, ipady=27)

    c = Button(numpad, text='C', style="W.TButton", command=(lambda: clear()))
    c.grid(row=0, column=1, ipadx=9, ipady=27)

    mul = Button(numpad, text='×', style="W.TButton", command=(lambda: intake('*')))
    mul.grid(row=0, column=2, ipadx=9, ipady=27)

    div = Button(numpad, text='÷', style="W.TButton", command=(lambda: intake('/')))
    div.grid(row=0, column=4, ipadx=9, ipady=27)

    button7 = Button(numpad, text="7", style="W.TButton", command=(lambda: intake(7)))
    button7.grid(row=1, column=0, ipadx=9, ipady=27)

    button8 = Button(numpad, text='8', style="W.TButton", command=(lambda: intake(8)))
    button8.grid(row=1, column=1, ipadx=9, ipady=27)

    button9 = Button(numpad, text='9', style="W.TButton", command=(lambda: intake(9)))
    button9.grid(row=1, column=2, ipadx=9, ipady=27)

    minus = Button(numpad, text='-', style="W.TButton", command=(lambda: intake('-')))
    minus.grid(row=1, column=4, ipadx=9, ipady=27)

    button4 = Button(numpad, text='4', style="W.TButton", command=(lambda: intake(4)))
    button4.grid(row=2, column=0, ipadx=9, ipady=27)

    button5 = Button(numpad, text='5', style="W.TButton", command=(lambda: intake(5)))
    button5.grid(row=2, column=1, ipadx=9, ipady=27)

    button6 = Button(numpad, text='6', style="W.TButton", command=(lambda: intake(6)))
    button6.grid(row=2, column=2, ipadx=9, ipady=27)

    plus = Button(numpad, text='+', style="W.TButton", command=(lambda: intake('+')))
    plus.grid(row=2, column=4, ipadx=9, ipady=27)

    button1 = Button(numpad, text='1', style="W.TButton", command=(lambda: intake(1)))
    button1.grid(row=3, column=0, ipadx=9, ipady=27)

    button2 = Button(numpad, text='2', style="W.TButton", command=(lambda: intake(2)))
    button2.grid(row=3, column=1, ipadx=9, ipady=27)

    button3 = Button(numpad, text='3', style="W.TButton", command=(lambda: intake(3)))
    button3.grid(row=3, column=2, ipadx=9, ipady=27)

    dot = Button(numpad, text='.', style="W.TButton", command=(lambda: intake(".")))
    dot.grid(row=3, column=4, ipadx=9, ipady=27)

    button0 = Button(numpad, text='0', style="W.TButton", command=(lambda: intake(0)))
    button0.grid(row=4, column=1, ipadx=9, ipady=27)

    openbrac = Button(numpad, text='(', style="W.TButton", command=(lambda: intake('(')))
    openbrac.grid(row=4, column=0, ipadx=9, ipady=27)

    closebrac = Button(numpad, text=')', style="W.TButton", command=(lambda: intake(')')))
    closebrac.grid(row=4, column=2, ipadx=9, ipady=27)

    logButton = Button(numpad, text='log', style="W.TButton", command=(lambda: takelog()))
    logButton.grid(row=4, column=3, ipadx=9, ipady=27)

    enterButton = Button(numpad, text='ENTER', style="W.TButton", command=(lambda: enter()))
    enterButton.grid(row=4, column=4, ipadx=9, ipady=27)

    sinButton = Button(numpad, text='sin', style="W.TButton", command=(lambda: takesin()))
    sinButton.grid(row=0, column=3, ipadx=9, ipady=27)

    cosButton = Button(numpad, text='cos', style="W.TButton", command=(lambda: takecos()))
    cosButton.grid(row=1, column=3, ipadx=9, ipady=27)

    tanButton = Button(numpad, text='tan', style="W.TButton", command=(lambda: taketan()))
    tanButton.grid(row=2, column=3, ipadx=9, ipady=27)

    expButton = Button(numpad, text='^', style="W.TButton", command=(lambda: intake('**')))
    expButton.grid(row=3, column=3, ipadx=9, ipady=27)

    root.title('Calculator.UI')
    root.mainloop()

