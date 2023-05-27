#! /usr/bin/env python3

import csv
import json

# Put where your CSV File is
CSV_FILE = ''
# Put where you want your JSON file
JSON_FILE = ''

data = []

with open(CSV_FILE, 'r') as f:
    
    csv_data = csv.reader(f)
    count = 0
    is_header_line = True
    headers = []
    
    # Fill up headers with the strings from the header line
    for row in csv_data:
        if is_header_line:
            is_header_line = False
            
            for header in row:
                headers.append(header)
            
            continue
        
        datum = {}
        
        for i in range(len(row)):
            cell = row[i]
            header = headers[i]
            datum[header] = cell
            
        data.append(datum)     
   
json_string = json.dumps(data, indent = 4)

with open(JSON_FILE,'w') as f:
    f.write(json_string)
