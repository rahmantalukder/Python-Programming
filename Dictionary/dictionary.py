
# Dictionary create concetp

person={
    "Name": "Rahman Talukder",
    "Age" : 22,
    "City": "Dhaka",
    #   ^        ^
    #  Key<---->Value
}

peroson = {
    "name": "Rahman Talukder",
    "age": 22,
    "City": "Dhaka",
}
print("Dicrionary: ", peroson)
print(peroson["name"])
print(peroson["age"])
print(peroson["City"])


Rahmn_Data={
    "name": "Rahman Talukder",
    "age": 22,
    "Adddres": "Kalkini, Madaripur"
}
print("Rahman Info: ", Rahmn_Data)
Rasedul_info={
    "name": "Rasedul Islam",
    "age":25,
    "city ": "Dhaka",
    "Addeess": "Kalkini, Madaripur"
}

print("Rasedul_info",Rasedul_info)
print(Rasedul_info["name"])
print(Rasedul_info["age"])

# Adding a new key or value pair
person1 ={
    "name": "Rahman",
    "age" : 25,
}
person1['emil']= 'rahmantalukder2002@gmail.com'
person1["Address"]= "Kalkini, Madaripur"
print(person1)

# modifying an existion key value pair

modifying={
    "name": "Rahman",
    "Address": "kalkini, madaripur",
    "Phone": "01312876690",
    "Postel Code": 2790,
}
print(modifying)
modifying['Postel Code']= 7920
print(modifying)

# remove dictionary items
remon = {
    "name": "Rahman",
    "Address": "kalkini, madaripur",
    "Phone": "01312876690",
    "Postel Code": 2790,
    "Postel Code": 2790,
}

# find dictionary length
print("Length: ", len(remon))

# remove dictionary items
del remon['Postel Code']
print(remon)

# find dictionary length len()
print("Length: ", len(remon))

# get() method in dictionary 

Get=remon.get('Phone')
print("Get for dictionary: ",Get)

# items() method in Dictionary
print(remon.items())

# keys() method in Dictionary 
person = {
    "Name": "Rahman Talukder",
    "age": 22,
    "City": "Dhaka",
    "Method": "CSE"
}
dict_keys= person.keys()
print(dict_keys)

# values() methos in dictionary
dict_values =person.values()
print(dict_values)
# clear() methos in dictionary
person3 = {
    "Name": "Rahman Talukder",
    "age": 22,
    "City": "Dhaka",
    "Method": "CSE"
}
data=person3.pop("age")
print("it is pop: ",data)
print("all:",person3)
data=person3.clear()
print(data)

country_capitals= {
    "United States": "Washington D. C",
    "Italy": "Rome",
}
for conutry in country_capitals:
    print("conutry : ",conutry)

for conutry in country_capitals:
    capitals=country_capitals[conutry]
    print("capitals: ",capitals)

myfrinad= {
    "child1":{
        "name": "rahman",
        "year": 2002,
    },
    "child2":{
        "name": "rahman",
        "year": 2002,
    },
    "child3":{
        "name": "rahman",
        "year": 2002,
    }
}

print(myfrinad)
print(myfrinad["child1"]["name"])