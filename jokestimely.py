import tkinter
import tkinter.messagebox as mbox
from time import sleep
from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
browser = webdriver.Firefox()
browser.get("http://www.laughfactory.com/jokes/latest-jokes")

sleep(40)

jokes = [str(joke.text) for joke in browser.find_elements_by_xpath("//div/p[starts-with(@id,'joke_')]")]


browser.quit()
display.stop()


window = tkinter.Tk()
window.wm_withdraw()
for joke in jokes:

    sleep(600)

    mbox.showinfo('Bored? Enjoy the JOk3!', joke)

