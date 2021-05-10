from setuptools import setup, find_packages

setup(
    name="oAuthPlayground",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "colorlog==5.0.1",
        "uvicorn==0.13.4",
        "pyjwt[crypto]==2.1.0",
        "blacksheep==1.0.3",
        "python-dotenv==0.17.1",
    ],
    extras_require={
        "test": ["black==21.5b0", "pytest==6.2.4"],
    },
)
