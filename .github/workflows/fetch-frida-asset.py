# This script needs to be run at root of repo

import requests
import subprocess
import tarfile
import re
import io
import os
import time

from _github_api_helper import github_api_get

## It's now directly included instead of manually updating

# print("Updating frida.d.ts...")
# pkgInfo = requests.get('https://registry.npmjs.org/@types/frida-gum').json()
# latestVer = pkgInfo["dist-tags"]['latest']
# pkgTarUrl = pkgInfo['versions'][latestVer]['dist']['tarball']
# pkgTarContent = requests.get(pkgTarUrl).content
# with tarfile.open(fileobj=io.BytesIO(pkgTarContent), mode='r:gz') as pkgTar:
#     fridaDef = pkgTar.extractfile('frida-gum/index.d.ts').read()

# with open('./Fermion/src/lang/frida.d.ts', 'wb') as f:
#     f.write(fridaDef)


#
# The old javascript-api.md update logic
#

# print("Updating javascript-api.md...")
# changes = github_api_get('https://api.github.com/repos/frida/frida-website/commits?path=_i18n/en/_docs/javascript-api.md')
# commitDate = changes[0]['commit']['committer']['date']
# 
# With CRLF or not, that a problem
# with open('./Fermion/src/docs/readme.txt', 'wb') as f:
#     f.write((
#         "Source      : https://github.com/frida/frida-website/blob/master/_i18n/en/_docs/javascript-api.md\n" + \
#         "Doc Version : Last commit " + commitDate).encode())

# jsReadme = requests.get('https://github.com/frida/frida-website/raw/main/_i18n/en/_docs/javascript-api.md').content
# with open('./Fermion/src/docs/javascript-api.md', 'wb') as f:
#     f.write(jsReadme)

print("Updating docs.html...")
docPage = requests.get('https://frida.re/docs/javascript-api/').text
docContent = re.findall(r'<h2 id="table-of-contents">Table of contents</h2>([\S\s]+?)<div class="section-nav">', docPage)[0]

DOC_CONTENT_MARKER = '<!-- FRIDA_DOC_REPLACE_MARKER -->'
with open('./Fermion/pages/docs.html.template', 'r') as f:
    docTemplate = f.read()

docOutput = docTemplate.replace(DOC_CONTENT_MARKER, docContent)
with open('./Fermion/pages/docs.html', 'w') as f:
    # f.write("<!-- AUTO GENERATED FILE, EDIT docs.html.template INSTEAD -->\n")
    f.write(docOutput)
