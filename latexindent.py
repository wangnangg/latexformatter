#! /usr/bin/python
import sys
import argparse
import re

parser = argparse.ArgumentParser(description='Format latex source code.');
parser.add_argument('sourcefile', 
                   help='file to be formatted');
parser.add_argument('-i', '--indent', type=int, default=4,
                   help='number of spaces for an indent.');

args = parser.parse_args();

#ferr = open('log.txt', 'w');


#this is not a pure function.
level = (  r'\begin',
		   r'\end',
		   r'\chapter',
		   r'\section',
		   r'\subsection',
		   r'\subsubsection');
stack = [];
level_depth = 0;
def update_level_depth(line):
	global level_depth, stack, level, ferr;
	leading_index = get_leading_index(line);
	if leading_index < 0:
		level_depth = len(stack);
		return None;
	leading = level[leading_index];
	if leading == r'\begin':
		stack.append(leading_index);
		level_depth = len(stack) - 1;
		return None;
	if leading == r'\end':
		while len(stack) > 0:
			if level[stack.pop()] == r'\begin':
				break;
		level_depth = len(stack);
		return None;
	
	if len(stack) == 0:
		stack.append(leading_index);
		level_depth = len(stack) - 1;
		return None;
	if leading_index == stack[-1]:
		level_depth = len(stack) - 1;
		return None;
	if leading_index > stack[-1]:
		stack.append(leading_index);
		level_depth = len(stack) - 1;
		return None;
	if leading_index < stack[-1]:
		while len(stack) > 0:
			if leading_index > stack[-1]:
				break;
			stack.pop();
		stack.append(leading_index);
		level_depth = len(stack) - 1;
		return None;

def get_leading_index(line):
	for i in range(0, len(level)):
		if line.startswith(level[i]):
			return i;
	return -1;

no_space = re.compile(r'\s*(.*)');
def main():
	global no_space, level_depth, args, ferr;
	fin = open(args.sourcefile, 'r');
	fout = sys.stdout;
	line = fin.readline();
	line_count = 1;
	while line:
		matched = no_space.match(line);
		if matched:
			line = matched.groups()[0];
			update_level_depth(line);
		
		fout.write(' ' * level_depth * args.indent);
		fout.write(line);
		fout.write("\n");

		#ferr.write('line:' + line+'\n');
		#ferr.write('line_count:' + str(line_count) +'\n');
		#ferr.write('stack: ' + str(stack)+'\n');
		#ferr.write('indent: ' + str(args.indent)+'\n');
		#ferr.write('depth: ' + str(level_depth)+'\n');
		#ferr.write('\n'*2);

		line = fin.readline();
		line_count += 1;

	fin.close();
	fout.close();
	#ferr.close();


if __name__ == '__main__':
	main();