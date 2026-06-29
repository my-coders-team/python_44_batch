import datetime 
status={
    
}

def upload():
    username=input("enter your name: ")
    message=input("enter message: ")
    
    status[username]={
        "message":message,
        "views":0,
        "time":datetime.datetime.now()
    }
    print("status uploded succesfully")



def view():
    user=input("enter username to view status: ")

    if user in status:
        current_time=datetime.datetime.now()
        upload_time=status[user]["time"]
        
        if current_time - upload_time > datetime.timedelta(minutes=1):
            print(user, "status expired")

        else:
            print("status: ",status[user]["message"])
            status[user]["views"]+=1
    else:
        print(f"user {user} not found")

def analytics():
    for k,v in status.items():
        print("user:",k)
        print("meaasge: ",v["message"])
        print("views:",v["views"])
        print("time:",v["time"])
        print()

while True:
    print("\n1.add status\n2.view status\n3.view analytics.\n4.exit")
    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            upload()
        case 2:
            view()
        case 3:
            analytics()
        case 4:
            exit()
        case _:
            print("invalid choice")
            



