# My savannah Technical Assessment 

A Django project that handles customers and oders, both online and with sms.

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
