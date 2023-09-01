from selenium.webdriver import Chrome

def pass_driver(f):

    def wrapper(*args, **kwargs):
        driver = Chrome()
        kwargs['driver'] = driver
        f(*args, **kwargs)

    return wrapper
