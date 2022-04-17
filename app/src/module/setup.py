from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='module',
    version='0.0.0',
    description='"Hype" is all you need. The custom built library to support the Python codebase',
    license="MIT",
    long_description=long_description,
    author='José Fabra Valverde',
    author_email='contact@hypeisallyouneed.com',
    packages=[
        'module'
    ],
    install_requires=[

    ],
    packages=find_packages(
        exclude=[
            "docs",
            "tests",
            ".gitignore",
            "README.md",
            "Dockerfile",
            "install.bat",
            "install.sh",
        ]
    ),
)
