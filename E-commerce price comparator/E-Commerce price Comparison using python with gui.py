from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import webbrowser
import time

flipkart = ''
amazon = ''

def flipkart_search(name):
    try:
        global flipkart
        name1 = name.replace(" ", "+")
        flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        
        service = Service("path_to_chromedriver")  # Replace "path_to_chromedriver" with the actual path to your ChromeDriver
        driver = webdriver.Chrome(service=service)
        driver.get(flipkart)
        driver.implicitly_wait(10)

        flipkart_name = driver.find_element(By.CSS_SELECTOR, '._4rR01T').text.strip().upper()
        if name.upper() in flipkart_name:
            flipkart_price = driver.find_element(By.CSS_SELECTOR, '._1_WHN1').text.strip()

            return f"{flipkart_name}\nPrice: {flipkart_price}\n"
        else:
            flipkart_price = 'Product Not Found'
        return flipkart_price
    except:
        flipkart_price = 'Product Not Found'
    finally:
        driver.quit()

def amazon_search(name):
    try:
        global amazon
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon = f'https://www.amazon.in/{name1}/s?k={name2}'

        service = Service("path_to_chromedriver")  # Replace "path_to_chromedriver" with the actual path to your ChromeDriver
        driver = webdriver.Chrome()
        driver.get(amazon)
        driver.implicitly_wait(10)

        amazon_page = driver.find_elements(By.CSS_SELECTOR, '.a-color-base.a-text-normal')
        
        for element in amazon_page:
            amazon_name = element.text.strip().upper()
            if name.strip().upper() in amazon_name[0:20]:
                amazon_name = element.text.strip().upper()
                amazon_price = driver.find_element(By.CSS_SELECTOR, '.a-price-whole').text.strip().upper()
                return f"{amazon_name}\nPrice: {amazon_price}\n"
        return 'Product Not Found'
    except Exception as e:
        print(e)
        return f'Product Not Found{e}'
    finally:
        driver.quit()


def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g


def urls():
    global flipkart
    global amazon
    return f"{flipkart}\n\n\n{amazon}"



def open_url(event):
        global flipkart
        global amazon
        webbrowser.open_new(flipkart)
        webbrowser.open_new(amazon)

from tkinter import Tk, Label, Button, Entry, Text, Scrollbar

def search():
    product_name_value = product_name.get()
    box1.delete(1.0, "end")
    box2.delete(1.0, "end")

    t1 = flipkart_search(product_name_value)
    if t1:
        box1.insert(1.0, t1)
    else:
        box1.insert(1.0, "Product not found on Flipkart.")

    t4 = amazon_search(product_name_value)
    if t4:
        box2.insert(1.0, t4)
    else:
        box2.insert(1.0, "Product not found on Amazon.")

window = Tk()
window.wm_title("Price Comparison Extension")
window.minsize(1500, 700)

label_one = Label(window, text="Enter Product Name :", font=("courier", 10))
label_one.place(relx=0.2, rely=0.1, anchor="center")

product_name = StringVar()
product_name_entry = Entry(window, textvariable=product_name, width=50)
product_name_entry.place(relx=0.5, rely=0.1, anchor="center")

search_button = Button(window, text="Search", width=12, command=search)
search_button.place(relx=0.5, rely=0.2, anchor="center")

l1 = Label(window, text="Flipkart", font=("courier", 20))
l2 = Label(window, text="Amazon", font=("courier", 20))

l1.place(relx=0.2, rely=0.3, anchor="center")
l2.place(relx=0.5, rely=0.3, anchor="center")

scrollbar = Scrollbar(window)

box1 = Text(window, height=7, width=50, yscrollcommand=scrollbar.set)
box2 = Text(window, height=7, width=50, yscrollcommand=scrollbar.set)

box1.place(relx=0.2, rely=0.4, anchor="center")
box2.place(relx=0.5, rely=0.4, anchor="center")

window.mainloop()

