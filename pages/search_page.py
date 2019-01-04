from pypom import page


class SearchPage(page.Page):
    URL_TEMPLATE = "/search.html"
    _search_field_locator = ("name", "search_field")
    _root_locator = ("id", "search_form")
    _search_form_submit_locator = ("name", "submit_btn")

    @property
    def loaded(self):
        return self.find_element(*self._root_locator) or False

    def search(self, text):
        self.find_element(*self._search_field_locator).fill(text)

        self.find_element(*self._search_form_submit_locator).click()
