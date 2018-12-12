#!/usr/bin/env python 
# -*- coding: utf-8 -*-

################################################################################
                        ##sha256 for BCO##
""" """
################################################################################

import hashlib
import sys, json

#______________________________________________________________________________#
def json_parse( filename ):
    """removes top level fields from BCO and returns a string"""
    
    with open(filename, 'rb') as f:
        data = json.load(f)
        bco_id, bco_spec = data['bco_id'], data['bco_spec_version']
        del data['bco_id'], data['checksum'], data['bco_spec_version']
    return data, bco_id, bco_spec
#______________________________________________________________________________#
def sha256_checksum( string ):
    """input to hash"""
    
    sha256 = hashlib.sha256()
    sha256.update(json.dumps(string))
    return sha256.hexdigest()
#______________________________________________________________________________#
def main():
    for bco in sys.argv[1:]:
        data, bco_id, bco_spec = json_parse(bco)
        checksum = sha256_checksum(data)
        print(bco + '\t' + checksum)
        data['bco_id'], data['checksum'], data['bco_spec_version'] =  bco_id, checksum, bco_spec
        with open('checksum_'+bco, 'w') as outfile:
            json.dump(data, outfile)

#______________________________________________________________________________#
if __name__ == '__main__':
    main()