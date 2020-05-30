import pandas as pd

# Assign your spreadsheet name
file = "ListOfPythonDevelopers.xlsx"

# Load your excel file
excel_data_frame = pd.read_excel(file, index_col=0)
print(excel_data_frame)

print("List of Names in the List")
for name_tuple in excel_data_frame.iterrows():
    print(name_tuple[0])
