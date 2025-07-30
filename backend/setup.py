# 🌱 Raiziomfix Core Engine – To be evolved into Raiziom

from setuptools import setup, find_packages
# 🧠 Core logic: part of Raiziom engine

setup(
    name='raiziomfix-backend',
    version='0.1.0',
    packages=find_packages("app"),
    package_dir={'': 'app'},
    install_requires=[
        'fastapi',
        'uvicorn[standard]',
        'python-dotenv',
        'httpx'
    ],
)
