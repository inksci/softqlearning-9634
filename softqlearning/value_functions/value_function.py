import tensorflow as tf

from rllab.core.serializable import Serializable

from softqlearning.misc.nn import MLPFunction


class NNVFunction(MLPFunction):
    def __init__(self,
                 env_spec,
                 hidden_layer_sizes=(100, 100),
                 name='value_function'):
        Serializable.quick_init(self, locals())

        self._Do = env_spec.observation_space.flat_dim
        self._observations_ph = tf.placeholder(
            tf.float32, shape=[None, self._Do], name='observations')

        super(NNVFunction, self).__init__(
            self._observations_ph,
            name=name,
            hidden_layer_sizes=hidden_layer_sizes)

    def eval(self, observations):
        return super(NNVFunction, self)._eval(observations)

    def output_for(self, observations, reuse=tf.AUTO_REUSE):
        return super(NNVFunction, self)._output_for(observations, reuse=reuse)


class NNQFunction(MLPFunction):
    def __init__(self,
                 env_spec,
                 hidden_layer_sizes=(100, 100),
                 name='q_function'):
        Serializable.quick_init(self, locals())

        self._Da = env_spec.action_space.flat_dim
        self._Do = env_spec.observation_space.flat_dim

        self._observations_ph = tf.placeholder(
            tf.float32, shape=[None, self._Do], name='observations')
        self._actions_ph = tf.placeholder(
            tf.float32, shape=[None, self._Da], name='actions')

        super(NNQFunction, self).__init__(
            self._observations_ph,
            self._actions_ph,
            name=name,
            hidden_layer_sizes=hidden_layer_sizes)

    def output_for(self, observations, actions, reuse=tf.AUTO_REUSE):
        return super(NNQFunction, self)._output_for(
            observations, actions, reuse=reuse)

    def eval(self, observations, actions):
        return super(NNQFunction, self)._eval(observations, actions)
