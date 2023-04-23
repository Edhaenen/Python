#!/usr/bin/python3

# if conditional
# astrolocial sign of a given data of birth

birthDay = int(input("\nWhat is your day of birth (e.g 26): "))
birthMonth = input("\nWhat is your month of birth (e.g june): ").lower()

if birthMonth == "december":
    if birthDay < 22:
        sign = "Sagittarius"
    else : 
        sign = "Capricorn"
elif birthMonth == "january":
    if birthDay <20:
        sign = "Capricorn"
    else :
        sign = "Aquarius"
elif birthMonth == "february":
    if birthDay < 19:
        sign = "Aquarius"
    else:
        sign = "Pisces"
elif birthMonth == "march":
    if birthDay < 21:
        sign = "Pisces"
    else:
        sign = "Aries"
elif birthMonth == "april":
    if birthDay < 20:
        sign = "Aries"
    else:
        sign = "Taurus"
elif birthMonth == "may":
    if birthDay < 21:
        sign = "Taurus"
    else:
        sign = "Gemini"
elif birthMonth == "june":
    if birthDay < 21:
        sign = "Gemini"
    else:
        sign = "Cancer"
elif birthMonth == "july":
    if birthDay < 23:
        sign = "Cancer"
    else:
        sign = "Leo"
elif birthMonth == "august":
    if birthDay < 23:
        sign = "Leo"
    else:
        sign ="Virgo"
elif birthMonth == "september":
    if birthDay < 23:
        sign = "Virgo"
    else:
        sign = "Libra"
elif birthMonth == "october":
    if birthDay <23:
        sign = "Libra"
    else: 
        sign = "Scorpio"
elif birthMonth == "november":
    sign = "Scorpio" if (day < 22) else "Sagittarius"

print("your astrolocial sign is {}".format(sign))