from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from bs4 import BeautifulSoup
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 700)
Config.set('graphics', 'height', 300)
import requests, lxml, re



class MainApp(App):


    def build(self):
        self.layout = GridLayout (cols = 1, spacing = 10, size_hint_y = None)
        self.layout.bind(minimum_height = self.layout.setter('height'))
        ScrollView
        bl = BoxLayout(orientation = 'vertical', pos_hint={'center_x': .5, 'center_y': .5})
        button = Button(text='Спарсить', size_hint_y = None, height = 40)
        bl.add_widget(button)
        bl.add_widget(self.layout)


        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        button.bind(on_press=self.on_press_button)
        return bl
    def on_press_button(self, instance):
        print('Вы нажали на кнопку!')
        button = Button(text = "Ура, работает!", size_hint_y = None, height = 40)
        self.layout.add_widget(button)
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
                print(str(i) + " " + a.find('a', class_='b-post__link').text + "\n")
                print("https://www.fl.ru" + a.find('a', class_='b-post__link').get('href'))
                summa = str(a.find('script')).replace('<script type="text/javascript">document.write(', '')
                summa = summa.replace("'", "")
                summa = summa.replace(");</script>", "")
                summa = BeautifulSoup(summa, 'lxml')
                # summa = summa.find('div')
                # print(summa.prettify())
                try:
                    print(summa.find('div').text)
                except AttributeError:
                    pass
                try:
                    print(summa.find('a').text)
                except AttributeError:
                    pass
                i = i + 1
                print("\n")
 
if __name__ == '__main__':
    app = MainApp()
    app.run()    



















