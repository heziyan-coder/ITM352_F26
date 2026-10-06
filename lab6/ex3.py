# determine movie price. the rules are
# - The normal price is $14
# - If someone is 65 or older, they pay $8.
# - If it is Tuesday, the price is $10.
# - If it is a matinee, the price is $5 for seniors and $8 otherwise
# name:Ziyan He
# date: sept.25.2026

age = 82
day = "Tuesday"
matinee = True

price = 14

if day == "Tuesday":
    price = 10

if age >= 65:
    price = 8

if matinee:
    if age >= 65:
        price = 5
    else:
        price = 8

print(f"Day:{day}, matinee:{matinee}")
if (age>=65):
    print("welcome, senior")
else:
    print("welcome, non-senior")

print(f"ticket price is ${price:.2f}")

