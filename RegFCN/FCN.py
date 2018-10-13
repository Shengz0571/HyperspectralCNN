# coding=utf-8
from __future__ import print_function
import tensorflow as tf
import numpy as np
 
import TensorflowUtils as utils
import read_MITSceneParsingData as scene_parsing
import datetime
import BatchDatsetReader as dataset
from six.moves import xrange

# dropout保留率
keep_probability = tf.placeholder(tf.float32, name="keep_probabilty")
# 图像占坑
image = tf.placeholder(tf.float32, shape=[None, IMAGE_SIZE, IMAGE_SIZE, 3], name="input_image")
# 标签占坑
annotation = tf.placeholder(tf.int32, shape=[None, IMAGE_SIZE, IMAGE_SIZE, 1], name="annotation")

print("111")