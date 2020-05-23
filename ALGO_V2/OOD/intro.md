
1. tic tac toe


2. vending machine




3. tiny url


4. 


## approach
1. handle ambuguity:

questions to ask: 
        six w:
        who are the users
        what
        where
        when
        how
        why
        
```commandline
Your coffee maker might be an industrial machine designed to be used in a massive restaurant servicing
hundreds of customers per hour and making ten different kinds of coffee products. Or it might be a very

simple machine, designed to be used by the elderly for just simple black coffee. These use cases will signifi-
cantly impact your design.

```

2. define the core objects:
Now that we understand what we're designing, we should consider what the "core objects" in a system
are. For example, suppose we are asked to do the object-oriented design for a restaurant. Our core objects
might be things like Table, Guest, Party, Order, Meal, Employee, Server, and Host.

3. Analyze Relationships
objects. Which objects are members of which other objects? Do any objects inherit from any others? Are
relationships many-to-many or one-to-many?

For example, in the restaurant question, we may come up with the following design:
- Party should have an array of Guests.
- Server and Host inherit from Employee.
- Each Table has one Party, but each Party may have multiple Tables.
- Be very careful here-you can often make incorrect assumptions. For example, a single Table may have
multiple Parties (as is common in the trendy"communal tables" at some restaurants). You should talk to
your interviewer about how general purpose your design should be.

4. Investigate Actions
At this point, you should have the basic outline of your object-oriented design. What remains is to consider
the key actions that the objects will take and how they relate to each other. You may find that you have
forgotten some objects, and you will need to update your design.

## Design Patterns

### Singleton Class
The Singleton pattern ensures that a class has only one instance and ensures access to the instance through
the application. It can be useful in cases where you have a "global" object with exactly one instance. For
example, we may want to implement Res tau rant such that it has exactly one instance of Rest au rant.

it should be noted that many people dislike the Singleton design pattern, even calling it an "anti-pattern:·
One reason for this is that it can interfere with unit testing.

### Factory Method




























