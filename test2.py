# 식별연산
# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x

# print(x is y)
# print(x is z)
# print(x is not y)

# a = 5
# b = 5

# print(a is b)
# print(s is not b)

# 3 == 3.0
# 3 is 5.0

# print(3 == 3.0)
# print(3 is 5.0)

# a = [3, 5, 1]
# b = a

# print(a is b)

    
# a[0] = 2

# print(a,b)

# print(a is b)

# 연산자 결합 순서
# x = 2 ** 3 ** 2
# print(x)

# x = 2 +  3 * 4
# print(x)

# x = 10 / 5 / 2
# print(x)

# x = 2 ** (3 ** 2)
# print(x)

# x = 10 % 3 % 2
# print(x)

# x = 1 + 2 > 3 and 4 - 1 < 2
# print(x)

# x = not false and true
# print(x)

# x = not true or false and true
# print(x)

# x = 1 & 2 | 3 ^ 4
# print(x)

# x = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
# print(x)

# x = 2 * -3 // 2
# print(x)

# x = 1== 2 != 3
# print(x)

# 조건문
# x = 10
# x = -1
# x = 0

# if x > 0:
#     print("x is positive")
    
# elif x < 0:
#     print("x is negative")
    
# else:
#     print("x is zero")

# num = 23
# if num % 2 == 0:
#     print("짝수")

# else:
#     print("홀수")

# a = 5
# b = 5

# if a == b:
#     print("같습니다")
# else:
#     print("다릅니다")

# 문자 = "a"

# if 문자 == "b"
#     print("false")
    
# else 문자 == "a"
#     print("true")
#     ?

# 반복문
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

# 이중 for문 출력
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in my_list:
#     for num in row:
#         print(num)

# for i in range(10) :
#     print(i)

# for char in "python":
#     print(char)

# fruits = ["apple", "banana", "cherry"]

# for fruit in reversed(fruits):
#     print(fruit)

# for fruit in sorted(fruits, reverse = True):
#     print(fruit)

# for i in range (1, 10):
#     for j in range(1, 10):
#         print(i, "x", j, "=", i*j)

# for ~ else문
# rang = [5, 8, 3, 1, 6]

# for i in rang:
#     print("element : ", i)
# else:
#     print("end process")

# 반복문 제어
# for i in range(10):
#     if i == 7:
#         break
#     elif i ==1:
#         continue
#     else:
#         pass
    
#     print(i) 

# for i in range(10):
#     if i == 7:
#         print("break", i)
#         break
#     elif i == 1:
#         print("continue", i)
#         continue
#     else:
#         print("pass", i)
#         pass
    
#     print(i)
  
# while문
# i = 1

# while i <= 5:
#     print(i)
#     i+=1

# 1
# i = 0

# while i <= 9:
#     print(i)
#     i+=1
    
# 2
# str_word = "python"
# i = 0

# while i < len(str_word):
#     print(str_word[i])
#     i += 1

# 3
# sum = 0
# i = 1

# while i <= 10:
#     sum += i
#     i +=1
    
#     print(sum)

# 4
# i = 1

# while i <= 100:
#     if i % 2 == 0:
#         print("짝수 : ", i)
#     elif i % 2 == 1:
#         print("홀수 : ", i)
#     i += 1

# 5
# i = 1

# while i <= 100:
#     if i % 7 == 0:
#         print(i)
#         i += 1