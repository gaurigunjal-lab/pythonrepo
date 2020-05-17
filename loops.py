# Week 2 Programming Assignment
# Author : Gauri Gunjal

# Problem Statement 1


# Python function threesquares(m) that takes an integer m as input and returns True if m can be expressed as the sum of three squares and False otherwise.
def threesquares(m): 

    for i in range(0, m):

        for j in range(0, m):

            for k in range(0, m):

                # if checks sum of three squares
                if i*i + j*j + k*k == m:

                    return True

    return False

  
# Week 2 Programming Assignment
# Author : Gauri Gunjal

# Problem Statement 2

def repfree(s):
    
    # user input from s is stored in newlist
    newlist = []
    
    #Add each characters from s to newlist
    for i in range(0, len(s)):
        newlist.append(s[i])
        
    # create a distinct set of characters from newlist
    newlist2 = set(newlist)
    
    # check size of newlist2 with user entered string
    if len(newlist) == len(newlist2):
        return True
    else:
        return False
        
        
        
# Week 2 Programming Assignment
# Author : Gauri Gunjal

# Problem Statement 3

# core function
def hillvalley(seq):
    
    #we need 2 flags to know trends of going up or down
    down_trend, up_trend = False, False
    
    #need a counter to know when array switches the trend from up to down or vise versa
    switch_trend = 0
    
    #iterate the user inputs
    for i in range(len(seq)-1):
        if switch_trend > 1:
            # Early stop if there are more than 2 switches in the trend
            return False
        next_element = seq[i+1]
        current_element = seq[i]
        diff = next_element - current_element
        if diff > 0:
            if down_trend:
                switch_trend += 1
            up_trend = True
            down_trend = False
        elif diff < 0:
            if up_trend:
                switch_trend += 1
            down_trend = True
            up_trend = False
    if switch_trend == 1:
        return True
    return False	



