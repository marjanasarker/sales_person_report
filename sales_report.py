"""Generate sales report showing total melons each salesperson sold."""

# empty dictionary to add keys(salesperson-names) 
# and values (amount sold and number of melons)

def melons_sold_salesperson(file_path):

    sales_per_person = {}

    f = open(file_path)
    for line in f:
        line = line.rstrip()
        #creating a list and unpacking it's values 
        salesperson_name, total_dollars, melons_sold = line.split('|')
        
        # creating key and value pair to add to empty dictionary
        if salesperson_name in sales_per_person:
            sales_per_person[salesperson_name] += int(melons_sold)
        else:
            sales_per_person[salesperson_name]= int(melons_sold)
    
    return sales_per_person
    #melons_sold_salesperson[salesperson_name]= melons_sold_salesperson(salesperson_name, 0) + int(melons_sold)

def print_sales_report(melons_sold_salesperson):  

    for salesperson_name, melons_sold in melons_sold_salesperson.items():
        print(f'{salesperson_name} sold {melons_sold} melons')

print_sales_report(melons_sold_salesperson('sales-report.txt'))




