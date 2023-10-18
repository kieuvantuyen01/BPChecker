import os
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
from datetime import datetime
import openpyxl

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Check Student Registration")
        self.master.geometry("400x200")
        self.master.resizable(False, False)
        self.master.config(bg="white")
        self.create_widgets()

    def create_widgets(self):
        self.csv_button = tk.Button(self.master, text="Open CSV File", command=self.open_csv)
        self.csv_button.pack(pady=10)

        self.txt_button = tk.Button(self.master, text="Open TXT File", command=self.open_txt)
        self.txt_button.pack(pady=10)

        self.run_button = tk.Button(self.master, text="Run Program", command=self.run_program)
        self.run_button.pack(pady=10)

        self.open_button = tk.Button(self.master, text="Open Excel File", command=self.open_excel, state="disabled")
        self.open_button.pack(pady=10)

    def open_csv(self):
        self.csv_file = filedialog.askopenfilename(initialdir="D:\OOP", title="Select CSV File", filetypes=(("CSV Files", "*.csv"),))
        if self.csv_file:
            self.csv_button.config(text="CSV File Selected")

    def open_txt(self):
        self.txt_file = filedialog.askopenfilename(initialdir="D:\OOP", title="Select TXT File", filetypes=(("TXT Files", "*.txt"),))
        if self.txt_file:
            self.txt_button.config(text="TXT File Selected")

    def run_program(self):
        if hasattr(self, "csv_file") and hasattr(self, "txt_file"):
            with open(self.csv_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                # each cell in the "MSSV" column (3rd column) contains multiple student IDs separated by ", "
                # student_ids should loop through each cell and add each student ID to the list
                student_ids = [id.strip() for row in reader for id in row[2].split(", ")]

            # print(student_ids)

            with open(self.txt_file, newline='', encoding='utf-8') as txtfile:
                reader = csv.reader(txtfile, delimiter='\t')
                students = {row[0].strip(): row[1].strip() for row in reader}

            # print(students)
            # not_registered list should contain id and name of students who are not registered in the Big Assignment Group
            not_registered = []
            for id, name in students.items():
                if id not in student_ids:
                    not_registered.append((id, name))

            if not not_registered:
                tk.messagebox.showinfo("Result", "All students are registered in the Big Assignment Group.")
            else:
                # display the student ID and name in dialog
                result = "\n".join([f"{id}\t{name}" for id, name in not_registered])
                tk.messagebox.showinfo("The following students are not registered in the Big Assignment Group", result)

                filename = f"D:\OOP\BA\student_not_registered_in_big_assignment_group{datetime.now().strftime('%Y%m%d-%H%M%S')}.xlsx"
                workbook = openpyxl.Workbook()
                worksheet = workbook.active
                worksheet.title = "Not Registered Students"
                worksheet.append(["Student ID", "Student Name"])
                # add each student to the worksheet from the not_registered list
                for student in not_registered:
                    worksheet.append(student)
                workbook.save(filename)
                # tk.messagebox.showinfo("Result", f"{len(not_registered)} students are not registered in the Big Assignment Group.")
                self.open_button.config(state="normal")

    def open_excel(self):
        filename = filedialog.askopenfilename(initialdir="D:\OOP\BA", filetypes=(("Excel Files", "*.xlsx"),))
        if filename:
            os.startfile(filename)

root = tk.Tk()
app = Application(master=root)
app.mainloop()