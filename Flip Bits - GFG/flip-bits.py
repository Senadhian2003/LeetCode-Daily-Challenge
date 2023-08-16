#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        # Your code goes here
        mini = 0
        for i in a:
            if i == 1:
                mini+=1
        
        cnt = mini
        maxi = cnt
        for i in a:
            
            if i==1:
                cnt-=1
                
            elif i==0:
                cnt+=1
            
            
            if cnt>maxi:
                maxi = cnt
            
            if cnt < mini:
                cnt = mini
        return(maxi)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends