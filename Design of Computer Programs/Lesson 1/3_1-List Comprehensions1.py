udacity_tas = ['Peter','Andy','Sarah','Gundega','Job','Sean']

bad_uppercase_tas = []
for i in range(len(udacity_tas)):
    bad_uppercase_tas.append(udacity_tas[i].upper())
print bad_uppercase_tas
    
uppercase_tas = [name.upper() for name in udacity_tas]
print uppercase_tas