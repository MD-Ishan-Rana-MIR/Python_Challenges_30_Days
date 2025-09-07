# for i in range(10,50,2):
#     print(i)
from operator import index

# for i in range (50,10,-2):
#     print(i)

# ১ থেকে ১০ পর্যন্ত সংখ্যা প্রিন্ট করো।

# result = 0
#
# for i in range (1,11) :
#     result = result + i
# print(result)

# ১ থেকে ১০ পর্যন্ত সব জোড় সংখ্যা প্রিন্ট করো।

# for number in range(1,11) :
#     if(number%2==0) :
#         print(number)

# ১ থেকে ১০ পর্যন্ত সব বেজোড় সংখ্যা প্রিন্ট করো।

# for number in range(1,11):
#     # print(number)
#     if(number %2==1) :
#         print(number)


# ৫ এর নামতা (মাল্টিপ্লিকেশন টেবিল) প্রিন্ট করো।

# for number in range(1,11):
#     print(number, "*", "5" "="  ,5 * number)

# একটা লিস্টে [2, 4, 6, 8, 10] আছে—এগুলোর বর্গ (square) বের করে প্রিন্ট করো।

# numbers = [2, 4, 6, 8, 10]
#
# for number in numbers :
#     squre = number * number
#     print(squre)



# একটা স্ট্রিং "Python" এর প্রতিটি অক্ষর আলাদা করে প্রিন্ট করো।

#
# name = "python"
# for letter in name:
#     print(letter)

# একটা লিস্টে নামগুলো আছে["Ali", "Hasan", "Sumi", "Rina"] — প্রত্যেকটার সাথে "Hello" # প্রিন্ট# করো।

# name_list = ["Ali", "Hasan", "Sumi", "Rina" ]
#
# for name in name_list:
#     print("Hello" ,name)




# ১ থেকে ১০ এর factorial বের করো।

# for number in range(1,11):
#     fact = 1
#     for i in range(1,number+1):
#         fact *= i
#     print(fact)


# ১ থেকে ৫০ এর মধ্যে সব মৌলিক সংখ্যা (prime number) বের করো।
#
# for num in range(2, 51):   # 2 থেকে 50 পর্যন্ত চেক করব
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):  # √num পর্যন্ত চেক করলেই যথেষ্ট
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")


# for number in range(1,51):
#     is_prime = True
#     print(number)
#     for num in range(int(number*0.5)+1):
#         if number % 2 == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(number)

# একটা লিস্টে সংখ্যা আছে [5, 10, 15, 20, 25] — এগুলোর যোগফল বের করো।

# numbers = [5, 10, 15, 20, 25]
#
# result = 0
# for number in numbers:
#     result = result + number
# print(result)

# একটা স্ট্রিং "Bangladesh" এ কয়টা স্বরবর্ণ (a, e, i, o, u) আছে সেটা গুনে বের করো।

# country_name = 'Bangladesh'
# count_number = 0
# for country in country_name:
#     if country == "a":
#         count_number += 1
#     elif country == "e":
#         count_number += 1
#     elif country == "i":
#         count_number += 1
#     elif country == "o":
#         count_number += 1
#     elif country == "u":
#         count_number += 1
# print(count_number)


# name = "I Love Data Science"
#
# data = name.split()
#
# print(data)
#
# for i in range (len(data)):
#     print(data[i],i)



# name = "Ishan"
#
# data = name.split(" ")
#
# print(data)
#
#
#
# for i in range(0,len(data)):
#     print(data[i])
#
# result = 0
# for i in range(1,20) :
#     if i%2 == 0 :
#         result += i
# print(result)
#
# count = 0
# while count < 10 :
#     count += 1
#     if count % 2 == 0 :
#         break
#     print("Python")

# numbers = [1, 20, 3, 30]
#
# total = 0
#
# index = 0
#
# while index < len(numbers):
#     total = total+numbers[index]
#     index = index+1
#     print(total, index)


data = "i love python"
index = 0

while index < len(data):
    print(data[index])
    index += 1




































