#To find optimum cost for digital advertising

#Import necessary libraries
import csv
from tabulate import tabulate
import pandas as pd

def read_file_with_pandas(csv_path):
  df = pd.read_csv(csv_path)
  return df

#To calculate Cost per customer,Number of customers,Marketing cost
def process_csv(csv_data):
  budget = 10000
  #Extract rate and conversion rate
  rates_conversion_rates = [[row["Rate"],row["ConversionRate"]] for index,row in csv_data.iterrows()]
  #Cost per customer = Rate/Conversion rate
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
  csv_data = read_file_with_pandas(csv_path)
  cost = process_csv(csv_data)
  display_csv(cost)
  
if __name__ == "__main__":
  main()