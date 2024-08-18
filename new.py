from tkinter import *
from tkinter import messagebox
import base64
import os

def encrypt():
    password = code.get().strip()  # Strip any extra spaces
    print(f"Entered password (for debugging): '{password}'")  # Debug print

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encrypt")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()  # Strip any extra spaces
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font=("Roboto", 10), bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted)

    elif password == "":
        messagebox.showerror("Encryption", "Input Password")

    else:
        messagebox.showerror("Encryption", "Invalid Password")

def decrypt():
    password = code.get().strip()  # Strip any extra spaces
    print(f"Entered password (for debugging): '{password}'")  # Debug print

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decrypt")
        screen2.geometry("400x200")
        screen2.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()  # Strip any extra spaces
        try:
            # Handle potential padding issues in Base64
            padding = len(message) % 4
            if padding:
                message += "=" * (4 - padding)
            base64_bytes = base64.b64decode(message.encode("ascii"))
            decrypted = base64_bytes.decode("ascii")
        except Exception as e:
            decrypted = f"Error: {e}"

        Label(screen2, text="DECRYPTED", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text3 = Text(screen2, font=("Roboto", 10), bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text3.place(x=10, y=40, width=380, height=150)

        text3.insert(END, decrypted)

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")

    else:
        messagebox.showerror("Decryption", "Invalid Password")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("380x400")
    screen.title("PactApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    # Path to the image file
    image_path = "pinterest.jpg"

    # Check if the file exists
    if os.path.isfile(image_path):
        try:
            image_icon = PhotoImage(file=image_path)
            screen.iconphoto(False, image_icon)
        except Exception as e:
            print(f"An error occurred while loading the image: {e}")
    else:
        print("Image file not found. Please check the file path.")

    Label(text="Enter Text for encryption and decryption", fg="White", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font=("Roboto", 20), bg="black", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="white", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="Black", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="Black", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="Black", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

if __name__ == "__main__":
    main_screen()





    


       




