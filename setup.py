import setuptools

setuptools.setup(
    name="simply-media-tools",
    version="0.0.1",
    author="Arsybai",
    description="Simply do something with your media file",
    packages=["mediaTools"],
    license="MIT",
    author_email="me@arsybai.com",
    url="https://github.com/Arsybai/simply-media-tools",
    keywords=[
        'mediaTools',
        'quicktools',
        'background remover',
        'video trimmer',
        'profile picture maker',
        'video cropper',
        'compress image',
        'video trimmer'
    ],
    install_requires=[
        'openCV-python',
        'pillow',
        'numpy',
        'moviepy'
    ]
)