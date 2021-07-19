# Session 11 Assignment on Iterable and Iterator

Here we have two classes Polygon and Polygons written in session11.py and custompolygon.py

##Iterable
Here custompolygon returns a list of polygons starting from edges of 3 to the value passed in the constructor. This custom polygons is a list which is also an iterable.

This Polygons iterable which means we can get individual item from the iterable, we can get the length of the ietrable and parse through individual items using for loop. when using an iterable all the values will be stored in the memory

The Polygons class has __iter__, __len__,__getitem__ methods to perform above operations.

##Iterator
So, here we are creating a sub class PolyIterator that is used as an iterator on top of Polygons iterable.

The advantage of iterator is the ability to use next to parse through each and every items in the list. There by we are storing only those individual item in the memory.

The iterator implements __next__ and __iter__ methods.

Once the iterator passed through the last item in the the iterable, it will give a stopiteration error

You can get the link of the notebook in following DeepNote Link - https://deepnote.com/project/Untitled-Python-Project-5tiowEzAQom08ZIVTmIEmA/%2FIterator%20and%20Iterable%20Session.ipynb

