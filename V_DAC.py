#That algorithm takes a decimal number representation of a signal and
#returns the analog voltage level that would be created by a DAC if it were
#given the same number in binary

def V_DAC(value):
    AVM = value * 5 / 1023
    return round(AVM, 2)

value = float(input("Enter a decimal number representation of a signal: "))
print("The analog voltage level equals", V_DAC(value))