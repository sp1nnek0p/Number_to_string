number = input("Enter a number upto 4 digits: ")
nums = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
numbertxt = ""

for i in number:
    if int(i) in nums.keys():
        if len(number) > 3:
            numbertxt += nums[int(i)] + " thousand, "
            number = number.removeprefix(i)
        elif len(number) == 3:
            numbertxt += nums[int(i)] + " hundred, "
            number = number.removeprefix(i)
        elif len(number) == 2:
            if int(i) == 1:
                if number == "10":
                    numbertxt += "ten "
                    number = number.removeprefix("10")
                if number == "11":
                    numbertxt += "eleven "
                    number = number.removeprefix("11")
                if number == '12':
                    numbertxt += "twelve "
                    number = number.removeprefix("12")
                if number == '13':
                    numbertxt += "thirteen "
                    number = number.removeprefix("13")
                if number == '14':
                    numbertxt += "four-teen "
                    number = number.removeprefix("14")
                if number == '15':
                    numbertxt += "fiv-teen "
                    number = number.removeprefix("15")
                if number == '16':
                    numbertxt += "six-teen "
                    number = number.removeprefix("16")
                if number == '17':
                    numbertxt += "seven-teen "
                    number = number.removeprefix("17")
                if number == '18':
                    numbertxt += "eight-teen "
                    number = number.removeprefix("18")
                if number == '19':
                    numbertxt += "nine-teen "
                    number = number.removeprefix("19")
            if int(i) == 2:
                numbertxt += "twenty "
                number = number.removeprefix(i)    
            if int(i) == 3:
                numbertxt += "thirty "
                number = number.removeprefix(i)  
            if int(i) == 4:
                numbertxt +="fourty "
                number = number.removeprefix(i)   
            if int(i) == 5:
                numbertxt += "fifty "
                number = number.removeprefix(i)
            if int(i) == 6:
                numbertxt += "sixty "
                number = number.removeprefix(i)  
            if int(i) == 7:
                numbertxt += "seventy "
                number = number.removeprefix(i)     
            if int(i) == 8:
                numbertxt += "eighty "
                number = number.removeprefix(i)  
            if int(i) == 9:
                numbertxt += "ninty "
                number = number.removeprefix(i) 

        elif len(number) == 1:
            numbertxt += nums[int(i)]
            number = number.removeprefix(i)
print(numbertxt)

