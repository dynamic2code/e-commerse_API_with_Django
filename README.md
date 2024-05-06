# My savannah Technical Assessment 

A Django project that handles customers and oders, both online and with sms.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

  ## Installation
1. Clone the repository:
```bash
git clone https://github.com/dynamic2code/savannah_project.git
```
2. Switch to the development branch:
```bash
git checkout development
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
6. Change settings to point to a local database
```bash
```
8. Apply database migrations:
```bash
python manage.py migrate
```
10. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Local Environment

When running the project locally, you can access the API endpoints at your local server.

### Production Environment

In the production environment, access the API endpoints at: [https://savannah-project-1.onrender.com/api/v1](https://savannah-project-1.onrender.com/api/v1)

### Endpoints

#### Customer Endpoints

##### Register User

- **Endpoint:** `/customers/sign_up`
- **Method:** POST
- **Description:** Register a new user.
- **Parameters:** None
- **Response:** Returns details of the newly registered user.

##### Log In

- **Endpoint:** `/customers/log_in`
- **Method:** POST
- **Description:** Log in a user and obtain an authentication token.
- **Parameters:** None
- **Response:** Returns a JWT token along with the user's ID.

#### Orders Endpoints

##### Add New Order

- **Endpoint:** `/orders`
- **Method:** POST
- **Description:** Add a new order.
- **Parameters:** Order details
- **Response:** Returns details of the newly added order.

##### Get All Orders

- **Endpoint:** `/orders`
- **Method:** GET
- **Description:** Retrieve all orders.
- **Parameters:** None
- **Response:** Returns a list of all orders.

##### Get Single Order

- **Endpoint:** `/orders/:id`
- **Method:** GET
- **Description:** Retrieve details of a single order.
- **Parameters:** Order ID
- **Response:** Returns details of the specified order.

##### Update Order

- **Endpoint:** `/orders/:id`
- **Method:** PUT
- **Description:** Update data for an existing order.
- **Parameters:** Order ID, Updated data
- **Response:** Returns details of the updated order.

#####Delete Order
Endpoint: /orders/:id
Method: DELETE
Description: Delete an order.
Parameters: Order ID
Response: Returns a message confirming the deletion of the order.
