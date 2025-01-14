import os
import shutil
from datetime import datetime
from tkinter import Tk, Button, Label, filedialog
from plyer import notification
from tqdm import tqdm  # Untuk progress bar

# Fungsi untuk membuat folder berdasarkan kategori
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Fungsi untuk memindahkan file dengan progress bar
def move_files_with_progress(file_list, destination):
    for file in tqdm(file_list, desc="Moving files", unit="file"):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):  # Pastikan ini adalah file, bukan direktori
            shutil.move(file_path, os.path.join(destination, file))
            # Menampilkan status untuk setiap file yang dipindahkan
            print(f"Moved: {file} -> {destination}")

# Fungsi untuk memilih folder sumber
def select_source_folder():
    global source_folder
    source_folder = filedialog.askdirectory(title="Pilih Sumber Folder")
    source_label.config(text=f"Sumber: {source_folder}")

# Fungsi untuk memilih folder tujuan
def select_destination_folder():
    global destination_folder
    destination_folder = filedialog.askdirectory(title="Pilih Folder Tujuan")
    destination_label.config(text=f"Tujuan: {destination_folder}")

# Fungsi untuk memindahkan file berdasarkan ekstensi
def move_files_by_extension():
    if not source_folder or not destination_folder:
        return  # Pastikan folder sumber dan tujuan sudah dipilih

    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        
        if os.path.isfile(file_path):  # Pastikan ini adalah file, bukan direktori
            extension = file_name.split('.')[-1].lower()  # Ambil ekstensi file
            destination = os.path.join(destination_folder, extension)
            create_folder(destination)
            
            # Pindahkan file ke folder tujuan berdasarkan ekstensi
            move_files_with_progress([file_name], destination)
    
    # Notifikasi selesai
    notification.notify(
        title='Pengorganisasian File Selesai',
        message='Semua file telah dipindahkan berdasarkan ekstensinya!',
        timeout=5
    )

# Fungsi untuk memindahkan file berdasarkan tanggal
def move_files_by_date():
    if not source_folder or not destination_folder:
        return  # Pastikan folder sumber dan tujuan sudah dipilih

    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        
        if os.path.isfile(file_path):  # Pastikan ini adalah file, bukan direktori
            file_date = datetime.fromtimestamp(os.path.getmtime(file_path))
            year_month = file_date.strftime('%Y-%m')  # Format tanggal tahun-bulan
            
            destination = os.path.join(destination_folder, year_month)
            create_folder(destination)
            
            # Pindahkan file ke folder tujuan berdasarkan tanggal
            move_files_with_progress([file_name], destination)
    
    # Notifikasi selesai
    notification.notify(
        title='Pengorganisasian File Selesai',
        message='Semua file telah dipindahkan berdasarkan ekstensinya!',
        timeout=5
    )

# Setup GUI
root = Tk()
root.title("Pengatur File & Folder")
root.geometry("400x300")

# Label dan tombol untuk memilih folder
source_label = Label(root, text="Sumber: Kosong")
source_label.pack(pady=10)

source_button = Button(root, text="Pilih Sumber Folder", command=select_source_folder)
source_button.pack(pady=5)

destination_label = Label(root, text="Tujuan: Kosong")
destination_label.pack(pady=10)

destination_button = Button(root, text="Pilih Folder Tujuan", command=select_destination_folder)
destination_button.pack(pady=5)

# Tombol untuk mulai memindahkan file berdasarkan ekstensi atau tanggal
extension_button = Button(root, text="Pindahkan File berdasarkan Ekstensi", command=move_files_by_extension)
extension_button.pack(pady=10)

date_button = Button(root, text="Pindahkan File berdasarkan Tanggal", command=move_files_by_date)
date_button.pack(pady=10)

# Menjalankan aplikasi GUI
root.mainloop()
