import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vicat_easy_mindoc", # Replace with your own username
    version="0.0.1",
    author="vicat",
    author_email="vicat47@qq.com",
    description="One of mindoc markdown uploader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zsb514/test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['vicat_easy_mindoc=easy_mindoc.easy_mindoc:main']
    },
    python_requires='>=3.6',
)