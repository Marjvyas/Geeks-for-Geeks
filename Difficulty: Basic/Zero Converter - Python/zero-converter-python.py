#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def pos(n):
    n-=1
    while n>=0:
        print(n, end=' ')
        n-=1
    ## Write the code
    
    
def neg(n):
    while n<=0:
        print(n,end=' ')
        n+=1
    ##Write the code
    

#{ 
 # Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n = int(input())
        if(n > 0):
            pos(n)
        elif(n < 0):
            neg(n)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        


        print("~")
if __name__=='__main__':
    main()
# } Driver Code Ends