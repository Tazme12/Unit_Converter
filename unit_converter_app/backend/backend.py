from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug = True)

def convert_length(unit, unit_from, unit_to):

    length_conversions = {
        "mm": 0.001,     
        "cm": 0.01,        
        "m": 1,          
        "km": 1000,    
        "in": 0.0254,     
        "ft": 0.3048,     
        "yd": 0.9144,   
        "mi": 1609.34,
     }
    
    length_in_meters = unit * length_conversions[unit_from]
    converted_length = length_in_meters / length_conversions[unit_to]

    return converted_length
    

def convert_temperature(unit, unit_from, unit_to):
        if unit_from == unit_to:
            return unit

        if unit_from == "C":
            celsius = unit
        elif unit_from == "F":
            celsius = (unit - 32) * 5 / 9
        elif unit_from == "K":
            celsius = unit - 273.15

        if unit_to == "C":
            return celsius
        elif unit_to == "F":
            return (celsius * 9 / 5) + 32
        elif unit_to == "K":
            return celsius + 273.15
        
def convert_weight(unit, unit_from, unit_to):

    weight_conversions = {
        "mg": 0.001,       
        "g": 1,            
        "kg": 1000,         
        "oz": 28.3495,    
        "lbs": 453.592,    
    }

    weight_in_grams = unit * weight_conversions[unit_from]
    converted_weight=  weight_in_grams / weight_conversions[unit_to]

    return converted_weight


@app.route("/")

def index():
    return render_template("index.html")

@app.route("/length", methods=["GET", "POST"])

def length():
    if request.method == "POST":
        try:
            unit = float(request.form["length"])
            unit_from = request.form["unitFrom"]
            unit_to = request.form["unitTo"]

            print(f"Calculating conversion: {unit} {unit_from} to {unit_to}...")

            converted_length = convert_length(unit, unit_from, unit_to)

            return render_template("length.html", result = converted_length, unit_to = unit_to)
        
        except ValueError:
            print("Form field empty")
            return render_template("length.html", result = None)
    
    else:
        return render_template("length.html", result = None)
    
@app.route("/temperature", methods=["GET", "POST"])

def temperature():

    if request.method == "POST":
        try:
            unit = float(request.form["temperature"])
            unit_from = request.form["unitFrom"]
            unit_to = request.form["unitTo"]

            print(f"Calculating conversion: {unit} {unit_from} to {unit_to}...")

            converted_temperature = convert_temperature(unit, unit_from, unit_to)

            return render_template("temperature.html", result = converted_temperature, unit_to = unit_to)

        except ValueError:
            print("Form field empty")
            return render_template("temperature.html", result = None)

    return render_template("temperature.html", result = None)

@app.route("/weight",methods=["GET", "POST"])

def weight():

    if request.method == "POST":
        try:
            unit = float(request.form["weight"])
            unit_from = request.form["unitFrom"]
            unit_to = request.form["unitTo"]

            print(f"Calculating conversion: {unit} {unit_from} to {unit_to}...")

            converted_weight = convert_weight(unit, unit_from, unit_to)

            return render_template("weight.html", result = converted_weight, unit_to = unit_to)
        
        except ValueError:
            print("Form field empty")
            return render_template("weight.html", result = None)

    return render_template("weight.html", result = None)

if __name__ == "__main__":
    app.run(debug=True);from flask import Flask, render_template, request

app = Flask(__name__)


def convert_length(unit, unit_from, unit_to):

    length_conversions = {
        "mm": 0.001,     
        "cm": 0.01,        
        "m": 1,          
        "km": 1000,    
        "in": 0.0254,     
        "ft": 0.3048,     
        "yd": 0.9144,   
        "mi": 1609.34,
     }
    
    length_in_meters = unit * length_conversions[unit_from]
    converted_length = length_in_meters / length_conversions[unit_to]

    return converted_length
    

def convert_temperature(unit, unit_from, unit_to):
        if unit_from == unit_to:
            return unit

        if unit_from == "C":
            celsius = unit
        elif unit_from == "F":
            celsius = (unit - 32) * 5 / 9
        elif unit_from == "K":
            celsius = unit - 273.15

        if unit_to == "C":
            return celsius
        elif unit_to == "F":
            return (celsius * 9 / 5) + 32
        elif unit_to == "K":
            return celsius + 273.15
        
def convert_weight(unit, unit_from, unit_to):

    weight_conversions = {
        "mg": 0.001,       
        "g": 1,            
        "kg": 1000,         
        "oz": 28.3495,    
        "lbs": 453.592,    
    }

    weight_in_grams = unit * weight_conversions[unit_from]
    converted_weight=  weight_in_grams / weight_conversions[unit_to]

    return converted_weight


@app.route("/")

def index():
    return render_template("index.html")

@app.route("/length", methods=["GET", "POST"])

def length():
    if request.method == "POST":
        try:
            unit = float(request.form["length"])
            unit_from = request.form["unitFrom"]
            unit_to = request.form["unitTo"]

            print(f"Calculating conversion: {unit} {unit_from} to {unit_to}...")

            converted_length = convert_length(unit, unit_from, unit_to)

            return render_template("length.html", result = converted_length, unit_to = unit_to)
        
        except ValueError:
            print("Form field empty")
            return render_template("length.html", result = None)
    
    else:
        return render_template("length.html", result = None)
    
@app.route("/temperature", methods=["GET", "POST"])

def temperature():

    if request.method == "POST":
        try:
            unit = float(request.form["temperature"])
            unit_from = request.form["unitFrom"]
            unit_to = request.form["unitTo"]

            print(f"Calculating conversion: {unit} {unit_from} to {unit_to}...")

            converted_temperature = convert_temperature(unit, unit_from, unit_to)

            return render_template("temperature.html", result = converted_temperature, unit_to = unit_to)

        except ValueError:
            print("Form field empty")
            return render_template("temperature.html", result = None)

    return render_template("temperature.html", result = None)

@app.route("/weight",methods=["GET", "POST"])

def weight():

    if request.method == "POST":
        try:
            unit = float(request.form["weight"])
            unit_from = request.form["unitFrom"]
            unit_to = request.form["unitTo"]

            print(f"Calculating conversion: {unit} {unit_from} to {unit_to}...")

            converted_weight = convert_weight(unit, unit_from, unit_to)

            return render_template("weight.html", result = converted_weight, unit_to = unit_to)
        
        except ValueError:
            print("Form field empty")
            return render_template("weight.html", result = None)

    return render_template("weight.html", result = None)

if __name__ == "__main__":
    app.run(debug=True)