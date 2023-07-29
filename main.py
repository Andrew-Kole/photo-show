from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import urllib



Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):
        # get user input
        query = self.manager.current_screen.ids.user_query.text
        # get wikipedia page and first image url
        page = wikipedia.page(query)
        image_link = page.images[0]
        image_path = "images/image.jpg"
        # download the image
        urllib.request.urlretrieve(image_link,image_path)
        # set image in widget
        self.manager.current_screen.ids.img.source = image_path
        self.ids.img.reload()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
