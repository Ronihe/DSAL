
### principles:
    - stay engaged with your interviewer
    - go board first
    - draw pics on the white board of what you are proposing
    - acknowledge the issues from the interviewers.
    - careful about the assumption
    - state your assumptions explicitly and let your interviewer correct it 
    - estimate the data when necessary
    - drive, ask questions, be open about the tradeoffs, continue to g deeper and keep making improvements
    
    
### design:
1. scope the question: - understand exactly what you need to implement.
            
            examples: tiny url
            questions:
            1. will people able to specify their own url? or it is auto-genrated
            2. will you keep tracks of the users clicks
            3. should the tiny url be alive forever
            4. do they have time out
   
   - Make a list of  MAJOR FEATURES or USE CASES:
   examples:
   - shorten the url to a tiny url
   - analytics for a url
   - retrieving the url
   - user accounts and links management

2. make reasonable assumption:
    DAU: daily active users
    assume inifnite memory    
    
3. draw major components:
draw a diagram if the major component.
        
        example:
        - front end server
        - backend servers - for different logics
        - database sql or nosql
walk through the process end to end

4. identify the key issues
        - bottlenecks and major challenges
        -  example: if the url is posted on reddit or other popular forum, how to handle a lot of reads
5. redesign the key issues.
        - example: using cache
        - be open about the limitation of your design
        - edit your whiteboard
6. if just design a feature:
        1. ask questions.
        2. make believe:    
                assume all the data can fit in one machine and no mempry limiation
                - solve the problem
        3. get real:
                now you can go back to the original problem:
                how much data can fit in one machine, what problem might be occur when split up the data, how to read data from different 
        4. solve the prob:
                solve the problem or just migrate the prob.
                iterative approach
### Key concepts:

1. Horizontal vs. Vertical Scaling
A system can be scaled one of two ways.

- Vertical scaling means increasing the resources of a specific node. For example, you might add additional memory to a server to improve its ability to handle load changes.
- Horizontal scaling means increasing the number of nodes. For example, you might add additional servers, thus decreasing the load on any one server.]
       
   
2. Load Balancer:
Typically, some frontend parts of a scalable website will be thrown behind a load balancer. This allows a
system to distribute the load evenly so that one server doesn't crash and take down the whole system. To
do so, of course, you have to build out a network of cloned servers that all have essentially the same code
and access to the same data.

3. Database Denormalization and NoSQL
Joins in a relational database such as SQL can get very slow as the system grows bigger. For this reason, you would generally avoid them.

Denormalization is one part of this. Denormalization means adding redundant information into a databasE
to speed up reads. For example, imagine a database describing projects and tasks (where a project can have
multiple tasks). You might need to get the project name and the task information. Rather than doing a join
across these tables, you can store the project name within the task table (in addition to the project table).

Or, you can go with a NoSQL database. A NoSQL database does not support joins and might structure data
in a different way. It is designed to scale better.

4. Database Partitioning (Sharding)
Sharding means splitting the data across multiple machines while ensuring you have a way of figuring out
which data is on which machine.

- Vertical Partitioning: This is basically partitioning by feature. For example, if you were building a social
network, you might have one partition for tables relating to profiles, another one for messages, and so
on. One drawback of this is that if one of these tables gets very large, you might need to repartition that
database (possibly using a different partitioning scheme).

- Key-Based (or Hash-Based) Partitioning: This uses some part of the data (for example an ID) to parti-
tion it. A very simple way to do this is to allocate N servers and put the data on mod (key, n). One issue with this is that the number of servers you have is effectively fixed. Adding additional servers means
reallocating all the data-a very expensive task.

- Directory-Based Partitioning: In this scheme, you maintain a lookup table for where the data can be
found. This makes it relatively easy to add additional servers, but it comes with two major drawbacks.
First, the lookup table can be a single point of failure. Second, constantly accessing this table impacts
performance.

5. Caching
An in-memory cache can deliver very rapid results. It is a simple key-value pairing and typically sits between
your application layer and your data store.

When an application requests a piece of information, it first tries the cache. If the cache does not contain the
key, it will then look up the data in the data store. (At this point, the data might-or might not-be stored
in the data store.)

When you cache, you might cache a query and its resultsdirectly.Or,alternatively, you can cache the specific
object (for example, a rendered version of a part of the website, or a list of the most recent blog posts).

6. Asynchronous Processing & Queues
Slow operations should ideally be done asynchronously. Otherwise, a user might get stuck waiting and waiting for a process to complete.

In some cases, we can do this in advance (i.e., we can pre-process). For example, we might have a queue of
jobs to be done that update some part of the website. If we were running a forum, one of these jobs might
be to re-render a page that lists the most popular posts and the number of comments. That list might end
up being slightly out of date, but that's perhaps okay. It's better than a user stuck waiting on the website
to load simply because someone added a new comment and invalidated the cached version of this page.

In other cases, we might tell the user to wait and notify them when the process is done. You've probably
seen this on websites before. Perhaps you enabled some new part of a website and it says it needs a few
minutes to import your data, but you'll get a notification when it's done.

7. Networking Metrics
- Bandwidth: This is the maximum amount of data that can be transferred in a unit of time. It is typically expressed in bits per second (or some similar ways, such as gigabytes per second).

- Throughput: Whereas bandwidth is the maximum data that can be transferred in a unit of time, throughput is the actual amount of data that is transferred.

- Latency: This is how long it takes data to go from one end to the other. That is, it is the delay between the
sender sending information (even a very small chunk of data) and the receiver receiving it.

- Building a fatter conveyor belt will not change latency. It will, however, change throughput and band-
width. You can get more items on the belt, thus transferring more in a given unit of time.

- Shortening the belt will decrease latency, since items spend less time in transit. It won't change the
throughput or bandwidth. The same number of items will roll off the belt per unit of time.

- Making a faster conveyor belt will change all three. The time it takes an item to travel across the factory decreases. More items will also roll off the conveyor belt per unit of time.

8. MapReduce
MapReduce is often associated with Google, but it's used much more broadly than that. A MapReduce program is typically used to process large amounts of data.

### Considerations
- Failures: Essentially any part of a system can fail. You'll need to plan for many or all of these failures.
- Availability and Reliability: Availability is a function of the percentage of time the system is operational. Reliability is a function of the probability that the system is operational for a certain unit of time.
- Read-heavy vs. Write-heavy: Whether an application will do a lot of reads or a lot of writes impacts the design. If it's write-heavy, you could consider queuing up the writes (but think about potential failure
here!). If it's read-heavy, you might want to cache. Other design decisions could change as well.
- Security: Security threats can, of course, be devastating for a system. Think about the types of issues a system might face and design around those.


























          
                

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
singleton design patterns:
1. statistics
query engine handles all the transactions: singleton desgin.
    query engine would only be called once.
    
what are threads:
read locks
write locks
