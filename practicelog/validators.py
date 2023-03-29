from django.core.exceptions import ValidationError
from datetime import date, timedelta


def validate_date(date):
    """
    Validator to ensure provided date is not in the future
    """
    if date > date.today() + timedelta(days=1):
        raise ValidationError("Your practice session can't be in the future")


def validate_duration(duration):
    """
    Validator to ensure provided duration is between
    1 min and 6 hours (360 mins), inclusive
    """
    if duration < 0:
        raise ValidationError("Practice has to last at least 1 minute")
    if duration > 360:
        raise ValidationError(
            "Did you really practice for more than 6 hours? "
            "Try breaking up your practice for better results."
            )
