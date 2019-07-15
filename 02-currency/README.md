# Show Me The Money
---

##### Challenge
* Write a function that takes in a float as an argument
* This function should return the number of American coins and bills needed to represent that float. (Round to the nearest penny)

Use the following as denominations for your currencies:

```
    Penny: 1 cent
    Nickel: 5 cent
    Dime: 10 cent
    Quarter: 25 cent
    One-dollar bill
    Five-dollar bill
    Ten-dollar bill
    Fifty-dollar bill
    Hundred-dollar bill
```

##### Please make sure the function follows the below format

```
def currency_converter(amount):
```

#####Example input/output
```
[input]
currency_converter(12.33)

[output]
1 $10
2 $1
1 quarter
1 nickel
3 penny
```
* Don't worry about making the denomination words plural. For example, `3 penny` is OK and doesn't need to be `3 pennies`.
