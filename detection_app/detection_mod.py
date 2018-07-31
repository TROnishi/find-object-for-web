#!/usr/bin/env python
# coding:utf-8
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import chainer

from chainercv.datasets import voc_bbox_label_names
from chainercv.links import SSD300
from chainercv.links import SSD512
from chainercv import utils
import vis_bbox
import copy
import params
# from chainercv.visualizations import vis_bbox

import numpy as np

"""
chainercvのSSDを用いて物体検出及び認識を行う
"""
class Detection:
    def __init__(self):
        self.bridge = CvBridge()
        print("モデル読み込み中...")
        self.model = SSD300(
            n_fg_class=len(voc_bbox_label_names),
            pretrained_model="voc0712")
        print("読み込み完了")


    def detection(self, img):
        """
        入力：画像
        出力：認識結果の画像、htmlで表示用のパス
        """
        img_ = np.asarray(img)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

        img = np.asarray(img, dtype=np.float32)
        img = img.transpose(2,0,1)
        bboxes, labels, scores = self.model.predict([img])
        bbox, label, score = bboxes[0], labels[0], scores[0]

        result = vis_bbox.vis_bbox(img_, bbox, label, score, label_names=voc_bbox_label_names)

        height, width, _ = img_.shape

        result = cv2.resize(result, (width, height))
        save_path = params.result_save_path+'1.png'
        cv2.imwrite(save_path, result)
        print(save_path)
        return result, params.result_path+'1.png'