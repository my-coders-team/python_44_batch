import datetime

user=[]
def Add_user():
    user_no=int(input("How many users you want to add\n"))
    user_count=1
    for i in range(user_no):
        user_name=input(f"Enter user {user_count} name : ")
        found=1
        for j in user:
            if user_name == j:
                found=0
                print("User already exists !")
        if found==1:
            user.append(user_name)
            print(f"User {user_count} is Added successfully\n")
            user_count+=1


status_add={}
def Add_status():
    u_name=input("Enter user name\n")
    found=0
    for i in user:
        if i==u_name:
            found=1
            status=input("Enter Status : ")
            upload_time=datetime.datetime.now()
            views=0
            Expiry_time=upload_time+datetime.timedelta(days=1)
            status_add[i]={
                "status": status,
                "upload time": upload_time,
                "views": views,
                "Expiry time": Expiry_time
            }
    if found==0:
        print(f"{u_name} does Not Exist !")


def View_status():
    for i in list(status_add):
        if datetime.datetime.now() > status_add[i]["Expiry time"]:
            status_add.pop(i)
    if not status_add:
        print("No Status")
    else:
        print("Available user status")
        for users in status_add:
            print(users)
        found=0
        v_status=input("View Status of : ")
        for i in status_add:
            if v_status==i:
                found=1
                print(f" Status : {status_add[i]['status']}")
                status_add[i]["views"]+=1
        if found==0:
            print(f"{v_status} does not have status")


def Status_Views():
    name=input("Enter user name to see Views\n")
    found=0
    for i in status_add:
        if i == name:
            found=1
            print(f"{status_add[i]['views']} Views")
    if found == 0:
        print("User does not Exist !")


def Check_expiry():
    name=input("Enter user name to check Expiry\n")
    found=0
    for i in status_add:
        if i == name:
            found=1
            print(f"Uploaded Date and Time : {status_add[i]['upload time']}")
            print(f"Expiry Date and Time : {status_add[i]['Expiry time']}")
    if found == 0:
        print("User does not Exist !")


def Delete_status():
    name=input("Enter user name to Delete Status\n")
    found=0
    for i in list(status_add):
        if name==i:
            found=1
            status_add.pop(i)
            print("Status Deleted Successfully")
    if found==0:
        print("No existing user status")



while True:
    print("=========== WhatsApp Status System ==========")
    
    choice=int(input("1.Add Users\n2.Add Status\n3.View Status\n4.Status Views\n5.Check Expiry\n6.Delete\n7.Logout\nEnter your choice\n"))
    match choice:
        case 1:
            Add_user()
        case 2:
            Add_status()
        case 3:
            View_status()
        case 4:
            Status_Views()
        case 5:
            Check_expiry()
        case 6:
            Delete_status()
        case 7:
            print("Logout from WhatsApp Status System")
            break
        case _:
            print("Invalid Choice !.. ")