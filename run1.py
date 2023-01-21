from bs4 import BeautifulSoup
import requests, lxml, re

num_of_page = 1
i = 0
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.709 Yowser/2.5 Safari/537.36'}
url = 'https://www.fl.ru/projects/?page='  # https://www.fl.ru/rss/all.xml?subcategory=279&category=5
for с in range(1, num_of_page + 1):  # Сколько страниц столько и итераций цикла
    page = requests.get(url + str(с) + '&kind=5', headers=headers)  # Полyчаем страницy в зависимости от i
    soup = BeautifulSoup(page.text, 'lxml')
    soup = soup.find_all('div', class_='b-post__grid')
    for a in soup:
        title = ""
        TechZadanie = ""
        Otkliks = ""
        href = ""
        price = ""
        time = ""
        prj_name = ""
        security = ""


        print (a)





        print(str(i) + " " + a.find('a', class_='b-post__link').text + "\n")
        title = a.find('a', class_='b-post__link').text
        print("https://www.fl.ru" + a.find('a', class_='b-post__link').get('href'))
        href = "https://www.fl.ru" + a.find('a', class_='b-post__link').get('href')
        summa = str(a.find('script')).replace('<script type="text/javascript">document.write(', '')
        summa = summa.replace("'", "")
        summa = summa.replace(");</script>", "")
        summa = BeautifulSoup(summa, 'lxml')
        # summa = summa.find('div')
        # print(summa.prettify())
        try:
            print(summa.find('div').text + "это сумма")
            price = summa.find('div').text
        except AttributeError:
            pass
        try:
            print(summa.find('a').text + "А это наличие безопасной сделки")
            security = summa.find('a').text
        except AttributeError:
            pass
        i = i + 1
        print("\n")



















