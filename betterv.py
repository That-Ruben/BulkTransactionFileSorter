import os
import csv
import shutil
from openpyxl import load_workbook

header_folders = {}

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.csv'):
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            if tuple(header) not in header_folders:
                folder_name = '_'.join(header)
                folder_path = os.path.join(os.getcwd(), folder_name)
                os.makedirs(folder_path)
                
                header_folders[tuple(header)] = folder_path
            
            folder_path = header_folders[tuple(header)]
            
            new_filepath = os.path.join(folder_path, filename)
            shutil.copyfile(filepath, new_filepath)
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        filepath = os.path.join(os.getcwd(), filename)
        workbook = load_workbook(filepath)
        sheet = workbook.active
        header = [cell.value for cell in sheet[1]]
        
        if tuple(header) not in header_folders:
            folder_name = '_'.join(header)
            folder_path = os.path.join(os.getcwd(), folder_name)
            os.makedirs(folder_path)

            header_folders[tuple(header)] = folder_path

        folder_path = header_folders[tuple(header)]
        
        new_filepath = os.path.join(folder_path, filename)
        shutil.copyfile(filepath, new_filepath)