# json module operation
import json

d = {"name": "python", "fees": 15000, "duration": "2 months"}

f = json.dumps(d)           # convert python object or data to json formate

print(type(f))
print(f)

y = json.loads(f)           # convert json to python object
print(type(y))
print(y)
