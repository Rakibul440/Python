from prettytable import PrettyTable

table = PrettyTable() # create table

table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])

table.align = 'l' # change alignment of table to left
print(table)