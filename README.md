# Flask Test with MVMED

## Introduction
Flask Test API is a RESTful web API for interacting with front-end users. All the data exchanged between front-end’s user and the API is JSON over HTTP.

### 1.	Base URLs
The base URLs for the API is: http://localhost:5000
All the requests on this URL use either POST or GET method and we need to add the specific end points to this URL. Example, if you want to register new user, you will have to make POST call to the below API: http://localhost:5000/auth/register with the parameters given in the section specific to this call.

### 2.	Auth Endpoint
Following are the end points of authentication
•	/auth/register
•	/auth/login

### 3.	User Endpoint
Following are the end points of user after login
•	/user/all
•	/user/all?page=<number>&per_page<number>

### 4.	Token’s Validity Period
The current validity period of token is 60 minutes

### NOTE:
- You have to create table in database postgresql with
  username: **postgres**
  password: **password**
  port: **5432**
  db_name: **FlaskTest**

- You have to create table as below script
  ```sql
  CREATE TABLE IF NOT EXISTS public.users
(
    id character varying COLLATE pg_catalog."default" NOT NULL,
    username character varying(64) COLLATE pg_catalog."default" NOT NULL,
    email character varying(120) COLLATE pg_catalog."default" NOT NULL,
    password character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_email_key UNIQUE (email),
    CONSTRAINT users_username_key UNIQUE (username)
)

TABLESPACE pg_default;
```
