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
module: systemglobal_authenticationpolicy_binding
short_description: Binding Resource definition for describing association between
  systemglobal and authenticationpolicy resources
description: Binding Resource definition for describing association between systemglobal
  and authenticationpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  builtin:
    choices:
      - MODIFIABLE
      - DELETABLE
      - IMMUTABLE
      - PARTITION_ALL
    description:
      - Indicates that a variable is a built-in (SYSTEM INTERNAL) type.
    type: list
    elements: str
  feature:
    choices:
      - WL
      - WebLogging
      - SP
      - SurgeProtection
      - LB
      - LoadBalancing
      - CS
      - ContentSwitching
      - CR
      - CacheRedirection
      - SC
      - SureConnect
      - CMP
      - CMPcntl
      - CompressionControl
      - PQ
      - PriorityQueuing
      - HDOSP
      - HttpDoSProtection
      - SSLVPN
      - AAA
      - GSLB
      - GlobalServerLoadBalancing
      - SSL
      - SSLOffload
      - SSLOffloading
      - CF
      - ContentFiltering
      - IC
      - IntegratedCaching
      - OSPF
      - OSPFRouting
      - RIP
      - RIPRouting
      - BGP
      - BGPRouting
      - REWRITE
      - IPv6PT
      - IPv6protocoltranslation
      - AppFw
      - ApplicationFirewall
      - RESPONDER
      - push
      - NSPush
      - NetScalerPush
      - AppFlow
      - CloudBridge
      - ISIS
      - ISISRouting
      - CH
      - CallHome
      - AppQoE
      - ContentAccelerator
      - SYSTEM
      - RISE
      - FEO
      - LSN
      - LargeScaleNAT
      - RDPProxy
      - Rep
      - Reputation
      - URLFiltering
      - VideoOptimization
      - ForwardProxy
      - SSLInterception
      - AdaptiveTCP
      - CQA
      - CI
      - ContentInspection
      - Bot
      - APIGateway
    description:
      - The feature to be checked while applying this config
    type: str
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
        if the current policy rule evaluates to TRUE. Applicable only for advanced
        authentication policies
    type: str
  nextfactor:
    description:
      - On success invoke label. Applicable for advanced authentication policy binding
    type: str
  policyname:
    description:
      - The name of the  command policy.
    type: str
  priority:
    description:
      - The priority of the command policy.
    type: float
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
