#! python3
import bs4, requests, smtplib

# ------------------- E-mail list ------------------------
toAddress = ['example1@email.com','example2@email.com']
# --------------------------------------------------------

#Download page
getPage = requests.get('http://www.somesite.com/menu')
getPage.raise_for_status() #if error it will stop the program

#Parse text for foods
menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
foods = menu.select('.foodname')

the_one = 'borzaska' # This is the name of the food you are looking for
flength = len(the_one)
available = False

for food in foods:
    for i in range(len(food.text)):
        chunk = food.text[i:i+flength].lower()
        if chunk == the_one:
            available = True

if available == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('youremail@gmail.com, 'appkey')
    conn.sendmail('youremail@gmail.com', toAddress, 'Subject: Borzaska Alert!\n\nAttention!\n\nYour favourite food is available today!\n\nBon apetite!:\nFood Notifier V1.0')
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
    print('')
else:
    print('Your favourite food is not available today.')
