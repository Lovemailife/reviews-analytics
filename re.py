data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1 #count= count +1   #進度條
        if count % 10000 == 0:  #如果count是10000配數就印出來
            print (len(data))
print('檔案讀取完成共有',len(data),'筆資料')


#print(len(data)) #印出流言有幾筆
#print(data[0])#印出清單第一筆 清單索引從0開始
#print('---------------------------------------------')
#print(data[1])
#ctrl+c 鍵盤強制阻斷


