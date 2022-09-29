# # Challenge 1: To find number of digits without using int method in the input function.
# def numberofdigit(num):
#     return len(num)
#
#
# challenge1 = numberofdigit(input("Enter a number: "))
# print(challenge1)
#
#
# # Challenge 2: Reverse the given output number, without using int method in the input function.
# def reversenum(num):
#     return num[::-1]
#
#
# challenge2 = reversenum(input("Enter a number: "))
# print(challenge2)
#
#
# # Challenge 3: To find number of zeros in the end of the factorial of number, without using int method in the input function.
# def endzero(n):
#     count = 0
#     while (n >= 5):
#         n //= 5
#         count += n
#
#     return count
#
# num3=input("Enter a number: ")
# result=0
# for i in num3:
#     for j in range(11):
#         if i==f"{j}":
#             result = 10 * result + j
# challenge3 = endzero(result)
# print(challenge3)
#
#
# # Challenge 4: make dict out of two lists.
# def makedict(list1, list2):
#     outputdict = {}
#     for i in range(len(list1)):
#         outputdict[list1[i]] = list2[i]
#     return outputdict
#
#
# list1 = ['India', 'England', 'Spain']
# list2 = ['Delhi', 'London', 'Madrid']
# challenge4 = makedict(list1, list2)
# print(challenge4)
#
# # Challenge 5: make dict readble.
# places = {("19.07'53.2", "72.54'51.0"): "Mumbai",
#
#           ("28.33'34.1", "77.06'16.6"): "Delhi"}
# city = {}
# for k, v in places.items():
#     city[v] = {"Latitude": k[0], "Longitude": k[1]}
# print(city)
#
# # Challenge 6: Using for loop find the sum of all even numbers in mylist.
# mylist = [3, 5, 4, 6, 9, 10, 2, 8, 7, 1]
# sum = 0
# for i in mylist:
#     if i % 2 == 0:
#         sum += i
# print(sum)
