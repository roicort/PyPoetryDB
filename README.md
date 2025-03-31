# PyPoetryDB

PyPoetryDB is a Python library for interacting with the [PoetryDB API](https://poetrydb.org). It allows you to fetch information about authors, titles, and poems from the PoetryDB database.

## Features

- List all authors available in the PoetryDB.
- List all poem titles available in the PoetryDB.
- Fetch poems by a specific author.
- Fetch a specific poem by its title.

## Installation

To install PyPoetryDB from [github](https://github.com/roicort/PyPoetryDB), you can use pip:

```bash
!pip install -e git+https://github.com/roicort/PyPoetryDB.git#egg=PyPoetryDB
```
or clone the repository and install it locally:

```bash
pip install -e .
```

## Usage

```python
# Import the PoetryDB class from the poetrydb module

from PyPoetryDB import PoetryDB

# Create an instance of the PoetryDB class
poetrydb = PoetryDB.API()

# List all authors available in the PoetryDB
authors = poetrydb.list_authors()
print(authors)
# List all poem titles available in the PoetryDB
titles = poetrydb.list_titles()
print(titles)
# Fetch poems by a specific author
poems_by_author = poetrydb.list_author_titles('Edgar Allan Poe')
print(poems_by_author)
# Fetch a specific poem by its title
poem = poetrydb.get_poem('The Raven')
print(poem)
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## Acknowledgements
- [PoetryDB](https://poetrydb.org) for providing the API.
- [requests](https://docs.python-requests.org/en/latest/) for making HTTP requests.
