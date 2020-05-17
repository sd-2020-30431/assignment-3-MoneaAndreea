from BusinessLayer.User import check_account
from Commands.EventHandler import EventHandler
from DataAccess.DBConnectionUser import insert_into_database
from Models.User import User


class CreateUserCommand(EventHandler):
    def handle(self, message):
        method = self._get_handle_method(message)
        if method:
            return method(message)

    def can_handle(self, message):
        if isinstance(message, str):
            method = getattr(self, 'handle_' + message)
            return method != None and callable(method)
        return self._get_handle_method(message) != None

    def _get_handle_method(self, message):
        try:
            method = getattr(self, self._get_handle_method_name(message), None)
        except AttributeError:
            return None
        else:
            if callable(method):
                return method
            else:
                return None



