import tensorflow as tf


with tf.Session() as sess:

    a = tf.ones([10], name="a")
    b = tf.add(a, a, name="b")

    ''' concat example '''
    t1 = [[1, 2, 3], [4, 5, 6]]
    t2 = [[7,8,9], [10,11,12]]

    tt1 = tf.ones([2,3], tf.int32)
    tt2 = tf.constant(t1, tf.int32)
    print(tt1)
    print(tt2)

    t3 = tf.concat([t1, t2], 0)
    t4 = tf.concat([t1, t2], 1)

    print(t3)
    print(t4)
    sess = tf.Session()

    print(sess.run(t3))
    print(sess.run(t4))

    print("------")
    print(sess.run(tt1))
    print(sess.run(tt2))
    # sess = tf_debug.LocalCLIDebugWrapperSession(sess)
    sess.run(b)


