import tensorflow as tf
import keras as K
from keras.engine.saving import load_model
from keras.utils import plot_model
from tensorflow.python.framework import graph_util


model = load_model('Best_motanaby4.h5')
#plot_model(model, to_file='model.png')

graph = tf.get_default_graph()
input_graph_def = graph.as_graph_def()
sess = tf.Session()

output_node_names="Softmax:0"
output_graph_def = graph_util.convert_variables_to_constants(
            sess, # The session
            input_graph_def, # input_graph_def is useful for retrieving the nodes
            output_node_names.split(",")
)

output_graph = "/motanaby-model.pb"
with tf.gfile.GFile(output_graph, "wb") as f:
    f.write(output_graph_def.SerializeToString())

sess.close()