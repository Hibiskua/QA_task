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

    def wait_for(self, timeout, period=1):
        """
        In loop trying to find element according to selector with timeout
        In case it's not successful raise exception
        :param timeout: Maximal time waiting for element in seconds
        :param period: Period time for recall of search element (default=1 second)
        """
        import time

        print(u"{0}.wait_for({1})".format(self.title, timeout))
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

