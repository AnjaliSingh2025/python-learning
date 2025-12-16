lst=[10,20,'Bharath',-10,35,5]
print(lst)
# print(lst[3])
# print(lst[3:5])
print(len(lst))
print(lst*4)
lst.append(40)
print(lst)
lst.remove(40)
print(lst)
del(lst[4])
print(lst)






USE ubersmith;
SELECT COUNT(DISTINCT i.invid)
FROM CLIENT c
JOIN INVOICES i
    ON c.clientid = i.clientid
WHERE c.email NOT LIKE '%@jdiuk.com%'
  AND c.email NOT LIKE '%@justdevelop.it%'
  AND c.email NOT LIKE '%@endurance.com%'
  AND c.email NOT LIKE '%@newfold.com%'
  AND c.email NOT LIKE '%@jdiautomation.com%'
  AND c.email NOT LIKE '%@test.com%'
  AND i.amount IN (0,1)
  AND c.class_id IN (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,19,21,23,25,27,29,31,33,35,97);