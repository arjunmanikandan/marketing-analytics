#To find optimum cost for digital advertising

#Import necessary libraries
import csv
from tabulate import tabulate

#To read csv file 
def read_csv_file(csv_path):
  data = []
  with open(csv_path,"r") as file:
    marketing_data = csv.reader(file)
    for item in marketing_data:
      data.append(item)
  return data

#To calculate Cost per customer,Number of customers,Marketing cost
def process_csv(data):
  budget = 10000
  #Extract rate and conversion rate
  rates_conversion_rates = [[item[1],item[2]]for item in data]   
  #Cost per customer = Rate/Conversion rate
  rates_conversion_rates=rates_conversion_rates[1:len(rates_conversion_rates)]
  customer_costs = [(float(item[0])/float(item[1]))for item in rates_conversion_rates]
  #No_of_customers = Budget/Cost per customer
  no_of_customers = [round(budget/cpc) for cpc in customer_costs]
  #marketing_cost = Cost per customer * No of customers
  marketing_cost = [round(cpc*customer_count) for cpc,customer_count in zip(customer_costs,no_of_customers)]
  output = [[customer_costs[i],no_of_customers[i],marketing_cost[i]]for i in range(0,len(customer_costs))]
  output.insert(0,["COST_PER_CUSTOMER","NO_OF_CUSTOMERS","MARKETING_COST"])
  return output

def display_csv(cost) :
  print(tabulate(cost,tablefmt="grid"))
  
#All function calls takes place from here
def main():
  csv_path = "marketing-analytics/marketing-master-offerings.csv"
  csv_data = read_csv_file(csv_path)
  cost = process_csv(csv_data)
  table = display_csv(cost)

if __name__ == "__main__":
  main()