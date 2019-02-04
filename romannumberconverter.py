import sys
import numbers




def Convert(input):
    # find the romertal.
    if isinstance(input, numbers.Number):
        if input > 5999:
            print("Max number exceeded. Please go no further than 5999.")
        else:
            result = GetRomertal(input)
            print(result)
    elif input.isalpha():
        if input == "X":
            result = 10
            print("%s is %d!" % (input,result))
    else:
        print("invalid value")



def GetRomertal(input):
    result = (input // 1000) * 'M'
    input -= ((input // 1000) * 1000)
    if input > 899 and input < 1000:
        result += 'CM'
        input -= 900
    else:
        result += (input // 500) * 'D'
        input -= ((input // 500) * 500)
    if input > 399 and input < 500:
        result += 'CD'
        input -= 400
    else:
        result += (input // 100) * 'C'
        input -=  ((input // 100) * 100)
    if input > 89 and input < 99:
        result += 'XC'
        input -= 90
    if input > 39 and input < 50:
        result += 'XL'
        input -= 40
    else:
        result += (input // 50) * 'L'
        input = input - ((input // 50) * 50)
    if input >= 10 or input <= 30:
        result += (input // 10) * 'X'
        input -= ((input // 10) * 10)
    if input == 9:
        result += 'IX'
        input -= 9
    if input > 5 and input < 9:
        calc = (input - 5) // 1 * 'I'
        num = 'V'
        result += ("%s%s" % (num, calc))
    if input == 4:
        result += 'IV'
    if input >= 0 and input <= 3:
        result += (input // 1) * 'I'
        input -= (input // 1)


    return result

Convert(1939)
