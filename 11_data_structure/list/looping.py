# loop on list

products = ["Pen", "Pencil", "Notebook"]

# for item in products :
#     print(item)  # products list me se harr ek item one by one print honge




# enumerate() =>

# agr hum chahte hai ki list ke item ke sath sath uss item ka index number bhi pri nt ho
# ye hame output tupple me dega 

# for x in enumerate(products) :
#     print(x)  # (0, 'Pen') aise ye sare items ke liye print krega one by one, isme pehle vo item ka index number lega then item ka name


# agr hum chahte hai ki ek ek item aur index individually  access  ho -
# for x in enumerate(products) :
#     # print(x[0])  # index print honge 
#     # print(x[1])  # items print honge
#     print(x[1], x[0]) # pehle item print hoga aur uske samne uska index print hoga


# isme hum unpacking bhi kr sakte hai -
# for x, y in enumerate(products) :  # isme jo index hoga vo x variable me store ho jayega aur jo item hoga vo y variable me store ho jayega
#     print(x, y)
