from bs4 import BeautifulSoup
import html2text
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import sys


def main():
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url = raw_input("Please enter the URL of the article: ")

    # Load the URL in PhantomJS.
    driver = webdriver.PhantomJS()
    # driver = webdriver.Firefox()
    driver.set_window_size(1280, 720)
    driver.get(url)

    WebDriverWait(driver, 45).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'p'))
    )

    soup = BeautifulSoup(driver.page_source)
    driver.quit()

    ps = soup.html.find_all("p")

    biggest_parent = None

    for p in ps:
        # How many p tags does this parent have?
        child_ps = len(p.parent.find_all('p', recursive=False))

        if not biggest_parent or child_ps > biggest_parent[0]:
            biggest_parent = (child_ps, p.parent)

    # We most likely have the article container stored as biggest_parent[1], so
    # turn it into Markdown.
    print html2text.html2text(unicode(biggest_parent[1]))

if __name__ == '__main__':
    main()
