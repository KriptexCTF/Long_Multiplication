def calk(a, b_number):
	flag10 = 0
	result = ""
	for i in range(len(a)):
		numb_a = int(a[len(a)-i-1])
		proiz = numb_a * b_number
		if(flag10 != 0):
			proiz += flag10
			flag10 = 0
		if((proiz >= 10) and (i != len(a)-1)):
			flag10 = int(proiz / 10)
			proiz %= 10
		result += str(proiz)[::-1]
	return result[::-1]
def final_summ(arr_summ):
	summ = ""
	number = 0
	flag10 = 0
	max_columns = len(arr_summ[0])-1
	for i in range(max_columns):
		for j in range(len(arr_summ)):
			try:
				number += int(arr_summ[j][max_columns-i-1])
				if(flag10 != 0):
					number += flag10
					flag10 = 0
			except ValueError:
				continue
		if((number >= 10) and (i != max_columns)):
			flag10 = int(number / 10)
			number %= 10
		if((flag10 != 0) and (i == max_columns-1)):
			number += flag10
			flag10 = 0
		summ += str(number)[::-1]
		number = 0
	return(summ[::-1])
try:
	a = str(float(input("Enter first number: ").replace(',','.')))
	b = str(float(input("Enter second number: ").replace(',','.')))
except ValueError:
	print("Not number!")
	exit()
except KeyboardInterrupt:
	print("\nExit")
	exit()
if(len(a) < len(b)):a, b = b, a
otstup = len(a) + len(b) - 2
print(' '*(otstup-len(a)) + a + '\n*' + ' '*(otstup-len(b)-1) + b + '\n' + '-'*(otstup))
number_float = len((a.split('.'))[1])+len((b.split('.'))[1])
a, b = a.replace('.',''), b.replace('.','')
arr_result = []
for i in range(len(b)):
	q = len(b) - i - 1
	res = calk(a, int(b[q]))
	qwe = (' '*(otstup-len(res)-i) + res + ' ')
	if(arr_result != []):
		qwe += ' '*(len(arr_result[0])-len(qwe))
	arr_result.append(qwe)
	print(qwe)
print('-'*(otstup))
answer = ""
result = final_summ(arr_result)
for i in range(len(result)):
	if(i == len(result) - number_float):
		answer += '.' + result[i]
	else:
		answer += result[i]
print(float(answer))	
