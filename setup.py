from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="convergence",
    version="0.1.0",
    author="ptxd",
    author_email="your.email@example.com",
    description="A package for converting machine learning data files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ptxd/convergence",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "numpy",
        "h5py",
        "protobuf",
        "tensorflow",
    ],
    extras_require={
        "test": [
            # Add your test dependencies here, e.g., "pytest>=5.0.0"
        ],
    },
)
