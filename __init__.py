import re
import smtplib
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def verify(email):
    if(re.search(regex, email)):
        x = re.split('@', email)
        domain = (x[1])
        username = (x[0])
        with open('logs.txt', 'a') as f:
            f.write(f"Username is {username}\n")
            f.write(f"Domain is {domain}\n")
    else:
        print("Please provide with a valid email")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    youremail = input("Enter your email: ")
    pass1 = input("Enter your password: ")
    server.login(youremail, pass1)
    server.sendmail(email, to, content)
    server.close()


if __name__ == '__main__':
    email = input("Enter an email adrress: ")
    verify(email)
    try:
        content = input("Enter Your message here: ")
        to = email
        sendEmail(to, content)
        print("Email sucessfully sent")
    except:
        print("Sorry!! An error occured and email was not sent")
