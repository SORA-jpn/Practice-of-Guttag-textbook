# P.20 指練習(教科書に解答例あり)

x, y, z = map(int, input("Enter 3 ints: ").split(","))

answer = min(x, y, z)
if x % 2 != 0:
    answer = x
if y % 2 != 0 and y > answer:
    answer = y
if z % 2 != 0 and z > answer:
    answer = z
print(answer)



# P.26 指練習
birthday = input('Enter your birthday(mm/dd/yyyy)')
month, day, year = birthday.split('/')
print(f'You were born in the year {year}.')

#