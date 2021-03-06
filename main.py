import random
import string

from selenium import webdriver


# Randomly changes the case of a word
def change_case(word, rand_number=random.randint(0, 2)):
    if rand_number == 0:
        return word.upper()
    elif rand_number == 1:
        return word.lower()
    else:
        return word.title()


def generate_email():
    # Opens the file, chooses a random line then strips any new lines at the end
    firstname = random.choice(open('firstnames.txt').readlines()).rstrip()
    lastname = random.choice(open('lastnames.txt').readlines()).rstrip()
    domain = random.choice(open('domains.txt').readlines()).rstrip()

    # Change the case of the names, add a random number,
    # randomly shuffle the order and finally return it with the domain appended
    username = [change_case(firstname), change_case(lastname), str(random.randint(0, 500))]
    random.shuffle(username)
    return ''.join(username) + domain


def generate_password(bottom, top):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(bottom, top)))


def generate_fullname():
    firstname = random.choice(open('firstnames.txt').readlines()).rstrip()
    lastname = random.choice(open('lastnames.txt').readlines()).rstrip()
    return firstname + " " + lastname


if __name__ == "__main__":
    # Setup web driver
    driver = webdriver.Chrome("chromedriver.exe", options=webdriver.ChromeOptions())

    # Start main loop
    while True:
        try:
            driver.get("WEBSITE HERE")

            # Structure for generic login wall
            email = driver.find_element_by_xpath('EMAIL EXPATH HERE')
            email.send_keys(generate_email())

            password = driver.find_element_by_xpath('PASSWORD XPATH HERE')
            password.send_keys(generate_password(10, 25))

            login = driver.find_element_by_xpath('LOGIN XPATH HERE')
            login.click()

        # Allow the user to exit the program by using using Control-C 
        except (KeyboardInterrupt, SystemExit):
            print("Exiting program...")
            exit()

        # Preventing timeouts
        except:
            pass
