def temperature_converter(original_temperature,conversion_unit):
    if conversion_unit == 'C':
        return (original_temperature - 32)*5/9
    elif conversion_unit == "F":
        return original_temperature * 9/5 + 32
    else:
        return("Wrong Conversion Unit")

print(temperature_converter(100,"F"))
print(temperature_converter(100,"C"))
print(temperature_converter(100,"baingan"))