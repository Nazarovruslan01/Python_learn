# Line 1 of the input is a whole number, line 2 is a decimal number.
whole_number = int(input())
decimal_number = float(input())

# TODO: turn the two lines of text into numbers and add them up
total = whole_number + decimal_number

print(float(total))  # the sum, as a decimal
print(int(total))  # the same sum with the fraction chopped off toward zero
print(f"{whole_number} + {decimal_number} = {total}")  # the report line
