import customtkinter as ctk
import db
from ui_dashboard import Dashboard

class LoginUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MoodTune Login")
        self.geometry("420x300")
        self.resizable(False,False)
        ctk.set_appearance_mode("dark")

        ctk.CTkLabel(self,text="Login",font=("Segoe UI",24)).pack(pady=10)

        self.username = ctk.CTkEntry(self,placeholder_text="Username",width=250)
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(self,placeholder_text="Password",show="*",width=250)
        self.password.pack(pady=10)

        ctk.CTkButton(self,text="Login",command=self.login).pack(pady=10)
        ctk.CTkButton(self,text="Quit",command=self.destroy).pack(pady=5)

    def login(self):
        user = db.login_user(self.username.get(),self.password.get())
        if user:
            self.destroy()
            Dashboard(user).mainloop()
        else:
            ctk.CTkLabel(self,text="Invalid credentials!",text_color="red").pack()

if __name__ == "__main__":
    LoginUI().mainloop()
