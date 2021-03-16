from setuptools import find_packages, setup


setup(
   name='centermask',
   version='2.0',
   description='CenterMask2 is an upgraded implementation on top of detectron2 beyond original CenterMask based on maskrcnn-benchmark',
   author='build by MiXaiLL76',
   author_email='https://github.com/youngwanLEE/centermask2',
   packages=find_packages(exclude=("configs", "tests*")), 
   install_requires=['detectron2'], #external packages as dependencies
)