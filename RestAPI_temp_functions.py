import requests, json

def get_data():
        API_ENDPOINT = "https://3agy2aan5j.execute-api.us-east-1.amazonaws.com/dev/record_temperature?"
        response = requests.get(url = API_ENDPOINT)
        if(response.ok):
            response_json = json.loads(response.content)
            for key in response_json["message"]:
                print("RECORD_INSERT_TS :" + key["RECORD_INSERT_TS"])
                print("SENSOR_ID :" + key["SENSOR_ID"])
                print("TEMPERATURE_CAPTURE_TS :" + key["TEMPERATURE_CAPTURE_TS"])
                print("TEMPERATURE_READING :" + key["TEMPERATURE_READING"])
                print("UNIQUE_GUID:" + str(key["UNIQUE_GUID"]))
                print("\n")
        else:
            print('Error on API request')

def create_data_list():
    data_list = []
    API_ENDPOINT = "https://3agy2aan5j.execute-api.us-east-1.amazonaws.com/dev/record_temperature?"
    response = requests.get(url = API_ENDPOINT)
    if(response.ok):
        response_json = json.loads(response.content)
        for key in response_json["message"]:
            data_list.append(key["TEMPERATURE_READING"])
        return data_list
    else:
        print('Error on API request')

def tempConvert (type, temperature):
    if type.upper() == "C":
        # Converts temperature to C
        new_temp = (temperature - 32.0) * (5.0/9.0)
        new_temp = round(new_temp, 2)
        return new_temp
    elif type.upper() == "F":
         # Converts temperature to F
        new_temp = (temperature * (9.0/5.0)) + 32.0
        new_temp = round(new_temp, 2.0)
        return new_temp

def average (list):
    sum = 0
    count = 0
    for value in list:
        sum = sum + float(value)
        count += 1
    average = round(sum/count, 2)
    return average

print("\nAVERAGE:")
print("The average is " + str(average(create_data_list())) + " degrees Farenheit.")
print("and " + str(tempConvert('c', average(create_data_list()))) + " degrees Celsius.")

def min_function(list):
    min_value = None
    for value in list:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value

print("\nMINIMUM:")
print("The minimum temperature is " + min_function(create_data_list()) + " degrees Farenheit")
print("and " + str(tempConvert('c', float(min_function(create_data_list())))) + " degrees Celsius.\n")

def max_function(list):
    max_value = None
    for value in list:
        if not max_value:
            max_value = value
        elif value > max_value:
            max_value = value
    return max_value

print('\nMAXIMUM:')
print("The maximum temperature is " + max_function(create_data_list()) + " degrees Farenheit")
print("and " + str(tempConvert('c', float(max_function(create_data_list())))) + " degrees Celsius.\n")
