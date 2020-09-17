## Project (CRUD)
### Note
- Make a new directory `project` inside week_08/day_6 
- all the files related to project should be inside this directory
**Transport Search System**
- Make three files to work from user.csv, trains.csv and buses.csv
- all the csv files should be stored in the `data/<filename>.csv`
- users.csv should have details (id, name, contact_number, address)
- buses.csv should have details (id, bus_number, departure_loc, arrival_loc, journey_duration, fare)
- trains.csv should have details (id, train_number, departure_loc, arrival_loc, journey_duration, fare)
- the routes (apis) of user that are required are
    - register user (POST Method)
    - login user (POST Method)
    - modify password (PATCH Method)
    - delete user (DELETE Method)
    - show all user details (GET Method)
- the routes (apis) of buses that are required are
    - create new bus details (POST Method)
    - get all bus details (POST Method)
    - search for a bus using bus_number (POST Method)
    - delete a bus details (DELETE Method)
    - modify bus details (PATCH Method)
- the routes (apis) of trains that are required are
    - create new train details (POST Method)
    - get all train details (POST Method)
    - search for a train using train_number (POST Method)
    - delete a train details (DELETE Method)
    - modify train details (PATCH Method)
- The user should send `username` and `password` in every request other than GET to verify that a registered user is doing the operation
- so, before manipulating buses.csv and trains.csv, always check if the `username` and `password` are correct and present in users.csv
**SHOWCASE** 
Make sure you have all the API's saved in POSTMAN as a collection to showcase.