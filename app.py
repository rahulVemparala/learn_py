# comparison operators:
print('bag' == 'BAG')
# should return a false, as numerical rep of each character is diff, even for upper and lower case letters

print(ord('b'))
print(ord('B'))


# ternary operator
age = 35

msg = "eligble" if age > 18 else "not eligible"
print(msg)

high_income = True
good_credit = True
is_student = True


if (high_income or good_credit) and not is_student:
    print("Eligible for loan")
else:
    print("Not eligible")

# and and or operators are short circuit in nature, that is ,in a complex boolean
# operation with 'and' operations, the first occurance of a false, exists out the condition, becuase
# becuase in and atleast one condition needs to be false. similar case with 'or'.
