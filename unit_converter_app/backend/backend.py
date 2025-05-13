while True:
    convert_to = input("Please enter a unit to convert to: ").lower()
    convert_from = input("Please enter a unit to convert from: ").lower()
    amount = int(input(f"Please enter the amount of {convert_from}: "))

    if (convert_from in ['meters', 'm']) and (convert_to in ['centimeters', 'cm']):
        result = amount * 100
        print(result,"cm")

    elif (convert_from in ['centimeters', 'cm']) and (convert_to in ['meters', 'm']):
        result = amount / 100
        print(result,"m")

    elif (convert_from in ['centimeter', 'cm']) and (convert_to in ['millimetre', 'mm']):
        result = amount * 10
        print(result,"mm")

    elif (convert_from in ['millimetre', 'mm']) and (convert_to in ['centimeter', 'cm']):
        result = amount / 10
        print(result,'cm')

    elif (convert_from in ['fahrenheit', 'f']) and (convert_to in ['celcius', 'c']):
        result = amount - 32
        newresult = result * 5 / 9
        print(newresult,'°C')

    elif (convert_from in ['celcius', 'c']) and (convert_to in ['fahrenheit', 'f']):
        result = amount * 9 / 5
        newresult = result + 32
        print(newresult,'°F')

    elif (convert_from in ['kilometers', 'km']) and (convert_to in ['miles']):
        result = amount * 0.621371
        print(result,'miles')

    elif (convert_from in ['miles']) and (convert_to in ['kilometers', 'km']):
        result = amount / 0.621371
        print(result,'km')

    else:
        print("Sorry, that unit is not available")