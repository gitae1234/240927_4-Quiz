#Quiz 1
if user_input == "안녕하세요":
    print("반갑습니다")
else:
    print("인사를 먼저하세요")



#Quiz 2
user_input = input("값을 입력하세요: ")

result = int(user_input) + 100

if result >= 150:
    print(result)
else:
    print("값이 부족합니다.")



#Quiz 3
numbers = [100, 200, 300]
result = []

for price in numbers:
    vat_included_price = price * 1.1
    result.append(vat_included_price)

print(result)



#Quiz 4
numbers = [3, 100, 23, 33, 72, 94]

print([num for num in numbers if num % 3 == 0])



#Quiz 5
waiting_number = 1
max_number = 1000

while waiting_number <= max_number:
    print(f"대기번호: {waiting_number}")
    waiting_number += 1



#Quiz 6
    number = 1
    sum = 0

    while number <= 100:
        if number % 2 != 0:
            sum += number
        number += 1

    print(sum)