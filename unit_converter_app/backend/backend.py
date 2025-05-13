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



    else:
        print("Sorry, that unit is not available")