total_users= int(input("total users: "))
staff_users= int(input("staff users: "))
non_teachingstaffs=staff_users//3
staff_users = staff_users+non_teachingstaffs
student_users = total_users-staff_users
if(total_users <= 0):
    print("Invalid Input")
elif(total_users <= staff_users):
    print("Invalid Input" )
else:
    print("student users = ",student_users)
