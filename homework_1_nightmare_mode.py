import random
from selene import browser

random.seed()
userNumber = '8'

for x in range(9):
    userNumber = userNumber + random.choice(list('1234567890'))

browser.config.browser_name = 'firefox'
browser.config.window_height = 1024
browser.config.window_width = 1024
browser.config.hold_browser_open = True
browser.config.click_by_js = True

browser.open('https://demoqa.com/automation-practice-form')
browser.element('[id=firstName]').type('firstName')
browser.element('[id=lastName]').type('lastName')
browser.element('[id=userEmail]').type('user@Email.net')

browser.element('[id=gender-radio-1]').click()
browser.element('[id=userNumber]').type(userNumber)
browser.element('[id=dateOfBirthInput]').click().press_enter()

#  Здесь будет код для выбора Subjects

browser.element('[id=hobbies-checkbox-1]').click()
browser.element('[id=hobbies-checkbox-2]').click()
browser.element('[id=hobbies-checkbox-3]').click()
browser.element('[id=hobbies-checkbox-1]').click()
