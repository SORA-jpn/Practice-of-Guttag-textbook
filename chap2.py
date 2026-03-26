# P.20 指練習(教科書に解答例あり)
x, y, z = map(int, input("Enter 3 positive integers: ").split(","))
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



# P.29 指練習
num_x = int(input('How many times should I print the letter X? '))
to_print = ''
# ここからがコメント部
while num_x > 0:
    to_print += 'X'
    num_x -= 1
print(to_print)



# P.30 指練習(本来はwhile文で解くことを意図された問題だが、for文による解法の方が楽？)
nums = list(map(int, input("Enter 10 positive integers: ").split()))
max_odd = None

for n in nums:
    if n % 2 != 0:  
        if max_odd is None or n > max_odd:
            max_odd = n

if max_odd is None:
    print("There are no odd numbers.")
else:
    print(f"The largest odd number is {max_odd}.")