

class AbstractRequest():
    def __init__(self):
        self._body = None
        self._pararms=None
        self._url = None
        self._name = None
        self._headers = None
    def send_request(self, api):
        pass
    def _post(self, api):
        pass
    def _delete(self, api):
        pass
    def _get(self, api):
        pass
        