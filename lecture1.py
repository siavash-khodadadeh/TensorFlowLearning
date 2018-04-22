import tensorflow as tf
# These imports are just to get rid of debugging warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#
#   3 ----|
#         |--(add)---> a
#   5 ----|
#

a = tf.add(3, 5)
print(a)

# Where is the graph?

g = tf.get_default_graph()


# Session

sess = tf.Session()
value_of_a = sess.run(a)
print(value_of_a)

# Having another graph

g = tf.Graph()

with g.as_default():
    b = tf.add(3, 6)

# This does not work
# sess = tf.Session()
# Create session for the corresponding graph
sess = tf.Session(graph=g)
print(sess.run(b))
