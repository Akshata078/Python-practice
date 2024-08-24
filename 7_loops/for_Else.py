# else in for loop :- 

# this condition will work in for loop when for ends normally (means pura loop sari condition check krega jitne iteration hai vo puri complete krega, aur bich me se break nhi hoga.)
# agr bich me for loop end ho gya break ho gya toh else wali condition run nhi hogi.
# else tb run hoga jab for loop normally execute hoke khatam hoga, agr vo break ki vajah se bahar aaya hai loop se toh vaha pr else kaam nhi krega.


for number in range(3):
    num = int(input("Enter odd number : "))
    if num % 2 == 0 :
        print("You loose !")
        break
else:
    print("You win !")










