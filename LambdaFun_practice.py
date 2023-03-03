"""
Reference: https://www.learncodewithmike.com/2019/12/python-lambda-functions.html#:~:text=Lambda%E5%87%BD%E5%BC%8F%E4%B8%8D%E9%9C%80%E8%A6%81,%E5%8A%A0%E4%B8%8A%20return%20%E9%97%9C%E9%8D%B5%E5%AD%97%E3%80%82

In Python, a lambda function is a special type of function without the function name.

We use the lambda keyword instead of def to create a lambda function. Here's the syntax to declare the lambda function:

Following are some examples how to use lambda funciton.
"""

"""
Ex1: Assign lambda Function with an Argument to variable.
- lambda arguments : expression
"""
multiply = lambda a,b : a*b
print(multiply(2,3))

"""
Ex2: immediately invoked function expression
- (lambda parameter: expression)(argument)
"""
print((lambda x,y : x*y)) 
# -> <function <lambda> at 0x7ff087442af0>, the lambda function not been invoked because there are no argument for it.  
print((lambda x,y : x*y)(2,3))
# -> 6

"""
Ex3: filter() 

- filter(function, iterable)
-> the function is applied to each iterable(list, tuple, etc.) and if it returns true, 
   the element is selected by the filter() function. 
"""

nums = [1,2,3,4,5,6]

def fun1(num):
    if num > 4:
        return True
    
print(filter(fun1, nums))
# -> <filter object at 0x7ff0874614c0>
print(list(filter(fun1, nums)))
# -> [5, 6], must casting the object to list 

'''Lambda version'''
print(list(filter(lambda num: num>4, nums)))

"""
Ex4: map()

- map(function, iterable)
-> the function is applied to each iterable(list, tuple, etc.) and returns an iterator containing the results.
"""
nums = [1,2,3,4,5,6]

def fun1(num):
    return num * 2

mpa_iterator = map(fun1, nums)
print(list(mpa_iterator))

'''Lambda version'''
mpa_iterator = map(lambda num : num*2, nums)
print(list(mpa_iterator))

"""
Ex4: sorted()

- sort(iterable, key=None, reverse=False)
-> The sorted() function sorts the elements of a given iterable in a specific order (ascending or descending) and returns it as a list.
-- reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
-- key (Optional) - A "function" that serves as a key for the sort comparison. Defaults to None.
"""

dict_ls = {"A":20, "B":15, "C":16}
def fun1(item):
    print(item)
    # 0 for key 1 for value
    return item[1]

# dict.items() return list of dictionary
print(sorted(dict_ls.items(), key= fun1))

'''Lambda version'''
print(sorted(dict_ls.items(), key= lambda item : item[1]))

