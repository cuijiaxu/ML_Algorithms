import tensorflow as tf

alist = [[1, 2, 3, 4, 5, 6 ,7, 8],
         [7, 6 ,5 ,4 ,3 ,2, 1, 0],
         [3, 3, 3, 3, 3, 3, 3, 3],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [2, 2, 2, 2, 2, 2, 2, 2]]

aa = tf.reshape(alist,[-1,5*8])
print(aa)

with tf.Session() as asess:
    print(asess.run(aa))