# Flask CRUD Application for User Management

This project is a Flask application that provides RESTful(Using Blueprint) API endpoints for performing CRUD (Create, Read, Update, Delete) operations on user data in a MongoDB database.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [GET /users](#get-users)
  - [GET /users/id](#get-usersid)
  - [POST /users](#post-users)
  - [PUT /users/id](#put-usersid)
  - [DELETE /users/id](#delete-usersid)
- [Database_connection](#ConnectionToDb)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x
- Flask
- Flask-PyMongo

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ravix007/flask-user-crud.git
   cd flask-user-crud
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Build the Docker Images:

   ```bash
   docker build -t flask_rest-mongo-crud: latest .
   ```
    ![Build](/images/build.png)
5. Start up the Docker :
    ```bash
   docker-compose up
   ```
   ![Docker-up](/images/compose.png)



## Usage

The application provides REST API endpoints for managing user data. You can access the API using HTTP requests.

## API Endpoints

### GET /users

Retrieve a list of all users.

![Get Users](/images/get_req.png)

### GET /user/id

Retrieve details of a user by ID.

![Get User by ID](/images/getById_req.png)

### POST /user

Create a new user.

![Create User](/images/post_req.png)

After creation

![Get](/images/get_req.png)

### PUT /user/id

Update details of a user by ID.

![Update User](/images/put_req.png)

After Updating

![New UserInfo](/images/after_put.png)

### DELETE /user/id

Before Deletion

![Before Delete User](/images/after_put.png)

Delete a user by ID.

![Delete User](/images/del_req.png)

## Connection-To-Db

For accessing the database inside the docker container to query your collection, you will have to follow following steps:

1. Get the Container Id:
    ```bash
    docker ps
    ```
    ![UserDB](/images/db_step1.png)

2. Get Inside the Mongo Container:
    ```bash
    docker exec -it 37cc630cd243 /bin/bash
    ```
    ![UserDB](/images/db_step2.png)
    
3. Connect To the MongoDB:
    ```bash
    mongosh
    ```
4. Access the Users Collection and perform queries:
    ```bash
    use Users
    ```
    ```bash
    db.user.find()
    ```
    ![UserDB](/images/db_step3.png)



## Testing

You can use tools like Postman to test the API endpoints. Send HTTP requests to the provided URLs and review the responses.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

