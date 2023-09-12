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
module: sslcertreq
short_description: Configuration for certificate request resource.
description: Configuration for certificate request resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  challengepassword:
    description:
      - Pass phrase, embedded in the certificate signing request that is shared only
        between the client or server requesting the certificate and the SSL certificate
        issuer (typically the certificate authority). This pass phrase can be used
        to authenticate a client or server that is requesting a certificate from the
        certificate authority.
    type: str
  commonname:
    description:
      - Fully qualified domain name for the company or web site. The common name must
        match the name used by DNS servers to do a DNS lookup of your server. Most
        browsers use this information for authenticating the server's certificate
        during the SSL handshake. If the server name in the URL does not match the
        common name as given in the server certificate, the browser terminates the
        SSL handshake or prompts the user with a warning message.
      - Do not use wildcard characters, such as asterisk (*) or question mark (?),
        and do not use an IP address as the common name. The common name must not
        contain the protocol specifier <http://> or <https://>.
    type: str
  companyname:
    description:
      - Additional name for the company or web site.
    type: str
  countryname:
    description:
      - Two letter ISO code for your country. For example, US for United States.
    type: str
  digestmethod:
    choices:
      - SHA1
      - SHA256
    description:
      - Digest algorithm used in creating CSR
    type: str
  emailaddress:
    description:
      - Contact person's e-mail address. This address is publically displayed as part
        of the certificate. Provide an e-mail address that is monitored by an administrator
        who can be contacted about the certificate.
    type: str
  fipskeyname:
    description:
      - Name of the FIPS key used to create the certificate signing request. FIPS
        keys are created inside the Hardware Security Module of the FIPS card.
    type: str
  keyfile:
    description:
      - Name of and, optionally, path to the private key used to create the certificate
        signing request, which then becomes part of the certificate-key pair. The
        private key can be either an RSA or a DSA key. The key must be present in
        the appliance's local storage. /nsconfig/ssl is the default path.
    type: str
  keyform:
    choices:
      - DER
      - PEM
    description:
      - Format in which the key is stored on the appliance.
    type: str
    default: PEM
  localityname:
    description:
      - Name of the city or town in which your organization's head office is located.
    type: str
  organizationname:
    description:
      - Name of the organization that will use this certificate. The organization
        name (corporation, limited partnership, university, or government agency)
        must be registered with some authority at the national, state, or city level.
        Use the legal name under which the organization is registered.
      - 'Do not abbreviate the organization name and do not use the following characters
        in the name:'
      - Angle brackets (< >) tilde (~), exclamation mark, at (@), pound (#), zero
        (0), caret (^), asterisk (*), forward slash (/), square brackets ([ ]), question
        mark (?).
    type: str
  organizationunitname:
    description:
      - Name of the division or section in the organization that will use the certificate.
    type: str
  pempassphrase:
    description:
      - '0'
    type: str
  reqfile:
    description:
      - Name for and, optionally, path to the certificate signing request (CSR). /nsconfig/ssl/
        is the default path.
    type: str
  statename:
    description:
      - Full name of the state or province where your organization is located.
      - Do not abbreviate.
    type: str
  subjectaltname:
    description:
      - 'Subject Alternative Name (SAN) is an extension to X.509 that allows various
        values to be associated with a security certificate using a subjectAltName
        field. These values are called "Subject Alternative Names" (SAN). Names include:'
      - '      1. Email addresses'
      - '      2. IP addresses'
      - '      3. URIs'
      - '      4. DNS names (this is usually also provided as the Common Name RDN
        within the Subject field of the main certificate.)'
      - '      5. Directory names (alternative Distinguished Names to that given in
        the Subject)'
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
