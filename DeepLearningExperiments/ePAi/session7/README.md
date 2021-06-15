# Assignment 7

in this assignment we will go over global scope, local scope , nonlocal scope, free variable, closures

## Global scope:

The global scope is the scope of the file.it is essentially the module scope

In Python, a variable declared outside of the function or in **global scope** is known as a **global variable**. This means that a **global variable** can be accessed inside or outside of the function.



## Local Scope: 

Local scope is the scope of the variable within a function. The scope is not created until the function is called and whenever a function is called a new scope is created. This scope created is **Functional scope** or **Local scope**.



## Non Local Scope:

Non local scope means it is neither local nor global nor bulit in but it is non local i.e can be found in enclosing scopes.

We define variable with nonlocal scope with the keyword nonlocal

```python
x = 15
def outer():
	x = 10
    def inner():
        nonlocal x
        x= x+1
       print(x)
    inner()
    print(x)
outer()

11
11

```



## free variable:

free are variable that are free in side a function i.e they are in nonlocal scope for that function. 

Example:

```python
def outer():
    x = "python"
    def inner():
        print("{0} rocks!".format(x)
    return inner()
outer()
              
              
python rocks!
```

here x is a free variable





## Closure:

 in the above example x is a free variable in function inner and it is bound to the x in outer variable. This happens when the outer is run and the inner is created. This is a closure. 

In this  if we just return the function inner without calling it we return a closure. the above code will modify as this:

```
def outer():
    x = "python"
    def inner():
        print("{0} rocks!".format(x)
    return inner
outer()
              
              
python rocks!
```



You can think of closure as a function plus an extended scope that contains a free variable. Free variable value is the object the cell points to , so this can change over time. Every time the function in the closure is called the free variable is referenced.

