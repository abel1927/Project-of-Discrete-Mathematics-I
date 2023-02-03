import os

p = p = './tests/'
cases = os.listdir(p)

def check_case(exp_file, out_file):
    exp_lines = list(map(int,exp_file.readlines()))
    out_lines = list(map(int,out_file.readlines()))
    if len(out_lines) != len(exp_lines):
        return False, 'Wrong answer'
    count_test = 1
    for i in range(len(exp_lines)):
        a = int(exp_lines[i])
        b = int(out_lines[i])
        if a != b:
            return False, 'Wrong answer. Test ' + str(count_test)
        count_test = count_test+1
    return True, 'Accepted'



for file in cases:
    name,extension  = os.path.splitext(file)
    if extension != '.in':
        continue
    expected_file = open( p + name + 'expected.out','r')
    output_file = open(p + name + '.out', 'r')
    check, judgement = check_case(expected_file,output_file)
    print(f'{name} {judgement} ')