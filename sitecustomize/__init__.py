# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

import os
import sys
import site

site.addsitedir(os.path.dirname(os.path.join(os.path.realpath(__file__), "..")))
# Work around https://bugs.python.org/issue7744
# by moving  local_site_packages to the front of sys.path
sys.path.insert(0, sys.path.pop())
