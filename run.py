# read yaml file 

import yaml # pip install pyyaml
import pprint as pp

with open('conf.yml', 'r') as f:
    parse_yaml= yaml.safe_load(f)

pp.pprint(parse_yaml)