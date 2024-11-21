import os
import pandas as pd

def get_file_names_to_excel(directory, excel_file):
    # Get all files in the directory (including subdirectories)
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    
    # Create a dataframe with the file names
    df = pd.DataFrame(file_list, columns=['File Path'])
    
    # Create an empty 'New Name' column for renaming later
    df['New Name'] = ''
    
    # Write the dataframe to an Excel file
    df.to_excel(excel_file, index=False)
    print(f"File names saved to {excel_file}")

# Specify the directory and excel file path
directory = 'C:\MBInverter\MB_Inverter\SYS4_System_Integration_Test_Inverter\HSCID\Cds2\AI'
excel_file = 'C:/Shravya/new.xlsx'

get_file_names_to_excel(directory, excel_file)
