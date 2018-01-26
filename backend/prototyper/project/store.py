import os
import json
from .initial import create_new_project


class Project(object):
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.name = os.path.basename(self.path)
        self.storage_path = os.path.join(self.path, '.djangoprototyper')
        self.storage_file = os.path.join(self.storage_path, 'project.json')
        self.init_storage()
    
    def init_storage(self):
        if os.path.exists(self.path) and not os.path.exists(self.storage_path):
            raise RuntimeError('Cannot init project. Path "%s" already exist and it is not djangoprototyper' % self.path)
        if not os.path.exists(self.path):
            self.init_new()
        else:
            self.load()  # pasing check
    
    def init_new(self):
        print ('Creating new project', self.name)
        os.makedirs(self.storage_path)
        data = create_new_project(self.name)
        self.save(data)
    
    def load(self):
        with open(self.storage_file, 'r') as f:
            return json.load(f)
    
    def save(self, data):
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=1)