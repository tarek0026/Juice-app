from tkinter import *
import webbrowser




index = Tk()
index.geometry("800x500")
index.title("Smoothie Paradise")
index.resizable(False, False)


im_logo = PhotoImage(file='photos/logo_app.png')
index.iconphoto(False, im_logo)

page3 = {}

def update_cart(item_name, price, amount):
    if item_name in page3:
        page3[item_name]["qty"] += amount
        if page3[item_name]["qty"] <= 0:
            del page3[item_name]
    else:
        if amount > 0:
            page3[item_name] = {"price": price, "qty": amount}

def show_cart():
    page2.place_forget()
    page3_frame = Frame(index, bg="#FFE969")
    page3_frame.place(x=0, y=0, width=800, height=500)
    y = 10
    for item_name, details in page3.items():
        Label(page3_frame, text=item_name, font=("Arial", 12), bg="#FFE969").place(x=10, y=y, width=200, height=30)
        Label(page3_frame, text=f"{details['qty']} x {details['price']}", font=("Arial", 12), bg="#FFE969").place(x=220, y=y, width=200, height=30)
        Label(page3_frame, text=f"{details['qty'] * details['price']}", font=("Arial", 12), bg="#FFE969").place(x=440, y=y, width=100, height=30)
        y += 40
    total = sum(details['qty'] * details['price'] for details in page3.values()) 
    vat = total * 0.14
    total_with_vat = total + vat
    Label(page3_frame, text=f"Total: {total_with_vat:.2f} (including 14% VAT)", font=("Arial", 12, "bold"), bg="#FFE969", fg="green").place(x=10, y=y, width=400, height=30)
    Button(page3_frame, text="Checkout", width=15, bg="green",command=lambda:show_frame(page4)).place(x=10, y=y + 40)
    # Button(page3_frame, text="Back to Menu", width=15, bg="blue", command=lambda:show_frame(page2)).place(x=675, y=470)
    Button(page3_frame, text="Back to Menu", width=15, bg="blue", command=lambda: page3_frame.place_forget() or page2.place(x=0, y=0, width=800, height=500)).place(x=675, y=470)







def show_frame(frame):  ###Using show_frame with tkraise() simplifies switching between frames, improves performance, and keeps the code organized and scalable.
    frame.tkraise()

# build pages
page1 = Frame(index, bg="white")
page2 = Frame(index, bg="#FFE969")
page4 = Frame(index, bg="#FFE969")

for oo in (page1, page2, page4):
    oo.place(x=0, y=0, width=800, height=500)

# ######PAGEEEEE1




##########photoooooo
photo_page1 = PhotoImage(file="photos/photo_home_page.png")
y=Label(page1,image=photo_page1).place(x=0,y=0,width=800,height=500)


l_intro= Label(page1, text="SMOOTHIE PARADISE", fg="yellow", bg="#afce9b", font=(("cairo", 20, "italic"))).place(x=265, y=0)
l_follow= Label(page1, text='Follow Us For More Updates!', fg="black", bg="yellow", font=("Times New Roman", 15, "italic")).place(x=0, y=395)
l_location= Label(page1, text='For Location', fg="black", bg="yellow", font=("Times New Roman", 15, "italic")).place(x=686, y=395)

face = "https://www.facebook.com/SmoothieParadise.egypt/"
insta = "https://www.instagram.com/smoothieparadise.egypt/?hl=ar"
tiktok = "https://www.tiktok.com/discover/smoothie-paradise-dokii"
location="https://maps.app.goo.gl/mxELsA7Dpc5txh1u6?g_st=iw"

# used the functions to put the link in an easy way and I can use them at any time if you need it
def facee():
    webbrowser.open_new(face)

def instaa():
    webbrowser.open_new(insta)

def tiktokk():
    webbrowser.open_new(tiktok)
def locationn() :
    webbrowser.open_new(location)
##logoo face

logoo1 = PhotoImage(file="photos/logo_face1.png")
y2 = Label(page1, image=logoo1, bg="#4267B2")

# logo insta
logoo2 = PhotoImage(file="photos/logo_insta1.png")
y3 = Label(page1, image=logoo2, bg="#E4405F")

# logo tiktok
logoo3 = PhotoImage(file="photos/logo_tik1.png")
y4 = Label(page1, image=logoo3, bg="#000000")
##logoo location
logoo4=PhotoImage(file="photos/logo_loc1.png")
y5 = Label(page1, image=logoo4, bg="#000000")
###logoooooo menu
logoo6=PhotoImage(file="photos/logo_menu1.png")
y7 = Label(page1, image=logoo6, bg="#000000")





b_face = Button(page1, text="Facebook", fg="white", bg="#4267B2", width=28, height =30,image=logoo1, font="Helvetica,16,bold", command=facee)
b_face.place(x=40,y=440)
b_insta = Button(page1, text="Instagram", fg="white", bg="#E4405F",image=logoo2, width=28, height=30, font="Helvetica,16,bold", command=instaa)
b_insta.place(x=90, y=440)
b_tiktok = Button(page1, text="Tiktok", fg="white", bg="#000000", width=28,image=logoo3, height=30, font="Helvetica,16,bold", command=tiktokk)
b_tiktok.place(x=150, y=440)
b_location = Button(page1, bg="red", width=28,image=logoo4, height=30, font="Helvetica,16,bold", command=locationn)
b_location.place(x=730, y=440)

l4 = Label(page1, text="أول براند متخصص في السموزي في مصر", bg="#afce9b", fg="white", font=("Dubai", 10, "bold"))
l4.place(x=599, y=40)
l5 = Label(page1, text="عصاير طبيعية بخامات %100", bg="#afce9b", fg="white", font=("Dubai", 10, "bold"))
l5.place(x=630, y=60)
l5 = Label(page1, text="عصاير بدون أي مواد حافظة", bg="#afce9b", fg="white", font=("Dubai", 10, "bold"))
l5.place(x=642, y=80)
btn_to_menu = Button(page1,width=0,height= 0, bg="white", font=("Helvetica", 14),image=logoo6, command=lambda: show_frame(page2))
btn_to_menu.place(x=0, y=60)


#### for arrow





def toggle_arrow(): ####
    global arrow_on
    if arrow_on:
        arrow_label.config(bg="red")  # اwhen arrow is on
    else:
        arrow_label.config(bg="black")  # when arrow is off
    arrow_on = not arrow_on
    page1.after(500, toggle_arrow)  
arrow_label = Label(page1, text="↓", font=("Arial", 8, "bold"), bg="gray", fg="white")
arrow_label.place(x=740, y=420)  


arrow_on = True #when it true start by red and when it false start by black
#to onnn arrow
toggle_arrow()
 



###page2




sections = [
    ("FRESH JUICES", [
        ("Apple", 45), ("Orange", 50), ("Strawberry", 40), ("Mango", 40), ("Lemon Mint", 30)
    ]),
    ("MILKSHAKE", [
        ("Vanilla Shake", 50), ("Oreo Shake", 55), ("Lotus Shake", 50),
        ("Pistachio Shake", 60), ("Strawberry Shake", 50)
    ]),
    ("SMOOTHIES", [
        ("Banana Smoothie", 60), ("Strawberry Smoothie", 65), ("Mango Smoothie", 60),
        ("Blueberry Smoothie", 70), ("Peach Smoothie", 65)
    ]),
    ("FRESCA", [
        ("Oreo", 35), ("Lotus", 35), ("Dark Chocolate", 35),
        ("White Chocolate", 35), ("Honey and Banana", 35)
    ])
]

x, y = 10, 10
for section_name, items in sections:
    section_height = 30 + (len(items) * 35)
    section_frame = Frame(page2, bg="#FFE969")
    section_frame.place(x=x, y=y, width=370, height=section_height)
    
    Label(section_frame, text=section_name, font=("Arial", 14, "bold"), bg="#FFE969", fg="green").place(x=10, y=5)
    item_y = 30
    for item_name, price in items:
        item_frame = Frame(section_frame, bg="#FFE969")
        item_frame.place(x=10, y=item_y, width=350, height=30)

        qty = IntVar(value=0)

        def add(qty=qty, item_name=item_name, price=price):
            current_qty = qty.get()
            qty.set(current_qty + 1)
            update_cart(item_name, price, 1)

        def subtract(qty=qty, item_name=item_name, price=price):
            if qty.get() > 0:
                current_qty = qty.get()
                qty.set(current_qty - 1)
                update_cart(item_name, price, -1)

        Label(item_frame, text=item_name, font=("Arial", 10), bg="#FFE969", fg="black").place(x=0, y=0, width=150, height=30)
        Label(item_frame, text=f"{price}", font=("Arial", 10), bg="#FFE969", fg="black").place(x=160, y=0, width=50, height=30)
        Button(item_frame, text="-", width=2, bg="#FFA500", command=subtract).place(x=220, y=0, width=30, height=30)
        Label(item_frame, textvariable=qty, font=("Arial", 10), bg="#FFE969").place(x=260, y=0, width=30, height=30)
        Button(item_frame, text="+", width=2, bg="#FFA500", command=add).place(x=300, y=0, width=30, height=30)

        item_y += 35

    x += 390
    if x > 780:
        x = 10
        y += section_height + 20

Button(page2, text="Return to Home", width=15, bg="blue",command=lambda: show_frame(page1)).place(x=10, y=470)
Button(page2, text="Go to Cart", width=15, bg="blue", command=show_cart).place(x=675, y=470)



#########page4


def order():
    # Get the user input
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()

    # Create a success or error message based on user input
    if name and address and phone:
        message_label.config(text="Order Successful! Your order will arrive in approx   15 minutes.", fg="green")
    else:
        message_label.config(text="Please fill in all fields.", fg="red")



# Create labels and entry widgets for the user to enter their name, address, and phone number
Label(page4, text="Name:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(page4, font=("Arial", 12), width=30, bd=2, relief="solid")
name_entry.grid(row=0, column=1, padx=10, pady=5)

Label(page4, text="Address:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
address_entry = Entry(page4, font=("Arial", 12), width=30, bd=2, relief="solid")
address_entry.grid(row=1, column=1, padx=10, pady=5)

Label(page4, text="Phone Number:", bg="#f0f0f0", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
phone_entry = Entry(page4, font=("Arial", 12), width=30, bd=2, relief="solid")
phone_entry.grid(row=2, column=1, padx=10, pady=5)

# Create the "Order" button with better styling
order_button = Button(page4, text="Order", font=("Arial", 14), bg="#4CAF50", fg="white", bd=0, relief="raised", width=20, height=2, command=order)
order_button.grid(row=3, column=0, columnspan=2, pady=20)

# Label for displaying the success or error message
message_label = Label(page4, text="", bg="#f0f0f0", font=("Arial", 12))
message_label.grid(row=4, column=0, columnspan=2, pady=10)



show_frame(page1)
index.mainloop()