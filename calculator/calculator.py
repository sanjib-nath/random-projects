from tkinter import *

class Calculator():
    """A overall class to maintian the main programe"""

    def __init__(self):        
        #window settings
        self.window = Tk()
        self.window.title("Calculator")

        #colors
        self.other = "#9FCB98"
        self.row1_col = "#79AE6F"
        self.colume3_col = "#36753D"
        self.label_col = "#F2EDC2"
        
        #window geo
        self.window.geometry()
        self.window.resizable(False, False)

        #frame
        self.frame = Frame(self.window)

        #A+B A-B etc
        self.first_num = "0"
        self.oparetor = None
        self.last_num = None

        #label
        self.label_0 = Label(self.frame,
                             text ="",
                             font = ("arial", 20),
                             anchor = "e",
                             bg = self.label_col,
                             fg = "black",
                             width = 4)
        self.label = Label(self.frame,
                           text = "0",
                           font= ("arial", 45),
                           anchor= "e",
                           bg = self.label_col,
                           fg = "black",
                           width = 4)
        
        self.label_0.grid(row=0,column=0,
                        columnspan=4,
                        sticky="ew")
        
        self.label.grid(row = 1, column= 0,
                        columnspan= 4,
                        sticky= "ew")
        
        self.frame.pack()       
        
        #the buttons
        self.row1 = ["AC","C","%"] #row 2 
        self.colume3 = ["÷","x","-","+","="] #last colume
        self.row24 = ["7","8","9","4","5","6","1","2","3","0",".","()"] #row 3 to 5

        #bracket
        self.bracket = 0

        #methods
        self._draw_buttons()
        
    def _draw_buttons(self):
        """draw the all buttons"""

        for index, value in enumerate(self.row1):
            row = index // 3 + 2
            col = index % 3
            button = Button(self.frame,
                            text = value,
                            font = ("arial", 30),
                            width = 4-1, height= 1,
                            bg= self.row1_col,
                            activebackground= self.row1_col,
                            fg = "white",
                            activeforeground= "white",
                            command= lambda value = value: self.button_command(value)
                            )
            button.grid(row= row, column= col)

        for index, value in enumerate(self.colume3):
            row = index // 1 + 2
            col = index % 1 + 3
            button = Button(self.frame,
                            text = value,
                            font = ("arial", 30),
                            width = 4-1, height= 1,
                            bg = self.colume3_col,
                            activebackground= self.colume3_col,
                            fg = "white",
                            activeforeground = "white",
                            command = lambda value = value: self.button_command(value)
                            )
            button.grid(row= row, column= col)
    
        for index, value in enumerate(self.row24):
            row = index // 3 + 3
            col = index % 3
            button = Button(self.frame,
                            text = value,
                            font = ("arial", 30),
                            width = 4-1, height= 1,
                            bg= self.other,
                            activebackground= self.other,
                            fg = "white",
                            activeforeground= "white",
                            command = lambda value = value: self.button_command(value)
                            )
            button.grid(row= row, column= col)
        
    def button_command(self, value):
        """maintaian the button command"""

        if value in self.row1:
            if value == "AC":
                self.first_num = "0"
                self.oparetor = None
                self.last_num = None

                self.label["text"] = "0"
                self.label_0["text"] = ""
            
            elif value == "C":
                current = self.label["text"]

                if len(current) > 1:
                    self.label["text"] = current[:-1]
                
                else:
                    self.label["text"] ="0"
            
            else:
                percentage = float(self.label["text"]) / 100
                self.label["text"] = str(percentage)

        elif value in self.colume3:
            if value == "=":
                    if "(" not in self.label["text"]:
                        if "=" not in self.label_0["text"]:
                            B = self.label["text"]
                            self.label_0["text"] += B
                            self.label_0["text"] += value

                            expression = self.label_0["text"]
                            expression = expression[:-1]
                            expression = expression.replace("x", "*").replace("÷", "/")
                            

                            try:
                                result = eval(expression)
                                result = round(result, 2)
                                self.label["text"] = str(result)

                            except Exception:
                                self.label["text"] ="Error"

                    else:
                        current = self.label["text"]
                        self.label_0["text"] = current
                        self.label_0["text"] += value

                        current = current.replace("(", "*(")

                        try:
                            result = eval(current)
                            result = round(result, 2)
                            self.label["text"] = str(result)
                        
                        except Exception:
                            self.label("Error")


            else:
                if value in "+-x÷":
                    if "(" in self.label["text"]:
                        A = self.label["text"]
                        
                        if A[-1] in "+-x÷":
                            self.label["text"] = A[:-1]
                            self.label["text"] += value

                        else:
                            self.label["text"] += value
                        
                    else:   
                        A = self.label_0["text"]
                        B = self.label["text"]

                        if B == "0" and A[-1] in "+-x÷":
                            self.label_0["text"] = A[:-1]
                            self.label_0["text"] += value
            

                        else:
                            self.label_0["text"] += B
                            self.label_0["text"] += value
                            self.label["text"] = "0"
        else:
            if value == ".":
                if "." in self.label["text"]:
                    pass

                else:
                    self.label["text"] += value
            
            elif value == "()":
                if self.bracket == 0:
                    self.label["text"] += "("
                    self.bracket += 1
                
                elif self.bracket == 1:
                    self.label["text"] += ")"
                    self.bracket -= 1
    
            else:
                if self.label["text"] =="0":
                    self.label["text"] = value
                    
                else:
                    self.label["text"] += value                    

    def run_programe(self):
        """run the main programe"""

        self.window.mainloop()

if __name__ == '__main__':
    calculator = Calculator()
    calculator.run_programe()