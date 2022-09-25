import tkinter as tk

def convert():
    c = int(e1.get()) #collects the value entered in the empty textbox and uses it in this function
    f = ((c*9)/(5))+32 #celsius conversion formula
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f) #prints the answer and places it in this empty textbox
    t1.config(state='disabled') #prevents user from altering the answer placed in textbox
 
def exit():
    window.destroy() #exits the program


window = tk.Tk()
window.geometry("450x250")
window.config(bg="#FFDEAD")
window.resizable(width=False,height=False)
window.title('Celsius to Fahrenheit Converter!')
 
l1 = tk.Label(window,text="Celsius to Fahrenheit Converter",font=("Arial", 12),fg="black",bg="#FFDEAD") #label 1
l2= tk.Label(window,text="Enter temperature in Celsius: ",font=("Arial", 10,"bold"),fg="black",bg="#FFDEAD")#label 2
l3= tk.Label(window,text="Temperature in Fahrenheit is: ",font=("Arial", 10,"bold"),fg="black",bg="#FFDEAD")#label 3
 
empty_l1 = tk.Label(window,bg="#FFDEAD") 
empty_l2 = tk.Label(window,bg="#FFDEAD")
empty_l3 = tk.Label(window,bg="#FFDEAD")
empty_l4 = tk.Label(window,bg="#FFDEAD")
#creates an empty space between elments. not necessary but makes the gui looker neater
 
e1= tk.Entry(window,font=('Arial',10)) #allows the temperature in celsius to be entered
 
btn1 = tk.Button(window,text="Convert to Fahrenheit!",font=("Arial", 10),command=convert) #button connected to the convert function
btn2 = tk.Button(window,text="Exit application",font=("Arial", 10),command=exit) #button connected to the exit function, exits program when clicked
 
t1=tk.Text(window,state="disabled",width=15,height=0) #allows the textbox showing the answer to not be altered
 
l1.pack()
l2.pack()
e1.pack()
empty_l1.pack()
btn1.pack()
empty_l3.pack()
l3.pack()
t1.pack()
empty_l2.pack()
btn2.pack()
#packs all elements in a particular order. 
 
window.mainloop()