#!/usr/bin/env python
##
## License.txt generator
##


from __future__ import print_function
from future.utils import iteritems
from six import iteritems
import yaml
import os

class LicenseGenerator(object):
    """docstring for LicenseGenerator"""
    def __init__(self, config):
        super(LicenseGenerator, self).__init__()
        self.config = os.path.abspath(config) 
        self.config_dir = os.path.dirname(self.config)

    def generate(self):
        with open(self.config, 'r') as stream:
            data = yaml.load(stream)
            for filename in data: # each file to generate
                with open(os.path.join(self.config_dir, "".join([filename ,".license.txt"])), 'w') as output:
                    for (name, options) in iteritems(data[filename]):
                        license_filename = options['file']
                        license_title = options['title'] if 'title' in options != "" else name
                        output.write("/** ")
                        output.write(license_title)
                        output.write(" **/\n\n")
                        with open(os.path.join(self.config_dir, license_filename),'r') as inputlicense:
                            output.write(inputlicense.read())
                        output.write("\n\n\n")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='License.txt generator')
    parser.add_argument('config', type=str)
    args = parser.parse_args()
    
    license = LicenseGenerator(args.config)
    license.generate()


if __name__ == '__main__':
    main()





