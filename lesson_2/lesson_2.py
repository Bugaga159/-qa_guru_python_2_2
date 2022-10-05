def print_func(func_name, *args):
    func_name = func_name.__name__.replace("_", " ").capitalize()
    print(func_name, *args)

def open_browser(browser_name):
    print_func(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    print_func(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    print_func(find_registration_button_on_login_page, page_url, button_text)

open_browser('Chrome')
go_to_companyname_homepage("https://www.google.com/")
find_registration_button_on_login_page("https://www.google.com/", "Войти")