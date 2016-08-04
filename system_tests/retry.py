import time
from functools import wraps

import six


def _retry_all(_):
    """Retry all caught exceptions."""
    return True


class RetryBase(object):
    """Base for retrying calling a decorated function w/ exponential backoff.

    :type max_tries: int
    :param max_tries: Number of times to try (not retry) before giving up.

    :type delay: int
    :param delay: Initial delay between retries in seconds.

    :type backoff: int
    :param backoff: Backoff multiplier e.g. value of 2 will double the
                    delay each retry.

    :type logger: logging.Logger instance
    :param logger: Logger to use. If None, print.
    """
    def __init__(self, max_tries=4, delay=1, backoff=2, logger=None):
        self.max_tries = max_tries
        self.delay = delay
        self.backoff = backoff
        self.logger = logger.warning if logger else six.print_


class RetryErrors(RetryBase):
    """Decorator for retrying given exceptions in testing.

    :type exception: Exception or tuple of Exceptions
    :param exception: The exception to check or may be a tuple of
                      exceptions to check.

    :type error_predicate: function, takes caught exception, returns bool
    :param error_predicate: Predicate evaluating whether to retry after a
                            caught exception.

    :type max_tries: int
    :param max_tries: Number of times to try (not retry) before giving up.

    :type delay: int
    :param delay: Initial delay between retries in seconds.

    :type backoff: int
    :param backoff: Backoff multiplier e.g. value of 2 will double the
                    delay each retry.

    :type logger: logging.Logger instance
    :param logger: Logger to use. If None, print.
    """
    def __init__(self, exception, error_predicate=_retry_all,
                 max_tries=4, delay=1, backoff=2, logger=None):
        super(RetryErrors, self).__init__(max_tries, delay, backoff, logger)
        self.exception = exception
        self.error_predicate = error_predicate

    def __call__(self, to_wrap):
        @wraps(to_wrap)
        def wrapped_function(*args, **kwargs):
            tries = 0
            while tries < self.max_tries:
                try:
                    return to_wrap(*args, **kwargs)
                except self.exception as caught_exception:

                    if not self.error_predicate(caught_exception):
                        raise

                    delay = self.delay * self.backoff**tries
                    msg = ("%s, Trying again in %d seconds..." %
                           (caught_exception, delay))
                    self.logger(msg)

                    time.sleep(delay)
                    tries += 1
            return to_wrap(*args, **kwargs)

        return wrapped_function


class RetryResult(RetryBase):
    """Decorator for retrying based on non-error result.

    :type result_predicate: function, takes result, returns bool
    :param result_predicate: Predicate evaluating whether to retry after a
                             result is returned.

    :type max_tries: int
    :param max_tries: Number of times to try (not retry) before giving up.

    :type delay: int
    :param delay: Initial delay between retries in seconds.

    :type backoff: int
    :param backoff: Backoff multiplier e.g. value of 2 will double the
                    delay each retry.

    :type logger: logging.Logger instance
    :param logger: Logger to use. If None, print.
    """
    def __init__(self, result_predicate,
                 max_tries=4, delay=1, backoff=2, logger=None):
        super(RetryResult, self).__init__(max_tries, delay, backoff, logger)
        self.result_predicate = result_predicate

    def __call__(self, to_wrap):
        @wraps(to_wrap)
        def wrapped_function(*args, **kwargs):
            tries = 0
            while tries < self.max_tries:
                result = to_wrap(*args, **kwargs)
                if self.result_predicate(result):
                    return result

                delay = self.delay * self.backoff**tries
                msg = "%s. Trying again in %d seconds..." % (
                    self.result_predicate.__name__, delay,)
                self.logger(msg)

                time.sleep(delay)
                tries += 1
            return to_wrap(*args, **kwargs)

        return wrapped_function


class RetryInstanceState(RetryBase):
    """Decorator for retrying based on instance state.

    :type instance_predicate: function, takes instance, returns bool
    :param instance_predicate: Predicate evaluating whether to retry after an
                               API-invoking method is called.

    :type max_tries: int
    :param max_tries: Number of times to try (not retry) before giving up.

    :type delay: int
    :param delay: Initial delay between retries in seconds.

    :type backoff: int
    :param backoff: Backoff multiplier e.g. value of 2 will double the
                    delay each retry.

    :type logger: logging.Logger instance
    :param logger: Logger to use. If None, print.
    """
    def __init__(self, instance_predicate,
                 max_tries=4, delay=1, backoff=2, logger=None):
        super(RetryInstanceState, self).__init__(
            max_tries, delay, backoff, logger)
        self.instance_predicate = instance_predicate

    def __call__(self, to_wrap):
        instance = to_wrap.__self__   # only instance methods allowed

        @wraps(to_wrap)
        def wrapped_function(*args, **kwargs):
            tries = 0
            while tries < self.max_tries:
                result = to_wrap(*args, **kwargs)
                if self.instance_predicate(instance):
                    return result

                delay = self.delay * self.backoff**tries
                msg = "%s. Trying again in %d seconds..." % (
                    self.instance_predicate.__name__, delay,)
                self.logger(msg)

                time.sleep(delay)
                tries += 1
            return to_wrap(*args, **kwargs)

        return wrapped_function
