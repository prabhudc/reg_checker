
'''
regular expression checker
'''
import sys
import re
import os


v_regex_fname = os.getcwd()+"/"+"input_regex_"+sys.argv[1]+".txt"
v_pattern_fname = os.getcwd()+"/"+"Problem"+sys.argv[1]+".txt"


if(len(sys.argv) == 2 ):
	if(not(os.path.exists(v_regex_fname)) or not(os.path.exists(v_pattern_fname))):
		print("File name ain't correct")
		print(v_regex_fname)
		print(v_pattern_fname)
		exit
else:
	print("No input - Not cool, so not cool!")
	exit;

def f_check(regex):
	print(regex)
	v_flag = True;
	#Each line will be evaluated
	f_pattern = open(v_pattern_fname,"r+")
	for line in f_pattern:
		if(bool(re.match(r"^[#]",line)) or bool(re.match(r"[a-zA-Z\s]*:",line))):
			print("COMMENT : " + line)
		elif(bool(re.match(regex,str.replace(line,'\n','')))):
			print ("PASS : " + str.replace(line,'\n',''))
		else:
			print ("FAIL : " + str.replace(line,'\n',''))
			v_flag = False
	f_pattern.close()
	return(v_flag)



#Anticipate only one and that being the regular expression
f_regex = open(v_regex_fname,"r+")

print ( "Overall check status : " +	 str(f_check(f_regex.readline())) );
f_regex.close()


