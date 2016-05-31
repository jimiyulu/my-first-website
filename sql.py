import sqlite3
import random
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# area = ('海淀区', '朝阳区', '西城区', '东城区', '丰台区', '昌平区',)
# jw = (116.300, 39.900)
# pk = 1
# for i in range(len(area)):
#     mall_count = 1
#     for j in range(1, 20):
#         # print(area[random.randint(0, 5)] + '%03d' % mall_count)
#
#         this_area = area[random.randint(0, 5)]
#         this_name = this_area + '%03d' % mall_count
#         cursor.execute("INSERT INTO myapp_mall VALUES (?, ?, ?, ?, ?, ?, ?)",
#                        (pk, this_name, this_area, this_area, '', 116.3, 39.9))
#
#         mall_count += 1
#         pk += 1
cursor.execute('SELECT * FROM myapp_store')
store_all = cursor.fetchall()
for store in store_all:
    print(store)

# cursor.execute('SELECT * FROM myapp_mall')
# mall_all = cursor.fetchall()
# cursor.execute('SELECT * FROM myapp_brand')
# brand_all = cursor.fetchall()
# pk = 0
# for mall in mall_all:
#     L = []
#     for i in range(5):
#         while True:
#             brand = brand_all[random.randint(0, len(brand_all) - 1)]
#             if brand[0] not in L:
#                 L.append(brand[0])
#                 break
#         store_name = mall[1] + '-' + brand[1]
#         store_location = mall[3] + str(random.randint(1, 4)) + '层'
#         store_discount = float('%.1f' % random.uniform(0.1, 9.9))
#         cursor.execute("INSERT INTO myapp_store VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )",
#                        (pk, store_name, store_location, 1, store_discount, '', '', '', brand[0], 1, mall[0]))
#         pk += 1
#     L = []




cursor.close()
conn.commit()
conn.close()