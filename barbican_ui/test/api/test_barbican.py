# Copyright 2024 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0

from types import SimpleNamespace

from barbican_ui.api import barbican


def _request_with_catalog(catalog):
    return SimpleNamespace(user=SimpleNamespace(service_catalog=catalog))


def test_barbicanclient_returns_none_when_key_manager_not_in_catalog():
    request = _request_with_catalog([])

    assert barbican.barbicanclient(request) is None
