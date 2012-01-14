import os
import yaml
from threading import RLock

class Config:
    _conf_per_path = {}
    _lock = RLock()

    def __init__(self, path):
        self.path = path

    def _conf(self):
        with Config._lock:
            if self.path not in Config._conf_per_path:
                    # a+ opens file or creates it, but the stream is positioned at the end
                    with open(self.path, 'a+') as f:
                        f.seek(0)
                        Config._conf_per_path[self.path] = yaml.load(f) or {}
            return Config._conf_per_path[self.path]

    def get(self, key, default):
        with Config._lock:
            conf = self._conf()
            if key in conf:
                return conf[key]
            else:
                return default

    def set(self, key, value):
        with Config._lock:
            self._conf()[key] = value
            self._write_conf()

    def unset(self, key):
        with Config._lock:
            del self._conf()[key]
            self._write_conf()

    def _write_conf(self):
        with Config._lock:
            with open(self.path, 'w') as f:
                yaml.dump(self._conf(), f)
