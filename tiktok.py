import requests
import os
import time
import string
import random
import requests
import sys as n
import time as mm
import webbrowser
import json,requests,random
req = requests.session()
chars = 'mnbvcxzlkjhgfdsapoiuytrewq0987654321_'
#user= str("".join(random.choice(chars)for i in range(4)))

headers = {
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
}
#file = open('users.txt' ,"r")

while True:
  user= str("".join(random.choice(chars)for i in range(4)))
  tiklog = f'https://www.tiktok.com/@{user}'
  rq = req.get(tiklog, headers=headers)
  if rq.status_code == 404:
    Account = 'https://api.telegram.org/bot1880968697:AAGnctyEl5qWuI_dhbf0hIg6nfWCBUgcxFQ/sendMessage?chat_id=811693011&text= {}'.format(user)
    with open('good.txt','a') as new:
                new.write(f'{user}\n')
    requests.get(Account)
    print("یوسەر تەواوە:  ✅ " + user)
  elif rq.status_code == 200:
     print("[!]یوسەر ئیش ناکات  ❌ -> : " + user)
     if (user== ""): 
    	 break