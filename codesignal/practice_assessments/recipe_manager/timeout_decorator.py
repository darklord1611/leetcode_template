"""
Timeout decorator for test cases.
Raises an exception if a test takes longer than the specified timeout.
"""
import signal
import functools


class TimeoutError(Exception):
    """Exception raised when a test exceeds its timeout."""
    pass


def timeout(seconds):
    """
    Decorator that raises a TimeoutError if the decorated function
    takes longer than `seconds` to execute.

    Args:
        seconds (float): Maximum execution time in seconds

    Returns:
        function: Decorated function with timeout enforcement

    Example:
        @timeout(0.4)
        def test_something(self):
            # Test code that must complete within 0.4 seconds
            pass
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def timeout_handler(signum, frame):
                raise TimeoutError(f"Test '{func.__name__}' exceeded timeout of {seconds} seconds")

            # Set up the signal handler
            old_handler = signal.signal(signal.SIGALRM, timeout_handler)
            # Schedule the alarm
            signal.setitimer(signal.ITIMER_REAL, seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                # Cancel the alarm and restore the old handler
                signal.setitimer(signal.ITIMER_REAL, 0)
                signal.signal(signal.SIGALRM, old_handler)

            return result

        return wrapper
    return decorator
