# Copyright 2015-2021 Florian Bruhin (The Compiler) <mail@qutebrowser.org>:
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

"""pytest fixtures for tests.keyinput."""

import pytest

import contextlib
from qutebrowser.keyinput import keyutils


BINDINGS = {'prompt': {'<Ctrl-a>': 'message-info ctrla',
                       'a': 'message-info a',
                       'ba': 'message-info ba',
                       'ax': 'message-info ax',
                       'ccc': 'message-info ccc',
                       'yY': 'yank -s',
                       '0': 'message-info 0',
                       '1': 'message-info 1'},
            'command': {'foo': 'message-info bar',
                        '<Ctrl+X>': 'message-info ctrlx'},
            'normal': {'a': 'message-info a', 'ba': 'message-info ba'}}
MAPPINGS = {
    'x': 'a',
    'b': 'a',
}


@pytest.fixture
def keyinput_bindings(config_stub, key_config_stub):
    """Register some test bindings."""
    config_stub.val.bindings.default = {}
    config_stub.val.bindings.commands = dict(BINDINGS)
    config_stub.val.bindings.key_mappings = dict(MAPPINGS)


@pytest.fixture
def pyqt_enum_workaround():
    """Get a context manager to ignore invalid key errors and skip the test.

    WORKAROUND for
    https://www.riverbankcomputing.com/pipermail/pyqt/2022-April/044607.html
    """
    @contextlib.contextmanager
    def _pyqt_enum_workaround(exctype=keyutils.InvalidKeyError):
        try:
            yield
        except exctype as e:
            pytest.skip(f"PyQt enum workaround: {e}")

    return _pyqt_enum_workaround
