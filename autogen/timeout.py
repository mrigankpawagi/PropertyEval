import errno
import os
import signal
import functools
from multiprocessing import Process

class TimeoutError(Exception):
    pass

def timeout(seconds=0.3, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            # signal.alarm(seconds)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorator

def run_with_timeout(timeout, function, *args, **kwargs):
    """
    Run a function with a timeout. If the function does not complete within the timeout, it is terminated.
    :param timeout: The timeout in seconds.
    :param function: The function to run.
    :param args: The positional arguments to pass to the function.
    :param kwargs: The keyword arguments to pass to the function.
    """
    process = Process(target=function, args=args, kwargs=kwargs)
    process.start()
    process.join(timeout=timeout)
    if process.is_alive():
        process.terminate()
    if process.exitcode is None:      
        print("Timeout!") 
        raise TimeoutError("Timeout")
