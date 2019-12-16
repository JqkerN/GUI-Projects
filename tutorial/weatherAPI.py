from tkinter import *
from PIL import ImageTk,Image
import requests
import json

# http://docs.airnowapi.org/
root = Tk()
root.title('Weather API - tutorial')
root.iconbitmap('images/diablo.ico')
root.geometry("600x100")

# Create zipcode lookup function
def ziplookup():
    # request API  by URL.
    # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=11417&distance=5&API_KEY=D4A92920-A59A-4584-9AD0-7DB81C46459D
    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=D4A92920-A59A-4584-9AD0-7DB81C46459D")
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = str(api[0]["AQI"])
        category = api[0]["Category"]["Name"]

        if category == "Good":
            color = '#0C0'
        elif category == "Moderate":
            color = '#FFFF00'
        elif category == "Unhealty for Sensitive Groups":
            color = '#ff9900'
        elif category == "Unhealthy":
            color = '#FF0000'
        elif category == "Very Unhealthy":
            color = '#990066'
        else:
            color = '#660000'

        root.config(background=color)
        lbl = Label(root, text=city + " Air Quality " + quality + " " + category, font=("Helvetica", 20), background = color)
        lbl.pack()

    except  Exception as e:
        api='Error 404 - Zip Code not found.'
        lbl = Label(root, text=api)
        lbl.pack()

zip = Entry(root)
zip.pack()
zip_btn = Button(root, text="Lookup Zipcode", command=ziplookup)
zip_btn.pack()


root.mainloop()