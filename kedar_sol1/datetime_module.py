from datetime import datetime, timedelta
def currenttime():
    return datetime.now()

def display_time(upload_time):
    return upload_time.strftime("%d %b %Y %I:%M %p")
def expired(upload_time):
    current_time=currenttime()
    if current_time>=upload_time+timedelta(hours=24):
        return True
    else:
        return False


