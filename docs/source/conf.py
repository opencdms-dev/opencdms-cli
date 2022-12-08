# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'pyopencdms documentation'
copyright = '2021, OpenCDMS Project'
author = 'OpenCDMS Project'

# The full version, including alpha/beta/rc tags
release = '0.1.0-alpha'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.duration",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    # "sphinx_copybutton",
    "sphinx.ext.napoleon",
    # "sphinx_panels"
]

templates_path = ['_templates']
exclude_patterns = []

# -- Napoleon extension -------------------------------------------------------
# See https://sphinxcontrib-napoleon.readthedocs.io/en/latest/sphinxcontrib.napoleon.html
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True  # includes dunders in api doc
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None

# -- spellingextension --------------------------------------------------------
# See https://sphinxcontrib-spelling.readthedocs.io/en/latest/customize.html
spelling_lang = "en_GB"
# The lines in this file must only use line feeds (no carriage returns).
spelling_word_list_filename = ["spelling_allow.txt"]
spelling_show_suggestions = False
spelling_show_whole_line = False
spelling_ignore_importable_modules = True
spelling_ignore_python_builtins = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_logo = "_static/opencdms.svg"
html_favicon = "_static/opencdms.svg"

html_sidebars = {
    "**": [
        "custom_sidebar_logo_version",
        "search-field",
        "sidebar-nav-bs",
        "sidebar-ethical-ads",
    ]
}

# See https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/configuring.html
html_theme_options = {
    "footer_items": ["copyright", "sphinx-version", "custom_footer"],
    # "collapse_navigation": True,
    # "navigation_depth": 3,
    # "show_prev_next": True,
    "navbar_align": "content",
    "github_url": "https://github.com/SciTools/iris",
    "twitter_url": "https://twitter.com/scitools_iris",
    # icons available: https://fontawesome.com/v5.15/icons?d=gallery&m=free
    "icon_links": [
        {
            "name": "GitHub Discussions",
            "url": "https://github.com/SciTools/iris/discussions",
            "icon": "far fa-comments",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/scitools-iris/",
            "icon": "fas fa-box",
        },
        {
            "name": "Conda",
            "url": "https://anaconda.org/conda-forge/iris",
            "icon": "fas fa-boxes",
        },
    ],
    "use_edit_page_button": True,
    "show_toc_level": 1,
}

html_context = {
    # pydata_theme
    "github_repo": "iris",
    "github_user": "scitools",
    "github_version": "main",
    "doc_path": "docs/src",
    # # custom
    # "on_rtd": on_rtd,
    # "rtd_version": rtd_version,
    # "rtd_version_type": rtd_version_type,
    # "version": version,
    # "copyright_years": copyright_years,
    # "python_version": build_python_version,
    # "commit_sha": commit_sha,
}