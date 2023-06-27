# Function to insert a string in middle of string
# 1.test_str and mid_str 2.split into temp 3.floor divide of middle portion 4.result=''.join[:middle]+mid+[middle]

test_str='Laughter is the midicine for heart'
mid_str='best'

temp=test_str.split()
middle_portion=len(temp)//2

result=' '.join(temp[:middle_portion]+[mid_str]+temp[middle_portion:])
print("Final String : " + str(result))