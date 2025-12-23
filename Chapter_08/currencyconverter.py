rates = {"USD": 83, "EUR": 90}

amt = float(input("Amount in INR: "))
currency = input("Convert to (USD/EUR): ")

if currency in rates:
    print("Converted:", amt / rates[currency])
else:
    print("Invalid Currency")
# Currency Converter: INR to USD/EUR
# Exchange Rates
# 1 USD = 83 INR
# 1 EUR = 90 INR
# Input Amount in INR
# Input Target Currency (USD or EUR)
# Perform Conversion
# Display Converted Amount or Error Message


