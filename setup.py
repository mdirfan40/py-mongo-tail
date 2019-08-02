import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-mongo-tail-irfan",
    version="0.0.1",
    author="Irfan",
    author_email="md.irfan40@gmail.com",
    description="Mongo DB tailable cursor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdirfan40/py-mongo-tail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)