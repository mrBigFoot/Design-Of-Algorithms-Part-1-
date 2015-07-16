 
# Quick Sort  for Analysis of Algorithms (Part 1)
# Week 2 Programming Problem
# Count No of QuickSort comparisons for the following pivot rules
#               - Pick first
#               - Pick last
#               - Use median 3 rule

comparisons=0  # Number of comparisons
#pivotRule="MEDIAN"
import copy

def ChoosePivot(A,n): # choose pivot from elements of A
	global pivotRule
	# n is length of A
	if n==0 : return [[],-1]
	if pivotRule=="FIRST" :return [A[0],0]
	if pivotRule=="LAST": return [A[len(A)-1],len(A)-1]
	if pivotRule=="MEDIAN":# median of 3 pivot rule
		 first,last=0,n-1
		 if int(n/2.0)==n/2.0: #ie even
			mid=int(n/2.0)-1
		 else:
			mid=(n-1)/2
		 First,Mid,Last=A[first],A[mid],A[last]
		 c=sorted([First,Mid,Last])
		 if(c[1]==First):return [First,0]
		 if(c[1]==Mid):return [Mid,mid]
		 if(c[1]==Last):return [Last,last]

def Partition(A,l,r):

	# A is array, l is leftmost index, r is rightmost index
	#
	pivot=A[l]
	i=l+1
	for j in range(l+1,r+1):
		if A[j]<pivot:
			A[j],A[i]=A[i],A[j]
			i+=1
	A[l],A[i-1]=A[i-1],A[l] #replace pivot in correct position
	return i-1 # return correct position of pivot ie i-1

def QuickSort(A,n): # Quicksort array A of length n

	# Pivot selection is leftmost
	global comparisons

	if n==1 : return A
	[pivot,p]=ChoosePivot(A,n)
	if p!=0 : A[0],A[p]=A[p],A[0]
	p=Partition(A,0,n-1)
	if p>0:
		A[0:p]=QuickSort(A[0:p],p)
		comparisons+=(p-1)
	if (len(A)-p-1)>0:
		 A[p+1:len(A)]=QuickSort(A[p+1:len(A)],len(A)-p-1)
		 comparisons+=(len(A)-p-2)
	return A

def CompareRules(v):

	global comparisons
	global pivotRule

	rules=("FIRST","LAST","MEDIAN")

	x=copy.deepcopy(v)

	results={"FIRST":0,"LAST":0,"MEDIAN":0}

	for r in rules:
		pivotRule=r
		comparisons=len(x)-1
		QuickSort(x,len(x))
		results[r]=comparisons
		x=copy.deepcopy(v)

	print "Comparison counts by rule :-"
	for i in rules:
		print i+"  : \t\t"+str(results[i])
	print "end."

def main():
	fname='C:\\Users\\QuickSort.txt'
	with open(fname,'r') as f: 
   		v = [int(x) for x in f.read().splitlines()]
		f.close()
	#A=  [8, 10, 1, 9, 7, 2, 6, 3, 5, 4]
	CompareRules(v)
	#QuickSort(v,len(v))
	#QuickSort(A,len(A))
	#print A

if __name__ == '__main__':
    main()
