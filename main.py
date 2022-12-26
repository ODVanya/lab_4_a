ll = [[1,2,3], [3,4,5], [5,6,7], [7,8,9]]
ls = [set(l) for l in ll]

su = ls[0]
ssd = ls[0]
for s in ls[1:]:
  su = su.union(s)
  ssd = ssd.symmetric_difference(s)

result = su.difference(ssd)
print (result)