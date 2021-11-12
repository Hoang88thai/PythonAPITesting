import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library


def test_add_multiple_students():
    # API
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/hthai/Desktop/Task_API/AddNewStudent.json")

    # Type cast into json format
    json_request = json.loads(f.read())

    obj = Library.Common("C:/Users/hthai/Desktop/Task_API/TestData.xlsx", "Sheet1")
    col = obj.fetch_row_count()
    row = obj.fetch_row_count()
    keylist = obj.fetch_key_names()

    # starting a loop from second row
    for i in range(2, row + 1):
        update_json_request = obj.update_request_with_data(i, json_request, keylist)
        response = requests.post(api_url, update_json_request)
        print(response)
