# APIConstants - class which contain all the endpoints
# keep the URLs

class APIConstants(object):
    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking"
    def base_url(self):
        return "https://restful-booker.herokuapp.com"
    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/apidoc/index.html#api-Auth"

    # update, put, patch, delete -booking id
    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking" + str(booking_id)