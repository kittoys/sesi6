#!/usr/bin/env python
# coding: utf-8

# In[1]:


umur = int(input('Masukan umur = '))

if umur <= 2 :
    print ('dilarang masuk')

elif umur <= 4 :
    tinggi_badan = int(input('Masukan tinggi badan = '))
    harga = 30000
    if tinggi_badan >= 70:
        print("total bayar kamu RP.", harga + 10000)
    else:
        print("total bayar kamu",harga)

elif umur<= 7 :
    tinggi_badan = int(input('Masukan tinggi badan = '))
    harga = 40000
    if tinggi_badan >= 120:
        print("total bayar kamu RP.", harga + 15000)
    else:
        print("total bayar kamu",harga)
        
elif umur <= 10 :
    tinggi_badan = int(input('Masukan tinggi badan = '))
    harga = 40000
    if tinggi_badan >= 150:
        print("total bayar kamu RP.",harga + 20000)
    else:
        print("total bayar kamu",harga)
        
else:
    harga = 80000
    print("total bayar kamu", harga)


# In[2]:


lari = 60/5
push_upA = 200/30
push_up = round(200/30,0)
plank = 5
menit = 0
menit1 = 0
menit2 = 0
menit3 = 0

print('''Kalori per menit
lari = {} kalori.
push up = {} kalori atau {} kalori.
plank = {} kalori.
'''.format(lari,push_upA,push_up,plank))
print('==================================')
print("1.lari saja")
print("2.lari dan push up")
print("3.lari dan plank")
print("4.push up dan plank")
print("5.lari, push up, dan plank")
print('==================================')

#pilihan
pilihan = int(input("Masukan pilihan olahraga :"))

#pilihan 1
if pilihan == 1:
    menit += int(input('Masukan berapa lama anda lari(menit) :'))
    lari *= menit
    print('Jumlah kalori yang dibakar setelah anda lari selama {} menit adalah {} kalori'.format(menit,lari))
          
#pilihan 2
elif pilihsn == 2:
          menit1 += int(input('Masukan berapa lama anda lari(menit) :'))
          lari *= menit1
          print('- Kalori yang di bakar = ',lari)
          menit2 += int(input('Masukan berapa lama anda push up(menit) :'))
          push_up *= menit2
          print('- Kalori yang di bakar = ',push_up)
          print('Jumlah kalori yang di bakar setelah anda lari dan push up selama {} menit adalah {} kalori'.format(menit1+menit2,lari+push_up))
                
#pilihan 3
elif pilihan == 3:
     menit1 += int(input('Masukan berapa lama anda lari(menit) :'))
     lari *= menit1
     print('- Kalori yang di bakar = ',lari)
     menit2 += int(input('Masukan berapa lama anda plank(menit) :'))
     plank *= menit2           
     print('- Kalori yang di bakar = ',plank)
     print('Jumlah kalori yang dibakar setelah anda lari dan plank selama {} menit adalah {} kalori'.format(menit1+menit2,lari+plank))

#pilihan 4
elif pilihan == 4:
     menit1 = int(input('Masukan berapa lama anda push up(menit) :'))
     push_up *= menit1
     print('- Kalori yang di bakar = ',push_up)      
     menit2 = int(input('Masukan berapa lama anda plank(menit) :'))      
     plank *= menit2      
     print('- Kalori yang di bakar =',plank)      
     print('Jumlah kalori yang dibakar setelah anda push_up dan plank selama {} menit adalah {} kalori'.format(menit1+menit2,push_up+plank))

#pilihan 5
elif pilihan == 5:
    menit1 = int(input('Masukan berapa lama anda lari(menit):'))
    lari *= menit1
    print('- Kalori yang di bakar = ',lari)
    menit2 = int(input('Masukan berapa lama anda push up(menit) :'))
    push_up *= menit2
    print('- Kalori yang di bakar =',push_up)
    menit3 = int(input('Masukan berapa lama anda plank(menit) :'))
    plank *= menit3
    print('- Kalori yang di bakar =',plank)
    print('Jumlah kalori yang dibakar setelah anda lari,push up, dan plank selama {} menit adalah {} kalori'.format(menit1+menit2+menit3,lari+push_up+plank))
else:
    print('Input salah')


# In[ ]:




