from selenium import webdriver


class Base():
    def __init__(self, browser, url):
        self.open_browser(browser)
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.driver.maximize_window()

    def locator(self, locator):
        el = self.driver.find_element_by_xpath(locator)
        return el

    def click_element(self, locator):
        el = self.locator(locator)
        el.click()

    def send_element(self, locator, text):
        el = self.locator(locator)
        el.send_keys(text)

    def quit(self):
        self.driver.quit()

    def handles(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    def iframe(self, name):
        # iframe的name切换
        self.driver.switch_to.frame(name)

    def open_browser(self, browser):
        if browser == 'ch':
            self.driver = webdriver.Chrome()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        elif browser == 'fi':
            self.driver = webdriver.Firefox()

        return self.driver
