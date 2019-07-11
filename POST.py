import requests

API_ENDPOINT = "https://3agy2aan5j.execute-api.us-east-1.amazonaws.com/dev/record_temperature"

data = {
    "SENSOR_ID": "RASPBERRYPI",
	"TEMPERATURE_CAPTURE_TS": "2019-07-11 10:31:30",
	"TEMPERATURE_READING": 90
}

r = requests.post(url = API_ENDPOINT, data = data)

pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 