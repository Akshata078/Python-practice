# continue statement :-
 
# if the condition is satisfied, then skip the currect iteration and continue to the next iteration.
# it is used to skip the remaining code inside a loop for the currect iteration only.


# continue statement in for loop

# ex. print the numbers from 0 to 9 but dont print 5 
# for num in range(10) :
#     if(num == 5) :
#         continue
#     print(num)




# continue statement in while loop

# ex. print the numbers from 1 to 5 but dont print 2

# num = 0
# while num <= 5 :
#     num += 1   # isme humne num pehle increment kiya because agr if ke baad increment krte toh vo kbhi execute hi nhi krta 1 ke baad, vo fir infinite loop bann jata. 
#     if num == 2:
#         continue
#     print(num)