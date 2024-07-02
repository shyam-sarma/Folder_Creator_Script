import openpyxl
import os

# Load the Excel workbook
workbook = openpyxl.load_workbook('your_excel_file.xlsx')

# Select the active sheet
sheet = workbook.active

# Get the folder names from column A
folder_names = [cell.value for cell in sheet['A'] if cell.value is not None]

# Specify the base directory where folders will be created
base_dir = '/Users/yourusername/Desktop/new_folders'  # Change this to your desired location

# Create the base directory if it doesn't exist
os.makedirs(base_dir, exist_ok=True)

# Create folders
for name in folder_names:
    folder_path = os.path.join(base_dir, str(name))
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder: {folder_path}")

print("Folder creation complete.")
