import json

data = '{"temp":30,"humidity":60,"city":"Delhi"}'
weather = json.loads(data)

print("City:", weather["city"])
print("Temp:", weather["temp"])
print("Humidity:", weather["humidity"])
