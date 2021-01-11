# Zadanie 2: Wykorzystaj narzędzie Selenium w celu wypełnienia formularza na dołączonej do zadania stronie
# internetowej (napisana we flasku – instrukcja uruchomienia w pliku app.py). Po wypełnieniu i
# wysłaniu formularza wyświetli się stosowny komunikat.
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("localhost:5000")

driver.find_element_by_xpath(xpath="//input[@value='Otwórz formularz']").click()

driver.find_element_by_id("email").send_keys("eksploracja@eksploracja.kis.p.lodz.pl")
driver.find_element_by_id("password").send_keys("tajnehaslo")
driver.find_element_by_id("password-repeat").send_keys("tajnehaslo")
driver.find_element_by_id("name").send_keys("eksploracja")
driver.find_element_by_id("answer").send_keys("Poprawna odpowiedź!")

driver.find_element_by_xpath(xpath="//button[text()='Wyślij']").click()
