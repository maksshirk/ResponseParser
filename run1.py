from bs4 import BeautifulSoup
import requests, lxml, re, os, openpyxl

wb = openpyxl.load_workbook(filename = 'zakaz.xlsx')
sheet = wb['test']
num_of_page = 1
i = 1
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.709 Yowser/2.5 Safari/537.36'}
url = 'https://fl.ru/projects/?page='  # https://www.fl.ru/rss/all.xml?subcategory=279&category=5
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
        type = ""
        print(str(i) + " " + a.find('a', class_='b-post__link').text)
        title = a.find('a', class_='b-post__link').text
        print("https://www.fl.ru" + a.find('a', class_='b-post__link').get('href'))
        prj_name = a.find('a', class_='b-post__link').get('onclick')
        prj_name = prj_name.replace("localStorage.setItem('disposableProjectId', ", "")
        prj_name = prj_name.replace(")", "")
        print(prj_name)
        href = "https://www.fl.ru" + a.find('a', class_='b-post__link').get('href')
        scripts = a.find_all('script')
        summa = str(scripts[0]).replace('<script type="text/javascript">document.write(', '')
        summa = summa.replace("'", "")
        summa = summa.replace(");</script>", "")
        summa = BeautifulSoup(summa, 'lxml')
        # summa = summa.find('div')
        # print(summa.prettify())
        try:

            price = summa.find('div').text
            price = price.replace("  Безопасная сделка ","")
            print(price + "это сумма")
        except AttributeError:
            pass
        try:
            print(summa.find('a').text + "А это наличие безопасной сделки")
            security = summa.find('a').text
        except AttributeError:
            pass
        tz = str(scripts[1]).replace('<script type="text/javascript">document.write(', '')
        tz = tz.replace("'", "")
        tz = tz.replace(');</script>', '')
        tz = BeautifulSoup(tz, 'lxml')
        TechZadanie = tz.find('div', class_ = "b-post__txt").text
        print(TechZadanie)
        otkl = str(scripts[2]).replace('<script type="text/javascript">document.write(', '')
        otkl = otkl.replace("'", "")
        otkl = otkl.replace(");</script>", "")
        otkl = BeautifulSoup(otkl, 'lxml')
        Otkliks = otkl.find('a').text
        print(Otkliks)
        time = otkl.find('div', class_ = "b-post__txt b-post__txt_fontsize_11")
        prosmotry = time.find_all('span')[1].text
        print(prosmotry)
        try:
            type = time.find_all('span')[3].text
        except IndexError:
            pass
        print(type)
        time = time.text
        time = time.replace(type, "")
        time = time.replace(prosmotry, "")
        time = time.replace(Otkliks, "")
        print(time)
        i = i + 1
        print("\n")
        sheet.cell(row=i, column=1).value = i
        sheet.cell(row=i, column=2).value = time
        sheet.cell(row=i, column=3).value = title
        sheet.cell(row=i, column=4).value = prj_name
        sheet.cell(row=i, column=5).value = href
        sheet.cell(row=i, column=6).value = type
        sheet.cell(row=i, column=7).value = prosmotry
        sheet.cell(row=i, column=8).value = TechZadanie
        sheet.cell(row=i, column=9).value = security
        sheet.cell(row=i, column=10).value = Otkliks
        sheet.cell(row=i, column=11).value = price
    wb.save('zakaz.xlsx')
wb.save('zakaz.xlsx')


















