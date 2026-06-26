"""📌 Problem Statement

WhatsApp allows users to upload statuses that remain visible for 24 hours.
Your task is to build a simplified version of the WhatsApp Status feature.

The system should allow users to:
✅ Upload a status
✅ View available statuses
✅ Track how many times a status has been viewed    """

import datetime

data = {} 
time = {}
while True:
    
    print("1.Upload Status\n2.View Status\n3.Check Expiry\n4.Delete Expired Status\n5.Exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            user = input("Enter user name: ")
            Upload = input("Upload the Status: ")
            Upload_Time = datetime.datetime.now() 
            data[user] = {
                "Status" : Upload,
                "Views" : 0,
                "Upload_time" : Upload_Time
            }
        
        case 2:
            print(f"Available Status:")
            for key in data:
                print(key)

            user_ch = input("Whose status you want to view: ")
            if user_ch in data:
                data[user_ch]["Views"] += 1
                print(f"\nUser: {user_ch}")
                print(f"Status: {data[user_ch]['Status']}")
                print(f"Views: {data[user_ch]['Views']}")
                print(
                    f"Uploaded On: "
                    f"{data[user_ch]['Upload_time'].strftime('%d-%m-%Y %H:%M:%S')}"
                )
            else:
                print("User not Found! ")

        case 3:
            print("which user status you want to check expiry: ")
            for key in data:
                print(key)
            user_exp = input("Enter User name: ")
            if user_exp in data:
                print(f"This User's Upload time is: {data[user_exp]["Upload_time"]}")               
                expiry = data[user_exp]["Upload_time"] + datetime.timedelta(hours=24)
                print(f"The current Expiry of this Status is: {data[user_exp][expiry]}")


        case 4:
            current_time = datetime.now()

            expired_users = []

            for user in data:
                expiry_time = data[user]["Upload_time"] + datetime.timedelta(hours=24)

                if current_time >= expiry_time:
                    expired_users.append(user)
            for user in expired_users:
                del data[user]
                print(f"{user}'s status has expired and been deleted.")
            if not expired_users:
                print("No expired statuses found.")

        case 5:
            print("Thank You!")
            break
                        
