def celsius_to_fahrenheit():
    temp = float(raw_input("Enter a temperature: "))

    temp_in_cels = temp * 9/5 + 32
    print("{} degrees celsius is {} in fahrenheit".format(temp, temp_in_cels))


def fahrenheit_to_celsius():
    temp = float(raw_input("Enter a temperature: "))

    temp_in_fahrenheit = temp - 32 * 5/9
    print("{}F is {} degrees celsius".format(temp, temp_in_fahrenheit))


temp_1 = raw_input("Enter the temperature you want converted [celsius/fahrenheit]: ").lower()
temp_2 = raw_input("Enter the metric you want the temperature converted to [celsius/fahrenheit]: ").lower()

def convert():
    while temp_1 == temp_2:
        print("Invalid operation")
        break
    if temp_1 == "celsius" and temp_2 == "fahrenheit":
        celsius_to_fahrenheit()
    elif temp_1 == "fahrenheit" and temp_2 == "celsius":
        fahrenheit_to_celsius()


convert()