## What is `REST`:

- REST == "REpresentational State Transfer"
- resource-based:
  which means in restful api, we talk about resrouces instead of actions
  - resources are identified by URIs, each individual resources are identified in each request.
  - multiple URIs can point to the same resource
  - you can apply different operations on it which correspondent to HTTP verbs
- representation:
  - how the resource is manipulated.
  - part of the resources state:
    - transferred betwen client and server
  - usually JSON or XML
- Six Constrains:

  1. uniform interface:
     - we use HTTP spec as verbs and URI being resource names. http verbs as actions to take on the sources
     -
  2. stateless:

  - server contains no client state
  - each request contains enough context to provide message
    - self-descriptive messages
  - any session state is held on client side

  3. client-server:

  - assume a disconnected system
  - separation of concerns
  - uniform interface is the link between the two

  4. Cacheable:

  - server response are cacheable:
    - implicitly
    - explicitly
    - negotiated

  5. layered system；
     －　 could have multiple software layers in the middle
  6. code on demand:

  - logic can be transfeered to the client

# quick tip

1. use `HTTP` verbs to make your request mean something
   get post put and delete

2. provide sensible resource names
   - user identifiers in URL not query string, querystring is for filtering not resource names
   - leverage the hierachical nature of the url to imply structure
   - design for clients / not your data
   - resource names shold be nouns
   - use plurals in the url segments to keep your api uri consistent , using the collection metapher
     _ recommended: /customers/33245/orders/54/lineitems/1
     _ not : customer/33245/order/3444```
   - avoid using collection verbiage in urls `cusomer_list`
   - user lower-case,seperate words with 　`_` or hyphens `-`
   - keep urls as short as possible
3. use http response codes to indicate status
   200 OK
   General success status code. This is the most common code. Used to indicate success.
   201 CREATED
   Successful creation occurred (via either POST or PUT). Set the Location header to contain a link to the newly-created resource (on POST). Response body content may or may not be present.
   204 NO CONTENT
   Indicates success but nothing is in the response body, often used for DELETE and PUT operations.
   400 BAD REQUEST
   General error for when fulfilling the request would cause an invalid state. Domain validation errors, missing data, etc. are some examples.
   401 UNAUTHORIZED
   Error code response for missing or invalid authentication token.
   403 FORBIDDEN
   Error code for when the user is not authorized to perform the operation or the resource is unavailable for some reason (e.g. time constraints, etc.).
   404 NOT FOUND
   Used when the requested resource is not found, whether it doesn't exist or if there was a 401 or 403 that, for security reasons, the service wants to mask.
   405 METHOD NOT ALLOWED
   Used to indicate that the requested URL exists, but the requested HTTP method is not applicable. For example, POST /users/12345 where the API doesn't support creation of resources this way (with a provided ID). The Allow HTTP header must be set when returning a 405 to indicate the HTTP methods that are supported. In the previous case, the header would look like "Allow: GET, PUT, DELETE"
   409 CONFLICT
   Whenever a resource conflict would be caused by fulfilling the request. Duplicate entries, such as trying to create two customers with the same information, and deleting root objects when cascade-delete is not supported are a couple of examples.
   500 INTERNAL SERVER ERROR
   Never return this intentionally. The general catch-all error when the server-side throws an exception. Use this only for errors that the consumer cannot address from their end.

4. offer json
5. consider connectedness:
   a link is a typed connection between two resources that are identified by Internationalised Resource Identifiers (IRIs) [RFC3987], and is comprised of:
   A context IRI,
   a link relation type
   a target IRI, and
   optionally, target attributes.
   A link can be viewed as a statement of the form "{context IRI} has a {relation type} resource at {target IRI}, which has {target attributes}."
