def celsius_to_fahrenheit():
    temp = float(raw_input("Enter a temperature: "))

    temp_in_cels = temp * 9/5 + 32
    print("{} degrees celsius is {} in fahrenheit".format(temp, temp_in_cels))

celsius_to_fahrenheit()