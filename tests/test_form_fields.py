import allure

from pages.form_fields_page import FormFieldsPage


@allure.title("Submit form shows success alert")
def test_form_submit(driver):
    page = FormFieldsPage(driver)

    page.open() \
        .set_name("Ivan") \
        .set_password("Password123") \
        .choose_drinks() \
        .choose_color() \
        .choose_like_automation("yes") \
        .set_email("name@example.com") \
        .set_message_auto() \
        .attach_filled_form_screenshot() \
        .submit()

    alert_text = page.get_and_accept_alert_text()
    assert alert_text == "Message received!"
