import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from baseObject.SeleniumObjects import SeleniumObject, SelectorType


class KiwiBooking(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def test_search_let(self):
        driver = self.driver
        action = self.action

        # open kiwi
        driver.get("https://www.kiwi.com/cz/hledej")
        self.assertIn("Kiwi.com", driver.title)

        # close cookies banner
        SeleniumObject(driver, "//*[@class='CookiesBanner-close']", SelectorType.xpath).click()

        # close_button = driver.find_elements_by_xpath("//*[@class='input-place-close']")
        close_button = SeleniumObject(driver, "//*[@class='input-place _default _italic']//*[@class='input-place-close']", SelectorType.xpath)
        close_button.wait_for(10)
        close_button.click()

        # fill odkud
        #  odkud = driver.find_element_by_xpath("//*[@class='input-places-input input-origin']")
        odkud = SeleniumObject(driver, "//*[@class='input-places']//input[@placeholder='Odkud']", SelectorType.xpath)
        odkud.wait_for(10)
        odkud.set_text("brno")

        #  brno_airport = driver.find_elements_by_xpath("//*[@class='place-icon spIcon ic_flight']")
        brno_airport = SeleniumObject(driver, "//*[@class='place-row selected clickable']", SelectorType.xpath)
        brno_airport.wait_for(5)
        brno_airport.click()

        # fill london as to
        close_button = SeleniumObject(driver, "//*[@class='ClickCheck SearchField SearchPlaceField destination _italic']//*[@class='input-place-close']", SelectorType.xpath)
        close_button.wait_for(5)
        close_button.click()

        kam = SeleniumObject(driver, "//*[@class='input-places']/input[@placeholder='Kam']", SelectorType.xpath)
        kam.set_text("londyn")
        london_airports = SeleniumObject(driver, "//*[@class='place-row clickable _level']//span[.='STN Londýn, Spojené království - Letiště London Stansted']", SelectorType.xpath)
        london_airports.wait_for(5)
        london_airports.click()

        # click on first nabidka
        offers = SeleniumObject(driver, "//div[contains(@data-test,'8404')]", SelectorType.xpath)
        offers.wait_for(10)
        offers.click()

        self.waitForElement("//*[@data-test='JourneyBookingButton']")
        rezervation_button = driver.find_element_by_xpath("//*[@data-test='JourneyBookingButton']")
        action.move_to_element(rezervation_button).perform()
        rezervation_button=SeleniumObject(driver, "//*[@data-test='JourneyBookingButton']", SelectorType.xpath)
        rezervation_button.wait_for(3)
        rezervation_button.click()

        # fill name
        personal_info_area = driver.find_element_by_xpath("//*[@data-test='ReservationPassenger']")
        personal_info_area.location_once_scrolled_into_view
        name_field = SeleniumObject(driver, "//*[@data-test='ReservationPassenger-FirstName']//input", SelectorType.xpath)
        name_field.wait_for(3)
        name_field.set_text("TEST")

        # fill surname
        surname_field = SeleniumObject(driver, "//*[@data-test='ReservationPassenger-LastName']//input", SelectorType.xpath)
        surname_field.wait_for(3)
        surname_field.set_text("TEST")

        # pohlaví - select box
        pohlavi = Select(driver.find_element_by_xpath("//*[@data-test='ReservationPassengerGender']//select"))
        pohlavi.select_by_value("mr")

        # narozeni
        narozeni_dadtum = driver.find_elements_by_xpath("//*[@data-test='ReservationDateSplitField-fields']//input")
        narozeni_dadtum[0].send_keys("14")
        narozeni_dadtum[1].send_keys("07")
        narozeni_dadtum[2].send_keys("1987")

        # kontaktni udaje
        email_area = driver.find_element_by_xpath("//*[@data-test='ReservationContact-email']")
        email_area.location_once_scrolled_into_view
        email_field = SeleniumObject(driver, "//*[@data-test='ReservationContact-email']//input", SelectorType.xpath)
        email_field.wait_for(3)
        email_field.set_text("test@test.cz")

        phone_field = SeleniumObject(driver, "//input[@type = 'tel']", SelectorType.xpath)
        phone_field.set_text("777666555")

        # Payment form
        payment_form = driver.find_element_by_xpath("//*[@class='ReservationPaymentForm']")
        payment_form.location_once_scrolled_into_view

        cislo_karty = SeleniumObject(driver, "//*[@data-test='ReservationPaymentForm-row-creditCardNumber']//input", SelectorType.xpath)
        cislo_karty.set_text("4580458045804580")

        platnost_karty_mm = SeleniumObject(driver, "//*[@class='Reservation-inputs-connected-fields']//input[@autocomplete='cc-exp-month']", SelectorType.xpath)
        platnost_karty_mm.set_text(1)
        platnost_karty_year = SeleniumObject(driver, "//*[@class='Reservation-inputs-connected-fields']//input[@autocomplete='cc-exp-year']", SelectorType.xpath)
        platnost_karty_year.set_text("20")
        cvv = SeleniumObject(driver, "//input[@name='payment.cardCvv']", SelectorType.xpath)
        cvv.set_text("123")
        card_owner = SeleniumObject(driver, "//input[@name='payment.cardName']", SelectorType.xpath)
        card_owner.set_text("TEST TEST")

        SeleniumObject(driver, "//*[@data-test='ReservationAgreement']", SelectorType.xpath).click()

        pay = SeleniumObject(driver, "//*[@data-test='ReservationSubmitButton']", SelectorType.xpath)
        pay.click()

        SeleniumObject(driver, "//*[@class='BookingThankyou-texts']", SelectorType.xpath).is_displayed()

    def waitForElement(self, xpath):
        wait = self.wait
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
