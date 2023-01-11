import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
print(x)
# parse x:
y = json.loads(x)
print(y)


z=json.dumps(x)
print(z)


print(json.dumps({"name": "John", "age": 30}))