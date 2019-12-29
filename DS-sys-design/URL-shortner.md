# design a URL shortener

## step1: scope the project:

    - what are we building, what features?


    1. is this a full web app, with web interface？
        －　no, just start with API
    2. since it is a API, do we need to authentication or user accounts or developer keys?
        - no , make it open to start
    3. can people modify or delete links?
        - no leave that out for now
    4. if not delete links, do they persist forever? do we automatically remove old ones?
        first, it is worth considering what policies we could use for removing old ones:
            1. we could remove links that were `created` some lenght of time ago... like 6 months
            2. we could remove linkes that have not been `visited` in some length of time .. 6 months

            (2) seems less frustrating than (1). Are there cases where (2) could still frustrate users? If a link is on the public web, it's likely to get hit somewhat regularly, at least by spiders. But what if it's on the private web (e.g. an internal "resources" page on a private university intranet)? Or...what if someone printed a bunch of pamphlets that had the URL on it, didn't give out any pamphlets for a few months, then started giving them out again? That seems like a pretty reasonable thing that might happen (putting a URL on a printed piece of paper is a great reason to use a link shortener!) and having the link suddenly stop working would be quite frustrating for the user. Worse, what if a book already had the shortlink printed in a million copies? So let's let links exist forever.
    5. Should we let people choose their shortlink, or just always auto-generate it?
            For example, say they want ca.ke/parkers-resume. Let's definitely support that.
    6. Do we need analytics, so people can see how many people are clicking on a link, etc?
            Hmmm, good idea. But let's leave it out to start.
    ...

## step 2: design goals

    1. We should be able to store a lot of links, since we're not automatically expiring them.
    2. Our shortlinks should be as short as possible. The whole point of a link shortener is to make short links! Having shorter links than our competition could be a business advantage.
    3. Follwing a shortlink should be fast.
    4. The shortlink follower should be resilient to load spikes. One of our links might be the top story on Reddit, for example.
    ```
    It's worth taking a moment to really think about the order of our goals. Sometimes design goals are at odds with each other (to do a better job of one, we need to do a worse job of another). So it's helpful to know which goals are more important than others.
    ```

## step 3: building data model:

    Think about the database schema or the models we'll want. What things do we need to store, and how should they relate to each other? This is the part where we answer questions like "is this a many-to-many or a one-to-many?" or "should these be in the same table or different tables?"

    **careful about how we name things - descriptive and consisitent

    Let's call our main entity a Link. A Link is a mapping between a shortLink on our site, and a longLink, where we redirect people when they visit the shortLink.
    ```
      Link
    - shortLink
    - longLink
    ```

    Of course, we don't need to store the full ShortLink URL (e.g. ca.ke/mysite), we just need to store the "slug"—the part at the end (e.g. "mysite").
    So let's rename the shortLink field to "slug."
    ```
    Link
    - slug
    - longLink
    ```

    Now the name longLink doesn't make as much sense without shortLink. So let's change it to destination.
    ```
      Link
    - slug
    - destination
    ```

    ```Investing time in carefully naming things from the beginning is always impressive in an interview. A big part of code readability is how well things are named!
    ```

what endpoint/views do we need.

## views/pages/endpoint

    shortliink should be created when the entity is created
    eg. ca.ke/api/v1/shortlink

    to create a shortlink 'slug', send POST request as below:
    ```
       $ curl --data '{"destination": "interviewcake.com"}' https://ca.ke/api/v1/shortlink

    {
    "slug": "ae8uFt",
    "destination": "interviewcake.com"
    }
    ```

    Of course, we haven't defined exactly how generateRandomSlug() works. Considering it a bit, it quickly becomes clear this is a pretty tangled issue. We'll have to figure out:

    1. What characters can we use in randomly generated slugs? More possible characters means more possible random slugs without making our shortlinks longer. But what characters are allowed in URLs?
    2. How do we ensure a randomly generated slug hasn't already been used? Or if there is such a collision, how do we handle it?

Second, let's make a way to follow a ShortLink. That's the whole point, after all!

Our shortened URLs should be as short as possible. So as mentioned before, we'll give them this format: ca.ke/l\$slug.

Where $slug is the slug (either auto-generated by us or specified by the user). We could make it clearer that this is a redirect endpoint, by using a format like ca.ke/r/$slug, for example. But that adds 2 precious characters of length to our shortlink URLs!

## slug generation:

```
A note about methodology: Our default process for answering questions like this is often "make a reasonable guess, brainstorm potential issues, and revise." That's fine, but sometimes it feels more organized and impressive to do something more like "brainstorm design goals, then design around those goals." So we'll do that.
```

Let's look back up at the design goals we came up with earlier. The first two are immediately relevant to this problem:

1. We should be able to store a lot of links.
2. Our shortlinks should be as short as possible.

The nore char we allow in the shortlinks, the diff more links we can store without making the shortlinks longer.

```
the math:
ex:
2 different char for 2 length slug: a and b. 2^2 = 4.
2 diff char for 2 length slug: 2^3= 8
if c diff char allowed, n length: c^n
```

To get as many slugs as possible:

1. figure out the max set of the char
2. figure out how many distinc shortlinks we want accommodate
3. figure out how long the short lkinks mist be to accomodate that many distinc possibilites

```
Sketching a process like this before jumping in is hugely impressive. It shows organized, methodical thinking. Whenever you're not sure how to proceed, take a step back and try to write out a process for getting to the bottom of things. It's fine if you end up straying from your plan—it'll still help you organize your thinking.
```

## what char can be allowed in the slug

what are the constrains on c?

1. we should only use the char allowed in URLs;

2. pick the char that are relatively easy to type on a key board.
   `Remember the use case we talked about where people are typing in a ShortLink that they're reading off a piece of paper?`

what chars are allowed in the url, it is ok to not know the answer off the top of your head. but you should be abke to let your interviewer know that you know how to figure it out.
googling or searching stack overflow. or say I am sure it is defined n RFC some where.

```
What's an RFC? RFC stands for "request for comments." The first ones are from 1969 (back in the day of ARPANET, the precursor to the internet), and we still get new ones every year. RFCs define lots of conventions for how internet communications work. Like how status code 404 means "not found". Hilariously, some of the latest RFCs spec a custom XML vocabulary for writing RFCs. Yo dog. Also there's this one on the history of calling variables "Foo." Easy to get lost browsing these...
```

it turns out the answer is "only alphanumerics, the special characters "\$-\_.+!\*'(),", and reserved characters used for their reserved purposes may be used unencoded within a URL" (RFC 1738). "Reserved characters" with "reserved purposes" are characters like '?', which marks the beginning of a query string, and '#', which marks the beginning of a fragment/anchor. We definitely shouldn't use any of those. If we allowed '?' in the beginning of our slug, the characters after it would be interpreted as part of the query string and not part of the slug!

So just alphanumerics and the "special characters" \$-\_.+!\*'(),. Are accented alphabetical characters allowed? No, according to RFC 3986.

What about uppercase and lowercase? Domains aren't case-sensitive (so google.com and Google.com will always go to the same place), but the path portion of a URL is case-sensitive. If I query parker.com/foo and parker.com/Foo, I'm requesting different documents (although, as a site owner, I may choose to return the same document in response to both requests). So yes, lowercase and capital versions of the same letter can be treated as different characters in our slugs.

Okay, so it seems like the set of allowed characters is A-Z, a-z, 0-9, and "\$-\_.+!\*'(),". The apostrophe character seems a little iffy, since sometimes URLs are surrounded by single quotes in HTML documents. So let's pull that one.

In fact, in keeping with point (2) above about ease of typing, let's pull all the "special characters" from our list. It seems like a small loss on character count (8 characters) in exchange for a big win on readability and typeability. If we find ourselves wanting those extra characters, we can add add 'em back in.

Ah, but what if a user is specifying her own slug? She might want to use underscores, or dashes, or parentheses...so let's say for user-specified slugs, we allow "\$-\_.+!\*()," (still no apostrophe).

```
While we're on the topic of making URLs easy to type, we might want to consider constraining our character set to clear up common ambiguities. For example, not allowing both uppercase letter O and number 0. Or lowercase letter l and number 1. Font choice can help reduce these ambiguities, but we don't have any control over the fonts people use to display our shortlinks. This is a worthwhile consideration, but at the moment it's adding complexity to a question we're still trying to figure out. So let's just mention it and say, "This is something we want to keep an eye on for later, but let's put it aside for now." Your interviewer understands that you can't accommodate everything in your initial design, but she'll appreciate you showing an ability to anticipate what problems may come up in the user experience.
```

Okay, so with a-z, A-Z, and 0-9, we have 26 + 26 + 10 = 62 possible characters in our randomly-generated slugs. And for user-generated slugs, we have another 10 characters ("\$-\_.+!\*(),"), for 72 total.

## how many distinct slugs do we need?

How many distinct slugs do we need?
About how many slugs do we need to be able to accommodate? This is a good question to ask your interviewer. She may want you to make a reasonable choice yourself. There's no one right answer; the important thing is to show some organized thinking.

Here's one way to come up with a ballpark estimate: about how many new slugs might we create on a busy day? Maybe 100,000 per minute? Hard to imagine more than that. That's 100,000 _ 60 _ 24 \approx 145100,000∗60∗24≈145 million new links a day. 52.5 billion a year. What's a number of years that feels like "almost forever"? I'd say 100. So that's 5.2 trillion slugs. That seems sufficiently large. It's pretty dependent on the accuracy of our estimate of 100,000 per minute. But it seems to be a pretty reasonable ceiling, and a purposefully high one. If we can accommodate that many slugs, we expect we'll be able to keep handing out random slugs effectively indefinitely.

## how short the slugs

the total is 5 trillion, 62 char, 62^n = 5 trillion. we need to solve what is the n.we can user wolfram alpha website to get the answer. it turns out the answer is 7.09 .
It's worth checking how many characters we could save by allowing "\$-\_.+!\*()," as well. So 72^n = 5.272
n=5.2 trillion. We get n\approx6.8n≈6.8. Including the special characters would save us something like .3.3 characters on our slug length.

Is it worth it? Of course, there's no such thing as a fraction of a character. If we really had to accommodate at least 5.2 trillion random slugs, we'd have to round up, which would mean 7.09 would round up to 8-character slugs for our 62-character alphabet (not including special characters) and 6.8 would round up to 7-character slugs for our 72-character alphabet (including special characters).

But we don't really have to accommodate 5.2 trillion or more slugs. 5.2 trillion was just a ballpark estimate—and it was intended to be a high ceiling on how many slugs we expect to get. So let's stick with our first instinct to remove those special characters for readability purposes, and let's choose 7 characters for our slugs.

```
For some added potential brevity, and some added possible random slugs, we could also allow for random slugs with fewer than 7 characters. How many additional random slugs would that get us?

If you're a whiz with mathematical series,you might know intuitively that the sum of these fewer-than-7-character slugs will be far less than the 7-character slugs. We can actually compute this to confirm.

62^6(for 6-char slugs), plus 62^5(for 5-char slugs), plus 62^4(for 4-char slugs) + 62^3 + 62^2 + 62. About 57 billion random slugs. Which isn't that much in comparison to 5.2 trillion—it's two orders of magnitude less.

Since this doesn't win us much, let's skip it for now and only use exactly-7-character random slugs.

One interesting lesson here: going from 6 characters to 7 characters gave us a two orders of magnitude leap in our number of possible slugs. Going from 7 characters to 8 will give us another two orders of magnitude. So if and when we do start running out of 7-character random slugs, allowing just 1 more character will dramatically push back the point where we run out of random slugs.
```

## how to generate a random slug

1. make random choice for each char

```
  function getRandom(floor, ceiling) {
  return Math.floor(Math.random() * (ceiling - floor + 1)) + floor;
}

function generateRandomSlug() {
  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  const numChars = 7;
  let result = '';

  for (let i = 0; i < numChars; i++) {
    const randomIndex = getRandom(0, alphabet.length - 1);
    result += alphabet[randomIndex];
  }
  return result;
}
```

2. how to make it unique

2 strategies: 1. re-roll when we git an already-used slug; 2. adjust our slug generation stratedgy to only generate un-claimed slugs.
`base conversion`

## use base conversion to generate slugs

We usually use base-10 numbers, which allow 10 possible numerals: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.

Binary is base-2 and has 2 possible numerals: 0 and 1.

Our random slug alphabet has 62 possible numerals (A-Z, a-z, and 0-9). So we can think of each of our possible "random" slugs as a unique number, expressed in base-62.

```
let currentRandomSlugId = 0;
function generateRandomSlug() {
  const newId = currentRandomSlugId++;
  return baseConversion(newId, base62Alphabet);
}
```

```
Where should we store our currentRandomSlugId? We can keep it in memory on our web server, perhaps with a regular writethrough to the database, to make it persistent even if the web server crashes. But what if we have multiple front-end web servers?
```

It has a 1 in the 100s place, a 2 in the 10s place, and a 5 in the 1s place. In general, the places in a base-10 number are:

10^0
10^1
10^2
10^3
etc
The places in a base-62 number are:
62^0
62^1
62^2=3,844
62^3=238,328
etc

```
0: 0,
1: 1,
2: 2,
3: 3,
...
10: a,
11: b,
12: c,
...
36: A,
37: B,
38: C,
...
61: Z
```

```
Can we convert from slugs back to numbers? Yep, easy. Take 23C, for example. Translate the numerals back to their id numbers, so we get 2 3 38. That 2 is in the 3844's place, so we take 2 * 3844. That 3 is in the 62's place, so we take 3 * 62. That 38 is in the 1's place, so we take 38 * 1. We add up all those results to get our original 7,912.
```

One potential issue: the currentRandomSlugId could be shorter than 7 digits in base-62. We could pad the generate slug with zeros to force it to be exactly 7 characters. Or we could simply accept shorter random slugs—we'd just need to make sure our function that converts slugs back to numbers doesn't choke when the slug is fewer than 7 characters.

Another issue is that the currentRandomSlugId could give us something that a user has already claimed as a user-generated slug. We'll need to check for that, and if it happens we'll just increment the currentRandomSlugId and try again (and again, potentially, until we hit a "random" slug that hasn't been used yet).

```
let currentRandomSlugId = 0;

function generateRandomSlug() {
  let slug = '';
  while (true) {
    const newId = currentRandomSlugId++;
    slug = baseConversion(newId, base62Alphabet);

    // Make sure the slug isn't already used
    if (!DB.checkSlugExists(slug)) {
      break;
    }
  }
  return slug;
}
```

then read back the desing goals:

1. We should be able to store a lot of links.
2. Our shortlinks should be as short as possible.
3. Following a shortlink should be fast.
4. The shortlink follower should be resilient to load spikes.

We're all set on (1) and (2)! Let's start tackling (3) and (4). How do we scale our link follower to be fast and resilient to load spikes?

```
Beware of premature optimization! That always looks bad. Don't just jump around random ideas for optimizations. Instead, focus on asking yourself which thing is likely to bottleneck first and optimizing around that.
```

The database read to get the destination for the given slug is certainly going to be our first bottleneck. In general, database operations usually bottleneck before business logic.

To figure out how to get these reads nice and fast, we should get specific about how we're storing our shortlinks. To start, what kind of database should we use?

Database choice is a very broad issue. And it's a contentious one. There are lots of different opinions about how to approach this. Here's how we'll do it:

1. Relational databases (RDBMs) like MySQL and Postgres.
2. "NoSQL"-style databases like BigTable and Cassandra.

In general (again, this is a simplification), relational databases are great for systems where you expect to make lots of complex queries involving joins and such—in other words, they're good if you're planning to look at the relationships between things a lot. NoSQL databases don't handle these things quite as well, but in exchange they're faster for writes and simple key-value reads.

Looking at our app, it seems like relational queries aren't likely to be a big part of our app's functionality, even if we added a few of the obvious next features we might want. So let's go with NoSQL for this.

```
We might consider adding an abstraction layer between our application and the database, so that we can change over to a new one if our needs change or if some new hotness comes out.
```

Okay, so we have our data in a NoSQL-type database. How do we un-bottleneck database reads?

The first step is to make sure we're indexing the right way. In a NoSQL context, that means carefully designing our keys. In this case, the obvious choice is right: making the key for each row in the ShortLink table be the slug.

```
If we used a SQL-type database like MySQL or Postgres, we usually default to having our key field be a standard auto-incrementing integer called "id" or "index." But in this case, because we know that slugs will be unique, there's no need for an integer id—the slug is enough of a unique identifier.

BUT here's where it gets clever: what if we represented the slug as an auto-incrementing integer field? We'd just have to use our base conversion function to convert them to slugs! This would also give us tracking of our global currentRandomSlugId for free—MySQL would keep track of the highest current id in the table when it auto increments. Careful though: user-generated slugs throw a pretty huge monkey wrench into things with this strategy! How can you maintain uniqueness across user-generated and randomly-generated slugs without breaking the auto-incrementing ids for randomly-generated slugs?
```

How else can we speed up database reads?

We could put as much of the data in memory as possible, to avoid disc seeks.

This becomes especially important when we start getting a heavy load of requests to a single link, like if one of our links is on the front page of Reddit. If we have the redirect URL right there in memory, we can process those redirects quickly.

Depending on the database we use, it might already have an in-memory cache system. To get more links in memory, we may be able to configure our database to use more space for its cache.

If reads are still slow, we could research adding a caching layer, like memcached. Importantly, this might not save us time on reads, if the cache on the database is already pretty robust. It adds complexity—we now have two sources of truth, and we need to be careful to keep them in sync. For example, if we let users edit their links, we need to push those edits to both the database and the cache. It could also slow down reads if we have lots of cache misses.

If we did add a caching layer, there are a few things we could talk about:

1. The eviction strategy. If the cache is full, what do we remove to make space? The most common answer is an LRU ("least recently used") strategy.
2. Sharding strategy. Sharding our cache lets us store more stuff in memory, because we can use more machines. But how do we decide which things go on which shard? The common answer is a "hash and mod strategy"—hash the key, mod the result by the number of shards, and you get a shard number to send your request to. But then how do you add or remove a shard without causing an unmanageable spike in cache misses?

Of course, we could shard our underlying database instead of, or in addition to caching. If the database has a built-in in-memory cache, sharding the data would allow us to keep more of our data in working memory without an additional caching layer! Database sharding has some of the same challenges as cache sharding. Adding and removing shards can be painful, as can migrating the schema without site downtime. That said, some NoSQL databases have great sharding systems built right in, like Cassandra.

This should get our database reads nice and fast.

The next bottleneck might be processing the actual web requests. To remedy this, we should set up multiple web server workers. We can put them all behind a load balancer that distributes incoming requests across the workers. Having multiple web servers adds some complexity to our database (and caching layers) that we'll need to consider. They'll need to handle more simultaneous connections, for example. Most databases are pretty good at this by default.

Okay, now our redirects should go pretty quick, and should be resilient to load spikes. We have a solid system that fits all of our design goals!

We can store a lot of links.
Our shortlinks are as short as possible.
Following a shortlink is fast.
The shortlink follower is resilient to load spikes.

## bonus

1. At some point we'd probably want to consider splitting our link creation endpoint across multiple workers as well. This adds some complexity: how do they stay in sync about what the currentRandomSlugId is?
2. Uptime and "single point of failure" (SPOF) are common concerns in system design. Are there any SPOFs in our current architecture? How can we ensure that an individual machine failure won't bring down our whole system?
3. Analytics. What if we wanted to show users some analytics about the links they've created? What analytics could we show, and how would we store and display them?
4. Editing and deleting. How would we add edit and delete features?
5. Optimizing for implementation time. We built something optimized for scale. How would our system design be different if we were just trying to get an MVP off the ground as quickly as possible?
