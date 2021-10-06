### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is an object relational database management system (ORDBMS).
It includes ***psql***, a terminal-based program for issuing database commands.

- What is the difference between SQL and PostgreSQL?
**SQL** is the standard language for interacting wtih relational databases.
**PostgreSQL** is just an *advanced* version of SQL which provides support to different functions of SQL

- In `psql`, how do you connect to a database?
psql is a terminal-based front-end to PostgreSQL.
In the *shell*, you just type in "psql" for issuing database commands.

- What is the difference between `HAVING` and `WHERE`?
**Having** determines which grouped results to keep.
**Where** decides which rows to use.

- What is the difference between an `INNER` and `OUTER` join?
**Inner** shows only the rows that match the condition in both tables.
**Outer** shows left, right, and full.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
**Left Outer** are all of the rows from the first table(left), combined with matching rows from the second table(right).
**Right Outer** are the matching rows from the first table(left), combined with all the rows from the second table(right).

- What is an ORM? What do they do?
**ORM** stands for Object-relational mapping. It's a programming technique for converting data between imcompatible type systems using OOP languages. 
In SQL, ORM library is a completely ordinary library written in your language of choice that encapsulates the code needed to manipulate the data so you don't use SQL

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
**AJAX** uses JavaScript to load data after the browser request has finished.
**HTTP Requests** is a method for users to requet information from servers. 

- What is CSRF? What is the purpose of the CSRF token?
**CSRF** stands for Cross-Site Request Forgery.
It is used to send malicious requets from an authenticated user to a web application.
The purpose of a CSRF token is to prevent these kinds of a attacks.

- What is the purpose of `form.hidden_tag()`?
This generates a hidden field that includes a token that is used to protect the form against CSRF attacks.
