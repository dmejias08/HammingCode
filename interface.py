from operator import pos
from unittest.mock import DEFAULT
from conversions import *
from hammingCode import *
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Table():
    def __init__(self,root, total_rows, total_columns, lst):
        self.entries = []
        for i in range(total_rows):
            rowOfEntries = []
            for j in range(total_columns):
                state = DISABLED
                width = 5
                if j > 17:
                    width = 7
                elif j == 0:
                    width = 10;
                if i == 1 and j!=0 and j!=1 and j!=2 and j!=4 and j!=8 and j<19:
                    state = NORMAL
                self.e = Entry(root, width=width, fg='blue', font=('Arial', 9), disabledbackground="white", disabledforeground="blue",)
                self.e.insert(END, lst[i][j])
                self.e.config(state= state)
                self.e.grid(row=i, column=j)
                rowOfEntries.append(self.e)
            self.entries.append(rowOfEntries)


class HammingInterface():
    def __init__(self, data, parity):
        hammingWindow=Toplevel()
        hammingWindow.title("Hamming Code") 
        hammingWindow.minsize(1000,700)
        hammingWindow.resizable(width=NO, height=NO)

        backgroundPanel=Canvas(hammingWindow, width=1000, height=700, background="white") #creación del canvas de la ventana principal
        backgroundPanel.place(x=0,y=0, anchor=NW)

        hammingPanel=Canvas(hammingWindow, width=600, height=500, background="white") #creación del canvas de la ventana principal
        hammingPanel.place(x=50,y=500, anchor=NW)

        decimalLabel=Label(hammingWindow, font=fnt, background="white", text="Decimal: "+str(octalToDecimal(int(data))))
        decimalLabel.place(x=50,y=10,anchor=NW)

        hexaLabel=Label(hammingWindow, font=fnt, background="white", text="Hexadecimal: "+str(octolToBinaryOrHexa(int(data),16)))
        hexaLabel.place(x=50,y=60,anchor=NW)
        
        binaryLabel=Label(hammingWindow, font=fnt, background="white", text="Binario: "+str(octolToBinaryOrHexa(int(data),2)))
        binaryLabel.place(x=50,y=110,anchor=NW)

        lst = [[''         ,'p1','p2','d1','p3','d2','d3','d4','p4','d5','d6','d7','d8','d9','d10','d11','p5' ,'d12'     ,'Prueba p','Bit p', 'Comp'],
            ['Datos(sin p)',''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''   ,''   ,''   ,''        ,''        ,''     ,''],
            ['p1'          ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''   ,''   ,''   ,''        ,''        ,''     ,''],
            ['p2'          ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''   ,''   ,''   ,''        ,''        ,''     ,''],
            ['p3'          ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''   ,''   ,''   ,''        ,''        ,''     ,''],
            ['p4'          ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''   ,''   ,''   ,''        ,''        ,''     ,''],
            ['p5'          ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''   ,''   ,''   ,''        ,''        ,''     ,''],
            ['Datos(con p)',''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''   ,''   ,''   ,''        ,''        ,''     ,'']]
        
        rows = len(lst)
        columns = len(lst[0])
        tempText = str(octolToBinaryOrHexa(int(data),2))

        self.encoder = Hamming(str(octolToBinaryOrHexa(int(data),2)),parity)
        hammingCodeWithZerosOG = self.encoder.insertZeroToRedudantBits(str(octolToBinaryOrHexa(int(data),2)), self.encoder.parityPositionsList)
        encodedOG = self.encoder.defineParityBits(hammingCodeWithZerosOG, self.encoder.parityPositionsList, parity)

        try:
            for j in range(columns):
                if j!=0 and j!=1 and j!=2 and j!=4 and j!=8 and j!=16 and j<19:
                    lst[1][j] = tempText[0]
                    lst[7][j] = tempText[0]
                    tempText=tempText[1:]
        except:
            pass

        for i in range(rows):
            n = 0
            for j in range(columns):
                if i > 1 and j > 2**n and i < 7 and j < 19:
                    try:
                        char = ("0000"+str(decimalToBinary(j)))[-1*i+1]
                        if char == "1":
                            lst[i][j] = lst[1][j];
                        if j==1 or j==2 or j==4 or j==8 or j==16:
                            n+=1
                    except:
                        pass
            n = 0
        m = 0
        while m < 5:
            oneCounter = 0
            for j in range(columns-(2**m)-2):
                if lst[m+2][(2**m)+j] == "1":
                    oneCounter+=1
            parityChar = ""
            if parity == "par":
                if oneCounter % 2 == 0:
                    parityChar = "0"
                else:
                    parityChar = "1"
            else:
                if oneCounter % 2 == 0:
                    parityChar = "1"
                else:
                    parityChar = "0"
            lst[m+2][2**m] = parityChar
            lst[7][2**m] = parityChar
            lst[m+2][18] = parityChar
            m+=1

        dataTable = Table(hammingPanel,rows,columns,lst)

        nombres = list(str(octolToBinaryOrHexa(int(data),2)))
        valores = []
        FLAG = True
        for element in nombres:
            if element == "1":
                if FLAG:
                    FLAG = False
                else:
                    FLAG = True;
            if FLAG:
                valores.append("1")
            else:
                valores.append("0")
        print(nombres)
        print(valores)

        graphArea = Text(hammingWindow, background="white", highlightthickness=0, highlightcolor="white", height=13, width=110, wrap="none", borderwidth=0)
        graphArea.place(x=50,y=200) 
        graphArea.insert(END,"\t")
        
        for element in nombres:
            graphArea.insert(END,element+"\t")
        
        graphArea.insert(END,"\n\n")
        graphArea.insert(END,"_____")

        for element in valores:
            if element == "1":
                graphArea.insert(END,"________")
            else:
                graphArea.insert(END,"        ")
        
        graphArea.insert(END,"\n\n")
        graphArea.insert(END,"     ")

        for element in valores:
            if element == "0":
                graphArea.insert(END,"________")
            else:
                graphArea.insert(END,"        ")
        
        graphArea.config(state=DISABLED)

        errorLabel=Label(hammingWindow, font=fnt, text="", background="white")
        errorLabel.place(x=50,y=450,anchor=NW)

        def back():
            mainWindow.deiconify()
            hammingWindow.destroy()

        def findError():
            newString = ""
            encoder = ""
            for j in range(columns-4):
                newString += (dataTable.entries[1][j+1]).get()
            positionError = ""
            try:
                encoderNew = Hamming(newString,parity)
                correct = ""
                hammingCodeWithZeros = encoderNew.insertZeroToRedudantBits(newString, encoderNew.parityPositionsList)
                encoded = encoderNew.defineParityBits(hammingCodeWithZeros, encoderNew.parityPositionsList, parity)

                for j in range(columns-4):
                    correct += (dataTable.entries[7][j+1]).get()

                (dataTable.entries[1][18]).config(state=NORMAL)
                (dataTable.entries[2][18]).config(state=NORMAL)
                (dataTable.entries[3][18]).config(state=NORMAL)
                (dataTable.entries[4][18]).config(state=NORMAL)
                (dataTable.entries[5][18]).config(state=NORMAL)
                (dataTable.entries[6][18]).config(state=NORMAL)

                if encoded[0] == correct[0]:
                    positionError="0"+positionError
                else:
                    positionError="1"+positionError;
                if encoded[1] == correct[1]:
                    positionError="0"+positionError
                else:
                    positionError="1"+positionError;
                if encoded[3] == correct[3]:
                    positionError="0"+positionError
                else:
                    positionError="1"+positionError;
                if encoded[7] == correct[7]:
                    positionError="0"+positionError
                else:
                    positionError="1"+positionError;
                if encoded[15] == correct[15]:
                    positionError="0"+positionError
                else:
                    positionError="1"+positionError;

            except Exception as e:
                msgbox=Toplevel()
                msgbox.minsize(500,200)
                message=Label(msgbox,text="Debe ingresar un dígito nada más, y binario",font=fnt)
                message.place(x=250, y=100, anchor="center")

            try:
                detectError=int(positionError,2)
                if(detectError==0):
                    errorLabel.configure(text="There is no error in the received message.")
                else:
                    errorLabel.configure(text="The position of error is "+ str(detectError)+ " from the left")
            except:
                pass

        backButton = Button(hammingWindow, text='Back', font=fnt, command=back)
        backButton.place(x=1000, y=0, anchor=NE)

        findError = Button(hammingWindow, text='FindErr', font=fnt, command=findError)
        findError.place(x=950, y=450, anchor=NE)

        hammingWindow.mainloop() 

fnt=("Arial",14)

mainWindow=Tk()
mainWindow.title("Hamming Code")
mainWindow.minsize(600,600) 
mainWindow.resizable(width=NO, height=NO)

mainPanel=Canvas(mainWindow, width=600, height=800) #creación del canvas de la ventana principal
mainPanel.place(x=0,y=0)

welcomeLabel=Label(mainPanel, font=fnt, fg="black", text="Ingrese un número octal:")
welcomeLabel.place(x=300,y=225,anchor=CENTER)

numberString = StringVar() #string dinámico
numberEntry= Entry(mainPanel, width=14, font=fnt, textvariable = numberString, justify=CENTER)

def validate(event):
        text = numberString.get()
        text = "".join([char for char in text if char in set(list("01234567"))])
        numberString.set(text)

numberEntry.bind("<KeyRelease>", validate)
numberEntry.place(x=300, y=275, anchor=CENTER)

def limitador(numberString): #limita el texto a 4 caracteres
    if numberString.get()!="":
        numberString.set(numberString.get()[:4])

numberString.trace("w", lambda *args: limitador(numberString))

currentParity = StringVar()
combobox = ttk.Combobox(mainPanel, textvariable=currentParity, state="readonly",)
combobox['values'] = ('impar', 'par')
combobox.place(x=300, y=375, anchor=CENTER)

def checkEntry(): #check del box de nombre que no esté vacío y corre nivel 1
    if numberEntry.get()=="" or combobox.get()=="":
        msgbox=Toplevel()
        msgbox.minsize(500,200)
        message=Label(msgbox,text="Debe ingresar un número octal y elegir tipo de paridad",font=fnt)
        message.place(x=250, y=100, anchor="center")
    else:
        mainWindow.withdraw()
        interface = HammingInterface(numberEntry.get(),combobox.get())

runProgram=Button(mainPanel, text='Run', font=fnt, command=checkEntry)
runProgram.place(x=300,y=325, anchor=CENTER)


mainWindow.mainloop()


