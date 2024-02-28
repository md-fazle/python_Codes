thisdict={
    "brand":"Frod",
    "model":"Mustang",
    "year": 2024
}
print(thisdict)
print(thisdict["brand"])

x=thisdict.get("model")
print(x)

y=thisdict.keys()
print(x)

z=thisdict.values()
thisdict["year"]=2020
print(z)

thisdict.popitem()
print(thisdict)

# nested Dictionaries
myfamily={
    "father":{
        "name":"Abdul",
        "age":60
    },
    "mother":{
        "name":"Beauty",
        "age":55
        
    }
}
print(myfamily)