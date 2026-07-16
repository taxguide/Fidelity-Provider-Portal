# Configuration file for the Sphinx documentation builder.

project = 'Bankers Fidelity Provider Portal Guide'
author = 'Bankers Fidelity Provider Portal'
release = '1.0'

# Extensions
extensions = [
    "sphinx_sitemap",
]

# Templates
templates_path = ['_templates']

exclude_patterns = []

# Theme
html_theme = 'alabaster'

# Static files
html_static_path = ['_static']

# Language
language = 'en'

# Browser Title
html_title = "Bankers Fidelity Provider Portal Login & Eligibility (2026)"

# Sitemap
html_baseurl = "https://bankers-fidelity-provider-portal.readthedocs-hosted.com/en/latest/"
sitemap_url_scheme = "{link}"
