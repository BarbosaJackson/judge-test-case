COLOR = {
	'RED': '\033[31m', 
	'GREEN': '\033[32m',
	'BLUE': '\033[33m',
	'BLACK': '\033[30m',
	'WHITE':'\033[37m',
	'BOLD': '\033[1m',
	'WHITE_BACKGROUND': '\033[47m',
	'ORIGINAL_COLOR': '\033[0;0m'
}

def insert_spaces(current_text):
	maxN = 80
	final_text = current_text
	pos = len(current_text)
	while(pos <= maxN):
		final_text += ' '
		pos += 1
	final_text += '|' + COLOR['ORIGINAL_COLOR']
	return final_text