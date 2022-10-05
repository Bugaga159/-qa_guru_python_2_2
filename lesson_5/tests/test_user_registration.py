import os

from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

first_name = 'Andrey'
last_name = 'Pupkin'
email = 'test@test.net'
mobile_number = '8777006941'
subjects = 'Maths'
current_address = 'London baker street'

def test_demoqa_practice_form():
    """Тест на регистрацию юзера по всем полям"""

    browser.open('https://demoqa.com/automation-practice-form')
    s('#firstName').type(first_name)
    s('#lastName').type(last_name)
    s('#userEmail').type(email)
    s('#gender-radio-1').double_click()
    s('#userNumber').type(mobile_number)
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').type('April')
    s('.react-datepicker__year-select').type('1993')
    s('[aria-label="Choose Monday, April 19th, 1993"]').click()
    s('#subjectsInput').type(subjects).press_enter()
    s('[for="hobbies-checkbox-2"]').click()
    s('#uploadPicture').send_keys(os.path.abspath('../resource/mini.jpg'))
    s('#currentAddress').type(current_address)
    s('#react-select-3-input').type('rajasthan').press_enter()
    s('#react-select-4-input').type('jaipur').press_enter()
    s('#submit').press_enter()

    #assert results

    s('.modal-title').should(have.text('Thanks for submitting the form'))
    ss('.table-responsive tr td:nth-of-type(2)').should(have.texts(
        f"{first_name} {last_name}",
        email,
        'Male',
        mobile_number,
        '19 April,1993',
        subjects,
        'Reading',
        'mini.jpg',
        current_address,
        'Rajasthan Jaipur'
    ))
    s('#closeLargeModal').click()
