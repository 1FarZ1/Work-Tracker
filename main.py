import requests
API_KEY ="212d008238be2af3e0c01d0c218640b9"
APP_ID="a461a982"
ENDPOINT =" https://trackapi.nutritionix.com/v2/natural/exercise"
SHETTY_ENDPOINT ="https://api.sheety.co/c80a12437aff393c8840a3a9ebcad17b/workout/workouts"
#---------------------------------------------------------------------------------------
from datetime import datetime
today=datetime.now().strftime("%d/%m/%Y")
time=datetime.today().strftime("%H:%M:%S")
#----------------------------------------------------------------------------------------


header={
    "x-app-id": APP_ID,
    "x-app-key":API_KEY,
    "Content-Type": "application/json",
}
# input("What Exercises u did ? ")
p={"query":"ran 3 miles and walked for 3km",
 "gender":"female",
 "weight_kg":52.5,
 "height_cm":167.64,
 "age":18}
response=requests.post(url=ENDPOINT,json=p,headers=header)
data=response.json()["exercises"]
for i in data:
    qq={
    "workout":{
        "Date":today,
        "Time":time,
         "Exercise":i["name"],
       "Duration":i["duration_min"],
       "Calories":i["nf_calories"],
    }
    }
    response=requests.post(url="https://api.sheety.co/c80a12437aff393c8840a3a9ebcad17b/workout/workouts",json=qq)
    print(response.text)

##_----------------------------------------------------------------


# response=requests.post(url=SHETTY_ENDPOINT,json=qq)
# data2=response.json()
