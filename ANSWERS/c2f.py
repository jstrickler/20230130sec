temp_str = input("Enter Celsius temp: ")
celsius = float(temp_str)
fahrenheit = ((9 * celsius) / 5) + 32

print("{:.1f}\u00B0 C is {:.1f}\u00B0 F".format(celsius, fahrenheit))

