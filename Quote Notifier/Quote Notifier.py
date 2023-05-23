import time
import win10toast 
import requests

while True:
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    querystring = {"language_code":"en"}

    headers = {
        "X-RapidAPI-Key": "cb25edf2ddmsh8939bb050b34032p15252djsn12b71cc21eb9",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    content = response.json()["content"]
    data = response.json()
    originator_name = data["originator"]["name"]

    toaster = win10toast.ToastNotifier()

    author_and_brand = 'Quote Notifier | Quote By '+originator_name

    toaster.show_toast(author_and_brand,content, duration=10)
    time.sleep(15)