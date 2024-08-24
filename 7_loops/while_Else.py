# else in while loop :- 

# this condition will work in while loop when for ends normally (means pura loop sari condition check krega jitne iteration hai vo puri complete krega, aur bich me se break nhi hoga.)
# agr bich me for loop end ho gya break ho gya toh else wali condition run nhi hogi.
# else tb run hoga jab for loop normally execute hoke khatam hoga, agr vo break ki vajah se bahar aaya hai loop se toh vaha pr else kaam nhi krega.



num = 1
while num <= 10 :
    if num == 5 :
        print("break while loop")
        break
    print(num)
    num += 1
else :
    print("while loop ended normally")









