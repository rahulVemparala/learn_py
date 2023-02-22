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


# chaining comparison operators

# if age >= 18 and age < 25:
if 18 <= age < 26:
    print("youth")


# loops
# for else loop:example
succesful = False

for num in range(3):
    if succesful:
        print("attempt succesful , ending loop")
        break

else:
    print("Attempted 3 times and ended, unsuccesful :( ")
# the else block is only executed when the inner if condition fails. In this case we set the succesful flag to false, then we can see our else block execute


# infinite loops
# while True:
#     command = input(">>")
#     print(f"ECHO: {command}")
#     if command.lower() == 'quit':
#         break


# iterables:
print(type(range(4)))
for x in range(4):
    print(x)

for ch in "python":
    print(ch)
