import logging


from error_scope import gather_errors
from sub_module import main

with gather_errors() as seen_actions:
    try:
        main()
    except:
        logging.exception("error")
    finally:
        print("\ngot seen_actions from gather_errors...:", seen_actions)
