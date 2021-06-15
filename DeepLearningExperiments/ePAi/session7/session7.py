counters = {'add':0,'mul':0,'div':0}
add_cnt = 0
mul_cnt = 0
div_cnt = 0

add_c,mul_c,div_c = 0,0,0
func_counter ={'add':0,'mul':0,'div':0}

def docstringcounter(fn:"function")->"function":
    '''This is a closure for doc string counter '''
    cnt = 50
    def inner(*args, **kwargs):
        nonlocal cnt
        docstring = fn.__doc__
        #print(len(docstring))
        if docstring:
            if len(docstring) > cnt:
                return True
            else:
                return False
        else:
            return False
    return inner

def getnextfibonacci()->"function":
    '''This is a closure to get next fibonacci'''
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418]
    def inner(n):
        nonlocal fibonacci
        if n >= 196418:
            return "Too big a fibonacci number"
        for i in fibonacci:
            if i > n:
                return i
    return inner

add_c,mul_c,div_c = 0,0,0
func_counter ={'add':0,'mul':0,'div':0}

def outer_track(fn:"function")->"function":
    '''a closure that counts how many times a function was called. Write a new one that can keep a track of how many times 
    add/mul/div functions were called, and update a global dictionary variable with the counts '''

    def func_count_tracker():
    
        global func_counter
        global add_c
        global div_c
        global mul_c
        
        if(fn.__name__=='mul'):
            mul_c += 1
            func_counter[fn.__name__] = mul_c
            
        if(fn.__name__=='add'):
            add_c += 1
            func_counter[fn.__name__] = add_c
            
        if(fn.__name__=='div'):
            div_c += 1
            func_counter[fn.__name__] = div_c
   
        return func_counter
    
    return func_count_tracker

def counter(fn:"function",dict_c:"dict"):
    '''a closure that counts how many times a function was called. Write a new one that can keep a track of how many times 
    add/mul/div functions were called, and update a global dictionary variable with the counts '''
    def inner(*args, **kwargs):
        if (fn.__name__) == 'add':
            dict_c[fn.__name__] += 1
        elif (fn.__name__) == 'mul':
            dict_c[fn.__name__] += 1
        elif (fn.__name__) == 'div':
            dict_c[fn.__name__] += 1
        return(dict_c)
    return inner
    

def mul(a:"int", b:"int", c:"int")->"int":
    '''This is a function for mul numbers'''
    return a * b * c


def add(a:"int", b:"int")->"int":
    '''This is a normal function for adding input numbers that are passed as input'''
    return a + b

def div(a:"int", b:"int")->"int":
    '''This is a normal function for dividing input numbers'''
    return a/b

def merge()-> 'list':
    '''This is a normal function for testing  '''
    deck= []
    for j in range(0,len(suits)):
        for i in range(0,len(vals)):
            deck.append(vals[i]+suits[j])
    return deck



if __name__ == '__main__':
    f = docstringcounter(mul)
    print(f(1,2,3))
    print(f.__code__.co_freevars)
    g = getnextfibonacci()
    print(g(1964188))
    mult = counter(mul,counters)
    add = counter(add,counters)
    div = counter(div,counters)
    mult(1, 2, 3)
    mult(1, 2, 3)
    mult(1, 2, 3)
    mult(1, 2, 3)
    add(1, 2)
    add(1, 2)
    div(5,6)
    print(counters)