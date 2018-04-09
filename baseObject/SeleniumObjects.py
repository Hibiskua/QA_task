from enum import Enum

class SelectorType(Enum):
    id = 1
    xpath = 2

class SeleniumObject:
    def __init__(self, driver, selector, selector_type=SelectorType.xpath, index=0, parent_object=None,
                 only_visible=False):

        """
        When called without arguments, set up default parameters
        :param driver: Instance of appium webdriver
        :param selector: Selector for element searching
        :param selector_type: Selector type. Enum of [id, text, class_name, uia_query, xpath]
        :param index: Index of element in case that search procedure can return array
        :param parent_object: Appium object will be searched in scope of parent Appium Object (for layouts)
        :param only_visible: Boolean value determining if the driver searches only among visible elements
        """
        self.driver = driver
        self.parent_object = parent_object
        self.selector = selector
        self.selector_type = selector_type
        self.index = index
        self.only_visible = only_visible

    def click(self):
        """
        Perform click on element
        """
        self.__get_object().click()

    def set_text(self, text):
        """
        Set text into element
        :param text: Set this text
        """
        self.__get_object().send_keys(text)

    def is_displayed(self):
        """
        Get bolean value is element displayed
        :return: bolean value
        """
        is_displayed = self.__get_object().is_displayed()
        return is_displayed

    def wait_for(self, timeout, period=1):
        """
        In loop trying to find element according to selector with timeout
        In case it's not successful raise exception
        :param timeout: Maximal time waiting for element in seconds
        :param period: Period time for recall of search element (default=1 second)
        """
        import time

        waitfor = False
        start_time = time.time()
        end_time = start_time + timeout

        while time.time() < end_time:
            try:
                self.__get_object()
                waitfor = True
                met_time = time.time()
                break
            except:
                time.sleep(period)

        if waitfor:
            print("Waiting for element was successful in {0}s".format(met_time - start_time))
        else:
            raise AssertionError("Waiting for element was not successful in {0}s".format(timeout))


# ===========================================================================================
# ===========================================================================================

    def __get_object(self):

        """
        Private method for getting object from driver/parent_object
        """

        # driver or parentObject
        if self.parent_object == None:
            __control = self.driver
        else:
            __control = self.parent_object.__get_object()

        # ID
        if self.selector_type == SelectorType.id:
            elements = __control.find_elements_by_id(self.selector)
        # XPATH
        elif self.selector_type == SelectorType.xpath:
            elements = __control.find_elements_by_xpath(self.selector)

        else:
            raise ValueError("Unknown SelectorType enum value")

        # filter only visible elements
        if self.only_visible:
            elements = [e for e in elements if e.is_displayed()]

        visible_info = " visible " if self.only_visible else ""

        if len(elements) == 0:
            raise LookupError(u"There is no {0}element given for {1}={2}".format(visible_info, self.selector_type.name, self.selector))
        elif len(elements) <= self.index:
            raise LookupError(u"There is {0} {1}element(s) given for {2}={3}. No element with index={4}".format(len(elements), visible_info, self.selector_type.name, logger.encode_to_unicode(self.selector), self.index))
        elif len(elements) == 1:
            return elements[0]
        else:
            return elements[self.index]