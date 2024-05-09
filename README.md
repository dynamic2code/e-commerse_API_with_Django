# My savannah Technical Assessment 

A Django project that handles customers and oders, both online and with sms.
The inspiration in the REST api was the headles CMS Strapi. Exposing the endpoints in the strapi way creats a more userble endpoint. Its a more global way and removes the naming constrains.
This project has
1. Sign up and login
2. Sign up and login with google
3. View products
4. Add products to cart
5. make orders
6. Get sms on succesfull order 
7. Add products for admins
8. See list of orders

## Technologies Used
1. Africa's talking for sms
2. GooGle Cloud for OAuth
3. Django rest framework 
4. Render
5. PostgreSQL(in production)
6. SQLite (in dev)
   


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

##### Delete Order
- **Endpoint:** `/orders/:id`
- **Method:** DELETE
- **Description:** Delete an order.
- **Parameters:** Order ID
- **Response:** Returns a message confirming the deletion of the order.

  # The Vue app consuming this api is hosted at https://savannah-front.vercel.app/
