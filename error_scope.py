from contextlib import contextmanager
from collections import UserList


class _SeenErrors(UserList):
    "A list that behaves like a set"

    def append(self, item):
        if item in self.data:
            return
        return super().append(item)


_seen_errors = None


class _RootException(Exception):
    action_name = None

    def __new__(cls, *args, **kwargs):
        if _seen_errors is not None:
            if cls.action_name is None:
                raise AttributeError(
                    "_RootException requires all children to define action_name classs attribute")
            _seen_errors.append(cls.action_name)
        return super(_RootException, cls).__new__(cls, *args, **kwargs)


class ActionReauthNeeded(_RootException):
    action_name = "reauth_needed"


class ActionBadDataFormat(_RootException):
    action_name = "bad_data_format"


@contextmanager
def gather_errors():
    global _seen_errors
    _seen_errors = _SeenErrors()
    try:
        yield _seen_errors
    finally:
        _seen_errors = None
