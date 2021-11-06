import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Zack Walker",
    version="0.0.1",
    author="Zack Walker",
    author_email="zackdavidwalker94@gmail.com",
    description="WG Organizer for FES40 WG TIM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZackDavidWalker/wgorganizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)