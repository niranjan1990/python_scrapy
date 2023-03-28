import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'/Users/apple/Downloads/chart data measures/Weight-for-age  GIRLS Birth to 13 weeks Z-Score/Weight-for-age  GIRLS Birth to 13 weeks  - Median.csv'
jsonFilePath = r'/Users/apple/Downloads/chart data measures/Weight-for-age  GIRLS Birth to 13 weeks Z-Score/Weight-for-age  GIRLS Birth to 13 weeks  - Median.json'

csv_to_json(csvFilePath, jsonFilePath)

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
