import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from tabulate import tabulate

class StudentDashboard:
    def __init__(self):
        self.students_list=[]

    def add_students(self):
        n=int(input("Enter how many students you want to admit in linkcode technologies:"))
        for i in range(n):
            print(f"\nEnter Details of student {i+1}")
            while True:
                stud_id=int(input("Enter Student ID: "))
                found = 0
                for student in self.students_list:
                    if student["Student_Id"] == stud_id:
                        found=1
                        break
                if found==1:
                    print("Student ID already exists. Please enter another ID.")
                else:
                    break
            name=input("Enter Student Name:")
            course=input("Enter course:")
            City=input("Enter City:")
            Qualification=input("Enter Qualification:")
            while True:
                Fees_paid = float(input("Enter Fees Paid: "))
                Total_fees = float(input("Enter Total Fees: "))

                if Fees_paid <= Total_fees:
                    break
                else:
                    print("Fees paid cannot be greater than total fees. Please enter again.")
            admission_month=input("enter admission month:")
            details={
                "Student_Id":stud_id,
                "Student_Name":name,
                "Course":course,
                "City":City,
                "Qualification":Qualification,
                "Fees_paid":Fees_paid,
                "Total_fees":Total_fees,
                "Admission_Month":admission_month
            }

            self.students_list.append(details)
        print("Total students in linkcode admitted")

    def display(self):
        print(tabulate(self.students_list, headers="keys", tablefmt="fancy_grid"))

    def search_student(self):
        pass
        s_id=int(input("Enter the id you want to search in the system:"))
        found=0
        for i in self.students_list:
            if i["Student_Id"]==s_id:
                print("Student found")
                print("Student_name:",i["Student_Name"])
                print("Couse:",i["Course"])
                print("Qualification:",i["Qualification"])
                print("fees_paid:",i["Fees_paid"])
                print("Total_fees:",i["Total_fees"])
                print("Admission month:",i["Admission_Month"])
                found=1
                break

        if not found:
            print("Student is not admitted in linkcode technologies")

    def update_fees(self):
        name=input("Enter the name of student for which you want to update fees:")
        found=0
        updated_fees=float(input("Enter the updated fees which is paid by student:"))
        for i in self.students_list:
            pass
            if i["Student_Name"]==name:
                i["Fees_paid"]+=updated_fees
                print(f"Total fees paid by {i['Student_Name']} is: {i['Fees_paid']}")
                found=1
                break
        if not found:
            print("No student found in the system for updation")
    
    def delete_student(self):
        student_id=int(input("Enter Student ID to delete: "))
        found=0
        for i in self.students_list:
            if i["Student_Id"]==student_id:
                self.students_list.remove(i)
                found=1
                print("Student deleted successfully.")
                break

        if not found:
            print("No student found with this ID.")

    def Course_wise_Bar_Chart(self):
        pass
        courses = [student["Course"] for student in self.students_list]
        count = Counter(courses)
        plt.bar(count.keys(), count.values())
        plt.title("Course-wise Admissions")
        plt.show()

    def City_wise_Pie_Chart(self):
        pass
        cities = [student["City"] for student in self.students_list]
        count = Counter(cities)
        plt.pie(count.values(), labels=count.keys(),autopct="%1.1f%%")
        plt.title("City-wise Admissions")
        plt.show()

    def fee_collection(self):
        pass
        names = [student["Student_Name"] for student in self.students_list]
        fees = [student["Fees_paid"] for student in self.students_list]
        plt.bar(names, fees)
        plt.title("Fee Collection")
        plt.xticks(rotation=45)
        plt.show()

    def pending_fee(self):
        pass
        names = [student["Student_Name"] for student in self.students_list]
        pending = [
            student["Total_fees"] - student["Fees_paid"]
            for student in self.students_list
        ]
        plt.bar(names, pending)
        plt.title("Pending Fees")
        plt.xticks(rotation=45)
        plt.show()

    def monthly_trend(self):
        pass
        months = [student["Admission_Month"] for student in self.students_list]
        count = Counter(months)
        plt.plot(count.keys(), count.values(), marker="o")
        plt.title("Monthly Admission Trend")
        plt.show()

    def Top_5(self):
        pass
        top5 = sorted(
        self.students_list,
        key=lambda student: student["Total_fees"] - student["Fees_paid"],
        reverse=True
        )
        for student in top5[:5]:
            print(student["Student_Name"], student["Total_fees"] - student["Fees_paid"])
    def export_to_excel(self):
        if len(self.students_list) == 0:
            print("No data to export.")
            return
        df = pd.DataFrame(self.students_list)
        df.to_excel("Student_Report.xlsx", index=False)
        print("Excel file exported successfully as 'Student_Report.xlsx'")

obj=StudentDashboard()
while True:
    print("\n=========================== LINKCODE DASHBOARD ===========================")
    print("1. Add Students")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Fees")
    print("5. Delete Student")
    print("6. Course-wise Bar Chart")
    print("7. City-wise Pie Chart")
    print("8. Fee Collection")
    print("9. Pending Fee Report")
    print("10. Monthly Trend")
    print("11. Top 5 Students")
    print("12. Export to Excel")
    print("13. Exit")
    print("============================================================================")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            obj.add_students()
        case 2:
            obj.display()
        case 3:
            obj.search_student()
        case 4:
            obj.update_fees()
        case 5:
            obj.delete_student()
        case 6:
            obj.Course_wise_Bar_Chart()
        case 7:
            obj.City_wise_Pie_Chart()
        case 8:
            obj.fee_collection()
        case 9:
            obj.pending_fee()
        case 10:
            obj.monthly_trend()
        case 11:
            obj.Top_5()
        case 12:
            obj.export_to_excel()
        case 13:
            print("Thank youuuuuuuuu!")
            break
        case _:
            print("Invalid choice! Please try again")
        