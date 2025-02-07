import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPO_NAME = "MLOps-End-To-End-Project"
AUTHOR_USER_NAME = "Asutosh"
SRC_REPO = "mlopsproject"
AUTHOR_EMAIL = "ashutoshsidhya69@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Mlpos foundation project",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/sidhyaashu/MLOps-End-To-End-Project.git",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)