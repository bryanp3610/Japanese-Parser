# Bryan Pham
# CS 351
#Single Line Lexer
#10-6-22

import re
# import tkinter as tk
from tkinter import * 
# from tkinter.ttk import * 
# from time import strftime
class Lexer:
    def __init__(self, root):
       self.counter = 0   
       self.top=root
       self.top.title("Lexical Analyzer for TinyPie")
       
       self.input = Text(self.top, width=50, height =20)
       self.input.grid(row=1, column=0, sticky=E)

       self.label = Label(self.top, text="        ")
       self.label.grid(row=0, column=2, sticky=W)
       
       self.label = Label(self.top, text= "Source Code Input")
       self.label.grid(row=0, column=0, sticky =  W)
       
       self.label = Label(self.top, text =  "Lexical Analyzed result: ")
       self.label.grid(row=0, column=3, sticky=W)
       
       self.output= Text(self.top, width = 50, height =20)
       self.output.grid(row=1, column=3, sticky=E)

       self.next = Button(self.top, text="  Next Line  ", command=self.nextline)
       self.next.grid(row=3, column=0, sticky=E)

       self.label = Label(self.top, text="Current Line: ")
       self.label.grid(row=2, column=0, sticky=W)

       self.count = Entry(self.top, width=3)
       self.count.grid(row=2, column=0, sticky=E)
       self.count.insert(INSERT, "0")
    #    self.count['state']='disabled' 

       self.end = Button(self.top, text="  QUIT  ", command=self.end)
       self.end.grid(row=3, column=3, sticky=E)
   
   
    def end(self):
        self.top.quit()
        #self.quit()        
       
       
    def CutOneLineTokens(self, s):
        list = []
        string = s
        while string != '':

            # Keywords:
            if re.search(r'^[a-z]+', string):
                x = re.search(r'^[a-z]+', string)
                key = string[x.start():x.end()]
                if key == "int":
                    out = f'<key, {key}>'
                    string = re.sub(r'^[a-z]+', '', string, 1)
                    list.append(out)
                elif key == "else":
                    out = f'<key, {key}>'
                    string = re.sub(r'^[a-z]+', '', string, 1)
                    list.append(out)
                elif key == "if":
                    out = f'<key, {key}>'
                    string = re.sub(r'^[a-z]+', '', string, 1)
                    list.append(out)
                elif key == "float":
                    out = f'<key, {key}>'
                    string = re.sub(r'^[a-z]+', '', string, 1)
                    list.append(out)

            # Separators:
            if re.search(r'[():"";]', string):
                x = re.search(r'[():"";]', string)
                key = string[x.start():x.end()]
                out = f'<separator, {key}>'
                string = re.sub(r'[():"";]', '', string, 1)
                list.append(out)

            # Identifiers:
            if re.search(r'[A-Z|a-z]+\d+|[a-z|A-Z]+', string):
                x = re.search(r'[A-Z|a-z]+\d+|[a-z|A-Z]+', string)
                key = string[x.start():x.end()]
                out = f'<identifier, {key}>'
                string = re.sub(r'[A-Z|a-z]+\d+|[a-z|A-Z]+', '', string, 1)
                list.append(out)

            # Operator:
            if re.search(r'[*=+>]', string):
                x = re.search(r'[*=+>]', string)
                key = string[x.start():x.end()]
                out = f'<operator, {key}>'
                string = re.sub(r'[*=+>]', '', string, 1)
                list.append(out)

            # Literals:
            if re.search(r'-?\d+\.\d+', string):
                x = re.search(r'-?\d+\.\d+', string)
                key = string[x.start():x.end()]
                out = f'<float_literal, {key}>'
                string = re.sub(r'-?\d+\.\d+', '', string, 1)
                list.append(out)
            # Int_literal:
            if re.match(r'-?\d+', string):
                x = re.match(r'-?\d+', string)
                key = string[x.start():x.end()]
                out = f'<int_literal, {key}>'
                string = re.sub(r'-?\d+', '', string, 1)
                list.append(out)
            # String_literal:
            if re.search(r'["]{1}[a-z|A-Z|0-9|\s]+', string):
                x = re.search(r'["]{1}[a-z|A-Z|0-9|\s]+["]{1}', string)
                key = string[x.start():x.end()]
                out = f'<string_literal, {key}>'
                string = re.sub(r'["]{1}[a-z|A-Z|0-9|\s]+["]{1}', '', string, 1)
                list.append(out)

            if re.match(r'\s', string):
                string = re.sub(r'\s', '', string)
        return list

    def nextline(self):
        user = self.input.get("1.0", END)
        inp = (user.splitlines())
        out = self.CutOneLineTokens(inp[self.counter])
        self.output.insert(INSERT, f'{out}\n')
        self.count.delete(0, END)
        self.count.insert(INSERT, (self.counter)+1)
        self.counter += 1

#open for user implementation
if __name__ == '__main__':
    tk = Tk()
    gui=Lexer(tk)
    tk.mainloop()
