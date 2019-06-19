import tensorflow as tf 
#creating computation graphs
#python is slow
#c++ is fast
#tensorflow makes computation in python fast




#constants
x1=tf.constant(5)
x2=tf.constant(6)
#result=x1*x2 also works but is not encouraged
result=tf.multiply(x1,x2)
print(result)
# to run a session
sess=tf.Session()
print(sess.run(result))
sess.close()





