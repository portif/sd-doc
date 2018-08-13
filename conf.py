from recommonmark.parser import CommonMarkParser
extensions = ['sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinx.ext.githubpages']
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
source_parsers = {'.md': CommonMarkParser}
master_doc = 'index'
project = u'Sistemas Distribuídos'
copyright = u'2018, AUTOR'
author = u'AUTOR'
version = u'2018.1'
release = u'2018.1'
language = 'pt_BR'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
        }
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}
htmlhelp_basename = 'sd-2018-2'
latex_elements = {
}
latex_documents = [
    (master_doc, 'sd-2018-2.tex', u'Sistemas Distribuídos',
     u'AUTOR', 'manual'),
]
man_pages = [
    (master_doc, 'sd-2018-2', u'Sistemas Distribuídos',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'sd-2018-2', u'Sistemas Distribuídos',
     author, 'sd-2018-2', 'One line description of project.',
     'Miscellaneous'),
]
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
