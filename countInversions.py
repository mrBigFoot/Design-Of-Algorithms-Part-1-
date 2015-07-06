

## Assignment 1

# counting inversions in O(n*logn) time

# This is a non-recursive version of counting
# the number of inversions in x

# An inversion occurs when elements a and b are such that
# a>b but a occurs before b in the ordered list

inversions=0 # global variable stores count of inversions found in x

# mergeSort returns sorted x

def mergeSort(x):
	bucket=1
	while(True):
		print "bucket size "+str(bucket)
		for i in range(0,len(x)-bucket+1,bucket*2):

			x[i:i+2*bucket]=merge(x[i:i+bucket],x[i+bucket:i+2*bucket])
		if bucket*2>=len(x): break
		bucket*=2
	return x

def merge(A,B): # return C
	global inversions
	C=[]
	bp=0 # B pointer
	ap=0 # A pointer
	while(True):
		if ap==len(A) and bp<len(B):
			C+=B[bp:]
			break
		if bp==len(B) and ap<len(A):
			C+=A[ap:]
			break
		if bp==len(B) or ap==len(A):
			break
		if A[ap] < B[bp]:
			#inversions+=1
			C+=[A[ap]]
			ap+=1
		else:
			C+=[B[bp]]
			inversions+=(len(A)-ap)
			bp+=1
	return C

def checkInversions(x):
	inCount=0
	for i in range(0,len(x)-1):
		for j in range(i+1,len(x)):
			if x[i]>x[j]: inCount+=1
	print inCount

def main():
	f = open('fileName.txt', 'r') # contains large list of numbers
	v=f.read()
	v=v.replace('\n',',')
	v=v[:-1]
	v=v.split(',')
	v=map(int,v)
	f.close()

 	mergeSort(v)
	print "number of inversions : ",inversions
	#checkInversions(v)

if __name__ == '__main__':
    main()
