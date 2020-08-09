#! python3
import bs4
import requests
import smtplib

the_one = 'borzaska'  # This is the name of the food you are looking for
to_address = ['example1@email.com', 'example2@email.com']  # E-mail list
email_content = 'Subject: Borzaska Alert!\n\nAttention!\n\nYour favourite food is available today!' \
                '\n\nBon apetite!:\nFood Notifier V1.0'

if __name__ == '__main__':
    # Download page
    getPage = requests.get('http://www.somesite.com/menu')
    getPage.raise_for_status()  # if error it will stop the program

    # Parse text for foods
    menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
    foods = menu.select('.foodname')

    for food in foods:
        if the_one in food.text.lower():
            conn = smtplib.SMTP('smtp.gmail.com', 587)  # smtp address and port
            conn.ehlo()  # call this to start the connection
            conn.starttls()  # starts tls encryption. When we send our password it will be encrypted.
            conn.login('youremail@gmail.com', 'appkey')
            conn.sendmail('youremail@gmail.com', to_address, email_content)
            conn.quit()
            print(f'Sent notification e-mails for the following recipients:\n{to_address}')
            exit(0)
    print('Your favourite food is not available today.')
