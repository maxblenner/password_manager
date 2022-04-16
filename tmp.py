# from collections import ChainMap
data = [{'AccountID': 1, 'Acc_name': 'admin2', 'Acc_pw': 'admin                                                   admin2  ', 'Acc_email': 'admin@gmail.com'}, {'AccountID': 2, 'Acc_name': 'Furkan', 'Acc_pw': 'Gormez                                                          ', 'Acc_email': 'furkan.gormez@gmail.com'}, {'AccountID': 3, 'Acc_name': 'Shakti', 'Acc_pw': 'Sikka                                                           ', 'Acc_email': 'shakti.sikka@gmail.com'}, {'AccountID': 5, 'Acc_name': 'test', 'Acc_pw': 'test                                                            ', 'Acc_email': 'testing@gmail.com'}, {'AccountID': 7, 'Acc_name': 'test', 'Acc_pw': 'test                                                            ', 'Acc_email': 'test'}, {'AccountID': 8, 'Acc_name': 'xyz', 'Acc_pw': 'xyz                                                             ', 'Acc_email': 'admin'}, {'AccountID': 9, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 10, 'Acc_name': 'admin2', 'Acc_pw': 'admin2                                                          ', 'Acc_email': 'admin2@gmail.com'}, {'AccountID': 11, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 12, 'Acc_name': 'admin2', 'Acc_pw': 'admin2                                                          ', 'Acc_email': 'admin2@gmail.com'}, {'AccountID': 13, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 14, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 15, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 16, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 17, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 18, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 19, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 20, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}, {'AccountID': 21, 'Acc_name': 'admin', 'Acc_pw': 'admin                                                           ', 'Acc_email': 'adm@gmail.com'}]

# file = open("userData.txt", "w")
def fetchData(arg):
	asd = "SELECT * FROM password WHERE AccountID = arg"
	return asd.fetchall()

name = 'Shakti'
for dic in db:
	for key in dic:
		if dic[key] == name:
			# SELECT Acc_pass WHERE Acc_name = name
			pas = "Shakti"
			acId = dic["AccountID"]
			if password == pas:
				print("Login Success")
				fetchData(acId)

# file.close()