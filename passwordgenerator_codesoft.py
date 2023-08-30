import tkinter as tk
import random 

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = tk.Label(root, text="Password Generator")
        self.label.grid(row=0, column=0, columnspan=2)

        self.entry = tk.Entry(root, width=30)
        self.entry.grid(row=1, column=0, columnspan=2)

        self.pass_length_label = tk.Label(root, text="Password Length:")
        self.pass_length_label.grid(row=2, column=0)

        self.len = tk.Entry(root, width=20)
        self.len.grid(row=2, column=1)

        self.gen_button = tk.Button(root, text="Generate password", command=self.generate_password)
        self.gen_button.grid(row=3, column=0, columnspan=2)

    def generate_password(self):
        try:
            length = int(self.len.get())

            if length <= 0:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Invalid length")
            else:
                password = self.generated_password(length)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, password)
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Invalid Length")

    def generated_password(self, length):
        a = "abcdefghijklmnopqrstuvwxyz"
        b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        c = "123456789"
        d = "!@#$%^&%&*><?:"
        total = a + b + c + d
        password = "".join(random.sample(total, length))
        return password

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
