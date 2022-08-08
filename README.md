# Esoteric Login proof of Concept
## Purpose
The purpose of this git repository is for demonstrating a browser based alternative for HL7.
## Postgres Configuration
The HL7 application doesn’t need any permissions outside of its own Postgres database.  A dedicated role is needed with all permissions granted to that database.

Postgres must be installed locally in order to run the development application 
<img width="731" alt="image" src="https://user-images.githubusercontent.com/59446532/183456297-e0ba8f7d-a98f-4582-9d08-28ca697c247a.png">

Once you've installed pgadmin, right click on a server on the left hand side and click "Register...server"
Name: 'quest-users'
password: 123456
host: localhost
<img width="766" alt="image" src="https://user-images.githubusercontent.com/59446532/183457426-48fa719e-47ca-4aa0-b529-7a6e3d4d64cf.png">


