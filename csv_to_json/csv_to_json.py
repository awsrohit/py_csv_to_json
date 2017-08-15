import csv
import json

def main():
    with open('test.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    with open('test.json', 'w') as f:
        json.dump(rows, f)
        

    
    
    
    
