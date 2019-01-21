# Data structure:

# linked list

the elements are linked using pointers.
A Linked List is a linear collection of data elements, called nodes, each pointing to the next node by means of a pointer. It is a data structure consisting of a group of nodes which together represent a sequence.

    Singly-linked list: linked list in which each node points to the next node and the last node points to null

    Doubly-linked list: linked list in which each node has two pointers, p and n, such that p points to the previous node and n points to the next node; the last node's n pointer points to null

    Circular-linked list: linked list in which each node points to the next node and the last node points back to the first node

Time Complexity:
Access: O(n)
Search: O(n)
Insert: O(1)
Remove: O(1)

definition:
https://www.geeksforgeeks.org/linked-list-set-1-introduction/

## Why Linked List?

- Arrays can be used to store linear data of similar types, but arrays have following limitations.
  1. The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
  2. Inserting a new element in an array of elements is expensive, because room has to be created for the new elements and to create room existing elements have to shifted.

## Advantages over arrays

1. Dynamic size
2. Ease of insertion/deletion

## Drawbacks:

1. Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here.
2. Extra memory space for a pointer is required with each element of the list.
3. Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.

## Representationv:

### A linked list is represented by a pointer to the first node of the linked list. The first node is called head. If the linked list is empty, then value of head is NULL.

### Each node in a list consists of at least two parts:

1. data
2. Pointer (Or Reference) to the next node
   In C, we can represent a node using structures. Below is an example of a linked list node with an integer data.
   In Java, LinkedList can be represented as a class and a Node as a separate class. The LinkedList class contains a reference of Node class type.
