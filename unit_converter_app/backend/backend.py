convert_to = input("Please enter a unit to convert to: ").lower()
convert_from = input("Please enter a unit to convert from: ").lower()
amount = int(input(f"Please enter the amount of {convert_from}: "))

if (convert_from in ['meters', 'm']) and (convert_to in ['centimeters', 'cm']):
    result = amount * 100
    print(result, "cm")

elif (convert_from in ['centimeters', 'cm']) and (convert_to in ['meters', 'm']):
    result = amount / 100
    print(result, "m")