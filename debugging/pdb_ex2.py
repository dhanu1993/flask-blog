import pdb
def add_one(num):
	res= num+1
	print(res)
	return res

def main():
	# pdb.set_trace()
	for num in range(0,10):
		add_one(num)

if __name__ == '__main__':
	main()