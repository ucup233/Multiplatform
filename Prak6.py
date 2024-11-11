import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        nilai_mata_pelajaran = [int(input_value.get()) for input_value in labels_input]
        
        for nilai in nilai_mata_pelajaran:
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        
        hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")
    
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x550") 

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 14, "bold"))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

labels_input = []
for i in range(10):
    mata_pelajaran_label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:", font=("Times New Roman", 14))
    mata_pelajaran_label.grid(row=i+1, column=0, padx=10, pady=5) 
    input_value = tk.Entry(root)
    input_value.grid(row=i+1, column=1, padx=10, pady=5)
    labels_input.append(input_value)

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20)

hasil_label = tk.Label(root, text="", font=("Times New Roman", 12))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()