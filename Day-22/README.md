
## API Fundamentals
---

###  API

`API (Application Programming Interface)` 
 - is a way for two systems to talk to each other using requests and responses, usually over HTTP.

---

### Endpoints

 - An `endpoint` is a specific URL where an API listens for requests.

- `https://api.example.com/users` → users endpoint  
- `https://api.example.com/users/123` → user with ID `123`

---

### HTTP Methods

- `GET` – Read data  
  - `GET /users` → get list of users  

- `POST` – Create new data  
  - `POST /users` → create a new user  

- `PUT` – Replace existing data  
  - `PUT /users/123` → update user 123 (full update)  

- `DELETE` – Remove data  
  - `DELETE /users/123` → delete user 123  

---

### Status Codes 

- `200 OK` – Request succeeded  
- `201 Created` – New resource created (usually after POST)  
- `400 Bad Request` – Client sent something wrong (bad data, missing field)  
- `401 Unauthorized` – No/invalid authentication (e.g., missing token)  
- `403 Forbidden` – Authenticated but not allowed  
- `404 Not Found` – Resource does not exist  
- `500 Internal Server Error` – Problem on server side  

---

## Headers, Cookies, Tokens & Auth

### Headers

`Headers` are key–value pairs sent with the request/response to provide extra information.

Common examples:

- `Content-Type: application/json` – body is JSON  
- `Accept: application/json` – client expects JSON back  
- `Authorization: Bearer <token>` – send access token  

---

### Cookies

`Cookies` are small pieces of data stored in the browser and sent automatically with requests to the same domain. Commonly used for:

- Session management (logged‑in user)  
- Remembering preferences  

---

### Tokens & Bearer Authentication

`Token` = string used to identify and authorize a user or application.

- Server issues a token after login.  
- Client sends token on every request (usually in header).  

`Bearer Authentication` (a common token‑based auth):

- Header format:  
  `Authorization: Bearer <your_token_here>`  
- "Bearer" means the client *bears* the token.

---

### API Keys

`API Key` = simple token (often static) used to identify the calling application.

- Can be sent in header:  
  `x-api-key: <key>`  
- Or as query param (less secure):  
  `?api_key=<key>`  
- Used for:
  - rate limiting  
  - billing  
  - basic access control  

---

## REST API Flow

Typical REST API call flow:

1. `Client sends request` to an endpoint  
   - Method: `GET`, `POST`, etc.  
   - URL: `/users`, `/orders/1`, ...  
   - Headers: `Content-Type`, `Authorization`, etc.  
   - Optional `payload/body` (for POST/PUT) – usually JSON.  

2. `Server processes the request`  
   - Validates data and permissions.  
   - Reads/Writes to database or other services.  

3. `Server sends response`  
   - Status code (e.g., `200`, `201`, `400`).  
   - Headers (e.g., `Content-Type: application/json`).  
   - Body (usually JSON) – data or error message.  

> `Payload` = the body of the request or response (e.g., JSON data you send or receive).

---

## Composite APIs

### What is a Composite API?

A `Composite API` combines multiple API operations into `one` request.

- Client sends a single request.  
- Server internally calls many APIs (or services).  
- Server returns `one aggregated response`.  

This is useful when the client would otherwise have to make many separate calls.

---

### Benefits

- `Fewer round trips` – less back‑and‑forth between client and server.  
- `Better performance` – especially important on mobile/low‑bandwidth networks.  
- `Simpler client code` – logic is moved to server (or orchestration layer).  
- `Optimized network usage` – less overhead per call.  

---

### Use Cases

- `OSS/BSS (telecom)`  
  One request to create a customer, activate a plan, and provision services.

- `Orchestration systems`  
  Automate sequences like:  
  `create VM → attach storage → configure network`.

- `Cloud automation`  
  Deploy a full stack (VM, database, load balancer) with a single API call.

- `Network provisioning`  
  Configure routers, firewalls, and policies in a single workflow.

---
