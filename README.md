# scope that gathers information about its inner errors

sometimes its useful to yield information about certain actions to be taken when you know about them at the origin of an error.

This repo contains a [error_scope module](./error_scope.py) that creates a context manager that gathers intel about events occuring in its inner scope and returns information about it afterwards

## usage

example (full code [here](./test.py)):

```python
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

```

output:

```bash
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionBadDataFormat: raising error here
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionReauthNeeded: raising error here
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionBadDataFormat: raising error here
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionReauthNeeded: raising error here
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionBadDataFormat: raising error here
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionReauthNeeded: raising error here
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionBadDataFormat: raising error here
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionReauthNeeded: raising error here
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionBadDataFormat: raising error here
ERROR:root:I survived that error
Traceback (most recent call last):
  File "PATHsub_module.py", line 10, in main
    raise exc_cls("raising error here")
error_scope.ActionReauthNeeded: raising error here

got seen_actions from gather_errors...: ['bad_data_format', 'reauth_needed']
```