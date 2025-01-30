from types import ModuleType

import cloudcoil.models.sealed_secrets as sealed_secrets


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), sealed_secrets.__dict__.values()))
    assert modules, "No modules found in sealed_secrets"
