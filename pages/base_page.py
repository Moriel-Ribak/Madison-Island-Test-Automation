from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def highlight(self, locator):
        element = self.page.locator(locator)

        element.evaluate("""
            el => {
                el.style.outline = '3px solid yellow';
                el.style.backgroundColor = 'rgba(255, 255, 0, 0.25)';
            }
        """)

        return element

    def click(self, locator):
        element = self.highlight(locator)
        element.click()

    def list_click(self, locator, index):
        element = self.page.locator(locator).nth(index)

        element.evaluate("""
            el => {
                el.style.outline = '3px solid yellow';
                el.style.backgroundColor = 'rgba(255, 255, 0, 0.25)';
            }
        """)

        element.click()

    def fill(self, locator, text):
        element = self.highlight(locator)
        element.fill(text)

    def get_text(self, locator):
        element = self.highlight(locator)
        return element.inner_text()

    def list_get_text(self, locator, index):
        return self.page.locator(locator).nth(index).inner_text()

    def list_is_visible(self, locator, index):
        element = self.page.locator(locator).nth(index)

        element.evaluate("""
            el => {
                el.style.outline = '3px solid yellow';
                el.style.backgroundColor = 'rgba(255, 255, 0, 0.25)';
            }
        """)

        return element.is_visible()

    def count(self, locator):
        return self.page.locator(locator).count()

    def get_attribute(self, locator, value):
        element = self.highlight(locator)
        return element.get_attribute(value)

    def list_get_attribute(self, locator, value, i):
        element = self.page.locator(locator).nth(i)
        element.highlight()
        return element.get_attribute(value)

    def wait_for_url(self,url):
        self.page.wait_for_url(url)
        return True

    def get_url(self):
        return self.page.url

    def is_visible(self,locator):
         return self.page.locator(locator).is_visible()

    def is_disabled(self,locator):
         return self.page.locator(locator).is_disabled()

    def is_list_item_visible(self, locator, index):
        element = self.page.locator(locator).nth(index)

        element.evaluate("""
                         el => {
                             el.style.outline = '3px solid yellow';
                             el.style.backgroundColor = 'rgba(255, 255, 0, 0.25)';
                         }
                         """)


        return element.is_visible()

    def reload_page(self):
        self.page.reload()

    def select_option(self,locator,index):
        self.page.locator(locator).select_option(index)