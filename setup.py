import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Dibbo\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Dibbo\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face_Recognition_Automatic_Attendace_System.py", base=base, icon="front.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["front.ico",'tcl86t.dll','tk86t.dll', 'photos','data','database','attendance_report','attendance_report']}},
    version = "1.0",
    description = "Face_Recognition_Automatic_Attendace_System | Developed By Dibbo",
    executables = executables
    )
