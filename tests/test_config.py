import os
from config import Config

def pytest_funcarg__config(request):
    tmpdir = request.getfuncargvalue('tmpdir')
    return Config(os.path.join(str(tmpdir), 'config.yaml'))

def test_set_get(config):
    config.set('mykey', 'myval')
    assert config.get('mykey', 'default') == 'myval'

def test_get_default(config):
    assert config.get('dne', 'default') == 'default'

def test_get_default_none(config):
    assert config.get('dne', None) == None

def test_set_get_object(config):
    obj = [0, 1, {'dictkey': 'dictval'}]
    config.set('myobj', obj)
    assert config.get('myobj', None) == obj

def test_set_is_in_sync(config):
    exis_config = Config(config.path)
    config.set('mykey', 'myval')
    new_config = Config(config.path)
    assert config.get('mykey', 1) is exis_config.get('mykey', 2)
    assert config.get('mykey', 4) is new_config.get('mykey', 3)

def test_diff_conf_for_diff_path(config):
    other = Config(config.path + 'other.yaml')
    config.set('mykey', 'myval')
    assert other.get('mykey', 'other') == 'other'

def test_file_written(config):
    config.set('mykey', 'myval')
    config.set('mykey2', 'myval2')
    with open(config.path, 'r') as f:
        assert len(f.read()) > 0

def test_unset(config):
    config.set('mykey', 'myval')
    config.unset('mykey')
    assert config.get('mykey', 'dne') == 'dne'
