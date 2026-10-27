# 2004
# Round 1 Q1
# Mayan Calendar

# Convert into days
# Remove all whole number of years
# Iterate through until month
# Print remaining number of days

mayan = input().split(' ')

for i in range(len(mayan)):
    mayan[i] = int(mayan[i])

days = mayan[0]*20*20*18*20 + mayan[1]*20*18*20 + mayan[2]*18*20 + mayan[3]*20 + mayan[4] # conversion into days
days -= 13*144000 + 20*7200 + 7*360 + 16*20 + 3 # subtracting reference date


monthbounds = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapbounds = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

years = [365, 365, 365, 366]
years = 0

while True:
    year_length = 365
    if (2000 + years) % 4 == 0:
        year_length = 366

    if days < year_length:
        break

    days -= year_length
    years += 1

if years%4 == 0:
    bounds = leapbounds

else:
    bounds = monthbounds

    
for i in range(len(bounds)):
    if days - bounds[i] >= 0:
        days -= bounds[i]

    else:
        month = i+1
        break

print(days+1, month, years+2000)


# b) 13, 20, 7, 17, 14 and 13, 20, 8, 16, 9
# c) 2880000 days, Wednesday

