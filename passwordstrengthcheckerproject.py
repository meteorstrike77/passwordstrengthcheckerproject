from tkinter import *
import random as r
import re 


root = Tk()
root.title("Password Strength Checker")
root.geometry("600x600")
root.configure(background = "lightseagreen")

headinglabel = Label(root, text = "Password Strength Checker")
headinglabel.configure(font = ("Times", 25, "bold"))
headinglabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)

instructionlabel = Label(root, text = "Enter your password in the input")
instructionlabel.configure(font = ("Times", 13))
instructionlabel.place(relx = 0.5, rely = 0.25, anchor = CENTER)

enterpasswordinput = Entry(root, text = "Enter Password")
enterpasswordinput.place(relx = 0.5, rely = 0.3, anchor = CENTER)

passwordscorelabel = Label(root, text = "Enter Password")
passwordscorelabel.configure(font = ("Times", 10, "roman"))
passwordscorelabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)

symbols = ['!', '@', "#", '%', '&']
lowercaseletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
uppercaseletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
headtail = ['Head', 'Tail']




data = [[['1', '2', '3','4','5','6','7','8','9'], 
         ["Head", "Tail"], 
         ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"], 
         ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 
         ["!", "@", "#", "%", "&"]]]

count = 0


def check_password():
    global count
    global headtail
    userpassword = enterpasswordinput.get()
    userpasswordlength = len(userpassword)
    
    count = 0
    
    if re.search("Head|Tail", userpassword):
        count = count + 2
        print(count)
    
    if re.search("A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z", userpassword):
        count = count + 2
        print(count)
    
    if re.search("a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z", userpassword):
        count = count + 2
        print(count)
    
    if re.search("1|2|3|4|5|6|7|8|9|0", userpassword):
        count = count + 2
        print(count)
        
    if re.search("!|@|#|%|&", userpassword):
        count = count + 2
        print(count)
        
    if userpasswordlength >= 8:
        count = count + 2
        print(count)
        
    if count == 12:
        print("Password is Strong Enough!")
        passwordscorelabel["text"] = "Password is Strong Enough! A change is not necessary."
        
    else:
        print("Password is not Strong Enough!")
        passwordscorelabel["text"] = "A strong password contains at least one uppercase letter, one lowercase letter, one number, and one symbol. The entered password was determined to not be strong enough. A new password will be generated at user request."
        
        
        
checkpasswordbtn = Button(root, text = "Check Password", bg = "aquamarine4", fg = "white", command = check_password)  
checkpasswordbtn.configure(font = ("Times", 10, "roman"))
checkpasswordbtn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

newpasswordlabel = Label(root)
newpasswordlabel.place(relx = 0.7, rely = 0.9, anchor = CENTER)

newpassword = ""
   
def generate_password():
    global newpassword
    rn1 = r.randint(0,8)
    rn2 = r.randint(0,1)
    rn3 = r.randint(0,13)
    rn4 = r.randint(0,11)
    rn5 = r.randint(0,4)
    
    char1 = str(data[0][0][rn1])
    char2 = str(data[0][1][rn2])
    char3 = str(data[0][2][rn3])
    char4 = str(data[0][3][rn4])
    char5 = str(data[0][4][rn5])
    
    newpassword = char1 + char2 + char3 + char4 + char5
    print(newpassword)
    
    enterpasswordinput.delete(0, END)
    enterpasswordinput.insert(END,newpassword)

generatenewpasswordbtn = Button(root, text = "Generate New Password", bg = "blue", fg = "white", command = generate_password)
generatenewpasswordbtn.configure(font = ("Times", 10, "roman"))
generatenewpasswordbtn.place(relx = 0.5, rely = 0.6, anchor = CENTER)


root.mainloop()