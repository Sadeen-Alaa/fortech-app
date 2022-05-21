from django.shortcuts import redirect
from functools import wraps
from urllib.parse import urlparse
from django.conf import settings
from django.shortcuts import resolve_url

from Website import views


def user_passes_test(test_func=None, login_url=None):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            print(request.session)
            print(test_func(request.session))
            if test_func(request.session):
                return view_func(request, *args, **kwargs)
            return redirect(login_url)
        return _wrapped_view
    return decorator


def login_session_required(test_func=None, login_url=None):
    actual_decorator = user_passes_test(
        lambda session: session.get('email'),
        login_url='signin'
    )
    if test_func:
        return actual_decorator(test_func)
    return actual_decorator
