
1. OOD needs coding
2. system design not
 
 
 面向对象：
 class, object, method, inheritance, interface
 1. design a vending machine
 2. de
 
 系统设计：
 database, schema, sql, Nosql, memchached, file system, distributed system, latency, scalbility, master slave, load balancer, web server, message queue, sharding, consistent hashing, qps.
        
        1.workability 25%
        2.special cases 20%
        3. analysis 20%
        4.tradeoff 15%
        5.knowledge base 15%
 
 ### questions to ask 
 to narrow down: 
        
    1. scenario:
        • Ask / Features / QPS / DAU / Interfaces
    2. services: 由大化小
        • Split / Application / Module
    3. storage： 如何存 如何访问
        • Schema / Data / SQL / NoSQL / File System
    4. scale
        • Sharding / Optimize / Special Case
    
 
 ## design twitter
  1. scenario：
        - what features
        - 日活跃用户： DAU daily active user
        
   the use of qps
        
    - QPS = 100
    • 用你的笔记本做 Web 服务器就好了
    • QPS = 1k
    • 用一台好点的 Web 服务器就差不多了
    • 需要考虑 Single Point Failure
    • QPS = 1m
    • 需要建设一个1000台 Web 服务器的集群
    • 需要考虑如何 Maintainance（某一台挂了怎么办）
    
    • QPS和 Web Server (服务器) / Database (数据库) 之间的关系
        • 一台 Web Server 约承受量是 1k 的 QPS （考虑到逻辑处理时间以及数据库查询的瓶颈）
        • 一台 SQL Database 约承受量是 1k 的 QPS（如果 JOIN 和 INDEX query比较多的话，这个值会更小）
        • 一台 NoSQL Database (Cassandra) 约承受量是 10k 的 QPS
        • 一台 NoSQL Database (Memcached) 约承受量是 1M 的 QPS
        
     
   2. service
    将大系统拆分为小服务
    1. Replay 重放需求
    2. Merge 归并需求
      
      
      
pull model
    
    
push  model
- fan out: user create twitter and push it each follower;s news feed list
    
      
      Denormalized 叫去标准化。通俗的解释是，通过在不同的 Table 中存储同一份数据的（也就是说至少一份是冗余数据）的形式，
      来加速数据的查询。因为当数据只存储在一个固定的 Table A 的时候，其他 Table B访问时如果需要同时取得关联的 Table A 
      的数据，则需要进行 join 操作之类的，会比较慢。一个例子就是在，统计有多少人点赞了一个帖子，可以通过 select count(*) 
      from like_table where post_id=<id> 的方式来获取，但是也可以在 post table 中新增一个 like_count，
      每次点赞就 +1。这里 like_count 就是一个 denormalized field，因为是可以通过 select count(*) 在 like table 
      中获得的。
    