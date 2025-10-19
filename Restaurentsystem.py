import tkinter  as tk

order_value = 0
menu = {
    "Pizza" : 150,
    "Momos" : 60,
    "Burger" : 80,
    "Sandwich" : 120,
    "Coffee" : 50,
    "Cold Coffee" : 80,
}

# Limitation is it currently use for single item at once

print(f"~Welcome to The Rotash Restaurent\n")
print("~Here is the menu")
for item, price in menu.items():
    print(f"{item}: ₹{price}")
print("                                                                                     ")
order = input("~What you want to order sir/ma'am: ").capitalize()

if order in menu:
    order_value += menu[order]
    print(order_value)
else:
    print(f"Item isn't available here!!")

again = input("you want to order anything else sir/ma'am? ").capitalize()
if again == "Yes":      
    order_2 = input("~What you want to order sir/ma'am: ").capitalize()
    if order_2 in menu:
        order_value += menu[order_2]
        print(order_value)
    else:
        print(f"Item isn't available here!!")
else:
    print("Thanks for visit our restaurent!")
order_item = (f"{order,order_2}: ₹{order_value}")


from tkinter import *
order_item = StringVar()
wd = Tk()
wd.geometry("420x420")
wd.title("Harsh Tiwari")
wd.config(background="skyblue",border=2)


order_item.set(order_item)
lbl = Label(wd,
            text ="Your bill",
            bg="skyblue",
            fg="white",
            font=("Arial", 30, "bold"),
            relief="groove",
            border=10)
lbl.pack(padx=10,pady=10)

oi = Label(wd,
            textvariable= order_item,
            bg="white",
            fg="black",
            font=("Arial", 30, "bold"),
            border=10)
oi.pack(padx=10,pady=10)

wd.mainloop()