1: Using one print statement, output the following text on two lines:
```
Twinkle, twinkle, little star,
How I wonder what you are!
```

2: Use the format method and the number 3.14159 to print "Pi is about equal to 3.14"

3: A bushel is 4 pecks. Use floor division and the remainder operator to find out how many bushels are in 51 pecks, and how many pecks are left over.

4: What function do you call to find out how many characters are in the string "Python is fun?"

5: Save your first name in a variable. Save your last name in another variable. Use an operator to combine them with a space in between in a third variable.

6: Ask the user to input a message. Then ask them to input an integer. Print the message repeated as many times as the integer. (You can use the \* operator)

7: Ask the user to input an integer and then tell the user if that integer was odd or even. 

8: Ask the user to input "rock", "paper", or "scissors"

* if they don't input any of the three, print "bad input"

* if they input rock print "it's a tie"

* if they input paper print "paper covers rock, you win"

* if they input scissors print "rock smashes scissors, you lose"

* Can you make this a complete program, where the computer picks a random rock, paper, or scissors? You might think of how to use random.randint creatively.

9: Use while to create an input loop. Ask the user to input an integer or the word 'done'. After they have input 'done' print the sum.

10: Use while to create an input loop. Ask the user to input strings and input 'done' when they are done. Build a list from the strings and then print the number of elements in that list.

11: Use while to create an input loop. Ask the user to input strings and input 'done' when they are done. Build a list from the strings. Afterward, print all of the strings in the list in UPPERCASE. (hint: .upper())

12: Use while to create an input loop. Ask the user to input strings and input 'done' when they are done. Create a new list that is the length of each of the corresponding strings. Then print the total length of all of the strings the user input.

13: Have the user input two strings. Print out all letters that appear in both strings.

14: Write a function that takes a single letter as its argument (a one character string) return True if the letter is a vowel and False if it is not.

15: Write a function that takes a word as its input and returns a new string that is the word with none of the vowels in it.

```
>>> print(removevowel("ByteAcademy"))
Bytcdmy
```

Use your function from problem 14 in your solution to problem 15

16: Write a function that takes a list of any kind of objects and returns a new list of all of those objects converted into strings. (you can call str(x) on anything in python)

17: list(range(20)) will create a list of the numbers from 0 to 19. Use your function from 16 to convert that list to a list of strings and then use ```", ".join(newlist)``` to print the numbers out as a comma separated list

18: Write a function that takes a positive integer as its one argument and prints out a comma separated list of the numbers from 1 to that integer (including it) print the word 'and' before the last element.

```
print_numbers(4)
1, 2, 3, and 4
```

19: Write a function that is given two lists as its arguments and returns the number of elements that are in both of the lists.

```
intersection(["A", "B", "C", "D"], ["C", "D", "E", "F"])
# returns 2
```

20: Write a function that reverses a string.

21: Write a function that returns the sum of every second element of a list of numbers starting with the first.

```
sum_even([2,3,4,5,6])
# returns 12
```

22: Write a function that takes a list as its argument and returns a new list that is that list repeated twice.
```
double_list([2,3,4,5,6])
# returns 2,3,4,5,6,2,3,4,5,6

23: Write a function that takes a positive whole number and returns a list of its digits as integers. You can solve this either by converting it to a string or using n % 10 = ones digit and n // 10 = number shifted to the right, dropping the ones digit.

24: Write a function that takes a list of strings and returns the longest string in the list. If there is a tie, return the earlier string in the list.

```
print(longest(['two', 'three', 'four', 'five', 'six', 'seven', 'eight']))
# prints 'three'
```

25: Write a function that takes a list of strings and returns a list of tuples, where each element is the original string and its length.

```
lengths(['two', 'three', 'four'])
[('two', 3), ('three', 5), ('four', 4)]
```

26: Write a function that takes a list of strings and returns a dictionary, where the keys are the strings from the list and the values are the lengths of those strings.

```
lengthdict(['two', 'three', 'four'])
# returns {'two' : 3, 'three': 5, 'four': 4}
```

27: Write a python function that takes two lists of equal length and creates a dictionary where each key is an element of the first, and the value is the element of the second at the same location.

```
zipdict(["A", "B", "C"], [1, 2, 3])
# returns {"A": 1, "B": 2, "C": 3}
```

28: Write a function that takes a string as its input and then counts the number of times each character appears in that string, returning a dictionary of those values.

```
countchar("An apple")
# returns {"A": 1, "n": 1, " ": 1, "a": 1, "p": 2, "l": 1, "e": 1}
```

29: Write a function that takes a dictionary of the format returned by the function in 28 and then prints out the counts for each alphabetical character. (string.isalpha() returns True for a letter and false for other characters)

```
printtable(countchar("An apple")
A appears 1 time(s).
n appears 1 time(s).
a appears 1 time(s).
p appears 2 time(s).
l appears 1 time(s).
e appears 1 time(s).
```

30: Write a function that takes two dictionaries where all the values are integers (the keys can be anything). Return a new dictionary that has all the keys from both dictionaries with their values. If a key appears in both dicitonaries, its value in the new dictionary should be the sum.


```
mergedict({"A": 1, "B": 2}, {"B": 3, "C": 4})
# returns {"A": 1, "B": 5, "C": 4}
```
