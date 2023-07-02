import enum
import fnmatch
import urllib.request as urllib2

from django.core.validators import validate_email
from django.utils.dateparse import parse_date

from future.utils import raise_


class BioTypeEnum(enum.Enum):
    """
    Enum for bio types
    """
    FULLNAME = 'FULLNAME'
    EMAIL = 'EMAIL'
    PHONE = 'PHONE'
    DATEOFBIRTH = 'DATEOFBIRTH'
    AGE = 'AGE'
    WEBSITE = 'WEBSITE'

    @property
    def convert_value_method(self):
        # TODO: It's better to use phone number validator for phone number
        # TODO: past_date has a little issue
        if self.name in [self.AGE.name, self.PHONE.name]:
            return int
        elif self.name == self.FULLNAME.name:
            return str
        elif self.name == self.WEBSITE.name:
            return _site_checker
        elif self.name == self.EMAIL.name:
            return validate_email
        elif self.name == self.DATEOFBIRTH.name:
            return parse_date
        else:
            return lambda x: raise_(ValueError("Invalid type: '%(datatype)s'" % {'datatype': self.name}))


def _site_checker(url):
    url_chk = url.split('/')
    if fnmatch.fnmatch(url_chk[0], 'http*'):
        url = url
    else:
        url = f"http://{url}"

    try:
        urllib2.urlopen(url).read()
    except Exception:
        raise ValueError
