import os
import csv
import shutil
from openpyxl import load_workbook
#import chardet

'''
"I decided to separate corrupt file flaggin to another script" 

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.csv'):
        with open(filename, 'rb') as f:
            contents = f.read()
            result = chardet.detect(contents)
            encoding = result['encoding']

            if encoding != 'UTF-8':
                new_filename = 'DELETE_ME_' + filename
                os.rename(filename, new_filename)
                print(f'{filename} is Invalid or Corrupt. Renamed to {new_filename}')
'''                
maxpathlenght = 255
header_folders = {}

for foldername in os.listdir(os.getcwd()):
    folderpath = os.path.join(os.getcwd(), foldername)
    if os.path.isdir(folderpath):
        header = tuple(foldername.split('_'))
        header_folders[header] = folderpath


        

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.csv'):
        print(f"Processing CSV file: {filename}")
        filepath = os.path.join(os.getcwd(), filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)
        except csv.Error as e:
            print(f"CSV error in file {filename}: {e}")
            continue

        # Replace '/' with '_'
        header = [h.replace('/', '_') for h in header]

        if tuple(header) not in header_folders:
            folder_name = '_'.join(header)
            folder_path = os.path.join(os.getcwd(), folder_name)

            if len(folder_path) > 200:
                folder_parts = folder_name.split('_')
                last_part = folder_parts[-1]
                shortened_parts = folder_parts[:6] + ['...'] + [last_part]
                shortened_folder_name = '_'.join(shortened_parts)
                folder_path = os.path.join(os.getcwd(), shortened_folder_name)


            try:
                os.makedirs(folder_path)
            except FileExistsError:
                pass
            
            header_folders[tuple(header)] = folder_path
        
        folder_path = header_folders[tuple(header)]
        
        new_filepath = os.path.join(folder_path, filename)
        
        try:
            shutil.copyfile(filepath, new_filepath)
        except shutil.SameFileError:
            pass

    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        print(f"Processing Excel file: {filename}")
        filepath = os.path.join(os.getcwd(), filename)
        workbook = load_workbook(filepath)
        sheet = workbook.active
        header = [cell.value for cell in sheet[1]]

       # Replace '/' with '_'
        header = [h.replace('/', '_') for h in header]

        if tuple(header) not in header_folders:
            folder_name = '_'.join(header)
            folder_path = os.path.join(os.getcwd(), folder_name)

            if len(folder_path) > 200:
                folder_parts = folder_name.split('_')
                last_part = folder_parts[-1]
                shortened_parts = folder_parts[:6] + ['...'] + [last_part]
                shortened_folder_name = '_'.join(shortened_parts)
                folder_path = os.path.join(os.getcwd(), shortened_folder_name)

            try:
                os.makedirs(folder_path)
            except FileExistsError:
                pass

            header_folders[tuple(header)] = folder_path

        folder_path = header_folders[tuple(header)]
        
        new_filepath = os.path.join(folder_path, filename)
        
        try:
            shutil.copyfile(filepath, new_filepath)
        except shutil.SameFileError:
            pass
