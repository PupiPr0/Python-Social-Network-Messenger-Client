import tkinter as tk
from tkinter import messagebox
from register import register
from login import login
from dialogs import DialogsWindow

class SocialNetworkClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Социальная сеть")
        self.root.geometry("300x400")

        self.create_login_form()

    def create_login_form(self):
        tk.Label(self.root, text="Вход", font=("Arial", 16)).pack(pady=10)

        self.username_entry = self.create_entry("Имя пользователя")
        self.username_entry.pack(pady=5)

        self.password_entry = self.create_entry("Пароль", show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Войти", command=self.login_user).pack(pady=10)
        tk.Button(self.root, text="Регистрация", command=self.create_register_form).pack(pady=5)

    def create_register_form(self):
        self.clear_form()
        tk.Label(self.root, text="Регистрация", font=("Arial", 16)).pack(pady=10)

        self.username_entry = self.create_entry("Имя пользователя")
        self.username_entry.pack(pady=5)

        self.fullname_entry = self.create_entry("Ваше имя")
        self.fullname_entry.pack(pady=5)

        self.password_entry = self.create_entry("Пароль", show="*")
        self.password_entry.pack(pady=5)

        self.email_entry = self.create_entry("Email")
        self.email_entry.pack(pady=5)

        self.referrer_entry = self.create_entry("Кто пригласил? (необязательно)")
        self.referrer_entry.pack(pady=5)

        tk.Button(self.root, text="Зарегистрироваться", command=self.register_user).pack(pady=10)
        tk.Button(self.root, text="Назад", command=self.create_login_form).pack(pady=5)

    def create_entry(self, placeholder, show=None):
        entry = tk.Entry(self.root, show=show)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e: self.on_entry_click(e, placeholder))
        entry.bind("<FocusOut>", lambda e: self.on_focusout(e, placeholder))
        return entry

    def on_entry_click(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, tk.END)  # Удаляем текст плейсхолдера
            event.widget.config(fg='black')  # Меняем цвет текста на черный

    def on_focusout(self, event, placeholder):
        if event.widget.get() == '':
            event.widget.insert(0, placeholder)  # Вставляем текст плейсхолдера
            event.widget.config(fg='grey')  # Меняем цвет текста на серый

    def clear_form(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        response = login(username, password)

        if response.get('error') is False:
            access_token = response['accessToken']
            account_id = response['accountId']
            self.open_dialogs_window(access_token, account_id)  # Открываем окно диалогов
        else:
            messagebox.showerror("Ошибка", "Ошибка входа. Проверьте свои учетные данные.")

    def register_user(self):
        username = self.username_entry.get()
        fullname = self.fullname_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        referrer = self.referrer_entry.get()

        response = register(username, fullname, password, email, referrer)

        if 'error' not in response:
            access_token = response['accessToken']
            account_id = response['accountId']
            self.open_dialogs_window(access_token, account_id)  # Открываем окно диалогов
        else:
            messagebox.showerror("Ошибка", f"Ошибка регистрации: {response.get('error_code')}")

    def open_dialogs_window(self, access_token, account_id):
        self.clear_form()  # Очищаем текущее окно
        DialogsWindow(self.root, access_token, account_id)  # Открываем окно диалогов

if __name__ == "__main__":
    root = tk.Tk()
    app = SocialNetworkClient(root)
    root.mainloop()

