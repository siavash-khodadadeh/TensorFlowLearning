# Amazing Tensorboard

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


#    (a + b) - c
#
#    a ----|
#          |--->(add) ---|
#    b ----|             |
#                        | ---(subtract)
#                        |
#    c ------------------|

def main():
    a = tf.constant([3., 4.])
    b = tf.constant([4., 6.])
    c = tf.constant([5., 8.])

    a_b_sum = tf.add(a, b)
    result = tf.subtract(a_b_sum, c)

# creatre tf.summary.FileWriter before running session

    writer = tf.summary.FileWriter('./lecture2/', tf.get_default_graph())
    sess = tf.Session()

    with sess.as_default():
        a_value = sess.run(a)
        result_value = sess.run(result)

        print('a: ' + str(a_value))
        print('result: ' + str(result_value))

    writer.close()


if __name__ == '__main__':
    main()
