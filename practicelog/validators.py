from django.core.exceptions import ValidationError
from datetime import date, timedelta

def validate_date(date):
    if date > date.today() + timedelta(days=1):
        raise ValidationError("Your practice session can't be in the future")


def validate_duration(duration):
    if duration < 0:
        raise ValidationError("Practice has to last at least 1 minute")
    if duration > 360:
        raise ValidationError("Did you really practice for more than 6 hours? Try breaking up your practice for better results.")