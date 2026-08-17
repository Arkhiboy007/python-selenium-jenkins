import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def test_page_title(driver):
    driver.get("https://www.selenium.dev/")

    assert "Selenium" in driver.title


def test_search_documentation(driver):
    driver.get("https://www.selenium.dev/")

    documentation_link = driver.find_element(
        By.LINK_TEXT,
        "Documentation"
    )

    documentation_link.click()

    assert "documentation" in driver.current_url.lower()