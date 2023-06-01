import page_objects.page as page


class TestAppUI:
    def test_solution_title_matches(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)

        assert main_page.is_title_matches('This is Test App')

    def test_solution_result_not_empty(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_text_intervals('[[1,2],[3,5],[6,7],[8,10],[12,16]]')
        main_page.fill_text_new_interval('[4,8]')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.is_results_found()

    def test_solution_result_empty_with_empty_string(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_text_intervals('')
        main_page.fill_text_new_interval('')
        main_page.click_submit_button()
        error_page = page.ResultsPage(browser)

        assert error_page.is_title_matches("400 Bad Request")

    def test_solution_result_with_with_intervals_element_start_or_end_less_then_0(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_text_intervals('[[-1, 2]]')
        main_page.fill_text_new_interval('[2, 4]')
        main_page.click_submit_button()
        error_page = page.ResultsPage(browser)

        assert error_page.is_title_matches("400 Bad Request")

    def test_solution_with_new_interval_length_equals_2(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_text_intervals('[[1, 5]]')
        main_page.fill_text_new_interval('[0, 4]')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.is_results_found()

    def test_solution_with_invalid_data(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_text_intervals('@!@#%&"')
        main_page.fill_text_new_interval('@!@#%&"')
        main_page.click_submit_button()
        error_page = page.ErrorPage(browser)

        assert error_page.is_title_matches("500 Internal Server Error")

