import os
import re


class Config:
    def __init__(self, config_path='/etc/httpd.conf'):
        self.config_path = config_path
        self.cpu_number = self.root = None
        if not os.path.exists(self.config_path):
            print('No config file at path: %s' % self.config_path)
        else:
            try:
                with open(self.config_path, 'r') as file:
                    data = file.read()
                    kv = data.split('\n')
                    options = {}
                    for v in kv:
                        if v:
                            (key, value) = re.search(r'\S* \S*', v).group(0).split(' ')
                            options[key] = value
                    self.cpu_number = int(options['cpu_limit'])
                    self.root = options['document_root']
                    self.address_port = (options['address'], int(options['port']))
                    self.queue = int(options['queue'])
                    self.receive_data_size = int(options['receive_data_size'])
            except Exception as e:
                print('Error in reading file:\n %s' % e)
