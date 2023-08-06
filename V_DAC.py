def V_DAC(value):
    AVM = value * 5 / 1023
    return round(AVM, 2)

value = float(input("Enter a decimal number representation of a signal: "))
print("The analog voltage level equals", V_DAC(value))