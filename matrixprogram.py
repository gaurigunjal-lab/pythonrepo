#Assignment : 3
#Author : Gauri Gunjal

# Problem statement:1
# Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the first occurrence of each number.

# Python code to remove duplicate elements 
def remdup(l): 
    final_list = [] 
    for num in l: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 


  
  #Assignment : 3
#Author : Gauri Gunjal

# Problem statement:2

#Write a Python function sumsquare(l) 


def sumsquare (l):
    
    E_sum, O_sum = 0, 0
    num = 0
      
    # using while loop      
    while(num < len(l)): 
          
        # checking condition 
        if l[num] % 2 == 0: 
            E_sum = E_sum + (l[num]*l[num])
        else: 
            O_sum = O_sum + (l[num]*l[num])
          
        # increment num  
        num += 1
        
    #print("Even numbers in the list: ", E_sum) 
    #print("Odd numbers in the list: ", O_sum)

    return  [ O_sum, E_sum ]
    
 


# Problem statement:3
#Author : Gauri Gunjal
# Write a Python function transpose(m). 

#*~~~~~~~~~~~~~~~~~~~~
#inputList [[1,2,3],[4,5,6]]
#inputList.len = 2
#inputList.element(1).len = 3 
#outputList.len =? = 3, How? <inputList.element(1).len>
#each element from output = size of inputList = <inputList.len>
#~~~~~~~~~~~~~~~~~~~~
#*/


def transpose(m):
    
    inputRows = len(m)
    inputCols = len(m[0])
    
    #print ("inputRows=", inputRows, " inputCols=", inputCols)
    #result = [[0]*inputRows]*inputCols
    result = [[0 for x in range(inputRows)] for y in range(inputCols)]
    #result = [[0,0,0,0],[0,0,0,0]]


    #print (len(result))

    # iterate through rows
    for i in range(len(m)):
         
        # iterate through columns
        for j in range(len(m[i])):
            #print ("m[",i,"],[",j,"] = " ,m[i][j])
            result[j][i] = m[i][j]
            #print ("result[",j,"],[",i,"] = " , result[j][i])
        
    

    return result
   

