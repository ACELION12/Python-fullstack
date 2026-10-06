import csv
products=[
    ['id','name','price'],
    [123,'Tv',50000],
    [124,'Ac',60000],
    [125,'Car',670000],
    [126,'Camera',200000]
]
with open('csv files/product.csv','w',newline='') as file1:
    writecontent=csv.writer(file1)
    writecontent.writerows(products)
    print('written to csv file')