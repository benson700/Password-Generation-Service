def test_service_04():
    # test service four in generating password
	passw = Password(password='1234567anyword')
	assert passw.password == '1234567anyword'
	assert type(passw.password) is str
	assert passw.password != None
