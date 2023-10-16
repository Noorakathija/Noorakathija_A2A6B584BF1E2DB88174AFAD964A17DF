def                                      linearsearchproduct(productlist,targetProduct):
 indices=[]

 for index, product in                  enumerate(productlist): 
    if product == targetProduct:
      indices.append(index)

 return indices



products =""
target="shoes"
result=linearsearchproduct(products,target)
print(result)