from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def jobseeker_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorators = user_passes_test(
        lambda u : u.is_active and u.is_jobseeker,
        login_url=login_url,
        redirect_field_name=REDIRECT_FIELD_NAME
    )
    if function:
        return actual_decorators(function)
    return actual_decorators


def employer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorators = user_passes_test(
        lambda u : u.is_active and u.is_employer,
        login_url=login_url,
        redirect_field_name=REDIRECT_FIELD_NAME
    )

    if function:
        return actual_decorators(function)
    return actual_decorators