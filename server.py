'''
**Transport Search System**
'''
from flask import Flask
from flask import request
import csv
import json

app = Flask(__name__)

@app.route('/user/register',methods=['POST'])
def user_registration():
    user_name = request.json['user_name']
    password = request.json['password']
    contact_number = request.json['contact_number']
    address = request.json['address']
    new_user = True
    with open('data/users.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['user_name'].lower() == user_name.lower():
                new_user = False
                break
    if new_user:
        user_list = {}
        with open('data/users.csv','r') as users_file:
            csv_reader = csv.reader(users_file)
            data = list(csv_reader)
        u_id = data[-1][0]
        user_list['id'] = int(u_id) + 1
        user_list['user_name'] = user_name
        user_list['password'] = password
        user_list['contact_number'] = contact_number
        user_list['address'] = address
        with open('data/users.csv','a') as users_file2:
            headers = ['id','user_name','password','contact_number','address']
            csv_writer = csv.DictWriter(users_file2,fieldnames=headers)
            csv_writer.writerow(user_list)
        return json.dumps({"message":"User Added Successfully"})
    else:
        return json.dumps({"message":"User name already exists!"})

@app.route('/user/login',methods=['POST'])
def user_login():
    user_name = request.json['user_name']
    password = request.json['password']
    with open('data/users.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        valid_user = False
        output_message = ''
        for row in csv_reader:
            # print(row['user_name'].lower())
            if row['user_name'].lower() == user_name.lower() and row['password'] == password:
                valid_user == True
                output_message = "Login Successful"
                break
            else:
                output_message = "User name or password is not matching"
    return json.dumps({"message":output_message})


@app.route('/user/modify',methods=['PATCH'])
def modify_user():
    user_id = request.json['id']
    password = request.json['password']
    with open('data/users.csv','r') as users_file:
        csv_reader = csv.reader(users_file)
        data = list(csv_reader)
        for i in range(len(data)):
            if data[i][0] == user_id:
                data[i][0] = user_id
                data[i][2] = request.json['password']
    with open('data/users.csv','w') as csv_file:
        csv_writer =  csv.writer(csv_file)
        csv_writer.writerows(data)
    return json.dumps({"message":"Password Updated Succesfully"})

@app.route('/user/delete/<user_id>',methods=['DELETE'])
def delete_user(user_id):
    new_list = []
    with open('data/users.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = list(csv_reader)
        for i in range(len(lines)):
            if i != int(user_id):
                new_list.append(lines[i])
    with open('data/users.csv','w') as csv_file2:
        csv_writer = csv.writer(csv_file2)
        csv_writer.writerows(new_list)
    return json.dumps({"message":"User Deleted Successfully!"})

@app.route('/users/view',methods=['GET'])
def view_users():
    user_list = []
    with open('data/users.csv','r') as users_file:
        csv_reader = csv.DictReader(users_file)
        for row in csv_reader:
            user_list.append(row)
        return json.dumps({"users":user_list})

def check_valid_user(uname,pwd):
    with open('data/users.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # print(row['user_name'].lower())
            if row['user_name'].lower() == uname.lower() and row['password'] == pwd:
                return True
            else:
                continue


@app.route('/bus/create',methods=['POST'])
def add_bus():
    user_name = request.json['user_name']
    password = request.json['password']    
    # print(valid_user)
    if valid_user:
        new_bus = True
        with open('data/buses.csv','r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['bus_number'].lower() == request.json['bus_number'].lower():
                    new_bus = False
                    break
        if new_bus:
            bus_list = {}
            with open('data/buses.csv','r') as users_file:
                csv_reader = csv.reader(users_file)
                data = list(csv_reader)
            print(data)
            u_id = data[-1][0]
            bus_list['id'] = int(u_id) + 1
            bus_list['bus_number'] = request.json['bus_number']
            bus_list['departure_loc'] = request.json['departure_loc']
            bus_list['arrival_loc'] = request.json['arrival_loc']
            bus_list['journey_duration'] = request.json['journey_duration']
            bus_list['fare'] = request.json['fare']
            with open('data/buses.csv','a') as users_file2:
                headers = ['id','bus_number','departure_loc','arrival_loc','journey_duration','fare']
                csv_writer = csv.DictWriter(users_file2,fieldnames=headers)
                csv_writer.writerow(bus_list)
            return json.dumps({"message":"Bus Added Successfully"})
        else:
            return json.dumps({"message":"Bus already exists!"})
    else:
        return json.dumps({"message":"Operation not allowed"})

@app.route('/buses/view',methods=['GET'])
def view_buses():
    bus_list = []
    with open('data/buses.csv','r') as users_file:
        csv_reader = csv.DictReader(users_file)
        for row in csv_reader:
            bus_list.append(row)
        return json.dumps({"buses":bus_list})

@app.route('/bus/search',methods=['POST'])
def search_bus():
    bus_number = request.json['bus_number']
    bus_found = False
    bus_details = {}
    with open('data/buses.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['bus_number'].lower() == bus_number.lower():
                bus_details['id'] = row['id']
                bus_details['bus_number'] = row['bus_number']
                bus_details['departure_loc'] = row['departure_loc']
                bus_details['arrival_loc'] = row['arrival_loc']
                bus_details['journey_duration'] = row['journey_duration']
                bus_details['fare'] = row['fare']
                bus_found = True
                break
        if bus_found == True:
            return json.dumps({"bus detail":bus_details})
        else:
            return json.dumps({"message":"Bus not found!"})

@app.route('/bus/delete',methods=['DELETE'])
def delete_bus():
    user_name = request.json['user_name']
    password = request.json['password']
    bus_id = request.json['id']
    valid_user = check_valid_user(user_name,password)
    if valid_user:
        new_list = []
        with open('data/buses.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            lines = list(csv_reader)
            for i in range(len(lines)):
                # print(lines[i][0],bus_id)
                if lines[i][0] != bus_id:
                    new_list.append(lines[i])
        with open('data/buses.csv','w') as csv_file2:
            csv_writer = csv.writer(csv_file2)
            csv_writer.writerows(new_list)
        return json.dumps({"message":"Bus Deleted Successfully!"})
    else:
        return json.dumps({"message":"Operation not allowed"})

@app.route('/bus/modify',methods=['PATCH'])
def modify_bus():
    user_name = request.json['user_name']
    password = request.json['password']
    valid_user = check_valid_user(user_name,password)
    if valid_user:
        bus_id = request.json['id']
        bus_number = request.json['bus_number']
        departure_loc = request.json['departure_loc']
        arrival_loc = request.json['arrival_loc']
        journey_duration = request.json['journey_duration']
        fare = request.json['fare']
        with open('data/buses.csv','r') as users_file:
            csv_reader = csv.reader(users_file)
            data = list(csv_reader)
            for i in range(len(data)):
                if data[i][0] == bus_id:
                    data[i][0] = bus_id
                    data[i][1] = bus_number
                    data[i][2] = departure_loc
                    data[i][3] = arrival_loc
                    data[i][4] = journey_duration
                    data[i][5] = fare
        with open('data/buses.csv','w') as csv_file:
            csv_writer =  csv.writer(csv_file)
            csv_writer.writerows(data)
        return json.dumps({"message":"Bus Details Updated Succesfully"})
    else:
        return json.dumps({"message":"Operations not allowed!"})

#Train
@app.route('/train/create',methods=['POST'])
def add_train():
    user_name = request.json['user_name']
    password = request.json['password']
    valid_user = check_valid_user(user_name,password)
    # print(valid_user)
    if valid_user:
        new_train = True
        with open('data/trains.csv','r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['train_number'].lower() == request.json['train_number'].lower():
                    new_train = False
                    break
        if new_train:
            train_list = {}
            with open('data/trains.csv','r') as users_file:
                csv_reader = csv.reader(users_file)
                data = list(csv_reader)
            # print(data)
            u_id = data[-1][0]
            train_list['id'] = int(u_id) + 1
            train_list['train_number'] = request.json['train_number']
            train_list['departure_loc'] = request.json['departure_loc']
            train_list['arrival_loc'] = request.json['arrival_loc']
            train_list['journey_duration'] = request.json['journey_duration']
            train_list['fare'] = request.json['fare']
            with open('data/trains.csv','a') as users_file2:
                headers = ['id','train_number','departure_loc','arrival_loc','journey_duration','fare']
                csv_writer = csv.DictWriter(users_file2,fieldnames=headers)
                csv_writer.writerow(train_list)
            return json.dumps({"message":"Train Added Successfully"})
        else:
            return json.dumps({"message":"Train already exists!"})
    else:
        return json.dumps({"message":"Operation not allowed"})

@app.route('/trains/view',methods=['GET'])
def view_trains():
    train_list = []
    with open('data/trains.csv','r') as users_file:
        csv_reader = csv.DictReader(users_file)
        for row in csv_reader:
            train_list.append(row)
        return json.dumps({"trains":train_list})

@app.route('/train/search',methods=['POST'])
def search_train():
    train_number = request.json['train_number']
    train_found = False
    train_details = {}
    with open('data/trains.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['train_number'].lower() == train_number.lower():
                train_details['id'] = row['id']
                train_details['train_number'] = row['train_number']
                train_details['departure_loc'] = row['departure_loc']
                train_details['arrival_loc'] = row['arrival_loc']
                train_details['journey_duration'] = row['journey_duration']
                train_details['fare'] = row['fare']
                train_found = True
                break
        if train_found == True:
            return json.dumps({"train detail":train_details})
        else:
            return json.dumps({"message":"Train not found!"})

@app.route('/train/delete',methods=['DELETE'])
def delete_train():
    user_name = request.json['user_name']
    password = request.json['password']
    train_id = request.json['train_id']
    valid_user = check_valid_user(user_name,password)
    if valid_user:
        new_list = []
        with open('data/trains.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            lines = list(csv_reader)
            for i in range(len(lines)):
                if lines[i][0] != train_id:
                    new_list.append(lines[i])
        with open('data/trains.csv','w') as csv_file2:
            csv_writer = csv.writer(csv_file2)
            csv_writer.writerows(new_list)
        return json.dumps({"message":"Train Deleted Successfully!"})
    else:
        return json.dumps({"message":"Operation not allowed"})

@app.route('/train/modify',methods=['PATCH'])
def modify_train():
    user_name = request.json['user_name']
    password = request.json['password']
    valid_user = check_valid_user(user_name,password)
    if valid_user:
        train_id = request.json['id']
        train_number = request.json['train_number']
        departure_loc = request.json['departure_loc']
        arrival_loc = request.json['arrival_loc']
        journey_duration = request.json['journey_duration']
        fare = request.json['fare']
        with open('data/trains.csv','r') as users_file:
            csv_reader = csv.reader(users_file)
            data = list(csv_reader)
            for i in range(len(data)):
                if data[i][0] == train_id:
                    data[i][0] = train_id
                    data[i][1] = train_number
                    data[i][2] = departure_loc
                    data[i][3] = arrival_loc
                    data[i][4] = journey_duration
                    data[i][5] = fare
        with open('data/trains.csv','w') as csv_file:
            csv_writer =  csv.writer(csv_file)
            csv_writer.writerows(data)
        return json.dumps({"message":"Train Details Updated Succesfully"})
    else:
        return json.dumps({"message":"Operations not allowed!"})
