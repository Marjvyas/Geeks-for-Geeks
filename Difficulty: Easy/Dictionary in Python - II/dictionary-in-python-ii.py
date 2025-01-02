#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


# Function to check if pair
# with given sum exists
def pair_sum(dict, N, arr, sum):
    for i in arr:
        complement=sum-i
        if complement in dict.keys():
            if complement==i and dict[i]>1:
                return True
            if complement!=i:
                return True
        else:
            continue
    return False
        
#{ 
 # Driver Code Starts.
# Driver code
def main():
    
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        N = int(input())
        sum = int(input())
        dict = {}
        x = N
        arr = [int(i) for i in (input().split())]
        
        for i in arr:
            dict[i] = 0
                
        for i in arr:
            dict[i] +=1
    
        if pair_sum(dict, N, arr, sum) is True:
            print ("Yes")
        else:
            print ("No")
        print("~")
        testcase -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends