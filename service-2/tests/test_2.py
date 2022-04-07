def test_service_02():
	# test service two if the submitted value is integer
	res = app_2.test_client().get('/')
	assert type(res.data[0]) is int
