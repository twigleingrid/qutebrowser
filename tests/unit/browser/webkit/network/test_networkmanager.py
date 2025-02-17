# Copyright 2015-2021 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
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

from qutebrowser.browser.webkit.network import networkmanager
from qutebrowser.browser.webkit import cookies


pytestmark = pytest.mark.usefixtures('cookiejar_and_cache')


def test_init_with_private_mode(fake_args):
    nam = networkmanager.NetworkManager(win_id=0, tab_id=0, private=True)
    assert isinstance(nam.cookieJar(), cookies.RAMCookieJar)
    assert nam.cache() is None
