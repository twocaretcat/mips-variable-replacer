# MIPS Variable Replacer
# 2019 John Goodliff
# Mozilla Public License 2.0
# All rights reserved


import sys
from re import findall, search, split, sub


if __name__ == '__main__':
	register_regex = r'(?:zero|\d\d?|[vk][01]|a[0-3]|s[0-7]|t[0-9]|[gsf]p|ra)'
	args = len(sys.argv)


	def SortLen(val):
		return len(val[0])


	def Success(text):
		print('\n\33[92mSUCCESS:\033[0m', text, '\n')


	def Warn(text):
		print('\n\33[93mWARNING:\033[0m', text)


	def Error(text):
		print('\n\33[91mERROR:\033[0m', text)
		exit(1)


	if args == 2:
		f = open(sys.argv[1], 'r')
		code = f.read()
		f.close()

	elif args < 2:
		Error('Too few arguments. Please enter the name of the assembly file')

	else:
		Error('Too many arguments. Just enter the name of the assembly file')

	lines = split('(?:\r)?\n', sub('(?:(?:(?:\r)?\n)?#\$(?:(?:\r)?\n)?|# ?)', '', search('# ?MVR(?:.*\n)*# ?MVR', code).group(0)))
	code = sub('#\$(?:.*\n)*#\$\n*', '', code)
	key_values = []

	for i in lines:
		split_pairs = tuple(split('\: ?', i))

		if len(split_pairs) == 2:
			key_values.append(split_pairs)

	key_values.sort(key = SortLen, reverse = True)
	replacement_num = len(key_values)
	unused_flag = False
	bad_registers_flag = False
	bad_registers = []
	new_register_regex = '^' + register_regex

	for i in key_values:
		newcode = sub('\$' + i[0], '$' + i[1], code)

		if code == newcode:
			if not unused_flag:
				Warn('There are variables in the definitions that are never used')
				unused_flag = True

			print('  $' + i[0])

		if not search(new_register_regex, i[1]):
			if not bad_registers_flag:
				Warn('You are replacing with nonstandard registers. Make sure you meant to do this:')
				bad_registers_flag = True

			bad_registers.append('$' + i[1])
			print('  $' + i[1])

		if search('\$', i[1]):
			Error('Please remove all $ symbols from the definitions')

			print(i[1])

		code = newcode

	used_vars = findall('\$[\w\d]+', code)
	unused_vars = []
	new_register_regex = '\$' + register_regex

	for i in used_vars:
		if not search(new_register_regex, i) and i not in bad_registers:
			unused_vars.append(i)

	if unused_vars:
		Warn('There are variables not listed in the definitions. You may want to replace them:')

		for match in unused_vars:
			print(' ', match)

	if replacement_num == 0:
		Success('No variables to replace :)')

	else:
		Success(str(replacement_num) + ' variables replaced :)')

	f = open(sub('\.', '_c.', sys.argv[1]), 'w')
	f.write(code)
	f.close()
