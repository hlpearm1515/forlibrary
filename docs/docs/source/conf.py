import os
import sys
# [수정됨] src 폴더가 아니라 프로젝트 최상위 폴더(../../)를 바라보게 설정
sys.path.insert(0, os.path.abspath('../../'))

# [수정됨] 프로젝트 이름 변경
project = 'ForLibrary'
copyright = '2024, Team Name'
author = 'Team Name'
release = '0.1'

# 확장 기능 (그대로 유지)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = []

# 테마 설정 (그대로 유지)
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']