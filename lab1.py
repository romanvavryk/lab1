from tabulate import tabulate

f = [i.strip('\n').split(',') for i in open('data.txt')]

for i in range(0, 4):
	for j in range(0,3):
		f[i][j] = float(f[i][j])

for i in range(0,5):
	for j in range(0,1):
		f[i][j] = float(f[i][j])
print(tabulate([f], headers=['A1','A2','A3', 'Possibility', 'Optimism criteria'], tablefmt='orgtbl'))

res_of_method = []

def bayes():
	bayes_res = []
	res_list = []
	for i in range(0, 3):
		res_value = 0
		for j in range(0,3):
			value = f[i][j] * f[3][j]
			res_value += value
		
		res_list.append(res_value)

	max_value = max(res_list)
	max_value_index = 'A' + str(res_list.index(max_value) + 1)

	bayes_res.append(max_value)
	bayes_res.append(max_value_index)
	
	res_of_method.append(bayes_res)

def laplace():
	laplace_res = []
	res_list = []
	for i in range(0,3):
		res_value = sum(f[i])/3
		res_list.append(res_value)

	max_value = max(res_list)
	max_value_index = 'A' + str(res_list.index(max_value) + 1)

	laplace_res.append(max_value)
	laplace_res.append(max_value_index)

	res_of_method.append(laplace_res)

def valda():
	valda_res = []
	res_list = []
	for i in range(0,3):
		res_value = min(f[i])
		res_list.append(res_value)

	max_value = max(res_list)
	max_value_index = 'A' + str(res_list.index(max_value) + 1)

	valda_res.append(max_value)
	valda_res.append(max_value_index) 

	res_of_method.append(valda_res)

def hurtwits():
	hurtwits_res = []
	res_list = []
	opt_criteria = f[4][0]
	for i in range(0,3):
		res_value = opt_criteria * min(f[i]) + (1 - opt_criteria) * max(f[i])
		res_list.append(res_value)

	max_value = max(res_list)
	max_value_index = 'A' + str(res_list.index(max_value) + 1)

	hurtwits_res.append(max_value)
	hurtwits_res.append(max_value_index)

	res_of_method.append(hurtwits_res)

bayes()
laplace()
valda()
hurtwits()

print('\n')
print(tabulate([res_of_method], headers=['bayes','laplace','valda', 'hurtwits'], tablefmt='orgtbl'))