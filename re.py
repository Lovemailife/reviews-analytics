data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1 #count= count +1   #進度條
        if count % 10000 == 0:  #如果count是10000配數就印出來
            print (len(data))
print('檔案讀取完成共有',len(data),'筆資料')


#計算留言平均長度
sum = 0
for d in data: #將data裡面每一個字提出來
    sum = sum + len(d)
    if sum % 100000000 == 0:
        print(len(sum)) #總共有這些數字

print('每筆平均留言長度是',sum/len(data))




#print(len(data)) #印出流言有幾筆
#print(data[0])#印出清單第一筆 清單索引從0開始
#print('---------------------------------------------')
#print(data[1])
#ctrl+c 鍵盤強制阻斷


