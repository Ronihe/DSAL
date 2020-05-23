
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
                
                

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
singleton design patterns:
1. statistics
query engine handles all the transactions: singleton desgin.
    query engine would only be called once.
    
what are threads:
read locks
write locks
