import datetime

status = {}
status_list=[]

#functions-----------------------------

def upload_status():
  name = input("\nEnter your name : ")
  status_message = input("Your status message : ")
  upload_time = datetime.datetime.now()
  count = 0

  new_status = {
    name : {
    "name":name,
    "status":status_message,
    "upload":upload_time,
    "count":count
  }
  }
  status.update(new_status)
  status_list.append(name)
  print("\nStatus uploaded successfully..!")


def view_status():
  if len(status)==0:
    print("\nThere is no status found...!")
    return
  
  print("\nAvailable Status :")
  ct=1
  for item in status:
    print(f"{ct}.{item}")
    ct+=1
  
  ip = int(input("\nWhich user's status you want to see - press number (e.g. 1 2 and so on) : "))

  if ip < 1 or ip > len(status_list):
    print("Invalid choice..!")
    return
  
  view_status_of = status_list[ip-1]
  
  status[view_status_of]["count"]+=1

  print(f"\nUser name : {status[view_status_of]["name"]} \nStatus : {status[view_status_of]["status"]} \nUploaded at : {status[view_status_of]["upload"]}")

  current_time = datetime.datetime.now()
  
  for item in status_list:
    difference = current_time - status[item]["upload"]

    if difference >= datetime.timedelta(hours=24):
      status.pop(item)
    

def remove_status():
  if len(status_list)==0:
    print("There is no status to remove...!")
    return

  name = input("Enter your name : ")

  if name in status_list:
    status.pop(name)
    status_list.remove(name)
    print("\nStatus removed successfully..!")
  else:
    print("You are not authorized person to perform this operation...!")
    return
  
 
def see_status_updates():
  name = input("Enter your name : ")

  if name not in status_list:
    print("Either you dont have status uploaded or you are unauthorized..!")
    return
  
  print(f"{name}, your status Updates : ")
  
  print(f"\nStatus : {status[name]["status"]} \nUploaded at : {status[name]["upload"]} \nSeen count : {status[name]["count"]}")
  

  
  
print("\n--------------------------------- WHATSAPP STATUS SYSTEM ------------------------------")
  
while(True):

  print("\n1.Upload your status \n2.View status \n3.Remove your status \n4.See your status updates \n5.Exit status system")
  choice = int(input("Enter choice : "))

  match choice:
       case 1:
           upload_status()
       case 2:
           view_status()
       case 3:
           remove_status()
       case 4:
           see_status_updates()
       case 5:
           print("\nExit from whatsapp status system")
           break
       case _ :
           print("\nInvalid choice...! , please try with valid one")