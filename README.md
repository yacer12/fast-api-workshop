# Building Apps with Docker and FastAPI Workshop

## Workshop Overview
This workshop will guide you through the creation of a RESTful API using FastAPI, with Docker integration and MongoDB. We will cover the following topics:

- Setting up a Fast API project with Docker.
- Creating a CRUD API with MongoDB.
- Data validation using Pydantic.
- Implementing search capabilities on the API.
- Generating OpenAPI documentation.
- Securing your API.
- Best Practices:
  - Rate Limit
  - More Security
  - API Throttling
- Running unit tests.

## Prerequisites
- Basic knowledge of Python.
- Familiarity with Docker.
  - This workshop uses Docker Desktop, it could work with other engines, however, it has not been tested. https://www.docker.com/products/docker-desktop/
- Understanding of RESTful concepts.
- Basic MongoDB Understanding.
  - Please install https://www.mongodb.com/try/download/compass
- Postman
  - https://www.postman.com/downloads/ 

## Project Setup
- Clone the repository:
   ```bash
   git clone https://github.com/yacer12/fast-api-workshop
   cd <repository-directory>
- Navigate to path: `workshop/expenses-api/` and execute the `debug.sh` file using the terminal of our preference. Notes: a) If you are using Windows, use the `debug.ps1` , b) if the scripts don't work, copy and paste the content of the scripts on your terminal and run directly from there as follow:

  ```bash
  docker-compose up --build
  ```

  - This command will start three containers:
    - `mongodb`: a container that will act as a MongoDB server.
    - `fastapi`: our actual fast api development setup.
    - `load_data`: a *one-off* container that will run only once at built time just to load sample data to MongoDB.

- Verify MongoDB server has been created by using the tool of your choice.
- Verify MongoDB server contains the database, collection and number of documents specified on the previous step by using the tool of your choice.
  - Database: financeDB
  - Collection: expensesDetails

If you have reached this point: Congratulations!! You are set to start the workshop!!