# Big Assignment Checker
! Only use for web: oasis.uet.vnu.edu.vn

## Description

1. This is a GUI application to check if any students are not registered in a Big Assignment Group
2. Input: 
- a csv file that contains a column named "MSSV" (each cell contains student ID of a Group, separated by ", ", e.g. 1712345, 1712346, 1712347)
- a txt file that contains first comlumn is a list of student IDs (separated by "\n", e.g. 1712345\n1712346\n1712347), second column is a list of student names (separated by "\n", e.g. Nguyen Van A\nTran Thi B\nLe Van C)
3. Program should check if any student ID in the second file is not in the first file then look up the student name in the second file
4. The students who are not registered in the Big Assignment Group will be displayed in a dialog and saved to a new excel file that has name follows this format: 
"D:\OOP\" + "student_not_registered_in_big_assignment_group" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".xlsx"
5. Program has a button to open the first file, a button to open the second file, and a button to run the program.
The default directory to select files is "D:\OOP"
6. Program has a button to open this new excel file that has just been created

## Installation
1. Clone this repository
2. Run imediatly file `main.py` with python3

## Usage
1. Select the csv file with the group that registered in the big assignment
2. Select the txt file with the list of student of the class
3. Click button `Run` to check the student that not register the group in the big assignment

## Demo
![Demo](    )

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
None

## Author
- [Kieu Van Tuyen](https://github.com/kieuvantuyen01)

## Contact
- [Facebook](https://www.facebook.com/kieuvantuyen01)
- [Email](mailto:tuyenkv@vnu.edu.vn)

## Project status
- [x] Finish

## To do
- [ ] None

## References
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pandas](https://pandas.pydata.org/docs/)
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [Datetime](https://docs.python.org/3/library/datetime.html)
- [OS](https://docs.python.org/3/library/os.html)
- [Sys](https://docs.python.org/3/library/sys.html)
- [Pyinstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html)
- [Pyinstaller with Tkinter](https://stackoverflow.com/questions/5458048/how-to-make-a-python-script-standalone-executable-to-run-without-any-dependency)

## Changelog
- [x] 2023/10/18: Create project
- [x] 2023/10/18: Finish project

## Note
- This project is only for educational purposes
- This project is only used for checking student registration from page oasis.uet.vnu.edu.vn