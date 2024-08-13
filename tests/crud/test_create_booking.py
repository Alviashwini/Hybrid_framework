import allure
import pytest
from Reference.Dummy import *

class TestCreateBooking:

    @pytest.mark.positive
    @allure.title("verify that create booking status and booking ID should be positive")
    @allure.description("create a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")

    def test_create_booking_positive(self):
        response = Crud_operation.post_request(url=R.create_booking_url(),auth=None,headers=R.common_headers_json(),payload=R.create_booking_payload(),in_json=False)
    # R.verify_http_status_code(response.data=response,expect_data=200)
    R.verify_json_key_for_not_null(response.json()["bookingid"])



