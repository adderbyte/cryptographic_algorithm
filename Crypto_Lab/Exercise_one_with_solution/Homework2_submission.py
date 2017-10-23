
# coding: utf-8

# ##  HOMEWORK 2

# ##  Exercise 2 

# In[2]:

n2=6518794751213912339554398226798855884842134115176146907514831965664129856392796248640865436554888615351152669908027069349565406296496650618175914124126297683347000487881209530373473
p21=3673416836971456525081559090170129524369019417597601004252642294866558863644012254956864739
p22=1836708418485728262540779545085064762184509708798800502126321147433279431822006127478432369
q21=1774586179712815748621681089129657600838739131155547222508971439586183672551879789643977707
q22=887293089856407874310840544564828800419369565577773611254485719793091836275939894821988853
g2=4947913844771620965646012205688441693970892381656556732140228785819676393977177142973812374964019499507551137737775475470100495258532024321211310429705917209270743631111412049330727


# ### Organise Parameters in a dictionary

# In[3]:

# Put parameters neatly in a dictionary
parameter_values = [n2,p21,p22,q21,q22,g2]
parameter_names = ["n2","p21","p22","q21","q22","g2"]
parameter_dict = dict( zip(parameter_names, parameter_values ) )


# In[4]:

for key in parameter_dict:
    print  'Is',  key, 'prime: ',  is_prime(parameter_dict[key])


# In your parameter file, you will find six integers n2, p21, p22, q21, q22 and g2 where g2 ∈ Z∗n2 , n2 = p21q21, p21 = 2p22 +1 and q21 = 2q22 +1. Find the order of g2 in Z∗n2 and write it under Q2 in your answer file.
# 

# In[5]:

print "Verify that n2= p21q21: " , n2 == p21 * q21


# In[6]:

# Since n2 = p21 * q21 and (p21 * q21 ) are prime
# Then the totient function is easy to compute 
# eu = (p21-1)(q21-1)

multiplicative_group_order = ((p21)-1)*((q21)-1)


# In[7]:

power_mod(g2,multiplicative_group_order,n2) # order of group verification
                                            # this returns one  verifying that g is an 
                                            # element of the group. This is because
                                            # its order 
                                            # should  be a factor of Group order.
                                            # ie # Order_group = k * order_of_g2
                                            # Or # order_of_g2 | Order_of_goup = k
                                        
    


# In[43]:

# The order of g2 should be a factor of multiplicative_group_order
# multiplicative_group_order= (p21-1)*(p22-1) =  (2p22+1-1)(2q22+1 -1) =  (2p22)(2q22)
# the factors of multiplicative_group_order are likely 2,4,2p22,2q22,4q22,4p22, q22 , q22,  (p22)(q22),4(p22)(q22)
# We pick the one that satisfies the condition g^k = 1 
# where k is an element of the factors


# In[9]:

order_check_list = [2,4, p22,q22,2*p22,2*q22,4*q22,4*q22,p22*q22,2*p22*q22,4*p22*q22 ] # list of factors of order of group 
order_names = ["2","4","p22","q22","2*p22","2*q22","4*p22","4*q22","p22*q22","2*p22*q22","4*p22*q22"]
order_dict = dict( zip(order_names, order_check_list ) )


# In[10]:

collector =[];
def order_of_g2_checker(order_dict,g2,n):
    '''
    Input: takes dictionary consisting
    of factors of order of group.
    and n2
    
    Output: returns the one satisfying 
    the condition that g2^k = 1
    
    '''
    for key in order_dict: 
        check = power_mod(g2,order_dict[key] ,n2)
        if check == 1:
            collector.append(key)
        else:
            continue
    return collector
                
            


# In[11]:

collector_ =   order_of_g2_checker(order_dict,g2,n2)


# In[ ]:




# In[15]:

print "all possible orders of g3",collector # show all factors equal


# In[17]:

print "We pick the minimum in the list ", order_dict["p22*q22"] , " ...since it is the smallest"


# In[ ]:




# # Exercise 1

# In[126]:

m11=2185009518812470266713980977591672001160104495906570899359329
m12=2829959501808824818968744543479596214902066890103603571190716
m13=2488773373073389824855058953944254285681363869733847010919619
m14=2903351574709552337015521886268657163608579148088889492054438
y11=162935749620444109872969676628557735855110794156738574730650631401980798927788880114037073383960432013291662159000
y12=180577856212268044905453951265943881014496973360420348707851024424113074719291223358677360479872565409018007799200
w1=118674347160075300731294
u1=1292323405965699583332436


# In[127]:

# Construct a matrix 
M =matrix(ZZ,[[m11,m12],[m13,m14]])


# In[128]:

# Construct y matrix
Y =matrix(ZZ,[[y11],[y12]])


# In[129]:

# compute M inverse
M_inverse = M.inverse()


# In[130]:

# Confirm  M_inverse 
print "Confirm the inverse: \n", M_inverse * M


# In[131]:

# Compute Q and Q_inverse
Q =  M_inverse * Y


# In[132]:

# Verify Q is correct. 
# Using M* Q should return true 

M * Q == Y 


# In[133]:

Q1a1 = 54296442266677581446281052516352573191115346750662600;
Q1a2 = 15653053127363916075896277170178676443530012934737100


# In[134]:

Q1b = gcd(Q1a1,Q1a2)


# In[135]:

print "the gcd  is : " , Q1b


# ### Task 2

# In[136]:

# w1 . z1 ≡ u1 (mod Q1b)
# We can use the theorems
# Important theorem :
# Theorem 1: If ac ≡ bc (mod m) and gcd(c, m) = 1, then a≡b (modm).
#  Theorem 2: If ac ≡ bc (mod m) and gcd(c, m) = d, then a ≡ b (mod (m/d))
# m/d and c/d are relatively prime are relatively prime from theorem 1


# In[137]:

######## Solution exist ########
# Similar to the question on exercise requirement test.
# We can compute the gcd of (Q1b, w1 )
# Then verify that, this   divides u1
print "gcd of Q1b and w1 ", gcd(Q1b, w1) 
print "gcd of Q1b and w1 divides u1. The remainder of u1 mod 2 is zero :", mod(u1,2)


# In[138]:

# Follwoing theorem 1
########################
# compute gcd of (u1,w1)


# In[139]:

print "greatest common factor of u1 and w1: ", gcd(u1,w1);


# In[140]:

# Using theorem 2 #
#########################
# Check if gcd of 2 and Q1b is one


# In[141]:

print "The gcd of 2 and Q1b is : ", gcd(Q1b,2)


# In[142]:

# Then confirm gcd(c/d,m/d) is 1
print "The gcd of 2/2 and Q1b/2 is : ", gcd(Q1b/2,2/2)


# In[143]:

### Divide out the common factor
##  Following theorem 2
print "Divide out  2 from the common integers following theorem 2 \n";

u_1 = ZZ(u1/2);
print "u1 divided by 2, u_1= ",u_1;
w1_1=ZZ(w1/2);
print "w1 divided by 2, w_1= ",w1_1;
Q1b_1 = ZZ(Q1b/2) 
print  "Q1b divided by 2, Q1b_1= " ,Q1b_1


# In[144]:

# Compute gcd of w1_1 and u_1 is : one (theorem 2)
print "the gcd of w1_1 and u_1 is: ", gcd(w1_1,u_1)
#  And gcd of 1 and Q1b_1 is one.
# gcd(1, Q1_b1) = 1, then w1_1≡u1_1 (modQ1b_1).
# If this returns another value, we can still divide further


# In[145]:

# gcd of  Q1b_1,w1_1 is one. Modular inverse computation can thus be carried out
print "gcd of Q1b_1 and w1_1 is :",gcd(Q1b_1,w1_1)


# In[146]:

# Compute w1_1 inverse modulo Q1b_1
inverse_w1_1 =  inverse_mod(ZZ(w1_1), ZZ(Q1b_1))


# In[147]:

# the list of all z1


# In[148]:

# Multiply w1_1 and u_1 to get 
z1 = mod((inverse_w1_1*u_1),Q1b_1)


# In[149]:

# To compute all solutions
# We solze  (z1 +  Q1b_l1 * k) mod Q1b


# In[150]:

solution_collector = [];
flag = True;
first = True 
while flag:
    while first==True:
        
        solution_collector.append(z1) # Append initial solution        
        temp = mod((ZZ(z1) + ZZ(Q1b_1) ),Q1b) # compute z1 plus the Q1b_1 as explained
        solution_collector.append(temp)
        first = False;  # break out of this loop
    if temp != z1: # check if the returned value is equal to initial value. At that point 
                    # we stop computation
        temp = mod((ZZ(temp)+ZZ(Q1b_1)),Q1b) # add temp to new Q1b_1
        solution_collector.append(temp); # append value
        temp = temp; # set temp to new value and continue loop
    else:
        break;
        
print "solution is : ", solution_collector    


# #  Exercise 5

# In[151]:

# Exercise 4 
## encrypt a given word using the caesar cipher
## Computation is done modulo 27
## Note use of ord keyword to return ascii values. ASCII valus for "A" to "Z" are 65 to 90 
## To get values between 0 and 65 subtract 65. Letters of alphabet are encoded as 0 to 25


# In[7]:

def str2Int(s):
    '''
    return integer representantion of the letters 
    The values should be between 0 and 25
    
    input: string of characters.
    output: integers representation (0 to 25) of the string input.  
    '''
    whiteSpaceNo = 26; # handle whitespace separatelt since it is not contiguous with the other alphabets.
    Substract = 97 ; # substract this value from ord to get a value between 0 and 25
    encode =[];
    for x in s:
            if ord(x)==ord(" "):
                encode.append(whiteSpaceNo)
            else:
                new = ord(x)-Substract
                encode.append(new)
                
    return encode
        


# In[8]:

str2Int("e e e ") # test the function


# In[9]:

def Int2str(lst):
    '''
    convert values after encryption to letters.
    Note 65 is added to the character representation.
    
    input: integer values between 0 and 25. White space is 26.
    output : string. 
    
    '''
    temp = [] # store integer string 
    whiteSpaceNo = 26;
    
    for x in lst: 
        if x==whiteSpaceNo:
            temp.append([chr(int(x)+6)]) # ord white space is 32
     
        else:
            temp.append([chr(int(x)+97)])
            
    my_list = [l[0] for l in temp] # strip square bracket in the list
    
    return "".join(f for f in my_list), my_list


# In[26]:

Int2str([4, 26, 4, 26, 4, 26]) # test the function. NOTE  function returns both
                                # comma separated values and the values without without the comma.
                                # ie a concatenatin of characters


# In[27]:

# Encryption of word 4
word4= 'incorporated'
# Using the str to Int function
word4_encryption = str2Int(word4)
print "Encryption of word4 is:, ", word4_encryption


# In[28]:

# Decode encoded4= [15, 4, 17, 2, 7, 8, 13, 6]
encoded4= [15, 4, 17, 2, 7, 8, 13, 6]
encoded4_decoded = Int2str(encoded4)
print "Decryption of word4 is:, ", encoded4_decoded


# In[49]:

C4= [19, 13, 26, 3, 26, 14, 5, 7, 10, 14, 7, 14, 19, 7, 11, 6, 26, 14, 10, 26, 19, 14, 15, 22, 19, 14, 22, 0, 4, 26, 3, 14, 7, 14, 19, 3, 26, 26, 14, 25, 0, 14, 9, 3, 15, 0, 19, 14, 15, 9, 14, 19, 13, 26, 14, 13, 15, 22, 10, 26, 14, 7, 0, 4, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 7, 0, 4, 14, 19, 13, 26, 14, 13, 7, 19, 19, 26, 3, 14, 5, 26, 3, 26, 14, 13, 7, 20, 25, 0, 18, 14, 19, 26, 7, 14, 7, 19, 14, 25, 19, 14, 7, 14, 4, 15, 3, 21, 15, 22, 10, 26, 14, 5, 7, 10, 14, 10, 25, 19, 19, 25, 0, 18, 14, 11, 26, 19, 5, 26, 26, 0, 14, 19, 13, 26, 21, 14, 9, 7, 10, 19, 14, 7, 10, 6, 26, 26, 16, 14, 7, 0, 4, 14, 19, 13, 26, 14, 15, 19, 13, 26, 3, 14, 19, 5, 15, 14, 5, 26, 3, 26, 14, 22, 10, 25, 0, 18, 14, 25, 19, 14, 7, 10, 14, 7, 14, 1, 22, 10, 13, 25, 15, 0, 14, 3, 26, 10, 19, 25, 0, 18, 14, 19, 13, 26, 25, 3, 14, 26, 6, 11, 15, 5, 10, 14, 15, 0, 14, 25, 19, 14, 7, 0, 4, 14, 19, 7, 6, 23, 25, 0, 18, 14, 15, 20, 26, 3, 14, 25, 19, 10, 14, 13, 26, 7, 4, 14, 20, 26, 3, 12, 14, 22, 0, 1, 15, 21, 9, 15, 3, 19, 7, 11, 6, 26, 14, 9, 15, 3, 14, 19, 13, 26, 14, 4, 15, 3, 21, 15, 22, 10, 26, 14, 19, 13, 15, 22, 18, 13, 19, 14, 7, 6, 25, 1, 26, 14, 15, 0, 6, 12, 14, 7, 10, 14, 25, 19, 10, 14, 7, 10, 6, 26, 26, 16, 14, 25, 14, 10, 22, 16, 16, 15, 10, 26, 14, 25, 19, 14, 4, 15, 26, 10, 0, 19, 14, 21, 25, 0, 4, 14, 19, 13, 26, 14, 19, 7, 11, 6, 26, 14, 5, 7, 10, 14, 7, 14, 6, 7, 3, 18, 26, 14, 15, 0, 26, 14, 11, 22, 19, 14, 19, 13, 26, 14, 19, 13, 3, 26, 26, 14, 5, 26, 3, 26, 14, 7, 6, 6, 14, 1, 3, 15, 5, 4, 26, 4, 14, 19, 15, 18, 26, 19, 13, 26, 3, 14, 7, 19, 14, 15, 0, 26, 14, 1, 15, 3, 0, 26, 3, 14, 15, 9, 14, 25, 19, 14, 0, 15, 14, 3, 15, 15, 21, 14, 0, 15, 14, 3, 15, 15, 21, 14, 19, 13, 26, 12, 14, 1, 3, 25, 26, 4, 14, 15, 22, 19, 14, 5, 13, 26, 0, 14, 19, 13, 26, 12, 14, 10, 7, 5, 14, 7, 6, 25, 1, 26, 14, 1, 15, 21, 25, 0, 18, 14, 19, 13, 26, 3, 26, 10, 14, 16, 6, 26, 0, 19, 12, 14, 15, 9, 14, 3, 15, 15, 21, 14, 10, 7, 25, 4, 14, 7, 6, 25, 1, 26, 14, 25, 0, 4, 25, 18, 0, 7, 0, 19, 6, 12, 14, 7, 0, 4, 14, 10, 13, 26, 14, 10, 7, 19, 14, 4, 15, 5, 0, 14, 25, 0, 14, 7, 14, 6, 7, 3, 18, 26, 14, 7, 3, 21, 1, 13, 7, 25, 3, 14, 7, 19, 14, 15, 0, 26, 14, 26, 0, 4, 14, 15, 9, 14, 19, 13, 26, 14, 19, 7, 11, 6, 26, 14, 13, 7, 20, 26, 14, 10, 15, 21, 26, 14, 5, 25, 0, 26, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 10, 7, 25, 4, 14, 25, 0, 14, 7, 0, 14, 26, 0, 1, 15, 22, 3, 7, 18, 25, 0, 18, 14, 19, 15, 0, 26, 14, 7, 6, 25, 1, 26, 14, 6, 15, 15, 23, 26, 4, 14, 7, 6, 6, 14, 3, 15, 22, 0, 4, 14, 19, 13, 26, 14, 19, 7, 11, 6, 26, 14, 11, 22, 19, 14, 19, 13, 26, 3, 26, 14, 5, 7, 10, 14, 0, 15, 19, 13, 25, 0, 18, 14, 15, 0, 14, 25, 19, 14, 11, 22, 19, 14, 19, 26, 7, 14, 25, 14, 4, 15, 0, 19, 14, 10, 26, 26, 14, 7, 0, 12, 14, 5, 25, 0, 26, 14, 10, 13, 26, 14, 3, 26, 21, 7, 3, 23, 26, 4, 14, 19, 13, 26, 3, 26, 14, 25, 10, 0, 19, 14, 7, 0, 12, 14, 10, 7, 25, 4, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 19, 13, 26, 0, 14, 25, 19, 14, 5, 7, 10, 0, 19, 14, 20, 26, 3, 12, 14, 1, 25, 20, 25, 6, 14, 15, 9, 14, 12, 15, 22, 14, 19, 15, 14, 15, 9, 9, 26, 3, 14, 25, 19, 14, 10, 7, 25, 4, 14, 7, 6, 25, 1, 26, 14, 7, 0, 18, 3, 25, 6, 12, 14, 25, 19, 14, 5, 7, 10, 0, 19, 14, 20, 26, 3, 12, 14, 1, 25, 20, 25, 6, 14, 15, 9, 14, 12, 15, 22, 14, 19, 15, 14, 10, 25, 19, 14, 4, 15, 5, 0, 14, 5, 25, 19, 13, 15, 22, 19, 14, 11, 26, 25, 0, 18, 14, 25, 0, 20, 25, 19, 26, 4, 14, 10, 7, 25, 4, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 25, 14, 4, 25, 4, 0, 19, 14, 23, 0, 15, 5, 14, 25, 19, 14, 5, 7, 10, 14, 12, 15, 22, 3, 14, 19, 7, 11, 6, 26, 14, 10, 7, 25, 4, 14, 7, 6, 25, 1, 26, 14, 25, 19, 10, 14, 6, 7, 25, 4, 14, 9, 15, 3, 14, 7, 14, 18, 3, 26, 7, 19, 14, 21, 7, 0, 12, 14, 21, 15, 3, 26, 14, 19, 13, 7, 0, 14, 19, 13, 3, 26, 26, 14, 12, 15, 22, 3, 14, 13, 7, 25, 3, 14, 5, 7, 0, 19, 10, 14, 1, 22, 19, 19, 25, 0, 18, 14, 10, 7, 25, 4, 14, 19, 13, 26, 14, 13, 7, 19, 19, 26, 3, 14, 13, 26, 14, 13, 7, 4, 14, 11, 26, 26, 0, 14, 6, 15, 15, 23, 25, 0, 18, 14, 7, 19, 14, 7, 6, 25, 1, 26, 14, 9, 15, 3, 14, 10, 15, 21, 26, 14, 19, 25, 21, 26, 14, 5, 25, 19, 13, 14, 18, 3, 26, 7, 19, 14, 1, 22, 3, 25, 15, 10, 25, 19, 12, 14, 7, 0, 4, 14, 19, 13, 25, 10, 14, 5, 7, 10, 14, 13, 25, 10, 14, 9, 25, 3, 10, 19, 14, 10, 16, 26, 26, 1, 13, 14, 12, 15, 22, 14, 10, 13, 15, 22, 6, 4, 14, 6, 26, 7, 3, 0, 14, 0, 15, 19, 14, 19, 15, 14, 21, 7, 23, 26, 14, 16, 26, 3, 10, 15, 0, 7, 6, 14, 3, 26, 21, 7, 3, 23, 10, 14, 7, 6, 25, 1, 26, 14, 10, 7, 25, 4, 14, 5, 25, 19, 13, 14, 10, 15, 21, 26, 14, 10, 26, 20, 26, 3, 25, 19, 12, 14, 25, 19, 10, 14, 20, 26, 3, 12, 14, 3, 22, 4, 26, 14, 19, 13, 26, 14, 13, 7, 19, 19, 26, 3, 14, 15, 16, 26, 0, 26, 4, 14, 13, 25, 10, 14, 26, 12, 26, 10, 14, 20, 26, 3, 12, 14, 5, 25, 4, 26, 14, 15, 0, 14, 13, 26, 7, 3, 25, 0, 18, 14, 19, 13, 25, 10, 14, 11, 22, 19, 14, 7, 6, 6, 14, 13, 26, 14, 10, 7, 25, 4, 14, 5, 7, 10, 14, 5, 13, 12, 14, 25, 10, 14, 7, 14, 3, 7, 20, 26, 0, 14, 6, 25, 23, 26, 14, 7, 14, 5, 3, 25, 19, 25, 0, 18, 4, 26, 10, 23, 14, 1, 15, 21, 26, 14, 5, 26, 14, 10, 13, 7, 6, 6, 14, 13, 7, 20, 26, 14, 10, 15, 21, 26, 14, 9, 22, 0, 14, 0, 15, 5, 14, 19, 13, 15, 22, 18, 13, 19, 14, 7, 6, 25, 1, 26, 14, 25, 21, 14, 18, 6, 7, 4, 14, 19, 13, 26, 12, 20, 26, 14, 11, 26, 18, 22, 0, 14, 7, 10, 23, 25, 0, 18, 14, 3, 25, 4, 4, 6, 26, 10, 14, 25, 14, 11, 26, 6, 25, 26, 20, 26, 14, 25, 14, 1, 7, 0, 14, 18, 22, 26, 10, 10, 14, 19, 13, 7, 19, 14, 10, 13, 26, 14, 7, 4, 4, 26, 4, 14, 7, 6, 15, 22, 4, 14, 4, 15, 14, 12, 15, 22, 14, 21, 26, 7, 0, 14, 19, 13, 7, 19, 14, 12, 15, 22, 14, 19, 13, 25, 0, 23, 14, 12, 15, 22, 14, 1, 7, 0, 14, 9, 25, 0, 4, 14, 15, 22, 19, 14, 19, 13, 26, 14, 7, 0, 10, 5, 26, 3, 14, 19, 15, 14, 25, 19, 14, 10, 7, 25, 4, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 26, 17, 7, 1, 19, 6, 12, 14, 10, 15, 14, 10, 7, 25, 4, 14, 7, 6, 25, 1, 26, 14, 19, 13, 26, 0, 14, 12, 15, 22, 14, 10, 13, 15, 22, 6, 4, 14, 10, 7, 12, 14, 5, 13, 7, 19, 14, 12, 15, 22, 14, 21, 26, 7, 0, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 5, 26, 0, 19, 14, 15, 0, 14, 25, 14, 4, 15, 14, 7, 6, 25, 1, 26, 14, 13, 7, 10, 19, 25, 6, 12, 14, 3, 26, 16, 6, 25, 26, 4, 14, 7, 19, 14, 6, 26, 7, 10, 19, 7, 19, 14, 6, 26, 7, 10, 19, 14, 25, 14, 21, 26, 7, 0, 14, 5, 13, 7, 19, 14, 25, 14, 10, 7, 12, 19, 13, 7, 19, 10, 14, 19, 13, 26, 14, 10, 7, 21, 26, 14, 19, 13, 25, 0, 18, 14, 12, 15, 22, 14, 23, 0, 15, 5, 14, 0, 15, 19, 14, 19, 13, 26, 14, 10, 7, 21, 26, 14, 19, 13, 25, 0, 18, 14, 7, 14, 11, 25, 19, 14, 10, 7, 25, 4, 14, 19, 13, 26, 14, 13, 7, 19, 19, 26, 3, 14, 12, 15, 22, 14, 21, 25, 18, 13, 19, 14, 8, 22, 10, 19, 14, 7, 10, 14, 5, 26, 6, 6, 14, 10, 7, 12, 14, 19, 13, 7, 19, 14, 25, 14, 10, 26, 26, 14, 5, 13, 7, 19, 14, 25, 14, 26, 7, 19, 14, 25, 10, 14, 19, 13, 26, 14, 10, 7, 21, 26, 14, 19, 13, 25, 0, 18, 14, 7, 10, 14, 25, 14, 26, 7, 19, 14, 5, 13, 7, 19, 14, 25, 14, 10, 26, 26, 14, 12, 15, 22, 14, 21, 25, 18, 13, 19, 14, 8, 22, 10, 19, 14, 7, 10, 14, 5, 26, 6, 6, 14, 10, 7, 12, 14, 7, 4, 4, 26, 4, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 19, 13, 7, 19, 14, 25, 14, 6, 25, 23, 26, 14, 5, 13, 7, 19, 14, 25, 14, 18, 26, 19, 14, 25, 10, 14, 19, 13, 26, 14, 10, 7, 21, 26, 14, 19, 13, 25, 0, 18, 14, 7, 10, 14, 25, 14, 18, 26, 19, 14, 5, 13, 7, 19, 14, 25, 14, 6, 25, 23, 26, 14, 12, 15, 22, 14, 21, 25, 18, 13, 19, 14, 8, 22, 10, 19, 14, 7, 10, 14, 5, 26, 6, 6, 14, 10, 7, 12, 14, 7, 4, 4, 26, 4, 14, 19, 13, 26, 14, 4, 15, 3, 21, 15, 22, 10, 26, 14, 5, 13, 15, 14, 10, 26, 26, 21, 26, 4, 14, 19, 15, 14, 11, 26, 14, 19, 7, 6, 23, 25, 0, 18, 14, 25, 0, 14, 13, 25, 10, 14, 10, 6, 26, 26, 16, 14, 19, 13, 7, 19, 14, 25, 14, 11, 3, 26, 7, 19, 13, 26, 14, 5, 13, 26, 0, 14, 25, 14, 10, 6, 26, 26, 16, 14, 25, 10, 14, 19, 13, 26, 14, 10, 7, 21, 26, 14, 19, 13, 25, 0, 18, 14, 7, 10, 14, 25, 14, 10, 6, 26, 26, 16, 14, 5, 13, 26, 0, 14, 25, 14, 11, 3, 26, 7, 19, 13, 26, 14, 25, 19, 14, 25, 10, 14, 19, 13, 26, 14, 10, 7, 21, 26, 14, 19, 13, 25, 0, 18, 14, 5, 25, 19, 13, 14, 12, 15, 22, 14, 10, 7, 25, 4, 14, 19, 13, 26, 14, 13, 7, 19, 19, 26, 3, 14, 7, 0, 4, 14, 13, 26, 3, 26, 14, 19, 13, 26, 14, 1, 15, 0, 20, 26, 3, 10, 7, 19, 25, 15, 0, 14, 4, 3, 15, 16, 16, 26, 4, 14, 7, 0, 4, 14, 19, 13, 26, 14, 16, 7, 3, 19, 12, 14, 10, 7, 19, 14, 10, 25, 6, 26, 0, 19, 14, 9, 15, 3, 14, 7, 14, 21, 25, 0, 22, 19, 26, 14, 5, 13, 25, 6, 26, 14, 7, 6, 25, 1, 26, 14, 19, 13, 15, 22, 18, 13, 19, 14, 15, 20, 26, 3, 14, 7, 6, 6, 14, 10, 13, 26, 14, 1, 15, 22, 6, 4, 14, 3, 26, 21, 26, 21, 11, 26, 3, 14, 7, 11, 15, 22, 19, 14, 3, 7, 20, 26, 0, 10, 14, 7, 0, 4, 14, 5, 3, 25, 19, 25, 0, 18, 4, 26, 10, 23, 10, 14, 5, 13, 25, 1, 13, 14, 5, 7, 10, 0, 19, 14, 21, 22, 1, 13, 14, 19, 13, 26, 14, 13, 7, 19, 19, 26, 3, 14, 5, 7, 10, 14, 19, 13, 26, 14, 9, 25, 3, 10, 19, 14, 19, 15, 14, 11, 3, 26, 7, 23, 14, 19, 13, 26, 14, 10, 25, 6, 26, 0, 1, 26, 14, 5, 13, 7, 19, 14, 4, 7, 12, 14, 15, 9, 14, 19, 13, 26, 14, 21, 15, 0, 19, 13, 14, 25, 10, 14, 25, 19, 14, 13, 26, 14, 10, 7, 25, 4, 14, 19, 22, 3, 0, 25, 0, 18, 14, 19, 15, 14, 7, 6, 25, 1, 26, 14, 13, 26, 14, 13, 7, 4, 14, 19, 7, 23, 26, 0, 14, 13, 25, 10, 14, 5, 7, 19, 1, 13, 14, 15, 22, 19, 14, 15, 9, 14, 13, 25, 10, 14, 16, 15, 1, 23, 26, 19, 14, 7, 0, 4, 14, 5, 7, 10, 14, 6, 15, 15, 23, 25, 0, 18, 14, 7, 19, 14, 25, 19, 14, 22, 0, 26, 7, 10, 25, 6, 12, 14, 10, 13, 7, 23, 25, 0, 18, 14, 25, 19, 14, 26, 20, 26, 3, 12, 14, 0, 15, 5, 14, 7, 0, 4, 14, 19, 13, 26, 0, 14, 7, 0, 4, 14, 13, 15, 6, 4, 25, 0, 18, 14, 25, 19, 14, 19, 15, 14, 13, 25, 10, 14, 26, 7, 3, 14, 7, 6, 25, 1, 26, 14, 1, 15, 0, 10, 25, 4, 26, 3, 26, 4, 14, 7, 14, 6, 25, 19, 19, 6, 26, 14, 7, 0, 4, 14, 19, 13, 26, 0, 14, 10, 7, 25, 4, 14, 19, 13, 26, 14, 9, 15, 22, 3, 19, 13, 14, 19, 5, 15, 14, 4, 7, 12, 10, 14, 5, 3, 15, 0, 18, 14, 10, 25, 18, 13, 26, 4, 14, 19, 13, 26, 14, 13, 7, 19, 19, 26, 3, 14, 25, 14, 19, 15, 6, 4, 14, 12, 15, 22, 14, 11, 22, 19, 19, 26, 3, 14, 5, 15, 22, 6, 4, 0, 19, 14, 10, 22, 25, 19, 14, 19, 13, 26, 14, 5, 15, 3, 23, 10, 14, 13, 26, 14, 7, 4, 4, 26, 4, 14, 6, 15, 15, 23, 25, 0, 18, 14, 7, 0, 18, 3, 25, 6, 12, 14, 7, 19, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 25, 19, 14, 5, 7, 10, 14, 19, 13, 26, 14, 11, 26, 10, 19, 14, 11, 22, 19, 19, 26, 3, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 21, 26, 26, 23, 6, 12, 14, 3, 26, 16, 6, 25, 26, 4, 14, 12, 26, 10, 14, 11, 22, 19, 14, 10, 15, 21, 26, 14, 1, 3, 22, 21, 11, 10, 14, 21, 22, 10, 19, 14, 13, 7, 20, 26, 14, 18, 15, 19, 14, 25, 0, 14, 7, 10, 14, 5, 26, 6, 6, 14, 19, 13, 26, 14, 13, 7, 19, 19, 26, 3, 14, 18, 3, 22, 21, 11, 6, 26, 4, 14, 12, 15, 22, 14, 10, 13, 15, 22, 6, 4, 0, 19, 14, 13, 7, 20, 26, 14, 16, 22, 19, 14, 25, 19, 14, 25, 0, 14, 5, 25, 19, 13, 14, 19, 13, 26, 14, 11, 3, 26, 7, 4, 23, 0, 25, 9, 26, 14, 19, 13, 26, 14, 21, 7, 3, 1, 13, 14, 13, 7, 3, 26, 14, 19, 15, 15, 23, 14, 19, 13, 26, 14, 5, 7, 19, 1, 13, 14, 7, 0, 4, 14, 6, 15, 15, 23, 26, 4, 14, 7, 19, 14, 25, 19, 14, 18, 6, 15, 15, 21, 25, 6, 12, 14, 19, 13, 26, 0, 14, 13, 26, 14, 4, 25, 16, 16, 26, 4, 14, 25, 19, 14, 25, 0, 19, 15, 14, 13, 25, 10, 14, 1, 22, 16, 14, 15, 9, 14, 19, 26, 7, 14, 7, 0, 4, 14, 6, 15, 15, 23, 26, 4, 14, 7, 19, 14, 25, 19, 14, 7, 18, 7, 25, 0, 14, 11, 22, 19, 14, 13, 26, 14, 1, 15, 22, 6, 4, 14, 19, 13, 25, 0, 23, 14, 15, 9, 14, 0, 15, 19, 13, 25, 0, 18, 14, 11, 26, 19, 19, 26, 3, 14, 19, 15, 14, 10, 7, 12, 14, 19, 13, 7, 0, 14, 13, 25, 10, 14, 9, 25, 3, 10, 19, 14, 3, 26, 21, 7, 3, 23, 14, 25, 19, 14, 5, 7, 10, 14, 19, 13, 26, 14, 11, 26, 10, 19, 14, 11, 22, 19, 19, 26, 3, 14, 12, 15, 22, 14, 23, 0, 15, 5, 14, 7, 6, 25, 1, 26, 14, 13, 7, 4, 14, 11, 26, 26, 0, 14, 6, 15, 15, 23, 25, 0, 18, 14, 15, 20, 26, 3, 14, 13, 25, 10, 14, 10, 13, 15, 22, 6, 4, 26, 3, 14, 5, 25, 19, 13, 14, 10, 15, 21, 26, 14, 1, 22, 3, 25, 15, 10, 25, 19, 12, 14, 5, 13, 7, 19, 14, 7, 14, 9, 22, 0, 0, 12, 14, 5, 7, 19, 1, 13, 14, 10, 13, 26, 14, 3, 26, 21, 7, 3, 23, 26, 4, 14, 25, 19, 14, 19, 26, 6, 6, 10, 14, 19, 13, 26, 14, 4, 7, 12, 14, 15, 9, 14, 19, 13, 26, 14, 21, 15, 0, 19, 13, 14, 7, 0, 4, 14, 4, 15, 26, 10, 0, 19, 14, 19, 26, 6, 6, 14, 5, 13, 7, 19, 14, 15, 1, 6, 15, 1, 23, 14, 25, 19, 14, 25, 10, 14]
hint4= [-1, 11, 1, -1, -1, 9, 18, 13, 25, -1, 23, -1, -1, 0, 15, 16, -1, -1, -1, -1, -1, -1, 5, 17, 12, 2, -1]


# ###  Solution is to Do frequency analysis

# In[44]:

# letterfreq lists the letters a-z, listed in decreasing order of frequency, 
# as given in note.
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
frequency = ['0.082','0.015','0.028','0.043','0.127','0.022','0.020','0.061','0.070','0.002','0.008','0.040','0.024','0.067',
             '0.075','0.019','0.001','0.060','0.063','0.091','0.028','0.010','0.023','0.001','0.020','0.001' ]
letterfrequency= parameter_dict = dict( zip(letter, frequency ) )


# In[45]:

letterprops = sorted(letterfrequency.items(), 
                           key=operator.itemgetter(1),reverse=True) # sort element in reverse order


# In[46]:

letterprops


# In[47]:

print "letter frequency is: "
letterprops


# In[53]:

# Histogram plot gives us hint that some integers are missing
# this integer must belong to the list occuring integer/ alphabet in the encosing
# Inparticular observe 2 and 24 are not represented.----have zero count
import matplotlib.pyplot as plt

get_unique_set_element = list(set(C4)) ## gets the unique values in the list

histo = []

for i in get_unique_set_element:
    histo.append(C4.count(i)) ## add the number of occurances to the histo list

plt.bar(get_unique_set_element, histo,color="teal")
plt.title("Histogram plot of Integer occurence in Ciphertext")
plt.ylabel("Frequency of Integers")
plt.xlabel("Integers in Cipher text")
plt.xlim([0,26])
plt.show()


# In[56]:

from collections import Counter # import collection to store count of integers in dictionary
                                # we can also use a for loop see below


# In[57]:

Frequency_of_occurency = Counter(C4) # call counter from collection --- see above


# In[58]:

Frequency_of_occurency # see integers and their frequency in a dictionary


# In[62]:

# to verify the output 
# we use default dictionary and use a for loop to count frequencies.
# This returns values same as that of using the counter from python collection
# library
from collections import defaultdict
Frequency_count_check = defaultdict(int)
counter_space= 0
for obj in C4:
    if Integer(obj) < 0:
        counter_space +=1 
    else:
        Frequency_count_check[obj] += 1


# In[63]:

Frequency_count_check # this agrees with the 


# In[73]:

# This is the hint 
hint4= [-1, 11, 1, -1, -1, 9, 18, 13, 25, -1, 23, -1,
        -1, 0, 15, 16, -1, -1, -1, -1, -1, -1, 5, 17, 12, 2, -1]


# In[73]:

# Observing the the histogram,
# we can verify the integer 2 and 24 did not occur
for x in C4:
    if x == 24 or x == 24: # No number 2 or 24 in the digits. So 2 must belong to less occuring alphabets
        print "yes"
    


# In[74]:

# sort the dicionary of intergers and count
Sorted_dictionary = sorted(Frequency_count_check.items(), 
                           key=operator.itemgetter(1),reverse=True) # sort element in reverse order


# In[ ]:




# In[75]:

print "cipher text frequency analysis:"
Sorted_dictionary


# In[76]:

# Now below is the English word frequency
print "English words frequency: \n "
letterprops


# In[91]:

count = 0;
# since white space is the most freqient we assign it  14
# and use count to increment the loop each letterprops which has no white space in it
print " Map the English word frequency to sorted  Frequuency analysis of cipher text: \n  "
for key in range(0,len(Sorted_dictionary)):
    if key == 0:
        print  "Freuency_analysis_comparism( [whitespace] ) = ", Sorted_dictionary[key][0]
        
    else:
        print  "Frequency_analysis_comparism(" , letterprops[count][0]  , " ) = " , Sorted_dictionary[key][0] 
        count+=1


# In[92]:

# Using the frequecy mapping above and the hint:
# We have that the most frequent string is the whitespace 
# Thus white space is the seperation between the words.
# Therefore, we read the cipher text at intervals of 14-(which is white space).
# This will show that 26 maps to e 
# and that t also maps to 19
# and finally 7 also maps to a,.
# The others we detect reading the text
# There is 2 missing in the whole cipher text and it corresponds to z in the hint4
# This is not suprising since it is less frequent
# In addition j and q mappings also seem to be correct directly from frequency analysis


# In[78]:

QValues = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26] # digits of alphabets
Qkeys = [7,11,1,4,26,9,18,13,25,8,23,6,21,0,15,16,24,3,10,19,22,20,5,17,12,2,14]


# In[79]:

Q3b = parameter_dict = dict( zip(QValues, Qkeys ) )


# In[80]:

for i in Q3b:
    print "Q3b(", i,") = ", Q3b[i]


# # Exercise 3

# In[154]:

n3=56883035787711984709746044941908542353686385686186899224808550168570130599373860352095788384779540489857823324955874869023454311629006040145757300801857373311136373616834703698720687767415133707862955923122374860442203297671741563306466830616624206896198829489085738354508433316862759303677891522671529474506904063726123173713813214897636183655813117059136988876122740373869948913796320528588756389545342882412104619885392954149891201825840631741576411769027105134346649160147525354685786470318546790158102201249405929079909525535068583998347275436585524970641433416011762473727233504385817560114708978362632734235277
g3=20369851835940902712426521423805948101711087377429155349869297746666361752916100033866067965683024450388325635500301613807971382264678378221840170421011992645099055537237195576076668177800642436245231927780260570179819322568524738499633464590024389571223413410056415513797872062267049359106139833105067086212478053810478187557687933761916634929131345699858586394866979761473774522425543238771512839441949137222055080227660655056605965046347608416868189314925850086232163668828204843222093804294165076898466206967127535952300343118990943678456704578134029704903924374718474625381329515941103080117252131360895405353120
X3=24867970608027675738217006892082276451387710136489801365355541194764246418962874457302198274606793642514272147468657522121779004213504019318106527948698546135235300996016938772166575867515319945371847818130762851426617107292588799298691883150147160644802270290479777394864129945835742555363050791756178191216882111333556921157794552626034265904365179295052676098708425218463318005663618625440106388152571250664725180099216929131257514948239886888185340176998474955534598439669405380772543047416983177056613741760325073508733765564548799432936134779479608977767555007314354656194866012098506467043441687308963631807290
Y3=28998520360344491368516995989380879785258343479731170535371628423289766761803163020038444457306916248740211357264424420480281391558436217690793530540426607302487394207013485939542936716858945166903168149930331170041070526065931738903269303679722720880098663712503847152704705579679964030759116644630013190435147191796255618759609723935287269015442934736360487466584809738916090988352740867306741310964662966748901533907909485018360133425016675026340539560276683684776319371594452020616098374885074999748057217238603000967667377579359942880752289402101939796596788983560720870913243793344197744409889672912469695599276


# In[155]:

# Alice chooses random a in {Z}_p^* and sends A=aP (this means  P+ ...+P$, a times).
# Bob chooses  b in {Z}_p^* and sends B=bP.
# Alice computes K=aB=(ab)P
# Bob computes K=bA=(ba)P=(ab)P


# In[156]:

# If we transpose the Diffie-Hellman in the additive group (Zp,+),
# the intractibility of the discrete logarithm problem is no longer satisfied.


# In[157]:

# The exponentation is transposed to a multiplication,
# while the discrete logarithm operation becomes 
# equivalent to a division (i.e., to a multiplication with an inverse element).


# In[158]:

# As computing the inverse (with respect to the multiplication) of an element 
# in Zp is an easy task with the Ex- tended Euclid Algorithm,


# In[159]:

# Solution#####
# we do not know a and b
# But we know bg = x_3 mod n3
# Which implies that computing the inverse: bg * g^-1 = x^3 * g^-1 mod n3 which gives b


# In[160]:

print "gcd of g3 and n3 is: ",gcd(g3, n3)
print "gcd of X3 and n3 is: ", gcd(X3, n3)
print "gcd of X3 and g3 is: ", gcd(X3, n3)



# In[161]:

inverse_g3 = inverse_mod(g3, n3)
b = mod((inverse_g3*X3),n3)
print "the inverse of g3 mod n3 is \n:", inverse_g3 
print  "\n this is our b \n", b


# In[162]:

# TO check, denote gb as product of g and b
gb = mod((g3*b), n3) 
print "is gb equal to X3:", gb == X3


# In[163]:

# Similarly to compute a 
# But we know ag = Y_3 mod n3
# Which implies that computing the inverse: bg * g^-1 = Y^3 * g^-1 mod n3 which gives b


# In[164]:

print "gcd of g3 and n3 is: ",gcd(g3, n3)
print "gcd of X3 and n3 is: ", gcd(X3, n3)
print "gcd of Y3 and g3 is: ", gcd(X3, n3)




# In[165]:

a = mod((inverse_g3*Y3),n3)
print  "\n This is our a:  \n", a


# In[166]:

# To check
# TO check, denote gb as product of g and b
ga = mod((a*g3), n3) 
print "is gb equal to X3", ga == Y3



# In[167]:

# To compute the final Compute the output Q3 of the 
# DH key exchange between Alice and Bob and write it in your
# Final output is : b(Y3) = b(ag3) and a(X3) = a (bg3)


# In[168]:

# Both Alice and Bob should have same final key
# We compute for each separately  and compare. To confirm 
# equality

Q3a = mod((b*Y3), n3)
Q3b = mod((a*X3),n3)


# In[169]:

# Check the output is same
print "the output of both Alice and Bob is same: ", Q3a == Q3b


# In[170]:

Q3 = Q3a


# In[171]:

print "The Q3 is: \n", Q3


# # Exercise 5 

# In[172]:

C5= [15, 1, 19, 19, 23, 14, 17, 3, 26, 9, 19, 26, 19, 2, 15, 20, 17, 7, 5, 19]
# WE observe that the plain text contains 26 at different intervals
# Since we made a good guess that the message contains words from dictionary 
# and spaces. we can reasonable assume the space correspond to 26.
# In particular since we also known that in any message the encoding of
# space is either 26 or 0 (26 + 1 = 0 or 26 + 0 = 26) and no zero in the text
# We can first work with the assumption that26 is space


# In[173]:

f = open("dictionary.txt","r") # open the dictionary
#ct = f.readlines()


# In[3]:

# read the dictionary
dictionary=[]
for line in f: 
    line=line.rstrip("\n")
    dictionary.append(line) 


# In[4]:

dictionary[1:10] # see the result of what was read


# In[10]:

# encode each word from the dictionary
dictionary_encoded =[];
for x in dictionary:
    temp = str2Int(x)
    dictionary_encoded.append(temp)


# In[64]:

dictionary_encoded[1]


# In[11]:

# Now combine the encoding and the dictionary text into a dictionary
from collections import OrderedDict

dictionary_of_encodings = OrderedDict( zip(dictionary, dictionary_encoded ) ) # this bears each word and 
                                                                              #  the corresponding encoding


# In[12]:

# This is our cipher text
# we consider the ciphertext small subset at a time
# In particular we consider all integers using 26 
# as our delimiter
# so that we get something like this
# [15, 1, 19, 19, 23, 14, 17, 3]  + 26 +
# [9, 19,] + 26 +
# [19, 2, 15, 20, 17, 7, 5, 19]
# we try to decode each of this subset
C5= [15, 1, 19, 19, 23, 14, 17, 3, 26, 9, 19, 26, 19, 2, 15, 20, 17, 7, 5, 19]  # cipher text


# In[152]:

dictionary_of_encodings.items()[0:5] # test the new word-encoding pair in the new dictionary


# In[14]:

dictionary_of_encodings['s'] # we can return the encoding for s


# In[ ]:

C5= [15, 1, 19, 19, 23, 14, 17, 3, 26, 9, 19, 26, 19, 2, 15, 20, 17, 7, 5, 19]  # cipher text


# In[241]:

# Break C5 into sublist using 26 as  space as explained above
C51 = [15, 1, 19, 19, 23, 14, 17, 3]
C52 = [9, 19]
C53 = [19, 2, 15, 20, 17, 7, 5, 19]


# In[242]:

import itertools

def key_combination_generator(K,N):
    '''
    Function returns all 
    combinations of 1 and 0 
    of length 2^(k*N)
    input : integer K and N
    output: 2^(k*N) of {1 , 0}* each of length (k*N)
    
    '''
    collector = [];
    [collector.append(i) for i in itertools.product([0, 1], repeat = K*N)]
    return collector 


# In[243]:

C51_keys_collector = key_combination_generator(1,len(C51))
C52_keys_collector = key_combination_generator(1,len(C52))
C53_keys_collector = key_combination_generator(1,len(C53))


# In[ ]:




# In[265]:

def all_possible_decryption(possible_keys,cipher_text):
    '''
    Input : decryption keys in the set {0,1}
    Output: List. All possible decryptions 
            List. All possible keys
    '''
    collector = [];
    for item in possible_keys:
        temp = list(item) # store an instance of key here
        templist =[] # empty list. to store values after subtration of keys
        for i,j in  map(None,cipher_text,temp):
            #print i,j
            temp2 = i-j # decryption step. Subtract the each element of keys from the cipher text
            templist.append(temp2) # put in templist. And empty temp list in next iteration
            #print
            #print templist
        collector.append(templist)
    return collector   
            
    


# In[274]:

C51_all_decryption = all_possible_decryption(C51_keys_collector,C51)
C52_all_decryption = all_possible_decryption(C52_keys_collector,C52)
C53_all_decrption =all_possible_decryption(C53_keys_collector,C53)


# In[275]:

# Use lambda mapping and any to see common element from the 
# lsit of decryption  and list words in dictionary


# In[276]:

#Use simple lambda expression to check if a common list element exist between
# the list of dictionary encodings and all possibe encryption
# As we can see there is a common element between dictionary encoding
# and the list of all possible encryption
print any(map(lambda x: x in dictionary_encoded,C51_all_decryption))
print any(map(lambda x: x in dictionary_encoded,C52_all_decryption))
print any(map(lambda x: x in dictionary_encoded,C53_all_decrption))


# In[310]:

# Since true was return above
# We use the function below
# to retrieve all element corresponding to true from list

all_decryption = [C51_all_deccryption,C52_all_decryption,C53_all_decrption]
def decryption(index):
    '''
    Input: integer i. Signifying index in all_decryption
    Output : List. The ecncoding for the element 
    '''
    common_element = []
    for i in dictionary_encoded:
        for j in all_decryption[index]:
            if j ==i:
                common_element.append(i)
    common_element = common_element[0]
    return common_element


# In[311]:

index1 = 0; # index of C51_all_deccryption in all_decryption
index2 =1; # index of C52_all_deccryption in all_decryption
index3 = 2 ; # index of C52_all_deccryption in all_decryption
C51_encoding = decryption(index1)
C52_encoding = decryption(index2)
C53_encoding =decryption(index3)


# In[312]:

# Next we get the word for the encoding from dictionary


# In[313]:

def phrase(index):
    temp = ''
    for k, v in dictionary_of_encodings.items():
        if index == v :
         temp = k
    return temp + " "
    


# In[314]:

phrase1 = phrase(C51_encoding)
phrase2 = phrase(C52_encoding)
phrase3 = phrase(C53_encoding)


# In[315]:

print "The decrypted phrase phrase is"
phrase1 + " " + phrase2 +" " + phrase3


# In[ ]:



