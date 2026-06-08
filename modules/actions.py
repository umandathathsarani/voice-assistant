import datetime
import webbrowser

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def open_website(url):
    webbrowser.open(url)
    return "Opening website"