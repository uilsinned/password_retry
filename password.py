#密碼重試程式
#最多重試3次
password = 'a123456'
i = 3
while i > 0:
	p = input('請輸入密碼:')
	if p == password:
		print('登入成功')
		break
	else:
		i = i - 1
		if i > 0:
			print('密碼錯誤,還有', i, '次機會')
		else:
			print('game over')
			

