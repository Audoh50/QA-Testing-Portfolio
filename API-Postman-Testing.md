# API Testing with Postman

## Project Overview

This project demonstrates basic API testing using Postman.

The objective is to validate API endpoints by checking response status codes, response body data, headers, and expected behavior.

## Skills Demonstrated

- REST API Testing
- GET Requests
- POST Requests
- Status Code Validation
- JSON Response Validation
- Positive Testing
- Negative Testing
- Postman Test Scripts
- API Response Verification

---

## Sample API

For this portfolio project, assume we are testing an e-commerce API with endpoints for users, products, and orders.

Example Base URL:

https://example.com/api

---

## Test 1 – Get All Users

### Request Method

GET

### Endpoint

```text
/api/users

Test Objective
Verify that the API successfully returns a list of users.
Expected Result
Response status code should be 200.
Response body should contain user data.
Response format should be JSON.
Postman Test Script

pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
Test 2 – Get a Specific User
Request Method
GET
Endpoint

/api/users/1

Test Objective
Verify that the API returns the correct user when a valid user ID is provided.
Expected Result
Response status code should be 200.
Response should contain the requested user.
User ID should match the requested ID.
Postman Test Script

pm.test("User ID is correct", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.id).to.eql(1);
});

Test 3 – Create a New User
Request Method
POST
Endpoint
/api/users
{
  "name": "John Smith",
  "email": "johnsmith@example.com"
}

Test Objective
Verify that a new user can be created successfully.
Expected Result
Response status code should be 201.
Response should contain the newly created user information.
Name and email should match the request data.
Postman Test Script

pm.test("User created successfully", function () {
    pm.response.to.have.status(201);
});
Test 4 – Validate Response Time
Test Objective
Verify that the API response is returned within an acceptable amount of time.
Postman Test Script
pm.test("Response time is less than 2000ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(2000);
});

Expected Result
The API should respond in less than 2 seconds.
Test 5 – Validate JSON Response
Test Objective
Verify that the API returns a valid JSON response.
Postman Test Script

pm.test("Response is JSON", function () {
    pm.response.to.be.json;
});

Test 6 – Invalid User ID
Request Method
GET
Endpoint

/api/users/99999

Test Objective
Verify the API response when a nonexistent user ID is requested.
Expected Result
API should return an appropriate error response.
Expected status code may be 404.
Error message should clearly indicate that the user was not found.
Postman Test Script

pm.test("Status code is 404", function () {
    pm.response.to.have.status(404);
});

Test 7 – Missing Required Email
Request Method
POST
Endpoint

/api/users

Request Body
{
  "name": "John Smith"
}

Test Objective
Verify that the API rejects a request when a required field is missing.
Expected Result
API should reject the request.
An appropriate validation error should be returned.
Expected status code may be 400.


pm.test("Bad request returned", function () {
    pm.response.to.have.status(400);
});

Test 8 – Validate Content Type
Test Objective
Verify that the API response Content-Type is JSON.
Postman Test Script

pm.test("Content-Type is JSON", function () {
    pm.expect(pm.response.headers.get("Content-Type"))
      .to.include("application/json");
});

