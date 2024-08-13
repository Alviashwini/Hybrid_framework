from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils

import allure
import pytest
import openpyxl