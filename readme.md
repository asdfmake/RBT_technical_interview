# Solution to technical interview for Red Black Tree
## by Ivan Makevic

 ---

# Features
- Admin
    - Login
    - Upload employee profiles, available vacations and used vacation records
- Employee
    - Login
    - See vacation data
    - Create new vacation record


# Installation:

1. Create enviroment with:
```bash
python3 -m venv venv
```

2. Activate enviroment by running:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run by using:
```bash
flask --app app.main:app run --port 5000
```

# Architecture

```
app/
    main.py
    controllers/
        errors.py           # centralazied errors storage
        login.py            # handels logins for admin and employee
        master.py           # general controller, used for basic functions
        upload_files.py     # hanles upload logic, parses files 
        users.py            # functions for API calls for employee logic
        utils.py            # function that can be usefull in multiple places
    database/
        crud_in.py          # all functions inputting data into database
        crud_out.py         # all functions getting data from database
        database_setup.py   # Engine/Session/Base setup, env config
        models.py           # SQLAlchemy models: User, VacationAllowance, VacationUsage
RBT.postman_collection.json # postman collection with examples for all posible api calls
.env
readme.md
requirements.txt
.gitignore
```

# Endpoints

## Login
For a user to be able to use API he must login using propriate route for it's role

If user is admin, **he must login with credetial set in .env file** an use this route:
### ```/login/admin```
Request body:
```json
{
  "useremail": "useremail_example",
  "password": "password_example"
}
```

Response body:
```json
{
    "token": "JWT_TOKEN_CODE"
}
```

For user that is an employee, he should use his credentials, given to him by management and use this route
### ```/login/employee```
Request body:
```json
{
  "useremail": "useremail_example",
  "password": "password_example"
}
```

Response body:
```json
{
    "token": "JWT_TOKEN_CODE"
}
```

## Admin (Upload files)
Admin routes are protected and all should have **token** header with token obtained from `/login/admin` endpoint

To send the file, file need to be inside **form-data** section with name `file`

### ```/admin/upload/vacation_days```
Response body:
```json
{
    "vacation_days added": 56
}
```

### ```/admin/upload/users_list```
Response body:
```json
{
    "users_added": 99
}
```

### ```/admin/upload/used_vacation```
Response body:
```json
{
    "Vacations added: ": 639
}
```

## Employee (Get and add vacation data)
Admin routes are protected and all should have **token** header with token obtained from `/login/employee` endpoint, **token jwt** contains data about *employee email* so submitting it for each route is not needed

### ```/employee/get_used_days?search_start=2019-1-1&search_end=2019-12-31```
Searches all used vacations days with `search_start` and `search_end` params
Response body:
```json
{
    "days on vacation": 3
}
```

### ```/employee/get_total_days```
Fetches total vacations days for a specific year with `year` param
Response body:
```json
{
    "total days": 20
}
```

### ```/employee/get_available_vacation_days?year=2019```
Returns all rest of available vacation days for a specific year with `year` param
Response body:
```json
{
    "available_days": 17
}
```

### ```/employee/register_new_vacation```
Allows employee to register new vacations **if employee has enough vacation days available**
**Must use date format as seen on the example bellow**
Request body:
```json
{
    "vacation_start": "Monday, January 1, 2019",
    "vacation_end": "Friday, January 4, 2019"
}
```
Response body:
```json
{
    "insert_id": "b04d1381-53aa-445b-b364-27fca31d2e6f"
}
```

## Errors
When api throws an error, it returns json format response with code **400** with `message` key and a description of the error as the value. As seen here:
```json
{
    "message": "wrong date format"
}
```