#Anyla Reeves
#11/20/24

#Init
#Functions

def is_leap_year(year):
    if year % 400 == 0:
        print("Is a leap year.")
    elif year % 100 == 0:
        print("Is a not leap year.")
    elif year % 4 == 0:
        print("Is a leap year.")
    else:
        print("Is not a leap year.")

#main
is_leap_year(2024) # Expected output: True
is_leap_year(1900)  # Expected output: False
is_leap_year(1600)
is_leap_year(2409)

