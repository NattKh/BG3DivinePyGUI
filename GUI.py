import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
from pathlib import Path
from tkinter import simpledialog
from pathlib import Path
# Get the directory of the current script (GUI.py)
current_directory = Path(__file__).parent
# Construct the path to the PyTools directory
pytools_directory = current_directory / "PyTools"
# Now you can reference any script inside the PyTools directory
extract_osiris_script = pytools_directory / "extract_osiris.py"
# Retrieve paths from environment variables
BG3_PATH = Path(os.environ.get("BG3_PATH", ""))
LSLIB_PATH = Path(os.environ.get("LSLIB_PATH", ""))
BG3_EXTRACTED = Path(os.environ.get("BG3_EXTRACTED", ""))
# Determine the path to divine.exe
def locate_divine_exe():
    if LSLIB_PATH.is_dir():
        exe_path = LSLIB_PATH.joinpath("divine.exe")
        if exe_path.exists():
            return exe_path
        elif LSLIB_PATH.joinpath("Tools").exists():
            return LSLIB_PATH.joinpath("Tools/divine.exe")
    return "divine.exe"  # Default value if not found
DIVINE_PATH = locate_divine_exe()
print(f"Using divine.exe at: {DIVINE_PATH}")
# Define the functions for each action
def create_package():
    source_folder = filedialog.askdirectory(title="Select Source Folder")
    output_file = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".pak", filetypes=[("PAK files", "*.pak")])
    input_format = input_format_var.get()
    output_format = output_format_var.get()
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{source_folder}\" -d \"{output_file}\" -a create-package -i {input_format} -o {output_format}"
    subprocess.run(cmd, shell=True)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def list_package_contents():
    pak_file = filedialog.askopenfilename(title="Select PAK File", filetypes=[("PAK files", "*.pak")])
    cmd = f"divine -g bg3 -s \"{pak_file}\" -a list-package"
    subprocess.run(cmd, shell=True)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def extract_single_file():
    pak_file = filedialog.askopenfilename(title="Select PAK File", filetypes=[("PAK files", "*.pak")])
    file_name_in_pak = simpledialog.askstring("Input", "Enter the name or path of the file within the PAK you want to extract:")
    output_file = filedialog.asksaveasfilename(title="Select Output File")
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{pak_file}\" -d \"{output_file}\" -f \"{file_name_in_pak}\" -a extract-single-file"
    subprocess.run(cmd, shell=True)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def extract_package():
    pak_file = filedialog.askopenfilename(title="Select PAK File", filetypes=[("PAK files", "*.pak")])
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    cmd = f"divine -g bg3 -s \"{pak_file}\" -d \"{output_folder}\" -a extract-package"
    subprocess.run(cmd, shell=True)
def convert_resource():
    source_file = filedialog.askopenfilename(title="Select Resource File")
    output_file = filedialog.asksaveasfilename(title="Select Output File")
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{source_file}\" -d \"{output_file}\" -a convert-resource"
    subprocess.run(cmd, shell=True)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def batch_convert_resources():
    source_folder = filedialog.askdirectory(title="Select Source Folder")
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    input_format = input_format_var.get()
    output_format = output_format_var.get()
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{source_folder}\" -d \"{output_folder}\" -a convert-resources -i {input_format} -o {output_format}"
    subprocess.run(cmd, shell=True)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def batch_extract():
    source_folder = filedialog.askdirectory(title="Select Folder Containing PAK Files")
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{source_folder}\" -d \"{output_folder}\" -a extract-packages"
    subprocess.run(cmd, shell=True)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def extract_osi_or_sav():
    source_file = filedialog.askopenfilename(title="Select .osi or .sav File", filetypes=[(".osi files", "*.osi"), (".sav files", "*.sav")])
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{source_file}\" -d \"{output_folder}\" -a extract-osiris"
    subprocess.run(cmd, shell=True)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def extract_osiris_to_txt():
    input_file = filedialog.askopenfilename(title="Select .osi File", filetypes=[("OSI files", "*.osi")])
    if not input_file:
        return
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return
    script_path = "path_to_extract_osiris.py"  # Replace with the actual path to your script
    cmd = f"python \"{script_path}\" -d \"{DIVINE_PATH}\" -o \"{output_folder}\" -f \"{input_file}\""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    if result.returncode == 0:
        messagebox.showinfo("Info", "Extraction completed!")
    else:
        messagebox.showerror("Error", "Extraction failed!")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
def extract_osiris_bytecode():
    input_file = filedialog.askopenfilename(title="Select .osi File", filetypes=[("OSI files", "*.osi")])
    if not input_file:
        return
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{input_file}\" -d \"{output_folder}\" -a extract-osiris -i osi"
    subprocess.run(cmd, shell=True)
    messagebox.showinfo("Info", "Extraction completed!")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def create_osiris_bytecode():
    input_file = filedialog.askopenfilename(title="Select .txt File", filetypes=[("Text files", "*.txt")])
    if not input_file:
        return
    output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".osi", filetypes=[("OSI files", "*.osi")])
    if not output_file:
        return
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{input_file}\" -d \"{output_file}\" -a create-osiris -i txt -o osi"
    subprocess.run(cmd, shell=True)
    messagebox.showinfo("Info", "Creation completed!")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def extract_databases():
    input_file = filedialog.askopenfilename(title="Select .sav File", filetypes=[("SAV files", "*.sav")])
    if not input_file:
        return
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{input_file}\" -d \"{output_folder}\" -a extract-databases -i sav"
    subprocess.run(cmd, shell=True)
    messagebox.showinfo("Info", "Extraction completed!")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def convert_txt_to_osi():
    input_file = filedialog.askopenfilename(title="Select Modified .txt File", filetypes=[("Text files", "*.txt")])
    if not input_file:
        return
    output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".osi", filetypes=[("OSI files", "*.osi")])
    if not output_file:
        return
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{input_file}\" -d \"{output_file}\" -a convert-resource"
    subprocess.run(cmd, shell=True)
    messagebox.showinfo("Info", "Conversion completed!")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
def package_osi_or_sav():
    source_folder = filedialog.askdirectory(title="Select Folder Containing Edited Files")
    output_file = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".osi", filetypes=[(".osi files", "*.osi"), (".sav files", "*.sav")])
    cmd = f"{DIVINE_PATH} -g bg3 -s \"{source_folder}\" -d \"{output_file}\" -a package-osiris"
    subprocess.run(cmd, shell=True)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
# Tooltips for buttons
def show_tooltip(event, text):
    tooltip = tk.Toplevel(root)
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry(f"+{event.x_root}+{event.y_root}")
    label = tk.Label(tooltip, text=text, background="yellow", relief="solid", borderwidth=1)
    label.pack()
    event.widget.tooltip = tooltip
def hide_tooltip(event):
    event.widget.tooltip.destroy()
# Create the main window
root = tk.Tk()
root.title("Divine Tool GUI")
# Create a frame for the options
frame_options = ttk.LabelFrame(root, text="Options")
frame_options.pack(padx=10, pady=10, fill="both", expand=True)
# Dropdown for input and output formats
formats = ["lsv", "pak", "lsj", "lsx", "lsb", "lsf"]
lbl_input_format = ttk.Label(frame_options, text="Input Format:")
lbl_input_format.grid(row=0, column=0, padx=5, pady=5)
input_format_var = tk.StringVar()
input_format_dropdown = ttk.Combobox(frame_options, textvariable=input_format_var, values=formats)
input_format_dropdown.grid(row=0, column=1, padx=5, pady=5)
lbl_output_format = ttk.Label(frame_options, text="Output Format:")
lbl_output_format.grid(row=1, column=0, padx=5, pady=5)
output_format_var = tk.StringVar()
output_format_dropdown = ttk.Combobox(frame_options, textvariable=output_format_var, values=formats)
output_format_dropdown.grid(row=1, column=1, padx=5, pady=5)
# Update button labels and add tooltips
btn_create_package = ttk.Button(root, text="Create a BG3 Package (.pak)", command=create_package)
btn_create_package.pack(pady=10)
btn_create_package.bind("<Enter>", lambda e: show_tooltip(e, "Create a new package for BG3 from a selected folder."))
btn_create_package.bind("<Leave>", hide_tooltip)
btn_list_contents = ttk.Button(root, text="List Contents of a BG3 Package (.pak)", command=list_package_contents)
btn_list_contents.pack(pady=10)
btn_list_contents.bind("<Enter>", lambda e: show_tooltip(e, "List the contents of a selected BG3 package."))
btn_list_contents.bind("<Leave>", hide_tooltip)
btn_extract_single = ttk.Button(root, text="Extract Single File from a BG3 Package (.pak)", command=extract_single_file)
btn_extract_single.pack(pady=10)
btn_extract_single.bind("<Enter>", lambda e: show_tooltip(e, "Extract a specific file from a selected BG3 package."))
btn_extract_single.bind("<Leave>", hide_tooltip)
btn_extract_package = ttk.Button(root, text="Extract All Files from a BG3 Package (.pak)", command=extract_package)
btn_extract_package.pack(pady=10)
btn_extract_package.bind("<Enter>", lambda e: show_tooltip(e, "Extract all files from a selected BG3 package to a specified folder."))
btn_extract_package.bind("<Leave>", hide_tooltip)
btn_batch_extract = ttk.Button(root, text="Batch Extract BG3 Packages (.pak)", command=batch_extract)
btn_batch_extract.pack(pady=10)
btn_batch_extract.bind("<Enter>", lambda e: show_tooltip(e, "Batch extract multiple BG3 packages."))
btn_batch_extract.bind("<Leave>", hide_tooltip)
# Buttons for .osi and .sav files
btn_extract_osi_or_sav = ttk.Button(root, text="Extract .osi or .sav File", command=extract_osi_or_sav)
btn_extract_osi_or_sav.pack(pady=10)
btn_extract_osi_or_sav.bind("<Enter>", lambda e: show_tooltip(e, "Extract the contents of a .osi or .sav file."))
btn_extract_osi_or_sav.bind("<Leave>", hide_tooltip)
btn_package_osi_or_sav = ttk.Button(root, text="Package .osi or .sav File", command=package_osi_or_sav)
btn_package_osi_or_sav.pack(pady=10)
btn_package_osi_or_sav.bind("<Enter>", lambda e: show_tooltip(e, "Package edited files into a .osi or .sav file."))
btn_package_osi_or_sav.bind("<Leave>", hide_tooltip)
# Add buttons for the new features
btn_extract_osiris = ttk.Button(root, text="Extract .osi story to .txt", command=extract_osiris_to_txt)
btn_extract_osiris.pack(pady=10)
btn_convert_txt = ttk.Button(root, text="Convert .txt to .osi", command=convert_txt_to_osi)
btn_convert_txt.pack(pady=10)
# Add a button for extracting Osiris bytecode
btn_extract_osiris = ttk.Button(root, text="Extract Osiris Story Bytecode", command=extract_osiris_bytecode)
btn_extract_osiris.pack(pady=10)
root.mainloop()