#FizzBuzz
"""- Write a function that will take a number as an argument.
- The function will loop from 0 to the number.
- If the number is divisible by 3 print `Fizz` to the terminal.
- If the number is divisible by 5 print `Buzz` to the terminal.
- if the number is divisible by 3 and 5 print `FizzBuzz` to the terminal."""

def FizzBuzz(x):
  for i in range(x+1):
    if i == 0:
      print (i)
    elif i % 3 == 0 and i % 5 != 0:
      print("Fizz")
    elif i % 5 == 0 and i %3 !=0:
      print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 != 0 and i %5 != 0:
      print(i)


#FizzBuzz(15)


#Show Me The Money
"""- Write a function that takes in a float as an argument
- This function should return the number of American coins and bills needed to represent that float. (Round to the nearest penny)

Example input/output

[input]
currency_converter(12.33)

[output]
1 $10
2 $1
1 quarter
1 nickel
3 penny"""

penny = 1
nickel = 5
dime = 10
quarter = 25
one_dollar= 100
five_dollar = 500
ten_dollar = 1000
twenty_dollar = 2000
fifty_dollar = 5000
hundred_dollar = 10000

def currency_converter(x):
  x = x * 100
  if x / hundred_dollar >= 1:
    print (str(x // hundred_dollar) + " hundred-dollar bill(s)")
    x = (x%hundred_dollar)
  if x / fifty_dollar >=1:
    print (str(x // fifty_dollar) + " fifty-dollar bill(s)")
    x = (x%fifty_dollar)
  if x / twenty_dollar >=1:
    print (str(x // twenty_dollar) + " twenty-dollar bill(s)")
    x = (x%twenty_dollar)
  if x / ten_dollar >=1:
    print(str(x // ten_dollar) + " ten-dollar bill(s)")
    x = (x%ten_dollar)
  if x / five_dollar >=1:
    print(str(x // five_dollar) + " five-dollar bill(s)")
    x = (x%five_dollar)
  if x / one_dollar >=1:
    print (str(x // one_dollar) + " one-dollar bill(s)")
    x = (x%one_dollar)
  if x / quarter >1:
    print ( str(x // quarter) + " quarter(s)")
    x = (x%quarter)
  if x / dime >1:
    print ( str(x // dime) + " dime(s)")
    x = (x%dime)
  if x / nickel >1:
    print ( str(x // nickel) + " nickel(s)")
    x = (x%nickel)
  if x / penny >1:
    print ( str(x // penny) + " penny/ies")
    x = (x%penny)
#currency_converter(171.5)


# 03-iterations-1 Challenge
"""Write a function that will take in any string and return an output that is the string in reverse
[input]
reverse_my_string("jeff")4

[output]
ffej"""

def reverse_my_string(x):
  return x[::-1]
#rint (reverse_my_string("some string"))

#04- Don't Hesitate, Iterate!!!
""" #### Challenge

- Write a for loop that will take in a number.
- When the loop is called it will iterate from `0` forward towards that number and print all the values in between to the terminal.
- Write another loop that will do the same thing but iterate backwards from that number to zero.

For example, if we have the following starter code: 

[input]
my_loop(10)

[output]
1
2
3
4
5
6
7
8
9
"""

def my_loop(x):
  num = 1
  for x in range(1,x):
    print (x)

#my_loop(4)

def my_reverse_loop(x):
  num = x-1
  for x in range (1,x):
    print (num)
    num -= 1

#my_reverse_loop(5)

#04-2 Challenge
"""Create a variable and assign it to the array below
[2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]
- Write a function that will take in this variable
- It will return the median number in the array
- It will return the average of that array
- It will return the number that occurs most frequently in the array

Please see the example `input` and `output` below.
[input]
[2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

[output]
9
14
8"""

a = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]
b = [1,2,3,4,5]
#print ("hi" + str(max(b)))
def a_function(a):
  #Median
  #import statistics
  if len(a)%2 == 0:
    median = (a[int(len(a)/2)] + a[int(len(a)/2)-1]) / 2
  else:
    median = a[int(len(a)/2)]
  #return statistics.median(a)

  #Mean
  count = 0
  total = 0
  for number in a:
    total += number
    count += 1
  average = total / count

  #Mode
  mode = max(set(a), key = a.count)

  print (mode)
  print (average)
  print (median)

#a_function(a)


# 05 - Iteration -4 Dont Hesitate, Iterate Pt2

c = [1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]]
# b = c.pop()
# print (c)
# print (b)

# for ele in c:
#   print (ele)

# for ele in c:
#   if len(str(ele)[0]) > 1:
#     for num in ele:
#       print (num)
#   else: 
#       print(ele)

  # if len(ele[0]) >= 1
  #   for num in ele:
  #     print (num)

def print_list(mylist):
    for element in mylist:
        if(isinstance(element, list)):
            print_list(element)
        else:
            print(element)

#print_list(c)

# 06 - Palindromes

def is_palindrome(word):
  lst=[]
  for letter in word:
    lst.append(letter)
  tsl=[]
  for letter in word[::-1]:
    tsl.append(letter)
  if tsl == lst:
    return True
  else:
    return False
#print (is_palindrome("jeff"))

#07 - Age Calculator
#Part 1
def age_to_time(x):
  years = x
  months = years * 12
  days = years * 365
  hours = days * 24
  minutes = hours * 60

  print("months : {}, days : {}, hours : {}, and minutes : {}".format(months, days, hours, minutes))
  #same as
  return f"months : {months}, days : {days}, hours : {hours}, and minutes : {minutes}" # will only work in Python3.6 and up
#print (age_to_time(18))

# #Part 2
# def bithday_to_time(birthday):
# def birthday_to_time(i):
def agecalc(i):
  import datetime
  today = datetime.date.today()
  i =  input("Insert Birthdate as YYYY-MM-DD: ")
  birthdate = i.split("-")
  birthyear = int(birthdate[0])
  birthmonth = int(birthdate[1])
  birthdaynum = int(birthdate[2])
  birthdaydate = datetime.date(birthyear,birthmonth,birthdaynum)
# print(isinstance(today,list))
# print(isinstance(birthdaydate,list))
# print (datetime.timedelta(today.year-birthdate.year))
  age = (today.year - birthdaydate.year - ((today.month, today.day) < (birthdaydate.month, birthdaydate.day)))
  print (f"months : {age*12}, days : {age*365}, hours : {age*365*24}, and minutes : {age*365*24*60}")

#agecalc("1994-06-20")

#DIVIDED WE FALL PT1

def divisibles(num):
  divs = []
  for i in range(1,num+1):
    if num%i == 0:
      divs.append(i)
  return divs

def divssum(num):
  divs = divisibles(num)
  sum = 0
  for ele in divs:
    sum += ele
  return sum

def divisors(num):
  divs = divisibles(num)
  count = 0
  for no in divs:
    count += 1
  return count

def divfunc(num):
  lst = []
  lst.append(divisibles(num))
  lst.append(divssum(num))
  lst.append(divisors(num))
  return lst

#print (divfunc(60))


# 99 - Review:
#1 Using one print statement, output the following text on two lines:
"""
Twinkle, twinkle, little star,
How I wonder what you are!
"""
#print("Twinkle, twinkle, little star \n How I wonder what you are!")

#2 Use the format method and the number 3.14159 to print "Pi is about equal to 3.14"
#print("Pi is about equal to {:.2f}".format(3.14159))

#3 """A bushel is 4 pecks. Use floor division and the remainder operator to find out how many bushels are in 51 pecks, and how many pecks are left over.""""
# print (51 // 4)
# print (51 % 4)

#4 What function do you call to find out how many characters are in the string "Python is fun?"
# print (len("Python is fun?"))

#5 Save your first name in a variable. Save your last name in another variable. Use an operator to combine them with a space in between in a third variable.
# var1 = "sami"
# var2 = "sawalha"
# var3 = var1 + " " + var2
# print(var3)

#6 Ask the user to input a message. Then ask them to input an integer. Print the message repeated as many times as the integer. (You can use the \* operator)
# uint = input("Please type an integer: ")
# print("Please type an integer: " * int(uint))

#7 Ask the user to input an integer and then tell the user if that integer was odd or even. 
# u = input("Please enter an integer")
# if u%2 == 0:
#   print("You picked an even integer")
# else:
#   print("You picked an odd integer")

#8 
"""Ask the user to input "rock", "paper", or "scissors"
- if they don't input any of the three, print "bad input"
- if they input rock print "it's a tie"
- if they input paper print "paper covers rock, you win"
- if they input scissors print "rock smashes scissors, you lose"
- Can you make this a complete program, where the computer picks a random rock, paper, or scissors? 
You might think of how to use random.randint creatively."""
# import random
# n = input("Please type rock, paper or scissors ")
# rand = random.randint(1,3)
# #1 is rock |  2 is paper | 3 is scissors#

# # user picked rock
# if n == "rock" and rand==2:
#   print ("computer picked paper, you lose")
# if n == "rock" and rand==1:
#   print("computer picked rock, you tie")
# if n == "rock" and rand==3:
#   print("computer picked scissors, you win")

# # user picked paper
# if n == "paper" and rand==2:
#   print ("computer picked paper, you tie")
# if n == "paper" and rand==1:
#   print("computer picked rock, you win")
# if n == "paper" and rand==3:
#   print("computer picked scissors, you lose")

# # user picked scissors
# if n == "scissors" and rand==2:
#   print ("computer picked paper, you win")
# if n == "scissors" and rand==1:
#   print("computer picked rock, you lose")
# if n == "scissors" and rand==3:
#   print("computer picked scissors, you tie")

# #bad input
# if n!= "rock" and n!="paper" and n!="scissors":
#   print("bad input")

#9 Use while to create an input loop. Ask the user to input an integer or the word 'done'. After they have input 'done' print the sum.
# sumlst = []
# suml = 0
# whileloop = input("Please input an integer or \"done\" ")
# while whileloop != "done":
#   sumlst.append(whileloop)
#   whileloop = input("Please input an integer or \"done\" ")
# for num in sumlst:
#   suml += int(num)
# print(suml)

#10 
"""Use while to create an input loop. Ask the user to input strings and input 'done' when they are done. 
Build a list from the strings and then print the number of elements in that list."""
# wordlst =[]
# whileloop = input("Please input a string or \"done\" ")
# while whileloop != "done":
#   wordlst.append(whileloop)
#   whileloop = input("Please input an string or \"done\" ")

# print(len(wordlst))

#11
"""Use while to create an input loop. 
Ask the user to input strings and input 'done' when they are done. 
Build a list from the strings. Afterward, print all of the strings in the list in UPPERCASE. (hint: .upper())
"""
# wordlst =[]
# whileloop = input("Please input a string or \"done\" ")
# while whileloop != "done":
#   wordlst.append(whileloop.upper())
#   whileloop = input("Please input an string or \"done\" ")
# for word in wordlst:
#   print (word)

#12 
""" Use while to create an input loop. Ask the user to input strings and input 'done' when they are done. 
Create a new list that is the length of each of the corresponding strings. 
Then print the total length of all of the strings the user input."""
# wordlst =[]
# lensum = 0
# whileloop = input("Please input a string or \"done\" ")
# while whileloop != "done":
#   wordlst.append(len(whileloop))
#   whileloop = input("Please input an string or \"done\" ")
# for num in wordlst:
#   lensum+=num
# print (lensum)

#13 Have the user input two strings. Print out all letters that appear in both strings
# x = input()
# y = input()
# lstxy = []
# for letter in x:
#   if letter in y and letter not in lstxy:
#     lstxy.append(letter)
# print(lstxy)

#14 Write a function that takes a single letter as its argument (a one character string) return True if the letter is a vowel and False if it is not.

def isvowel(letter):
  vowels = ['a','e','i','o','u','y']
  if letter in vowels:
    return True
  else:
    return False

# print(isvowel("a"))

#15 Write a function that takes a word as its input and returns a new string that is the word with none of the vowels in it.
# Use your function from problem 14 in your solution to problem 15
def remove_vowels(word):
  vowels = ['a','e','i','o','u','y']
  for letter in word:
    if isvowel(letter) == True:
      new = word.split(letter)
  newstr = ""
  for letter in new:
    newstr += letter
  return newstr

#print(remove_vowels('cheese'))

#16 Write a function that takes a list of any kind of objects and returns a new list of all of those objects converted into strings. 
# (you can call str(x) on anything in python)
def strobj(obj):
  lst =[]
  for ele in obj:
    lst.append(str(ele))
  return lst

#print (strobj("x"))

#17 list(range(20)) will create a list of the numbers from 0 to 19. Use your function from 16 to
#convert that list to a list of strings and then use ```", ".join(newlist)``` to print the numbers out as a comma separated list
#print(", ".join(strobj(range(20))))

#18 Write a function that takes a positive integer as its one argument
#and prints out a comma separated list of the numbers from 1 to that integer (including it) print the word 'and' before the last element.
def print_numbers(positive_int):
  print(", ".join(strobj(range(positive_int))) + ", and " + str(positive_int))

#print_numbers(20)

#19 Write a function that is given two lists as its arguments and returns the number of elements that are in both of the lists.
def intersection(Alst,Blst):
  count = 0
  for element in Alst:
    count += Blst.count(element)
  return count

#print(intersection(["A", "B", "C", "D"], ["C", "D", "E", "F"]))

#20 Write a function that reverses a string.
def reverse(x):
  return x[::-1]

#21 Write a function that returns the sum of every second element of a list of numbers starting with the first.
def sumeven(numlst):
  sum2 = 0
  for num in numlst[::2]:
    sum2 += num
  return sum2
#print(sumeven([2,3,4,5,6]))

#22 Write a function that takes a list as its argument and returns a new list that is that list repeated twice.
def double_list(lst):
  lst2 = lst
  lst3 = lst + lst2
  return lst3
#print(double_list([2,3,4,5,6]))

#23 Write a function that takes a positive whole number and returns a list of its digits as integers. 
# You can solve this either by converting it to a string or 
# using n % 10 = ones digit and n // 10 = number shifted to the right, dropping the ones digit.
def digitlst(num):
  numlst = []
  for ele in str(num):
    numlst.append(ele)
  print(numlst)
#digitlst(33)

#24 Write a function that takes a list of strings and returns the longest string in the list. 
#If there is a tie, return the earlier string in the list.

def longest(stringlst):
  elelen = 0
  for ele in stringlst:
    if len(ele) > elelen:
      elelen = len(ele)
      mostlen = ele
  return mostlen
#print(longest(['two', 'three', 'four', 'five', 'six', 'seven', 'eight']))

#25 Write a function that takes a list of strings and returns a list of tuples, where each element is the original string and its length.
def lengths(lst):
  tup = []
  for element in lst:
    tup = tup + [(element,len(element))]
  return tup
#print(lengths(['two', 'three', 'four']))

#26 Write a function that takes a list of strings and returns a dictionary, 
# where the keys are the strings from the list and the values are the lengths of those strings.

def lengthdict(lst):
  ldict = {}
  for ele in lst:
    ldict[ele] = len(ele)
  return ldict
#print(lengthdict(['two', 'three', 'four']))

#27 Write a python function that takes two lists of equal length and 
# creates a dictionary where each key is an element of the first, 
# and the value is the element of the second at the same location.

def zipdict(lst,lst1):
  zdict = dict(zip(lst,lst1))
  return zdict
#print(zipdict(["A", "B", "C"], [1, 2, 3]))

#28 Write a function that takes a string as its input and then
# counts the number of times each character appears in that string, returning a dictionary of those values.
def countchar(words):
  char = []
  count = []
  ccdict = {}
  for ele in words:
    char.append(ele)
    count.append(words.count(ele))
    ccdict[ele] = words.count(ele)
  return ccdict
#print (countchar("An apple"))

#29 Write a function that takes a dictionary of the format returned by the function in 28 
# and then prints out the counts for each alphabetical character. 
# (string.isalpha() returns True for a letter and false for other characters)

def printtable(dict28):
  for key in dict28:
    if key.isalpha() == True:
      print(str(key) + " appears " + str(dict28[key]) + " time(s).")
      
#printtable(countchar("An apple"))

#30 Write a function that takes two dictionaries where all the values are integers (the keys can be anything). 
# Return a new dictionary that has all the keys from both dictionaries with their values. 
# If a key appears in both dicitonaries, its value in the new dictionary should be the sum.

def mergedict(dict1,dict2):
  dict3 = {}
  for key in dict1:
    if key in dict2:
      dict3[key]=(dict1[key]+dict2[key])
    else:
      dict3[key] = dict1[key]
  for key in dict2:
    if key not in dict3:
      dict3[key] = dict2[key]
  return dict3
print (mergedict({"A": 1, "B": 2}, {"B": 3, "C": 4}))

#to add files to github
#git add . (to select all files in current directory)
#git commit -m (commit to hash) (-m " " to add a message for the commit)
# git push origin master (master is for master branch)

