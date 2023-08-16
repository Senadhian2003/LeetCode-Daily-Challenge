#User function Template for python3

class Solution:
	def singleNumber(self, nums):
	    
		# Code here
		l=[]
		h={}
		for i in nums:
		    if i in h:
		        
		        h[i]+=1
            else:
		        h[i]=1
        for i in h:
            
            if h[i]==1:
                l.append(i)
        l.sort()
         
        # for i in l:
        #     print(i,end=" ")

        return l
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends