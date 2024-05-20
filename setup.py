from setuptools import setup, find_packages

setup(
    name='TransMIL',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'addict==2.2.1',
        'albumentations==0.4.3',
        'einops==0.3.0',
        'matplotlib==3.5.1',
        'numpy==1.20.3',
        'nystrom-attention==0.0.9',
        'omegaconf==2.2.3',
        'opencv-python==4.2.0.34',
        'opencv-python-headless==4.2.0.34',
        'pandas==1.2.3',
        'Pillow==8.4.0',
        'pytorch-lightning==1.2.3',
    ],
    author='szc19990412',
    author_email='your@email.com',
    description='TransMIL: Transformer based Correlated Multiple Instance Learning for Whole Slide Image Classification',
    url='https://github.com/szc19990412/TransMIL',
)