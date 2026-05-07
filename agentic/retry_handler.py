import time
from functools import wraps


def retry_on_failure(retries=3, delay=2):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(retries):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    last_exception = e

                    print(f"[RETRY] Attempt {attempt + 1} failed")

                    time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator