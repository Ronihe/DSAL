## memory allocation 
https://www.geeksforgeeks.org/how-are-variables-stored-in-python-stack-or-heap/


### garbage collection:
a process in which the interpreter frees up the memory when not in use to make it available for other projects.

```commandline
Assume a case where no reference is pointing to an object in memory i.e. it is not in use so, the virtual machine has a garbage collector that automatically deletes that object from the heap memor

```

### reference counting:
Reference counting works by counting the number of times an object is referenced by other objects in the system. When references to an object are removed, the reference count for an object is decremented. When the reference count becomes zero, the object is deallocated.

```commandline
Example:

# Literal 9 is an object  
b = 9
a = 4
    
# Reference count of object 9   
# becomes 0 and reference count 
# of object 4 is incremented 
# by 1 
b = 4

```

### Memory Allocation in Python
There are two parts of memory:
- stack memory
- heap memory
The methods/method calls and the references are stored in stack memory and all the values objects are stored in a private heap.






