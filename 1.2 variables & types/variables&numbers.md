
# 1.2 Variables & Types & 1.3 Basic Arithmetic

## 1.2

variables are created when a value is assigned. 

````python
a = 10

b = "bria"


print(a)


print(b)
````
 variables can change even after being set 
```python
 x = 10     # x is of type int
x = "bria" # x is now of type str
print(x) 
```
To retrieve data type of a variable you can
````python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
````
variables are case sensitive
a or A will create two variables for example
````python
a = 5
A = 5
# two variables will be created 
````


'Data types are very important using python. You dont have to declare the type of variable Python will automatically. The most common types of data types python uses are'

   1. int: an integer, e.g., 1, 2, 3
   2. float: a floating-point (decimal) number, e.g., 1.0, 1.5, 3.14
   3. str: a string (text), e.g., “hello”, “world”
   4. bool: a boolean, which can be True or False.
   5. To check the type of variable use the type() function:

   ````python
   print(type(name)) # <class 'str'>
   ````

## 1.3 Basic Arithmetic
Performs common mathematical operations. 
   Heres the basic arithmetics python accepts:
   - Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Exponentiation (**)
- Modulus (%)
- Floor division (//)
Heres how they can be used:

````python
x = 10
y = 2

print(10 + 2) # 12
print(10 - 2) # 8
print(10 * 2) # 20
print(10 / 2) # 5.0
print(10 ** 2) # 100
print(10 % 2) # 0
print(10 // 2) # 5
````
