import attr
import math

import tensorflow as tf

logit_laplace_eps: float = 0.1

def map_pixels(x: tf.Tensor) -> tf.Tensor:
	if len(x.shape) != 4:
		raise ValueError('expected input to be 4d')
	if x.dtype != tf.float:
		raise ValueError('expected input to have type float')

	return (1 - 2 * logit_laplace_eps) * x + logit_laplace_eps

def unmap_pixels(x: tf.Tensor) -> tf.Tensor:
	if len(x.shape) != 4:
		raise ValueError('expected input to be 4d')
	if x.dtype != tf.float:
		raise ValueError('expected input to have type float')

	return tf.clip_by_value((x - logit_laplace_eps) / (1 - 2 * logit_laplace_eps), 0, 1)