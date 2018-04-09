import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import python_test.SeleniumObjects as selobj
from python_test.SeleniumObjects import SeleniumObject, SelectorType
import time

class KiwiBooking(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def test_search_let(self):
        driver = self.driver
        action = self.action

        driver.get("https://www.kiwi.com/cz/hledej")
        self.assertIn("Kiwi.com", driver.title)
        close_button = driver.find_elements_by_xpath("//*[@class='input-place-close']")
        close_button[0].click()

        #fill odkud
        odkud = driver.find_element_by_xpath("//*[@class='input-places-input input-origin']")
        odkud.send_keys("brno")

        praha_airports = driver.find_elements_by_xpath("//*[@class='place-icon spIcon ic_flight']")
        praha_airports[0].click()

        # fill london as to
        close_button[1].click()
        kam = driver.find_element_by_xpath("//*[@class='input-places-input input-destination']")
        kam.send_keys("londyn")
        london_airports = driver.find_elements_by_xpath("//*[@class='place-icon spIcon ic_flight']")
        london_airports[0].click()

        # click on first nabidka
        #offers = driver.find_elements_by_xpath("//*[@class='Journey-overview Journey-oneWay']")
        offers = SeleniumObject(driver, "//*[@class='Journey-overview Journey-oneWay']", SelectorType.xpath)

        offers.click()
        #rezervation_button = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@data-test='JourneyBookingButton']")))
        self.waitForElement("//*[@data-test='JourneyBookingButton']")
        rezervation_button = driver.find_element_by_xpath("//*[@data-test='JourneyBookingButton']")
        action.move_to_element(rezervation_button).perform()
        #time.sleep(1)
        rezervation_button.click()

        #fill name
        personal_info_area = driver.find_element_by_xpath("//*[@data-test='ReservationPassenger']")
        personal_info_area.location_once_scrolled_into_view
        name_field = driver.find_element_by_xpath("//*[@data-test='ReservationPassenger-FirstName']//input")
        name_field.send_keys("TEST")

        #fill surname
        surname_field = driver.find_element_by_xpath("//*[@data-test='ReservationPassenger-LastName']//input")
        surname_field.send_keys("TEST")

        #pohlaví
        pohlavi = Select(driver.find_element_by_xpath("//*[@data-test='ReservationPassengerGender']//select"))
        pohlavi.select_by_value("mr")

        #narozeni
        narozeni_dadtum = driver.find_elements_by_xpath("//*[@data-test='ReservationDateSplitField-fields']//input")
        narozeni_dadtum[0].send_keys("14")
        narozeni_dadtum[1].send_keys("07")
        narozeni_dadtum[2].send_keys("1987")

        #kontaktni udaje
        email_area = driver.find_element_by_xpath("//*[@data-test='ReservationContact-email']")
        email_area.location_once_scrolled_into_view
        email_field = driver.find_element_by_xpath("//*[@data-test='ReservationContact-email']//input")
        email_field.send_keys("test@test.cz")

        phone_field = driver.find_element_by_xpath("//input[@type = 'tel']")
        phone_field.send_keys("777666555")

        #Payment form
        payment_form = driver.find_element_by_xpath("//*[@class='ReservationPaymentForm']")
        payment_form.location_once_scrolled_into_view

        cislo_karty = driver.find_element_by_xpath("//*[@data-test='ReservationPaymentForm-row-creditCardNumber']//input")
        cislo_karty.send_keys("4580458045804580")

        platnost_karty_mm = driver.find_element_by_xpath("//*[@class='Reservation-inputs-connected-fields']//input[@autocomplete='cc-exp-month']")
        platnost_karty_mm.send_keys(1)
        platnost_karty_year = driver.find_element_by_xpath("//*[@class='Reservation-inputs-connected-fields']//input[@autocomplete='cc-exp-year']")
        platnost_karty_year.send_keys("20")
        cvv = driver.find_element_by_xpath("//input[@name='payment.cardCvv']")
        cvv.send_keys("123")
        card_owner = driver.find_element_by_xpath("//input[@name='payment.cardName']")
        card_owner.send_keys("TEST TEST")

        driver.find_element_by_xpath("//*[@data-test='ReservationAgreement']").click()

        pay = driver.find_element_by_xpath("//*[@data-test='ReservationSubmitButton']")
        pay.click()

        driver.find_element_by_xpath("//*[@class='BookingThankyou-texts']").is_displayed()

    def waitForElement(self, xpath):
        wait = self.wait
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()