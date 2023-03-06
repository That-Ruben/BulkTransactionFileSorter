import os
import chardet
import csv
from tqdm import tqdm
from openpyxl import load_workbook


for filename in tqdm(os.listdir(os.getcwd()), desc='Progress', bar_format="{l_bar}{bar}{r_bar}", colour='green'):
    if filename.endswith('.csv'):
        with open(filename, 'rb') as f:
            contents = f.read()
            result = chardet.detect(contents)
            encoding = result['encoding']
            #print(f'Checking {filename} ==> {result}')

        if encoding is None:
            new_filename = '___I AM INVALID...DELETE_ME!___' + filename
            os.rename(filename, new_filename)
            print(f'{filename} is Invalid or Corrupt. Renamed to {new_filename}')
    elif filename.endswith(('.xls', '.xlsx')):
        try:
            workbook = load_workbook(filename, read_only=True)
        except Exception as e:
            new_filename = '___I AM INVALID...DELETE_ME!___' + filename
            os.rename(filename, new_filename)
            print(f'{filename} is Invalid or Corrupt. Renamed to {new_filename}. Error: {e}')
print('Done!')
