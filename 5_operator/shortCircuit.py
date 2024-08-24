# Short Circuit in Logical Operator


# Logical AND ke case me short circuit evolution ka matalb ye hota hai ki jab tk usse true milta rahega vo evaluate krta rhega, 

# ssc = 66
# hsc = 65
# test = 85

# if ssc >= 60 and hsc >= 60 and test >= 60 :
#     print("Eligible")
# else :
#     print("Not Eligible")


# In the above example, hum isme and operator ka use kr rhe hai, aur and operator me puri condition satisfy huyi tbhi if wala part run hoga nhi toh nhi hoga, toh short circuit of logical operator ke case me jab hum and operator ka use kr rhe hote hai toh pehle vo first condition check krega agr true hai toh fir next condition check krega aur agr first condition hi false huyi toh fir vo aage ki condition check nhi krega direct else wala part print kr dega
# and - isme jab tk true milta jata hai tb tk vo aage ki condition check krta rehta hai. agr jaise hi usko false mila vo kaam karna band kr dega



# Logical OR ke case me jaise hi usse true milega vo evoluate krna band kr dega.

# ssc = 66
# hsc = 65
# test = 85

# if ssc >= 60 or hsc >= 60 or test >= 60 :
#     print("Eligible")
# else :
#     print("Not Eligible")


# In the above example, hum isme or operator ka use kr rhe hai, aur or operator me ek bhi condition satisfy huyi toh if wala part run hoga, toh short circuit of logical operator ke case me jab hum or operator ka use kr rhe hote hai toh pehle vo first condition check krega agr false hai toh next condition check karega but agr true hai toh fir next condition check nhi krega, directly if wale part me jo bhi code hai usse execute kr dega. 
# or - jab tk usse false milta jayega vo aage check krta jayega, jaise hi usse true milega vo aage check krna band kr dega.


