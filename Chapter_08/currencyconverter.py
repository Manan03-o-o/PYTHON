rates = {"USD": 83, "EUR": 90}

amt = float(input("Amount in INR: "))
currency = input("Convert to (USD/EUR): ")

if currency in rates:
    print("Converted:", amt / rates[currency])
else:
    print("Invalid Currency")
