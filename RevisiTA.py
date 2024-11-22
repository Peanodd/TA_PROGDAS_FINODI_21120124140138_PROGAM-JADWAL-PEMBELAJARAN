import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class JadwalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tugas Akhir")
        self.root.geometry("800x600")
        self.root.configure(bg="#D2691E")

        # Variabel jadwal dan UI
        self.schedules = {}
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.new_day = tk.StringVar()
        self.new_schedule = tk.StringVar()
        self.logo_image_path = "Logo.png"

        self.create_login_page()

    def create_login_page(self):
        self.clear_window()
        self.add_logo(self.logo_image_path)
        container = tk.Frame(self.root, bg="#D2691E")
        container.pack(expand=True)

        tk.Label(container, text="Username:", font=("Times New Roman", 14), bg="#D2691E", fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(container, textvariable=self.username, font=("Times New Roman", 14)).grid(row=0, column=1, padx=10, pady=10, sticky="we")

        tk.Label(container, text="Password:", font=("Times New Roman", 14), bg="#D2691E", fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(container, textvariable=self.password, font=("Times New Roman", 14), show="*").grid(row=1, column=1, padx=10, pady=10, sticky="we")

        tk.Button(container, text="Login", font=("Times New Roman", 14), bg="white", fg="black", command=self.login).grid(row=2, columnspan=2, pady=20)
        container.grid_columnconfigure(1, weight=1)

    def add_logo(self, image_path):
        try:
            logo_image = Image.open(image_path)
            logo_image = logo_image.resize((100, 100), Image.Resampling.LANCZOS)
            logo_photo = ImageTk.PhotoImage(logo_image)
            logo_label = tk.Label(self.root, image=logo_photo, bg="#D2691E")
            logo_label.image = logo_photo
            logo_label.place(x=10, y=10)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat logo: {e}")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        if self.username.get() == "Finodi" and self.password.get() == "Sigma":
            self.open_schedule_menu()
        else:
            messagebox.showerror("Error", "Username atau password salah!")

    def open_schedule_menu(self):
        self.clear_window()
        self.add_logo(self.logo_image_path)

        container = tk.Frame(self.root, bg="#D2691E")
        container.pack(expand=True)

        tk.Label(container, text="Pilih Hari:", font=("Times New Roman", 18), bg="#D2691E", fg="black").pack(pady=10)
        for day in self.schedules.keys():
            tk.Button(container, text=day, font=("Times New Roman", 14), bg="white", fg="black", command=lambda d=day: self.show_schedule(d)).pack(pady=5, padx=10, fill="x")

        tk.Button(container, text="Tambah Hari", font=("Times New Roman", 14), bg="green", fg="white", command=self.add_day).pack(pady=10, fill="x")
        tk.Button(container, text="Logout", font=("Times New Roman", 14), bg="white", fg="black", command=self.logout).pack(pady=10, fill="x")

    def add_day(self):
        self.clear_window()
        self.add_logo(self.logo_image_path)

        container = tk.Frame(self.root, bg="#D2691E")
        container.pack(expand=True)

        tk.Label(container, text="Masukkan Hari untuk Ditambahkan:", font=("Times New Roman", 18), bg="#D2691E", fg="black").pack(pady=10)
        tk.Entry(container, textvariable=self.new_day, font=("Times New Roman", 14)).pack(pady=10, fill="x")
        tk.Button(container, text="Tambah Hari", font=("Times New Roman", 14), bg="green", fg="white", command=self.confirm_add_day).pack(pady=10)
        tk.Button(container, text="Kembali", font=("Times New Roman", 14), bg="white", fg="black", command=self.open_schedule_menu).pack(pady=10)

    def confirm_add_day(self):
        valid_days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        day = self.new_day.get().strip()
        if day not in valid_days:
            messagebox.showwarning("Peringatan", "Masukkan hari yang valid (Senin - Minggu)!")
        elif day in self.schedules:
            messagebox.showwarning("Peringatan", f"Hari '{day}' sudah ada!")
        else:
            self.schedules[day] = []
            messagebox.showinfo("Sukses", f"Hari '{day}' berhasil ditambahkan!")
            self.new_day.set("")
            self.open_schedule_menu()

    def show_schedule(self, day):
        self.clear_window()
        self.add_logo(self.logo_image_path)

        container = tk.Frame(self.root, bg="#D2691E")
        container.pack(expand=True)

        tk.Label(container, text=f"Jadwal Hari {day}:", font=("Times New Roman", 18), bg="#D2691E", fg="black").pack(pady=10)

        for i, schedule in enumerate(self.schedules[day]):
            row_container = tk.Frame(container, bg="#D2691E")
            row_container.pack(fill="x", pady=5)

            tk.Label(row_container, text=f"{i + 1}. {schedule}", font=("Times New Roman", 14), bg="#D2691E", fg="black").pack(side="left", padx=10)
            tk.Button(row_container, text="Hapus", font=("Times New Roman", 10), bg="red", fg="white", command=lambda idx=i: self.delete_schedule(day, idx)).pack(side="right", padx=10)

        tk.Label(container, text="Tambahkan Jadwal:", font=("Times New Roman", 14), bg="#D2691E", fg="black").pack(pady=10)
        tk.Entry(container, textvariable=self.new_schedule, font=("Times New Roman", 14)).pack(pady=10, fill="x")
        tk.Button(container, text="Tambah Jadwal", font=("Times New Roman", 14), bg="green", fg="white", command=lambda: self.add_schedule(day)).pack(pady=10)

        tk.Button(container, text="Hapus Hari", font=("Times New Roman", 14), bg="red", fg="white", command=lambda: self.delete_day(day)).pack(pady=10)
        tk.Button(container, text="Kembali", font=("Times New Roman", 14), bg="white", fg="black", command=self.open_schedule_menu).pack(pady=10)

    def add_schedule(self, day):
        schedule = self.new_schedule.get().strip()
        if schedule:
            self.schedules[day].append(schedule)
            self.new_schedule.set("")
            messagebox.showinfo("Sukses", f"Jadwal '{schedule}' berhasil ditambahkan!")
            self.show_schedule(day)
        else:
            messagebox.showwarning("Peringatan", "Jadwal tidak boleh kosong!")

    def delete_schedule(self, day, index):
        confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus jadwal ini?")
        if confirm:
            removed = self.schedules[day].pop(index)
            messagebox.showinfo("Sukses", f"Jadwal '{removed}' berhasil dihapus!")
            self.show_schedule(day)

    def delete_day(self, day):
        confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus hari '{day}'?")
        if confirm:
            del self.schedules[day]
            messagebox.showinfo("Sukses", f"Hari '{day}' berhasil dihapus!")
            self.open_schedule_menu()

    def logout(self):
        self.username.set("")
        self.password.set("")
        self.create_login_page()


if __name__ == "__main__":
    root = tk.Tk()
    app = JadwalApp(root)
    root.mainloop()
