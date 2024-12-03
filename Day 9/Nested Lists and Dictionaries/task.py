capitals = {
    "France" : "Paris",
    "India" : "Delhi",
    "Germany" : "Berlin",
}


travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# Accessing list into dict
print(travel_log["France"][1])

for country in travel_log : # Accessing Key from dict
    print(country,end=" : ")
    for city in travel_log[country]: # accessing element from list
        print(city,end=" , ")
    print("\n")

#                          0    1
nested_list = ["A", "B", ["C", "D"]]
#               0    1    ----2----
print(nested_list[2][1]) # position of D

# Nested Dict
travel_log2 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

# Accessing 'Stuttgrat'
print(travel_log2["Germany"]["cities_visited"][2])