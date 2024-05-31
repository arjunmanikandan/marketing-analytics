#To find optimum cost for digital advertising

#Import necessary libraries
import csv
from typing import List
from typing import Union

#To read csv file 
def read_csv_file(csv_path):
  data = []
  with open(csv_path,"r") as file:
    marketing_data = csv.reader(file)
    for item in marketing_data:
      data.append(item)
  return data

#All function calls takes place from here
def main():
  csv_path = "marketing-analytics/marketing-master-offerings.csv"
  csv_data = read_csv_file(csv_path)
  print(csv_data)

if __name__ == "__main__":
  main()