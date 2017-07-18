# -*- coding: utf-8 -*-
"""
    sphinx.util.typing
    ~~~~~~~~~~~~~~~~~~

    The composit types for Sphinx.

    :copyright: Copyright 2007-2017 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from typing import Callable, Dict, List, Tuple, Text

from docutils import nodes
from docutils.parsers.rst.states import Inliner

# common role functions
RoleFunction = Callable[[Text, Text, Text, int, Inliner, Dict, List[Text]],
                        Tuple[List[nodes.Node], List[nodes.Node]]]
