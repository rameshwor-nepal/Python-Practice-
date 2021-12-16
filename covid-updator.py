import requests
from win10toast import ToastNotifier
import json
import time


def update():
    r = request.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text = {
        'Confirmed cases:{data["Cases"]} \n Deaths:{data["death"]} \n recovered:{data["recovered"]}'
        }

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 updates", text,duration=1)
        time.sleep(60)

update()        