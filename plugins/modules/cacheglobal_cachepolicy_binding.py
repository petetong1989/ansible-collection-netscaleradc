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
module: cacheglobal_cachepolicy_binding
short_description: Binding Resource definition for describing association between
  cacheglobal and cachepolicy resources
description: Binding Resource definition for describing association between cacheglobal
  and cachepolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  globalbindtype:
    choices:
      - SYSTEM_GLOBAL
      - VPN_GLOBAL
      - RNAT_GLOBAL
      - APPFW_GLOBAL
    description:
      - '0'
    type: str
    default: SYSTEM_GLOBAL
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  invoke:
    description:
      - Invoke policies bound to a virtual server or a user-defined policy label.
        After the invoked policies are evaluated, the flow returns to the policy with
        the next priority. Applicable only to default-syntax policies.
    type: bool
  labelname:
    description:
      - Name of the label to invoke if the current policy rule evaluates to TRUE.
        (To invoke a label associated with a virtual server, specify the name of the
        virtual server.)
    type: str
  labeltype:
    choices:
      - reqvserver
      - resvserver
      - policylabel
    description:
      - Type of policy label to invoke.
    type: str
  policy:
    description:
      - Name of the cache policy.
    type: str
  precededefrules:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Specify whether this policy should be evaluated.
    type: str
    default: 'NO'
  priority:
    description:
      - Specifies the priority of the policy.
    type: float
  type:
    choices:
      - REQ_OVERRIDE
      - REQ_DEFAULT
      - RES_OVERRIDE
      - RES_DEFAULT
      - HTTPQUIC_REQ_OVERRIDE
      - HTTPQUIC_REQ_DEFAULT
      - HTTPQUIC_RES_OVERRIDE
      - HTTPQUIC_RES_DEFAULT
    description:
      - The bind point to which policy is bound. When you specify the type, detailed
        information about that bind point appears.
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
