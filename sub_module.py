import logging

from error_scope import ActionBadDataFormat, ActionReauthNeeded


def main():
    for i in range(5):
        for exc_cls in [ActionBadDataFormat, ActionReauthNeeded]:
            try:
                raise exc_cls("raising error here")
            except:
                logging.exception("I survived that error")
