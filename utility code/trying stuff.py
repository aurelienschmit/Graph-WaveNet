import torch as t

a = t.randn(4, 3, 32, 32) 

#print(a.shape)

s= t.sigmoid(a)
print(s.shape)