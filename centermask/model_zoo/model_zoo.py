# Copyright (c) Facebook, Inc. and its affiliates.
import os
from typing import Optional
import pkg_resources
import torch

from detectron2.checkpoint import DetectionCheckpointer
from centermask.config import get_cfg
from detectron2.modeling import build_model


class _ModelZooUrls(object):
    """
    Mapping from names to officially released Detectron2 pre-trained models.
    """

    S3_PREFIX = "https://dl.dropbox.com/s/"

    # format: {config_path.yaml} -> model_id/model_final_{commit}.pkl
    # https://dl.dropbox.com/s/
    CONFIG_PATH_TO_URL_SUFFIX = {
        "centermask/centermask_lite_V_39_eSE_FPN_ms_4x.yaml": "uwc0ypa1jvco2bi/centermask2-lite-V-39-eSE-FPN-ms-4x.pth",
        "centermask/centermask_lite_V_19_eSE_FPN_ms_4x.yaml ": "dret2ap7djty7mp/centermask2-lite-V-19-eSE-FPN-ms-4x.pth",
        "centermask/centermask_V_39_eSE_FPN_ms_3x.yaml" : "tczecsdxt10uai5/centermask2-V-39-eSE-FPN-ms-3x.pth"
    }


def get_checkpoint_url(config_path):
    """
    Returns the URL to the model trained using the given config

    Args:
        config_path (str): config file name relative to centermask's "configs/"
            directory, e.g., "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml"

    Returns:
        str: a URL to the model
    """
    name = config_path.replace(".yaml", "")
    if config_path in _ModelZooUrls.CONFIG_PATH_TO_URL_SUFFIX:
        suffix = _ModelZooUrls.CONFIG_PATH_TO_URL_SUFFIX[config_path]
        return _ModelZooUrls.S3_PREFIX + "/" + suffix
    raise RuntimeError("{} not available in Model Zoo!".format(name))


def get_config_file(config_path):
    """
    Returns path to a builtin config file.

    Args:
        config_path (str): config file name relative to centermask's "configs/"
            directory, e.g., "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml"

    Returns:
        str: the real path to the config file.
    """
    cfg_file = pkg_resources.resource_filename(
        "centermask.model_zoo", os.path.join("configs", config_path)
    )
    if not os.path.exists(cfg_file):
        raise RuntimeError("{} not available in Model Zoo!".format(config_path))
    return cfg_file