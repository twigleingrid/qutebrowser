# Copyright 2017-2021 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <https://www.gnu.org/licenses/>.

import pytest

from qutebrowser.misc import objects
from qutebrowser.utils import usertypes


@pytest.mark.parametrize('func', [
    lambda: objects.NoBackend() == usertypes.Backend.QtWebEngine,
    lambda: objects.NoBackend() != usertypes.Backend.QtWebEngine,
    lambda: objects.NoBackend() in [usertypes.Backend.QtWebEngine],
])
def test_no_backend(func):
    with pytest.raises(AssertionError, match='No backend set!'):
        func()
