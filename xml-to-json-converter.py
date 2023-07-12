import json
import xmltodict
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def xml_to_json(xml_file):
    # Open the XML file
    with open(xml_file, 'r') as file:
        # Parse XML to a dictionary
        xml_data = xmltodict.parse(file.read())
        
        # Convert dictionary to JSON
        json_data = json.dumps(xml_data, indent=4)
        
        return json_data

# Open a file dialog to choose an XML file
Tk().withdraw()
xml_file = askopenfilename(filetypes=[('XML files', '*.xml')])

if xml_file:
    json_data = xml_to_json(xml_file)
    save_file_path = asksaveasfilename(defaultextension='.json', filetypes=[('JSON files', '*.json')])
    if save_file_path:
        with open(save_file_path, 'w') as save_file:
            save_file.write(json_data)
        print(f'JSON data saved to: {save_file_path}')
    else:
        print('JSON file path not provided. JSON data not saved.')
else:
    print('No XML file selected.')
