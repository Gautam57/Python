# creating basic school administration program and writing it into CSV file

import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact-Number", "Email-ID"])

        writer.writerow(info_list)

if __name__ == "__main__":
    student_num = 1

    while True:

        student_info = input("Enter information for student {} in following format (Name Age Contact_Number E-Mail ID): ".format(student_num)).split(' ')

        print("The Entered Information is:\nName: {}\nAge: {}\nContact_ Number: {}\nE-Mail-ID: {}".format(student_info[0], student_info[1], student_info[2], student_info[3]))

        choice_check = input("Is the entered information correct? (yes/no): ").casefold()

        if choice_check == "yes":
            write_into_csv(student_info)
            condition_check = input("Enter (yes/no) if you want to enter information for another student: ").casefold()

            if condition_check == "yes":

                student_num = student_num + 1
                continue

            elif condition_check == "no":
                    break

        elif choice_check == "no":
            print("Please re-enter the values!")
