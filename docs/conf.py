"""Sphinx configuration."""
project = "krml"
author = "Anthony So"
copyright = "2023, Anthony So"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
