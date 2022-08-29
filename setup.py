import setuptools

import plazmixsdk

setuptools.setup(
    name='plazmixsdk',
    author="Krashe85",
    description='Plazmix Python SDK',
    author_email='development@plazmix.space',
    url="https://gitlab.plazmix.space/",
    version=plazmixsdk.__version__,
    packages=setuptools.find_packages(),
    python_requires='>=3.10',
    include_package_data=True,
    install_requires=[
        "requests>=2.27.1",
        "Flask-SQLAlchemy>=2.4.4",
        "pydantic>=1.9.0"
    ],
)