import urllib.request

url = input("Enter URL: ")
try:
    urllib.request.urlopen(url)
    print("Website is UP")
except:
    print("Website is DOWN")
