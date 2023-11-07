
from math import sqrt

def getNumbers() :
    nums = [] # start with an empty l i st
    # sent inel loop to get numbers
    xStr = input (" Enter a number ( <Enter> to quit ) >> ")
    while xStr != "" :
        x = float (xStr)
        nums.append (x) # add this value to the list
        print(xStr != "")
        xStr = input ( " Enter a number ( <Enter> to quit ) >> " )
    return nums


def mean (nums) :
    total = 0.0
    for num in nums :
        total = total + num
    return total / len(nums)
    

def stdDev (nums , xbar) :
    sumDevSq = 0.0
    for num in nums :
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt (sumDevSq/( len (nums ) - 1 ) )


def median (nums ) :
    nums.sort()
    size = len (nums )
    
    midPos = size // 2
    if size % 2 == 0 :
        med = (nums [midPos] + nums [midPos- 1] ) / 2.0
    else :
        med = nums [midPos]
    return med



def meanStdDev(nums):
    if not nums:
        return None
    xbar = mean(nums)
    std = stdDev(nums, xbar)
    return xbar, std



def main() :
    print ( " This program computes mean , median , and standard deviation . " )
    data = getNumbers()

    medStd = meanStdDev(data)

    #xbar = mean (data)
    #std = stdDev (data , xbar)
    #med = median (data)
    
    print ( " \nThe mean and standard deviation is " , medStd)
    #print ( " \nThe mean is " , xbar)
    #print ( " The standard deviat i on is " , std)
    #print ( " The median is " , med)

if __name__ == '__main__': main()


