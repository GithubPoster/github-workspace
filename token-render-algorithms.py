def uuid4_token(times):
	from uuid import uuid4
	hash_set = set()
	crash_times = 0
	for i in range(times):
		token = uuid4().hex
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))



def b2a_base64_token(times):
	import os
	import binascii
	hash_set = set()
	crash_times = 0
	for i in range(times):
		token = binascii.b2a_base64(os.urandom(24))[:-1]
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))


def b2a_base64_token_ex(times):
	import os
	import binascii
	translations = [chr(_x) for _x in range(256)]
	translations[ord('/')] = '_'
	translations[ord('+')] = '-'
	translationstr = ''.join(translations)
	hash_set = set()
	crash_times = 0
	for i in range(times):
		token = (binascii.b2a_base64(os.urandom(24))[:-1]).translate(translationstr)
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))


def b2a_base64_token_ex_ex(times):
	import os
	import binascii
	hash_set = set()
	crash_times = 0
	for i in range(times):
		translations = [chr(_x) for _x in range(256)]
		translations[ord('/')] = '_'
		translations[ord('+')] = '-'
		translationstr = ''.join(translations)
		token = (binascii.b2a_base64(os.urandom(24))[:-1]).translate(translationstr)
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))


def b2a_base64_token_ex2(times):
	import os
	import binascii
	hash_set = set()
	crash_times = 0
	for i in range(times):
		token = (binascii.b2a_base64(os.urandom(24))[:-1]).replace('/','_').replace('+','-')
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))


def custom_random_choice_token(times):
	import random
	import string
	alphabet_digits = string.letters + string.digits
	hash_set = set()
	crash_times = 0
	for i in range(times):
		token = ''.join(random.choice(alphabet_digits) for _ in range(32))
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))


def use_sha1_token(times):
	import os
	from hashlib import sha1
	hash_set = set()
	crash_times = 0
	for i in range(times):
		token = sha1(os.urandom(24)).hexdigest()
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))


def use_base32_token(times):
	import os
	import base64
	hash_set = set()
	crash_times = 0
	for i in range(times):
		token = base64.b32encode(os.urandom(20))
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))


def use_base64_token(times):
	import os
	import base64
	hash_set = set()
	crash_times = 0
	for i in range(times):
		token = base64.b64encode(os.urandom(24), ['_','-'])
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))


def openssl_b2a_base64_random_token(times):
	import OpenSSL
	import binascii
	hash_set = set()
	crash_times = 0
	for i in range(times):
		token = binascii.b2a_base64(OpenSSL.rand.bytes(24))[:-1]
		if i == 1:
			print("token: %s, len: %d" % (token, len(token)))
		if token in hash_set:
			crash_times += 1
		hash_set.add(token)
	return (crash_times, len(hash_set))


def crash_testx(times, func):
	import time
	print('\r\n--------------------------------------------')
	print("test function: %s" % func.func_name)
	print("begin time: %s" % time.strftime('%Y%m%d %X'))
	begin_time = time.time()
	(crashed_times, hash_data_len) = func(times)
	print("end time: %s" % time.strftime('%Y%m%d %X'))
	print("take time:%s" % (time.time() - begin_time))
	print("test times: %d, crashed times:%d, hash data length:%d" % (times, crashed_times, hash_data_len))
	print('--------------------------------------------\r\n')



def crash_test(times, token_funcs):
	if isinstance(token_funcs, list):
		for f in token_funcs:
			crash_testx(times, f)
	else:
		crash_testx(times, token_funcs)


crash_test(10000000, [use_base64_token, use_base32_token, use_sha1_token,custom_random_choice_token, b2a_base64_token, b2a_base64_token_ex, b2a_base64_token_ex_ex, b2a_base64_token_ex2, uuid4_token, openssl_b2a_base64_random_token,])

# Test Result 0x01:
# --------------------------------------------
# test function: use_sha1_token
# token: bcd0134c3dfff27d67715c2abab55725f9c97831, len: 40
# take time:29.4249999523
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: custom_random_choice_token
# token: ZbsMocQ5DZshcQjSEMvpmxmicHijXHCO, len: 32
# take time:214.944000006
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: b2a_base64_token
# token: 4GgxAeYQ9JiTHNOo8ArcCsckoXmvUQas, len: 32
# take time:22.6069998741
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: uuid4_token
# token: 108f215c076e42938d34ab9d2b678717, len: 32
# take time:160.949999809
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------

# Test Result 0x02:
# --------------------------------------------
# test function: use_base64_token
# token: 93bbK_MbTNz98o-piyrdn0sPjZIohxxE, len: 32
# take time:68.3020000458
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: use_base32_token
# token: NVWSKJS237ZM6O7Z65SD2EAVE2QIFE5T2OMOI5U3, len: 40
# take time:103.411999941
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: use_sha1_token
# token: d5a36fd3767fbf578b0303b1a3d11537d5361413, len: 40
# take time:30.1319999695
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: custom_random_choice_token
# token: TOHarOS5jA0lDeF9FyyeFfsyXeQdKBd7, len: 32
# take time:218.799000025
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: b2a_base64_token
# token: 46oWXHHlGT/2jdV5Eft0mDP26SHfdA4z, len: 32
# take time:22.9439997673
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: uuid4_token
# token: 59027809b53e4a05bfc5abea0168d508, len: 32
# take time:160.842999935
# test times: 10000000, crashed times:0, hash data length:10000000


# test result 0x03
# --------------------------------------------
# test function: use_base64_token
# begin time: 20151107 17:02:18
# token: _I_-1bThWISFtIXKElgEFf3hih7LyKCC, len: 32
# end time: 20151107 17:03:24
# take time:66.4470000267
# test times: 10000000, crashed times:0, hash data length:10000000

# --------------------------------------------
# test function: use_base32_token
# begin time: 20151107 17:03:24
# token: MACVDACHU4FVLZSSVFQQVLSVC4HLDRI2B3PBEZQR, len: 40
# end time: 20151107 17:05:05
# take time:100.685000181
# test times: 10000000, crashed times:0, hash data length:10000000

# --------------------------------------------
# test function: use_sha1_token
# begin time: 20151107 17:05:05
# token: 701255920772ebbc3ff18186b0909ef94a678ba3, len: 40
# end time: 20151107 17:05:35
# take time:29.6259999275
# test times: 10000000, crashed times:0, hash data length:10000000

# --------------------------------------------
# test function: custom_random_choice_token
# begin time: 20151107 17:05:35
# token: ccdSU0CgdS0obZZuXI66MR0KaWPGJ8V0, len: 32
# end time: 20151107 17:09:11
# take time:216.281000137
# test times: 10000000, crashed times:0, hash data length:10000000

# --------------------------------------------
# test function: b2a_base64_token
# begin time: 20151107 17:09:11
# token: khLXftthmolwuCEhpUqFPabJbVOiyRKL, len: 32
# end time: 20151107 17:09:34
# take time:23.0020000935
# test times: 10000000, crashed times:0, hash data length:10000000

# --------------------------------------------
# test function: uuid4_token
# begin time: 20151107 17:09:34
# token: cf249b20faaa486ba50e801c9a4822d2, len: 32
# end time: 20151107 17:12:15
# take time:161.184999943
# test times: 10000000, crashed times:0, hash data length:10000000


# TEST RESULT 0x04
# crash_test(10000000, [use_base64_token,
# 						use_base32_token,
# 						use_sha1_token,
# 						custom_random_choice_token,
# 						b2a_base64_token,
# 						b2a_base64_token_ex,
# 						b2a_base64_token_ex_ex,
# 						b2a_base64_token_ex2,
# 						uuid4_token,
# 						openssl_b2a_base64_random_token,])
# --------------------------------------------
# test function: use_base64_token
# begin time: 20151108 11:09:26
# token: CBKCnoLqO2DyosrixcRk2dviPxfWj0RY, len: 32
# end time: 20151108 11:10:32
# take time:65.9289999008
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: use_base32_token
# begin time: 20151108 11:10:32
# token: QM7N3PKB5O2QCRIJC7MXQDTNCYS6VD4B, len: 32
# end time: 20151108 11:11:59
# take time:86.3580000401
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: use_sha1_token
# begin time: 20151108 11:11:59
# token: dc58549ae1a9b0fcb78b7e7f6e3ded45109d62e5, len: 40
# end time: 20151108 11:12:28
# take time:29.3980000019
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: custom_random_choice_token
# begin time: 20151108 11:12:28
# token: ZDNvD2adXyQpF7FAsTJU9Rt90cyFXZo1, len: 32
# end time: 20151108 11:16:03
# take time:214.484999895
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: b2a_base64_token
# begin time: 20151108 11:16:03
# token: qQSfWlu6gaFBGgN+HOKRIIZjGDHAxoUe, len: 32
# end time: 20151108 11:16:25
# take time:22.5640001297
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: b2a_base64_token_ex
# begin time: 20151108 11:16:25
# token: Rbh4NA6kvOZgfVQ7uOHo8biYCUXl-gwO, len: 32
# end time: 20151108 11:16:50
# take time:24.5349998474
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: b2a_base64_token_ex_ex
# begin time: 20151108 11:16:50
# token: FtsWrXtSJnqXfGI_vOK0YEFKhBY58fV3, len: 32
# end time: 20151108 11:23:28
# take time:398.623999834
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: b2a_base64_token_ex2
# begin time: 20151108 11:23:28
# token: QezsfWpFmbJ3vdQQMsp7iIeqALNcTlsF, len: 32
# end time: 20151108 11:23:56
# take time:27.271999836
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: uuid4_token
# begin time: 20151108 11:23:56
# token: 9ffa09413fb0472695ca55a6028a1719, len: 32
# end time: 20151108 11:26:35
# take time:159.762000084
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------


# --------------------------------------------
# test function: openssl_b2a_base64_random_token
# begin time: 20151108 11:26:35
# token: HFyWTzo2cGx+fA2S5bCfQtU422QXrPO7, len: 32
# end time: 20151108 11:27:37
# take time:61.1059999466
# test times: 10000000, crashed times:0, hash data length:10000000
# --------------------------------------------