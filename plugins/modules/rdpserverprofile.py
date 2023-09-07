#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: rdpserverprofile
short_description: Configuration for RDP serverprofile resource.
description: Configuration for RDP serverprofile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  name:
    description:
      - The name of the rdp server profile
    type: str
  psk:
    description:
      - Pre shared key value
    type: str
  rdpip:
    description:
      - IPv4 or IPv6 address of RDP listener. This terminates client RDP connections.
    type: str
  rdpport:
    description:
      - TCP port on which the RDP connection is established.
    type: float
    default: 3389
  rdpredirection:
    choices:
      - ENABLE
      - DISABLE
    description:
      - Enable/Disable RDP redirection support. This needs to be enabled in presence
        of connection broker or session directory with IP cookie(msts cookie) based
        redirection support
    type: str
    default: DISABLE
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
