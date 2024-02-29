thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
thisdict.update({"type": "sedan"})
print(thisdict)
thisdict.setdefault("brand", "Hyundai")  ## update value of a key
print(thisdict)
thisdict.setdefault("brand", False)  ## update value of a key
print(thisdict)
