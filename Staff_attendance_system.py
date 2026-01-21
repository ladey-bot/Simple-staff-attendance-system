attendance_records = []

def mark_attendance():
    staff_name = input("Enter staff name: ")
    status = input("Enter status (Present/Absent): ")
    attendance_records.append({"staff": staff_name, "status": status})
    print("Attendance recorded")

def view_attendance():
    if not attendance_records:
        print("No attendance records found")
    else:
        for record in attendance_records:
            print("Staff:", record["staff"], "| Status:", record["status"])

def main():
    while True:
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
