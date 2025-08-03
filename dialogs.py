import requests
import tkinter as tk
from tkinter import messagebox

class DialogsWindow:
    def __init__(self, root, access_token, account_id):
        self.root = root
        self.access_token = access_token
        self.account_id = account_id
        self.root.title("Выбор диалогов")
        self.root.geometry("600x500")

        self.create_dialogs_view()

    def create_dialogs_view(self):
        tk.Label(self.root, text="Выбор диалогов", font=("Arial", 16)).pack(pady=10)

        self.dialogs_frame = tk.Frame(self.root)
        self.dialogs_frame.pack(fill=tk.BOTH, expand=True)

        self.dialogs_listbox = tk.Listbox(self.dialogs_frame, font=("Arial", 12))
        self.dialogs_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.dialogs_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.dialogs_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.dialogs_listbox.yview)

        self.load_dialogs_button = tk.Button(self.root, text="Загрузить диалоги", command=self.load_dialogs)
        self.load_dialogs_button.pack(pady=10)

        self.dialogs_listbox.bind('<<ListboxSelect>>', self.on_dialog_select)

    def load_dialogs(self):
        url = 'https://api.dkon.app/api/v3/method/dialogs.get'
        data = {
            'clientId': '1302',
            'accountId': self.account_id,
            'accessToken': self.access_token
        }

        try:
            response = requests.post(url, data=data)
            response_data = response.json()

            if response_data.get('error'):
                messagebox.showerror("Ошибка", f"Ошибка при загрузке диалогов: {response_data.get('error_code')}")
                return

            self.dialogs_listbox.delete(0, tk.END)  # Очистка списка перед загрузкой
            for chat in response_data.get('chats', []):
                display_text = f"{chat['withUserFullname']} ({chat['withUserUsername']}): {chat['lastMessage']}"
                self.dialogs_listbox.insert(tk.END, display_text)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при загрузке диалогов: {str(e)}")

    def on_dialog_select(self, event):
        selected_index = self.dialogs_listbox.curselection()
        if selected_index:
            selected_dialog = self.dialogs_listbox.get(selected_index)
            messagebox.showinfo("Выбранный диалог", f"Вы выбрали: {selected_dialog}")

