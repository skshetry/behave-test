from pypom import page


class LoginPage(page.Page):
    URL_TEMPLATE = "http://hello.com"
    _username_field_locator = ("css", "")
    _password_field_locator = ("css", "")
    _form_locator = ("css", "")
    _form_submit_locator = ("name", "submit")

    @property
    def loaded(self):
        form = self.find_element(*self._form_locator)
        return form.is_displayed()

    def login(self, username, password):
        self.find_element(*self._username_field_locator).fill(username)
        self.find_element(*self._password_field_locator).fill(password)
        self.find_element(*self._form_submit_locator).click()
