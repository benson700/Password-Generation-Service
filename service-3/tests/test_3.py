def test_service_03():
    # test service three if it gives the character
	res = app_3.test_client().get('/')
	assert type(res.data[0]) is str