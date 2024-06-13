
class TestSecondMod:
    def test_second_1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox - образовательная платформа с онлайн-курсами.' == driver.title
