import datetime_module as dt

Statuses=[]

def ip_details():
    print("Enter how many names along with statues you want to add")
    n=int(input())
    for i in range(n):
        name=input("Enter username (lowercase): ")
        msg=input("Enter Status: ")
        upload_time=dt.currenttime()
        status = {
            "name":name,
            "message":msg,
            "upload_time":upload_time,
            "view": 0
        }
        Statuses.append(status)
    

    print(f"Status uploaded successfully at {dt.display_time(upload_time)}")
    


def status_views():
    print("-------------Status View----------------")
    print("\nTotal Statuses")
    for x in Statuses:
        print(x["name"])
    name=input("Enter the name whose status you want to see: ")
    for i in Statuses:
        if name==i["name"]:
            print("Status Message:", i["message"])
            i["view"]+=1
            return

    print("User not found")

def expiry():
    pass
    print("-------------Check for expiry of statuses----------------")   
    print("Select the name whose status you want to check for expiry(plz enter the name in lower case)")
    for i in Statuses:
        print(i["name"])

    name=input("enter the name you want to check expired status:")
    for x in Statuses:
        if name==x["name"]:
            print("\nUpload Time :", dt.display_time(x["upload_time"]))
            print("Current Time:", dt.display_time(dt.currenttime()))
            if dt.expired(x["upload_time"]):
                print("\nStatus Expired")
                Statuses.remove(x)
                print("Status removed")
            else:
                print("\nStatus Not Expired")
            return
print("User not found.")
def analysis():
    pass
    print("-------------Analysis of statuses----------------")
    print("Enter the name whose status you want to check for analysis(plz enter the name in lower case)")
    name=input("Enter the name:")
    found=0

    for i in Statuses:
        if name==i["name"]:
            found=1
            print("Status message:", i["message"])
            print("Total views:", i["view"])
            print("Uploaded time:", dt.display_time(i["upload_time"]))
            break
    if found==0:
        print("User does not exist as the status has expired")




while True:
    print("\nWelcome to WhatsApp Statuses")
    print("Select the option you want to perform")
    print("1.Add Statuses\n2.View Statuses\n3.Check for Expiry of Statuses\n4.Analysis of Statuses\n5.Exit")
    ch=int(input("Enter your choice: "))
    match ch:
        case 1:
            ip_details()
        case 2:
            status_views()
        case 3:
            expiry()
        case 4:
            analysis()
        case 5:
            print("Thank youuuuuuuuuuuu for using the application")
            break
        case _:
            print("Invalid Choice")




    
        

    

