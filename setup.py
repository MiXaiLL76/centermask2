from setuptools import find_packages, setup
import shutil
import os
from os import path
from typing import List
import glob

def get_model_zoo_configs() -> List[str]:
    """
    Return a list of configs to include in package for model zoo. Copy over these configs inside
    centermask/model_zoo.
    """

    # Use absolute paths while symlinking.
    source_configs_dir = path.join(path.dirname(path.realpath(__file__)), "configs")
    destination = path.join(
        path.dirname(path.realpath(__file__)), "centermask", "model_zoo", "configs"
    )
    # Symlink the config directory inside package to have a cleaner pip install.

    # Remove stale symlink/directory from a previous build.
    if path.exists(source_configs_dir):
        if path.islink(destination):
            os.unlink(destination)
        elif path.isdir(destination):
            shutil.rmtree(destination)

    if not path.exists(destination):
        try:
            os.symlink(source_configs_dir, destination)
        except OSError:
            # Fall back to copying if symlink fails: ex. on Windows.
            shutil.copytree(source_configs_dir, destination)

    config_paths = glob.glob("configs/**/*.yaml", recursive=True)
    return config_paths


setup(
   name='centermask',
   version='2.0',
   description='CenterMask2 is an upgraded implementation on top of detectron2 beyond original CenterMask based on maskrcnn-benchmark',
   author='build by MiXaiLL76',
   author_email='https://github.com/youngwanLEE/centermask2',
   packages=find_packages(exclude=("configs", "tests*")), 
   package_data={"centermask.model_zoo": get_model_zoo_configs()},
   install_requires=['detectron2'], #external packages as dependencies
)