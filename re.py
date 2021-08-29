#ctrl+c 鍵盤強制阻斷

data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1 #count= count +1   #進度條
        if count % 10000 == 0:  #如果count是10000配數就印出來
            print (len(data)) #印出流言有幾筆
print('檔案讀取完成共有',len(data),'筆資料')
print(data[0])     #印出清單第一筆 清單索引從0開始
print(data[1])    #印出清單第二筆
print('---------------------------------------------')


#計算留言平均長度
sum = 0
for d in data: #將data裡面每一個留言提出來
    sum = sum + len(d)
    if sum % 100000000 == 0:
        print(len(sum)) #總共有這些數字

print('每筆平均留言長度是',sum/len(data))
print('----------------------------------------------')


#篩選
new = []
for d in data: #將data清單裡每個留言都提出來
    if len(d) < 100: #如果清單留言每筆小於100
        new.append(d)
print('每筆留言小於100字的共有',len(new),'筆資料')
print(new[0]) #印出第一筆留言
print(new[1]) #印出第二筆留言
print('----------------------------------------------')

#篩選出good字的留言
good = []
for d in data:
    if 'good' in d: #檢查留言裡有good的
        good.append(d)
print('評價有good的共',len(good),'筆資料')
print(good[0])
print('--------------------------------------------')