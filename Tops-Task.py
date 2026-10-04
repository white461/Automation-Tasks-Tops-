# # 1. Write a function that accepts a list of numbers and returns the average of the numbers.
# # lst = [10, 20, 30, 40]
# # print(sum(lst) / len(lst))

# # 2.Uppercase if length is greater than 5, otherwise lowercase
# # upper_or_lower = lambda t: t.upper() if len(t) > 5 else t.lower()
# # print(upper_or_lower(input("Enter string: ")))

# # 3.Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.
# # def divisible_by_3(numbers):
# #     return list(filter(lambda n: n % 3 == 0, numbers))

# # print(divisible_by_3([1, 3, 5, 6, 9, 10, 12])) 

# # 4. Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.
# # def square_list(numbers): 
# #     # Using list comprehension to square each number
# #     return [n ** 2 for n in numbers]
# # print(square_list([1, 2, 3, 4, 5]))


# # # 5.Write a function that accepts a string and counts how many vowels are in the string.
# # def count_vowels(text):
# #     count = 0
# #     for ch in text.lower():
# #         if ch in "aeiou":
# #             count += 1
# #     return count

# # print(count_vowels("Dhaval is best Engineer"))

# # # 6. Write a function that accepts a list of strings and returns the longest string in the list.
# # def longest_string(words):
# #     longest = words[0]
# #     for word in words:
# #         if len(word) > len(longest):
# #             longest = word
# #     return longest

# # print(longest_string(["ZNMD", "Fighter", "Road", "Race"])) 

# # 7. Write a function that accepts a number and checks if it is an Armstrong number.
# # is_armstrong = lambda n: sum(int(d) ** len(str(n)) for d in str(n)) == n

# # n = int(input("Enter a number: "))
# # if is_armstrong(n):
# #     print("Armstrong number")
# # else:
# #     print("Not an Armstrong number")

# # # 8. Write a function that accepts a number and returns the sum of its digits

# # def sum_digits(num):
# #     total = 0

# #     for digit in str(num):
# #         total = total + int(digit)

# #     return total


# # print(sum_digits(1234))

# # 9.Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.
# # def alternate_case(text):
# #     result = ""

# #     for i in range(len(text)):
# #         if i % 2 == 0:
# #             result = result + text[i].upper()
# #         else:
# #             result = result + text[i].lower()

# #     return result


# # print(alternate_case("python"))

# # # 10.Write a function that accepts a list of strings and returns a new list with only the strings that have an odd length.
# # def odd_length_strings(lst):
# #     result = []

# #     for word in lst:
# #         if len(word) % 2 != 0:
# #             result.append(word)

# #     return result


# # print(odd_length_strings(["cat", "apple", "hi", "python", "dog"]))

# # 11.Write a function that accepts a string and a substring, and returns True if the substring is found in the string, otherwise False.
# # def check_substring(text, sub):
# #     if sub in text:
# #         return True
# #     else:
# #         return False


# # print(check_substring("Hello Python", "Welcome"))

# # 12.Write a function that accepts a list of numbers and returns a new list with all the numbers that are divisible by both 2 and 3.
# def divisible_by_2_and_3(lst):
#     result = []

#     for num in lst:
#         if num % 2 == 0 and num % 3 == 0:
#             result.append(num)

#     return result


# print(divisible_by_2_and_3([6, 10, 12, 15, 18, 20]))

# 13.Write a function that accepts a string and returns True if the string is a valid email address (contains "@" and "."), otherwise False.

# def valid_email(email):
#     if "@" in email and "." in email:
#         return True
#     else:
#         return False


# print(valid_email("abc@gmail.com"))

# 14.Write a function that accepts a list of integers and returns the second largest number in the list.
# def second_largest(lst):
#     lst.sort()
#     return lst[-2]


# print(second_largest([10, 20, 5, 30, 15]))

# 15. Write a function that accepts a list of numbers and returns the average of the numbers, excluding any zero values
# def average_without_zero(lst):
#     total = 0
#     count = 0

#     for num in lst:
#         if num != 0:
#             total = total + num
#             count = count + 1

#     return total / count


# print(average_without_zero([10, 20, 0, 30, 0, 40]))

# 16. Write a function that accepts two strings and returns the common characters between them.
# def common_characters(str1, str2):
#     result = ""
#     for ch in str1:
#         if ch in str2 and ch not in result:
#             result += ch
#     return result

# print(common_characters("hello", "world"))

# 17. Write a function count_character(string, char) that accepts a string and a character, and returns the number of times the character appears in the string.
# Using the built-in count()
# def count_character(string, char):
#     return string.count(char)



# 23. Write a Python program that uses the map() function to square each number in a given list of integers. Input: [1, 2, 3, 4], Output: [1, 4, 9, 16]
# numbers = [1, 2, 3, 4]
# squares = list(map(lambda n: n ** 2, numbers))
# print(squares)  

# # 24. Write a Python program that uses map() to convert a list of strings to uppercase. Input: ['apple', 'banana', 'cherry'], Output: ['APPLE', 'BANANA', 'CHERRY']
# fruits = ['apple', 'banana', 'cherry']
# upper_fruits = list(map(str.upper, fruits))
# print(upper_fruits) 

# # 25. Write a Python program that uses map() to find the length of each string in a list of strings. Input: ['hello', 'world', 'python'], Output: [5, 5, 6]
# words = ['hello', 'world', 'python']
# lengths = list(map(len, words))
# print(lengths)

# # 26. Write a Python program that uses map() to add a given number to each element in a list. Input: [1, 2, 3, 4], 5, Output: [6, 7, 8, 9]
# nums = [1, 2, 3, 4]
# add = 5
# result = list(map(lambda n: n + add, nums))
# print(result) 


