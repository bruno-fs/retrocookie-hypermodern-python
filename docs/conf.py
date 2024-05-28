"""Sphinx configuration."""

project = "Retrocookie Hypermodern Python"
author = "Bruno Ciconelle"
copyright = "2024, Bruno Ciconelle"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
