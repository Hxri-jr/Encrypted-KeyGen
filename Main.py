import hashlib
import tkinter as tk

#gui = Tk()

#gui.geometry("500x600")

def generate_key(email):
    hashed = hashlib.sha256(email.encode()).hexdigest()
    key = hashed[:16]
    key_formatted = '-'.join([key[i:i+4] for i in range(0, len(key), 4)])
    return key_formatted.upper()

def generate_key_gui():
    email = email_entry.get()
    key = generate_key(email)
    key_label.config(text="Your 16-digit key is: " + key)

root = tk.Tk()
root.title("Key Generator")

#root.geometry("700x350+500+500")

window_width = 700
window_height = 350

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)

root.iconbitmap("H:\image.ico")
#"C:\Users\hxri\Downloads\encryption-key1.ico"

email_label = tk.Label(root, text="Enter your E-Mail ID:")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()



generate_button = tk.Button(root, text="Generate Key", command=generate_key_gui)
generate_button.pack()

key_label = tk.Label(root, text="")
key_label.pack()

root.mainloop()
