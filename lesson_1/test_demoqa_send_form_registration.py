from selene import have
from selene.support.shared import browser

def test_set_part_data_in_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Andrey')
    browser.element('#lastName').type('Pupkin')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('2121421222').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))