def create_note(self, title, description):

    WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable(self.ADD_NOTE)
    )

    self.driver.execute_script(
        "arguments[0].click();",
        self.driver.find_element(*self.ADD_NOTE)
    )

    WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located(self.TITLE)
    )

    self.type(self.TITLE, title)
    self.type(self.DESCRIPTION, description)

    self.click(self.SAVE)

    WebDriverWait(self.driver, 30).until(
        lambda d: len(d.find_elements(*self.NOTES)) > 0
    )