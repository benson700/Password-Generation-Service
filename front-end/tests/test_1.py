# from . import app_1
from service_01 import app as app_1
from service_02 import app as app_2
from service_03 import app as app_3
from service_04 import app as app_4

from models import Password, Digit


def test_service_01():
	# test service one if it give the right template
	res = app_1.test_client().get('/')
	assert res.status_code == 200
	assert b"password" in res.data