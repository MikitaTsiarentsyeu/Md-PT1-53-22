
def validate_input(control_value, inputed_value):
    try:
        int_value = int(inputed_value)

        if int_value <= control_value:
            raise RuntimeError("The value is too low")
    except ValueError:
        return "The value is not numeric"
    except RuntimeError as er:
        return str(er)

cv = 35

while True:
    x = input(f"Please input your value higher then {cv}:\n")
    validation_res = validate_input(cv, x)
    if validation_res:
        print(validation_res)
        continue
    else:
        break

print("the main logic")

