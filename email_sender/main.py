# importing single email sender
from single_em_sender import singleEmailSender
from bul_email import bulkEmailSender




# main
if __name__ == "__main__":
    print("Welcome to email send using python")
    subject = input("Enter subject:")
    body = input("Enter body msg:")
    choice = int(input("1. Single email send \n 2. Bulk \
                       email send \n Enter your operation:"))
    if choice == 1:
        reciever_email = input("Enter Reciever email: ")
        
        # single email function calling
        singleEmailSender(to_email= reciever_email, subject= subject, body= body)
        print(f"{reciever_email} to Email send successfully")
    elif choice == 2:
         # calling bulk email sender
         emails = input("Enter list of emails separated by comma: ")
         bulkEmailSender(list_of_emails=emails, subject=subject, body= body)
    else:
        print("select valid operation")