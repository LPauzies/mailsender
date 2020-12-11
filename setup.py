import setuptools

with open("Readme.md", "r", encoding="utf-8") as readme_descriptor:
    long_description = readme_descriptor.read()

setuptools.setup(
    name = "emailsender",
    version = "1.0",
    author = "Lucas Pauzies",
    author_email = "lucas.pauzies@hotmail.fr",
    description = "A simple package to interact with mail sending",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/LPauzies/mailsender",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",
)