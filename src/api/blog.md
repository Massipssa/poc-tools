# Choose the right API architecture

As data engineer you need to undestand the how those api are  work to anticipate the data types and the stucture that may 
send by those API in your ingestion process.

## Rest API 

client requests or updata data in the server
Asynchronous communication, so the client and server can communicate without interrupting operations
Stateless design, so the server doesn’t have to remember the client state

- Protocol
  - HTTP 1.1

- This mechanism is a request-response model and is a unary data connection (one-to-one), a client sent 
request to the server and wait until the server respond to continue the operation

- Callable operations: limite to HTTP verbs (entity-oriented design)
- Data exchange format
  - JSON
  - Support XML and HTML
  - Coupling
  REST is loosely coupled, which means the client and the server do not need to know anything about the other's 
  implementation. This loose coupling makes the API easier to evolve over time. This is because a change in server
  definitions does not necessarily require a code change in the client.

Bidirectional streaming
REST does not offer this feature.

when to use
Here are use cases for a REST API:

- Web-based architectures
- Public-facing APIs for ease of understanding by external users
- Simple data communications

## gRPC

client invoke the function in the server as they were in local
- Asynchronous communication, so the client and server can communicate without interrupting operations
- Stateless design, so the server doesn’t have to remember the client state
- Protocol
  - HTTP 2

a client can send one or multiple API requests to the server that may result in one or multiple replies
from the server. Data connections may be unary (one-to-one), server-streaming (one-to-many), client-streaming 
(many-to-one), or bidirectional-streaming (many-to-many). This mechanism is a client-response communication model and 
is possible because gRPC is based on HTTP 2. 

- Callable operations: service-oriented design (a server can define a limitless callabel operations)
- Data exchange format
  - Protocol Buffers (Protobuf) format by default
  - JSON
- Coupling
  gRPC is tightly coupled, which means the client and server must have access to the same proto file. Any updates 
  to the file require updates in both the server and the client.

Bidirectional streaming
gRPC offers bidirectional streaming communication. This means both the client and the server can send and receive multiple requests and responses simultaneously on a single connection.

When to use:

A gRPC API is better for these use cases:

- High-performance systems
- High data loads
- Real-time or streaming applications