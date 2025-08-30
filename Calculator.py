import tkinter as tk # tkinter library are import
# let's a create new Tkinter window

window =tk.Tk()
window.title("My Quick calculator") # the window name has been set
# an entry widget where the user input and result will be displayed

entry = tk.Entry(window, width= 40 , borderwidth = 5)
entry.grid(row = 0 ,column =0, columnspan =4 ,padx=10, pady=10) # the entry has been placed in the grid

# when a button is pressed this function will run
def button_click(value):  
    current = entry.get()         # get cureent text from the entry
    entry.delete(0 , tk.END)       #clear entry
    entry.insert(0 , current + value)      #add new value to existing text
    
    # function to perform calculation manually
def calculate():
         try:
            expression = entry.get()   # it takes in the user's compleete expression
            if "%" in expression:    # if there is a % in the expression
                number = float(expression.replace("%",""))    #it removes the % and then takes the number
                result= number / 100 # calculate the percentage
            elif "+" in expression:
                parts = expression.split("+")     #it splits based on the +
                result = float(parts[0]) + float(parts[1])    # they add
            elif "-" in expression:
                parts = expression.split("-")
                result= float(parts[0]) - float(parts[1])    # they subtract
            elif "*" in expression:
                parts = expression.split("*")
                result = float(parts[0]) * float(parts[1])    # they multiply
            elif "/" in expression:
                parts = expression.split("/")
                result = float(parts[0]) / float(parts[1])    # they divide
            else:
                result = "error"     # if nothing is found show an erroe
                
            entry.delete(0 ,tk.END)  #it removes the previous text
            entry.insert(0, str(result))  #they show the result
                
         except:
             entry.delete(0 ,tk.END)
             entry.insert(0 , "error")   #if there is an error,it show the error
             
             #function to clear the entry
def clear():
                    entry.delete(0 ,tk.END)   #it xlear the entry box
                    
                    #all buttons lable,row and columns are in the list
buttons = [
        ("7",1, 0), ("8",1 , 1), ("9", 1 ,2) ,("/", 1,3),
        ("4",2, 0) ,("5",2,1) ,("6", 2 ,2) ,("*" ,2,3),
        ("1",3, 0) ,("2" ,3 ,1) ,("3" ,3 ,2) ,("-" ,3,3),
        ("0" ,4,0) ,("." ,4 ,1) ,("=" ,4 ,2) ,("+" ,4,3),
        ("C",5,0) ,("%" ,5 ,1)        
        ]                 
                    
        # button have been created and place in a grid
for(text , row , col) in buttons:
        if text == "=" :
            button = tk.Button(window ,text=text,width=9,height=2,command= calculate)
        elif text =="C" :
            button = tk.Button(window , text=text,width=9,height=2,command=clear)
        else:
            button = tk.Button(window, text=text, width=9, height=2,command=lambda t=text: button_click(t))
        button.grid(row=row,column=col ) # the button is placed in the grid
            
window.mainloop()  # we run the window continuosly            
    




                                                                              
