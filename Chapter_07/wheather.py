import json

data = '{"temp":30,"humidity":60,"city":"Delhi"}'
weather = json.loads(data)

print("City:", weather["city"])
print("Temp:", weather["temp"])
print("Humidity:", weather["humidity"])
# Output:
# City: Delhi
# Temp: 30
# Humidity: 60
# The code above demonstrates how to parse a JSON string in Python using the json module.

