while True:
    convert_to = input("Please enter a unit to convert to: ").lower()
    convert_from = input("Please enter a unit to convert from: ").lower()
    amount = float(input(f"Please enter the amount of {convert_from}: "))

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

    elif (convert_from in ['inches']) and (convert_to in ['feet', 'ft']):
        result = amount / 12
        print(result,'ft')

    elif (convert_from in ['feet', 'ft']) and (convert_to in ['inches']):
        result = amount * 12
        print(result,'inches')

    elif (convert_from in ['litre', 'l']) and (convert_to in ['pint']):
        choice = input("Would you like UK or US pints?: ").lower()
        if choice == 'us':
            result = amount * 1.75975
        elif choice == 'uk':
            result = amount * 2.11338
        else:
            print("Please enter either US or Uk.")

    elif (convert_from in ['pint']) and (convert_to in ['litre', 'l']):
        choice = input("Would you like to UK or US pints?: ").lower()
        if choice == 'us':
            result = amount / 1.75975
        elif choice == 'uk':
            result = amount / 2.11338
        else:
            print("Please enter either US or Uk.")

    elif (convert_from in ['hour', 'hrs', 'hours', 'hr']) and (convert_to in ['minutes', 'mins', 'min']):
        result = amount * 60
        print(f"{result:.0f} mins")

    elif (convert_from in ['minutes', 'mins', 'min']) and (convert_to in ['hours', 'hrs', 'hour', 'hr']):
        result1 = amount // 60
        remaining_mins = amount % 60
        print(f"{result1} hr {remaining_mins} mins")

    else:
        print("Sorry, that unit is not available")