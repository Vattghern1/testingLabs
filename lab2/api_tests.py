import pytest

from lib.api import *


class TestHttpBaseChecks:
    def test_http_ok_on_default_page(self):
        assert get_form().status_code == 200

    def test_http_ok_on_results_page(self):
        assert post_form('[[1,2],[3,5],[6,7],[8,10],[12,16]]', '[4,8]').status_code == 200

    def test_http_result_page_not_empty(self):
        assert post_form('[[1,2],[3,5],[6,7],[8,10],[12,16]]', '[4,8]').text != ''

    def test_http_form_page_not_empty(self):
        assert get_form().text != ''

    def test_http_form_page_content_type(self):
        assert get_form().headers['Content-Type'] == 'text/html; charset=utf-8'

    def test_http_result_page_content_type(self):
        assert post_form('[[1,2],[3,5],[6,7],[8,10],[12,16]]', '[4,8]').headers['Content-Type'] == 'text/plain; charset=utf-8'

    def test_http_404_on_nonexistent_url(self):
        assert get_page('dfjksgjkbnsdfgnjkdfgs').status_code == 404

    def test_http_post_form_with_extra_fields(self):
        data = {
            'invervals': '[[1,2],[3,5],[6,7],[8,10],[12,16]]',
            'newInterval': '[4,8]',
            'jklnsdfgjklnsdfb': 1,
            2: 3
        }
        assert post_data('/result', data=data).status_code == 400

    def test_http_get_with_authentication_header(self):
        headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIxMDc2ODQud"
                                    "2ViLmhvc3RpbmctcnVzc2lhLnJ1IiwiZXhwIjoxNjgwMDA5Nzk1LCJLRVl"
                                    "fQ0xBSU1fVVNFUiI6ImI5NTVkYzBlLWJmNTEtNDRhNy05ZWIxLTZmN2ZlY"
                                    "zk0YTI2YiJ9.sp9WP7T-yHZaujk2n-k-cAJip0QeRKuHTVRPhuaElzE"
                   }
        assert get_page('/', headers).status_code == 200


class TestErrorResponses:
    def test_400_with_too_long_input_list(self):
        intervals = [[1, 2]] * 10001
        newInterval = [2, 4]
        assert post_form(intervals, newInterval).status_code == 400

    def test_400_with_new_interval_length_less_then_2(self):
        intervals = [[1, 5]]
        newInterval = [0]

        assert post_form(intervals, newInterval).status_code == 400

    def test_400_with_new_interval_length_more_then_2(self):
        intervals = [[1, 5]]
        newInterval = [0, 2, 5]

        assert post_form(intervals, newInterval).status_code == 400

    def test_400_with_intervals_element_length_greater_than_2(self):
        intervals = [[1, 7, 9]]
        newInterval = [2, 4]

        assert post_form(intervals, newInterval).status_code == 400

    def test_400_with_intervals_element_length_less_than_2(self):
        intervals = [[1]]
        newInterval = [2, 4]

        assert post_form(intervals, newInterval).status_code == 400

    def test_400_with_intervals_element_start_or_end_less_then_0(self):
        intervals = [[-1, 2]]
        newInterval = [2, 4]

        assert post_form(intervals, newInterval).status_code == 400

    def test_400_with_intervals_element_start_or_end_greater_then_100000(self):
        intervals = [[100001, 100001]]
        newInterval = [2, 4]

        assert post_form(intervals, newInterval).status_code == 400

    def test_400_with_new_intervals_element_start_or_end_greater_then_100000(self):
        intervals = [[2, 4]]
        newInterval = [100001, 100001]

        assert post_form(intervals, newInterval).status_code == 400

    def test_400_with_empty_lists(self):
        intervals = [[]]
        newInterval = []

        assert post_form(intervals, newInterval).status_code == 400



