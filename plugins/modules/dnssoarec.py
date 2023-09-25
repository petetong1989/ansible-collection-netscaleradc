#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: dnssoarec
short_description: Configuration for SOA record resource.
description: Configuration for SOA record resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  contact:
    description:
      - Email address of the contact to whom domain issues can be addressed. In the
        email address, replace the @ sign with a period (.). For example, enter domainadmin.example.com
        instead of domainadmin@example.com.
    type: str
  domain:
    description:
      - Domain name for which to add the SOA record.
    type: str
  ecssubnet:
    description:
      - Subnet for which the cached SOA record need to be removed.
    type: str
  expire:
    description:
      - Time, in seconds, after which the zone data on a secondary name server can
        no longer be considered authoritative because all refresh and retry attempts
        made during the period have failed. After the expiry period, the secondary
        server stops serving the zone. Typically one week. Not used by the primary
        server.
    type: float
    default: 3600
  minimum:
    description:
      - Default time to live (TTL) for all records in the zone. Can be overridden
        for individual records.
    type: float
    default: 5
  nodeid:
    description:
      - Unique number that identifies the cluster node.
    type: float
  originserver:
    description:
      - Domain name of the name server that responds authoritatively for the domain.
    type: str
  refresh:
    description:
      - Time, in seconds, for which a secondary server must wait between successive
        checks on the value of the serial number.
    type: float
    default: 3600
  retry:
    description:
      - Time, in seconds, between retries if a secondary server's attempt to contact
        the primary server for a zone refresh fails.
    type: float
    default: 3
  serial:
    description:
      - The secondary server uses this parameter to determine whether it requires
        a zone transfer from the primary server.
    type: float
    default: 100
  ttl:
    description:
      - Time to Live (TTL), in seconds, for the record. TTL is the time for which
        the record must be cached by DNS proxies. The specified TTL is applied to
        all the resource records that are of the same record type and belong to the
        specified domain name. For example, if you add an address record, with a TTL
        of 36000, to the domain name example.com, the TTLs of all the address records
        of example.com are changed to 36000. If the TTL is not specified, the Citrix
        ADC uses either the DNS zone's minimum TTL or, if the SOA record is not available
        on the appliance, the default value of 3600.
    type: float
    default: 3600
  type:
    choices:
      - ALL
      - ADNS
      - PROXY
    description:
      - 'Type of records to display. Available settings function as follows:'
      - '* C(ADNS) - Display all authoritative address records.'
      - '* C(PROXY) - Display all proxy address records.'
      - '* C(ALL) - Display all address records.'
    type: str
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
failed:
    description: Indicates if the module failed or not
    returned: always
    type: bool
    sample: false
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()
