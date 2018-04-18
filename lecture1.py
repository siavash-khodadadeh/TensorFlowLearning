import tensorflow as tf


# Default graph is on the current thread
tf.get_default_graph()

a = tf.add(3, 5)
# Write a = 3 + 5
print(a)
# This is the line of code for executing it


# session lets us run our code
sess = tf.Session()
sess.run(a)
sess.close()


with tf.Session() as sess:
    sess.run(a)


g = tf.Graph()
with g.as_default():
    x = tf.add(3, 5)

# This does not work!

# sess = tf.Session()
# print(sess.run(x))
# sess.close()


# this works
sess = tf.Session(graph=g)
print(sess.run(x))
sess.close()


g = tf.Graph()
# add ops to the default graph
a = tf.constant(3)
# add ops to the user created graph
with g.as_default():
    b = tf.constant(5)

sess = tf.Session(graph=g)
print(sess.run(b))


g1 = tf.get_default_graph()
g2 = tf.Graph()

with g1.as_default():
    a = tf.constant(2)
    a1 = tf.constant(3)

with g2.as_default():
    a = tf.constant(10)
    a2 = tf.constant(4)


with tf.Session(graph=g1) as sess:
    # this does not work
    # print(sess.run(a))
    print(sess.run(a2))
