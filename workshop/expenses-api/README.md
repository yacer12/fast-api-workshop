# Key Concepts
In this section you will encounter a few key concepts covered on this workshop.

## Pydantic
Pydantic is a data validation and settings management library for Python. It uses Python 
type annotations to validate the structure and types of data, ensuring that the data adheres to defined schemas. 
Pydantic models provide a convenient way to parse, validate, and serialize data,
making it easier to work with complex data structures. It’s commonly used in frameworks like FastAPI for building APIs.

For more information visit the [official](https://docs.pydantic.dev/latest/) documentation.

## OpenAPI

OpenAPI is a specification for building APIs that provides a standardized format for describing the 
endpoints, methods, parameters, and responses of an API in a machine-readable way. It allows developers 
to create interactive documentation, generate client libraries, and automate API testing. 
OpenAPI enables better communication between teams and tools, making it easier to design, document, 
and consume APIs.

For more information visit the [official](https://www.openapis.org/) documentation.

# Designing the API

## Models

In FastAPI, models are typically defined using Pydantic. A model serves as a blueprint for the data 
structures that your API will accept and return. They are used for data validation and serialization.
For example, you might define a Pydantic model for a user with fields like _id, name, and email_. 
FastAPI automatically validates incoming request data against these models and converts them into appropriate Python types.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

## Schemas

Schemas in FastAPI refer to Pydantic models (or subsets of models) that represent the structure of request and response 
payloads. They define what data the API expects and what will be returned. You can create different schemas for creating,
updating, and viewing resources. This separation helps in providing clear API documentation and validation.

For example, you may have a UserCreate schema for handling user creation, while a UserResponse schema is used for responses.

```python
class UserCreate(User):
    name: str
    email: str

class UserResponse(User):
    id: int
    name: str
    email: str
```

## Routing
Routing in FastAPI refers to the way you define the available endpoints for your API. FastAPI uses Python decorators to 
create routes that map HTTP requests to Python functions (also known as path operations). You can define routes for 
different HTTP methods like GET, POST, PUT, and DELETE, and specify the URL path for each route.

Here's a simple example that illustrates routing in FastAPI:

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    new_user = User(id=1, **user.dict())
    return new_user

```
In this example, the create_user function handles POST requests to the `/users/` endpoint. It accepts a
UserCreate object as input and returns a UserResponse object.
