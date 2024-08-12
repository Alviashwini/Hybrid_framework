import allure
import pytest

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("verify that create booking status and booking ID should be positive")
    @allure.description("create a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")

    def test_create_booking_positive(self):
        pass
