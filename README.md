# FastAPI Workshop

## Workshop Overview
This workshop will guide you through the creation of a RESTful API using FastAPI, with Docker integration and MongoDB. We will cover the following topics:

- Setting up a Fast API project with Docker.
- Creating a CRUD API with MongoDB.
- Implementing search capabilities on the API.
- Data validation using Pydantic.
- Generating OpenAPI documentation.
- Securing your API.
- Best Practices:
  - Rate Limit
  - More Security
  - API Throttling
- Running unit tests.
- Deployment?

## Prerequisites
- Basic knowledge of Python.
- Familiarity with Docker.
  - This workshop uses Docker Desktop, but it could work with other engines, however, it has not been tested.
- Understanding of RESTful concepts.
- Basic MongoDB Understanding.

## Project Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yacer12/fast-api-workshop
   cd <repository-directory>
2. Navigate to path: `workshop/scripts/` and execute the `start_mongo.sh` file using the terminal of our preference. Notes: a) If you are using Windows, use the `start_mongo_ps1` , b) if the scripts don't work, copy and paste the content of the scripts on your terminal and run directly from there:

```bash
docker pull mongodb/mongodb-community-server:latest
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```

3. Verify MongoDB server has been created by using the tool of your choice.
4. The next step for this setup is to load sample data to a MongoDB database so we can use this data in the API, to do so, please follow these steps:
   
   -  Navigate to path: `workshop/expenses-api/data` and execute the `load_data.py` file using the terminal of our preference.
      -  Before running the script, make sure to make adjustments as suggested by the instructor.
```bash
python load_data.py
```
5. Verify MongoDB server contains the database, collection and number of documents specified on the previous step by using the tool of your choice.

