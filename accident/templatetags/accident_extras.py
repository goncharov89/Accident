from django.utils import timezone
from django.template import Library

register = Library()

# return timedelta beetwen two dates
# TEMPLATE USE:  {{ date1|diff_date:date2 }}
# OR {{ accident.created_date|diff_date }} default date2 is now.


def diff_date(value, arg=None):

    if arg is None:
        time_end = timezone.now()
    else:
        time_end = arg

    time_begin = value
    on_delay = time_end - time_begin

    return on_delay


# Сделать вывод строки в красивом виде
register.filter('diff_date', diff_date)
