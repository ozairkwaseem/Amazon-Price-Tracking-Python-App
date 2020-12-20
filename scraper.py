import requests
from bs4 import BeautifulSoup
import smtplib

# Add link to whichever product you would like to track prices for**
URL = 'https://www.amazon.com/Linsy-Home-Computer-Shelves-LS209V1/dp/B0899LXDFV/ref=sr_1_2_sspa?dchild=1&keywords=office+desk&qid=1608499638&sr=8-2-spons&psc=1&smid=A132YFTWUIX4XS&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFGWFpXNlowWlZSUVgmZW5jcnlwdGVkSWQ9QTA2OTU3MDczSzJOWkw0NUdGV1JJJmVuY3J5cHRlZEFkSWQ9QTAyNDExNDYyOEFERkRXVkZNSUJaJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}



def check_price():

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="price_inside_buybox").get_text()
    converted_price = float(price[0:5])
    if(converted_price < 99.0):
        send_email()

    print(converted_price)
    print(title)

    if(converted_price < 99.0):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
# you will need to generate and insert your own password below***
    server.login('ozairkwaseem@gmail.com', 'insert your generated password' )

    subject = 'The PRICE FELL!!'
    body = 'Go check this Amazon link:https://www.amazon.com/Linsy-Home-Computer-Shelves-LS209V1/dp/B0899LXDFV/ref=sr_1_2_sspa?dchild=1&keywords=office+desk&qid=1608499638&sr=8-2-spons&psc=1&smid=A132YFTWUIX4XS&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFGWFpXNlowWlZSUVgmZW5jcnlwdGVkSWQ9QTA2OTU3MDczSzJOWkw0NUdGV1JJJmVuY3J5cHRlZEFkSWQ9QTAyNDExNDYyOEFERkRXVkZNSUJaJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'ozairkwaseem@gmail.com',
        'oza1rw@gmail.com',
        msg
    )

    print('The email has been sent!')

    server.quit()


check_price()
