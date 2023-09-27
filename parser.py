from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(requests.get('https://2ch.hk/zog').content, 'html.parser')
threads = soup.find_all('article', class_='post__message post__message_op')[:5]
print("\n".join([thread.text for thread in threads]))

# Парсер моего любимого раздела на моем любимом сайте
