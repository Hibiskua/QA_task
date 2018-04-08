from splinter import Browser

with Browser("chrome") as browser:
    url = "http://www.kiwi.com"
    #open kiwi home page
    browser.visit(url)

    #find x for remove brno-praha
    remove_praha = browser.find_by_xpath("//*[@class='input-place-close']")
    remove_praha.click()

    #fill praha as from
    imput_field = browser.find_by_xpath("//*[@class='input-places-input input-origin']")
    browser.find_by_xpath("//span[@class='_highlighted]").click()

    #fill london as to
    browser.find_by_xpath("//*[@class='input-places-input input-destination']")
    browser.fill("londyn")
    browser.find_by_xpath("//*[@class='place-row clickable']").click()

    #click on search button
    browser.find_by_xpath("//*[@class='Button SimpleLandingPage-button ButtonWrapper _large _primary']")
