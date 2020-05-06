from requests import Response

class AbstractResponse():
    def __init__(self, response):
        self._response = response
        
    def expect_success(self):
        self._expect_ok()
        self._expect_attribute('success',True)

    def _expect_ok(self):
        assert self._response.status == 200
    def _expect_attribute(self, attr, val):
        assert attr in self._response.json()
        assert self._response.json()[attr] == val
        return self
