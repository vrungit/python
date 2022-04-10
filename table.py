from prettytable import PrettyTable
my_table= PrettyTable()


my_table.add_column("city",["Lonodon","Paris","NY"])
my_table.add_column("Visitors",[100,200,300])
my_table.align="c"
print(my_table)