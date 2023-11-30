import errno
import os
import signal
import functools
import multiprocessing
import contextlib
import traceback

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

@contextlib.contextmanager
def time_limit(seconds: float):
    def signal_handler(signum, frame):
        raise TimeoutError("Timed out!")
    signal.setitimer(signal.ITIMER_REAL, seconds)
    signal.signal(signal.SIGALRM, signal_handler)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        
class Process(multiprocessing.Process):

    def __init__(self, *args, **kwargs):
        multiprocessing.Process.__init__(self, *args, **kwargs)
        self._pconn, self._cconn = multiprocessing.Pipe()
        self._exception = None

    def run(self):
        try:
            multiprocessing.Process.run(self)
            self._cconn.send(None)
        except Exception as e:
            tb = traceback.format_exc()
            self._cconn.send((e, tb))
            #raise e  # You can still rise this exception if you need to

    @property
    def exception(self):
        if self._pconn.poll():
            self._exception = self._pconn.recv()
        return self._exception

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
    if process.exception:
        raise Exception(process.exception)
    if process.is_alive():
        process.terminate()
    if process.exitcode is None:
        raise TimeoutError("Timeout")
