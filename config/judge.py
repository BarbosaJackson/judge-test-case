from config.create import *
from config.formatter import *
def compare_tests(filename, ext):
	ans = COLOR['BOLD'] + COLOR['WHITE_BACKGROUND']
	text = insert_spaces(ans + COLOR['BLACK'] + "| FILE: " + filename + ext)
	print(text)
	suite_a = get_suite_test(filename + '_user_out')
	suite_b = get_suite_test(filename + '_judge_out')
	for i in range(len(suite_a)):		
		if(suite_a[i] == suite_b[i]):
			print(insert_spaces(ans + COLOR['GREEN'] + '| Case #' + str(i + 1) + ': ACCEPTED'))
		else:
			print(insert_spaces(ans + COLOR['RED'] + '| Case #' + str(i + 1) + ': WRONG ANSWER'))

def compile_arq(filename, ext):
	os.system('g++ ' + filename + ext + ' -o ' + filename + ' -lm')

def get_suite_test(filename):
	suite_test = []
	outputs = open(filename)
	for output in outputs:
		suite_test.append(output)
	return suite_test

def run_test_case(filename, ext):
	os.system('./' + filename + ' < ' + filename + '_inp' + ' > ' + filename + '_user_out')
	compare_tests(filename, ext)