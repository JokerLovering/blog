from setuptools import setup
from studiorxgy_blog import __version__


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="studiorxgy_blog",
    fullname='studiorxgy_blog',
    author='JokerLovering',  # 替换为您的名字
    version=__version__,
    author_email='wuzhenhao.china@outlook.com',  # 替换为您的邮箱
    url='https://github.com/JokerLovering/blog/tree/blog',  # 替换为您的仓库链接
    description="I want us to be together, for as long as we've got.",  # 替换为主题简短描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=[
        'mkdocs>=1.5.2'
    ],
    packages=["studiorxgy_blog"],  # 替换为您的主题文件夹名称
    package_data={'studiorxgy_blog': ['*','*/*','*/*/*']},  # 如果需要的话，可以保留不变
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=True,
    entry_points={
        'mkdocs.themes': [
            'studiorxgy_blog = studiorxgy_blog',  # 替换为主题名称和文件夹名称
        ]
    },
)
