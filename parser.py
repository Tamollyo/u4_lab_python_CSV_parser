####################################################
#  python library imports here: csv, json
import csv
import json


####################################################
# Set up 3 global variables to process the csv file
# and convert it to JSON
# All variables will be empty lists to start: []
read_data = []
fields = []
employee_list = []


def csv_to_json(csv_path, json_path):
    with open(csv_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for entry in csv_data:
            read_data.append(tuple(entry))
    # print(read_data[0])
    headers = read_data[0]
    # employee = read_data[2]
    # print(headers)
    # print(employee)
    employees = [read_data[i] for i in range(1, len(read_data))]
    # print(employees)

    for i, name in enumerate(headers):
        fields.append(name.replace(' ', '_').lower())
    print(fields)

    for employee in employees:
        employee_json = {}
        for i, data in enumerate(employee):
            employee_json[fields[i]] = data
        employee_list.append(employee_json)
        employee_json = {}
    print(employee_list[1])

    with open(json_path, mode='w') as output_file:
      # json.dump(???, ???, indent=2)


csv_to_json('data/employee_data.csv', 'data/employees.json')
####################################################
# main function
# Takes in the path of the csv file and an output path
# for creating a new JSON file as arguments
# creates a new JSON file with formatted csv data
