from django.utils import timezone
from django.template import Library


register = Library()


def diff_date(value, arg=None):

    if arg is None:
        time_end = timezone.now()
    else:
        time_end = arg

    time_begin = value
    on_delay = time_end - time_begin

    return on_delay
#Сделать вывод строки в красивом виде

register.filter('diff_date', diff_date)
