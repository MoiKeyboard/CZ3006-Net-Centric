import csv
import sys
import pprint

# Function to convert a csv file to a list of dictionaries.  Takes in one variable called &quot;variables_file&quot;
 
def csv_dict_list(variables_file):
     
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
 
    reader = csv.DictReader(open(variables_file, 'r'), fieldnames=None)
    dict_list = []
    print(dict_list)
    countline = 1
    for line in reader:
        dict_list.append(line)
        # print(line)
        break

    print(countline)
    return dict_list
 
# Calls the csv_dict_list function, passing the named csv
 
device_values = csv_dict_list('test_SFLow_data.csv.csv')
 
# Prints the results nice and pretty like
 
# pprint.pprint(device_values)
print(device_values)