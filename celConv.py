#Celsius to Fahrenheit converter
celsius = int(input("Enter the units in celsius :"))

def conv(c):
    
    return (c*9/5) +32

fahrenheit = conv(celsius)
print(fahrenheit)
