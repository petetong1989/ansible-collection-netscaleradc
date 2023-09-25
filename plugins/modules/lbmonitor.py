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
module: lbmonitor
short_description: Configuration for monitor resource.
description: Configuration for monitor resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  Snmpoid:
    description:
      - SNMP OID for SNMP monitors.
    type: str
  acctapplicationid:
    description:
      - List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request
        (CER) message to use for monitoring Diameter servers. A maximum of eight of
        these AVPs are supported in a monitoring message.
    type: list
  action:
    choices:
      - NONE
      - LOG
      - DOWN
    description:
      - 'Action to perform when the response to an inline monitor (a monitor of type
        HTTP-INLINE) indicates that the service is down. A service monitored by an
        inline monitor is considered C(DOWN) if the response code is not one of the
        codes that have been specified for the Response Code parameter. '
      - 'Available settings function as follows: '
      - '* C(NONE) - Do not take any action. However, the show service command and
        the show lb monitor command indicate the total number of responses that were
        checked and the number of consecutive error responses received after the last
        successful probe.'
      - '* C(LOG) - Log the event in NSLOG or SYSLOG. '
      - '* C(DOWN) - Mark the service as being down, and then do not direct any traffic
        to the service until the configured down time has expired. Persistent connections
        to the service are terminated as soon as the service is marked as C(DOWN).
        Also, log the event in NSLOG or SYSLOG.'
    type: str
    default: DOWN
  alertretries:
    description:
      - Number of consecutive probe failures after which the appliance generates an
        SNMP trap called monProbeFailed.
    type: int
  application:
    description:
      - Name of the application used to determine the state of the service. Applicable
        to monitors of type CITRIX-XML-SERVICE.
    type: str
  attribute:
    description:
      - Attribute to evaluate when the LDAP server responds to the query. Success
        or failure of the monitoring probe depends on whether the attribute exists
        in the response. Optional.
    type: str
  authapplicationid:
    description:
      - List of Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request
        (CER) message to use for monitoring Diameter servers. A maximum of eight of
        these AVPs are supported in a monitoring CER message.
    type: list
  basedn:
    description:
      - The base distinguished name of the LDAP service, from where the LDAP server
        can begin the search for the attributes in the monitoring query. Required
        for LDAP service monitoring.
    type: str
  binddn:
    description:
      - The distinguished name with which an LDAP monitor can perform the Bind operation
        on the LDAP server. Optional. Applicable to LDAP monitors.
    type: str
  customheaders:
    description:
      - Custom header string to include in the monitoring probes.
    type: str
  database:
    description:
      - Name of the database to connect to during authentication.
    type: str
  destip:
    description:
      - IP address of the service to which to send probes. If the parameter is set
        to 0, the IP address of the server to which the monitor is bound is considered
        the destination IP address.
    type: str
  destport:
    description:
      - TCP or UDP port to which to send the probe. If the parameter is set to 0,
        the port number of the service to which the monitor is bound is considered
        the destination port. For a monitor of type USER, however, the destination
        port is the port number that is included in the HTTP request sent to the dispatcher.
        Does not apply to monitors of type PING.
    type: int
  deviation:
    description:
      - Time value added to the learned average response time in dynamic response
        time monitoring (DRTM). When a deviation is specified, the appliance learns
        the average response time of bound services and adds the deviation to the
        average. The final value is then continually adjusted to accommodate response
        time variations over time. Specified in milliseconds, seconds, or minutes.
    type: float
  dispatcherip:
    description:
      - IP address of the dispatcher to which to send the probe.
    type: str
  dispatcherport:
    description:
      - Port number on which the dispatcher listens for the monitoring probe.
    type: int
  domain:
    description:
      - Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or
        Web Interface servers are present. Required by CITRIX-XD-DDC and CITRIX-WI-EXTENDED
        monitors for logging on to the DDC servers and Web Interface servers, respectively.
    type: str
  downtime:
    description:
      - Time duration for which to wait before probing a service that has been marked
        as DOWN. Expressed in milliseconds, seconds, or minutes.
    type: int
    default: 30
  evalrule:
    description:
      - 'Expression that evaluates the database server''s response to a MYSQL-ECV
        or MSSQL-ECV monitoring query. Must produce a Boolean result. The result determines
        the state of the server. If the expression returns TRUE, the probe succeeds. '
      - For example, if you want the appliance to evaluate the error message to determine
        the state of the server, use the rule MYSQL.RES.ROW(10) .TEXT_ELEM(2).EQ("MySQL").
    type: str
  failureretries:
    description:
      - Number of retries that must fail, out of the number specified for the Retries
        parameter, for a service to be marked as DOWN. For example, if the Retries
        parameter is set to 10 and the Failure Retries parameter is set to 6, out
        of the ten probes sent, at least six probes must fail if the service is to
        be marked as DOWN. The default value of 0 means that all the retries must
        fail if the service is to be marked as DOWN.
    type: int
  filename:
    description:
      - Name of a file on the FTP server. The appliance monitors the FTP service by
        periodically checking the existence of the file on the server. Applicable
        to FTP-EXTENDED monitors.
    type: str
  filter:
    description:
      - Filter criteria for the LDAP query. Optional.
    type: str
  firmwarerevision:
    description:
      - Firmware-Revision value for the Capabilities-Exchange-Request (CER) message
        to use for monitoring Diameter servers.
    type: float
  group:
    description:
      - Name of a newsgroup available on the NNTP service that is to be monitored.
        The appliance periodically generates an NNTP query for the name of the newsgroup
        and evaluates the response. If the newsgroup is found on the server, the service
        is marked as UP. If the newsgroup does not exist or if the search fails, the
        service is marked as DOWN. Applicable to NNTP monitors.
    type: str
  grpchealthcheck:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Option to enable or disable gRPC health check service.
    type: str
    default: 'NO'
  grpcservicename:
    description:
      - Option to specify gRPC service name on which gRPC health check need to be
        performed
    type: str
  grpcstatuscode:
    description:
      - gRPC status codes for which to mark the service as UP. The default value is
        12(health check unimplemented). If the gRPC status code 0 is received from
        the backend this configuration is ignored.
    type: list
  hostipaddress:
    description:
      - Host-IP-Address value for the Capabilities-Exchange-Request (CER) message
        to use for monitoring Diameter servers. If Host-IP-Address is not specified,
        the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address
        from which the CER request (the monitoring probe) is sent.
    type: str
  hostname:
    description:
      - 'Hostname in the FQDN format (Example: porche.cars.org). Applicable to STOREFRONT
        monitors.'
    type: str
  httprequest:
    description:
      - HTTP request to send to the server (for example, "HEAD /file.html").
    type: str
  inbandsecurityid:
    choices:
      - NO_INBAND_SECURITY
      - TLS
    description:
      - Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to
        use for monitoring Diameter servers.
    type: str
  interval:
    description:
      - Time interval between two successive probes. Must be greater than the value
        of Response Time-out.
    type: int
    default: 5
  ipaddress:
    description:
      - Set of IP addresses expected in the monitoring response from the DNS server,
        if the record type is A or AAAA. Applicable to DNS monitors.
    type: list
    elements: str
  iptunnel:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Send the monitoring probe to the service through an IP tunnel. A destination
        IP address must be specified.
    type: str
    default: 'NO'
  kcdaccount:
    description:
      - KCD Account used by MSSQL monitor
    type: str
  lasversion:
    description:
      - Version number of the Citrix Advanced Access Control Logon Agent. Required
        by the CITRIX-AAC-LAS monitor.
    type: str
  logonpointname:
    description:
      - Name of the logon point that is configured for the Citrix Access Gateway Advanced
        Access Control software. Required if you want to monitor the associated login
        page or Logon Agent. Applicable to CITRIX-AAC-LAS and CITRIX-AAC-LOGINPAGE
        monitors.
    type: str
  lrtm:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Calculate the least response times for bound services. If this parameter is
        not enabled, the appliance does not learn the response times of the bound
        services. Also used for LRTM load balancing.
    type: str
  maxforwards:
    description:
      - Maximum number of hops that the SIP request used for monitoring can traverse
        to reach the server. Applicable only to monitors of type SIP-UDP.
    type: float
    default: 1
  metric:
    description:
      - Metric name in the metric table, whose setting is changed. A value zero disables
        the metric and it will not be used for load calculation
    type: str
  metrictable:
    description:
      - Metric table to which to bind metrics.
    type: str
  metricthreshold:
    description:
      - Threshold to be used for that metric.
    type: float
  metricweight:
    description:
      - The weight for the specified service metric with respect to others.
    type: float
  monitorname:
    description:
      - Name for the monitor. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
      - ''
      - 'CLI Users:  If the name includes one or more spaces, enclose the name in
        double or single quotation marks (for example, "my monitor" or ''my monitor'').'
    type: str
  mqttclientidentifier:
    description:
      - Client id to be used in Connect command
    type: str
  mqttversion:
    description:
      - Version of MQTT protocol used in connect message, default is version 3.1.1
        [4]
    type: float
    default: 4
  mssqlprotocolversion:
    choices:
      - 70
      - 2000
      - 2000SP1
      - 2005
      - 2008
      - 2008R2
      - 2012
      - 2014
    description:
      - Version of MSSQL server that is to be monitored.
    type: str
    default: 70
  netprofile:
    description:
      - Name of the network profile.
    type: str
  oraclesid:
    description:
      - Name of the service identifier that is used to connect to the Oracle database
        during authentication.
    type: str
  originhost:
    description:
      - Origin-Host value for the Capabilities-Exchange-Request (CER) message to use
        for monitoring Diameter servers.
    type: str
  originrealm:
    description:
      - Origin-Realm value for the Capabilities-Exchange-Request (CER) message to
        use for monitoring Diameter servers.
    type: str
  password:
    description:
      - Password that is required for logging on to the RADIUS, NNTP, FTP, FTP-EXTENDED,
        MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC-ECV
        or CITRIX-XDM server. Used in conjunction with the user name specified for
        the User Name parameter.
    type: str
  productname:
    description:
      - Product-Name value for the Capabilities-Exchange-Request (CER) message to
        use for monitoring Diameter servers.
    type: str
  query:
    description:
      - Domain name to resolve as part of monitoring the DNS service (for example,
        example.com).
    type: str
  querytype:
    choices:
      - Address
      - Zone
      - AAAA
    description:
      - Type of DNS record for which to send monitoring queries. Set to C(Address)
        for querying A records, C(AAAA) for querying C(AAAA) records, and C(Zone)
        for querying the SOA record.
    type: str
  radaccountsession:
    description:
      - Account Session ID to be used in Account Request Packet. Applicable to monitors
        of type RADIUS_ACCOUNTING.
    type: str
  radaccounttype:
    description:
      - Account Type to be used in Account Request Packet. Applicable to monitors
        of type RADIUS_ACCOUNTING.
    type: float
    default: 1
  radapn:
    description:
      - Called Station Id to be used in Account Request Packet. Applicable to monitors
        of type RADIUS_ACCOUNTING.
    type: str
  radframedip:
    description:
      - Source ip with which the packet will go out . Applicable to monitors of type
        RADIUS_ACCOUNTING.
    type: str
  radkey:
    description:
      - Authentication key (shared secret text string) for RADIUS clients and servers
        to exchange. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.
    type: str
  radmsisdn:
    description:
      - Calling Stations Id to be used in Account Request Packet. Applicable to monitors
        of type RADIUS_ACCOUNTING.
    type: str
  radnasid:
    description:
      - NAS-Identifier to send in the Access-Request packet. Applicable to monitors
        of type RADIUS.
    type: str
  radnasip:
    description:
      - Network Access Server (NAS) IP address to use as the source IP address when
        monitoring a RADIUS server. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.
    type: str
  recv:
    description:
      - String expected from the server for the service to be marked as UP. Applicable
        to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.
    type: str
  respcode:
    description:
      - Response codes for which to mark the service as UP. For any other response
        code, the action performed depends on the monitor type. HTTP monitors and
        RADIUS monitors mark the service as DOWN, while HTTP-INLINE monitors perform
        the action indicated by the Action parameter.
    type: list
    elements: str
  resptimeout:
    description:
      - Amount of time for which the appliance must wait before it marks a probe as
        FAILED.  Must be less than the value specified for the Interval parameter.
      - ''
      - 'Note: For UDP-ECV monitors for which a receive string is not configured,
        response timeout does not apply. For UDP-ECV monitors with no receive string,
        probe failure is indicated by an ICMP port unreachable error received from
        the service.'
    type: int
    default: 2
  resptimeoutthresh:
    description:
      - Response time threshold, specified as a percentage of the Response Time-out
        parameter. If the response to a monitor probe has not arrived when the threshold
        is reached, the appliance generates an SNMP trap called monRespTimeoutAboveThresh.
        After the response time returns to a value below the threshold, the appliance
        generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated,
        the "MONITOR-RTO-THRESHOLD" alarm must also be enabled.
    type: float
  retries:
    description:
      - Maximum number of probes to send to establish the state of a service for which
        a monitoring probe failed.
    type: int
    default: 3
  reverse:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Mark a service as DOWN, instead of UP, when probe criteria are satisfied,
        and as UP instead of DOWN when probe criteria are not satisfied.
    type: str
    default: 'NO'
  rtsprequest:
    description:
      - RTSP request to send to the server (for example, "OPTIONS *").
    type: str
  scriptargs:
    description:
      - String of arguments for the script. The string is copied verbatim into the
        request.
    type: str
  scriptname:
    description:
      - Path and name of the script to execute. The script must be available on the
        Citrix ADC, in the /nsconfig/monitors/ directory.
    type: str
  secondarypassword:
    description:
      - Secondary password that users might have to provide to log on to the Access
        Gateway server. Applicable to CITRIX-AG monitors.
    type: str
  secure:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use a secure SSL connection when monitoring a service. Applicable only to
        TCP based monitors. The secure option cannot be used with a CITRIX-AG monitor,
        because a CITRIX-AG monitor uses a secure connection by default.
    type: str
    default: 'NO'
  secureargs:
    description:
      - List of arguments for the script which should be secure
    type: str
  send:
    description:
      - String to send to the service. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV
        monitors.
    type: str
  servicegroupname:
    description:
      - The name of the service group to which the monitor is to be bound.
    type: str
  servicename:
    description:
      - The name of the service to which the monitor is bound.
    type: str
  sipmethod:
    choices:
      - OPTIONS
      - INVITE
      - REGISTER
    description:
      - SIP method to use for the query. Applicable only to monitors of type SIP-UDP.
    type: str
  sipreguri:
    description:
      - SIP user to be registered. Applicable only if the monitor is of type SIP-UDP
        and the SIP Method parameter is set to REGISTER.
    type: str
  sipuri:
    description:
      - SIP URI string to send to the service (for example, sip:sip.test). Applicable
        only to monitors of type SIP-UDP.
    type: str
  sitepath:
    description:
      - URL of the logon page. For monitors of type CITRIX-WEB-INTERFACE, to monitor
        a dynamic page under the site path, terminate the site path with a slash (/).
        Applicable to CITRIX-WEB-INTERFACE, CITRIX-WI-EXTENDED and CITRIX-XDM monitors.
    type: str
  snmpcommunity:
    description:
      - Community name for SNMP monitors.
    type: str
  snmpthreshold:
    description:
      - Threshold for SNMP monitors.
    type: str
  snmpversion:
    choices:
      - V1
      - V2
    description:
      - SNMP version to be used for SNMP monitors.
    type: str
  sqlquery:
    description:
      - SQL query for a MYSQL-ECV or MSSQL-ECV monitor. Sent to the database server
        after the server authenticates the connection.
    type: str
  sslprofile:
    description:
      - SSL Profile associated with the monitor
    type: str
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of the monitor. The C(DISABLED) setting disables not only the monitor
        being configured, but all monitors of the same type, until the parameter is
        set to C(ENABLED). If the monitor is bound to a service, the state of the
        monitor is not taken into account when the state of the service is determined.
    type: str
    default: ENABLED
  storedb:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Store the database list populated with the responses to monitor probes. Used
        in database specific load balancing if MSSQL-ECV/MYSQL-ECV  monitor is configured.
    type: str
    default: DISABLED
  storefrontacctservice:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable/Disable probing for Account Service. Applicable only to Store Front
        monitors. For multi-tenancy configuration users my skip account service
    type: str
    default: 'YES'
  storefrontcheckbackendservices:
    choices:
      - 'YES'
      - 'NO'
    description:
      - This option will enable monitoring of services running on storefront server.
        Storefront services are monitored by probing to a Windows service that runs
        on the Storefront server and exposes details of which storefront services
        are running.
    type: str
    default: 'NO'
  storename:
    description:
      - Store Name. For monitors of type STOREFRONT, STORENAME is an optional argument
        defining storefront service store name. Applicable to STOREFRONT monitors.
    type: str
  successretries:
    description:
      - Number of consecutive successful probes required to transition a service's
        state from DOWN to UP.
    type: int
    default: 1
  supportedvendorids:
    description:
      - List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request
        (CER) message to use for monitoring Diameter servers. A maximum eight of these
        AVPs are supported in a monitoring message.
    type: list
  tos:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Probe the service by encoding the destination IP address in the IP TOS (6)
        bits.
    type: str
  tosid:
    description:
      - The TOS ID of the specified destination IP. Applicable only when the TOS parameter
        is set.
    type: float
  transparent:
    choices:
      - 'YES'
      - 'NO'
    description:
      - The monitor is bound to a transparent device such as a firewall or router.
        The state of a transparent device depends on the responsiveness of the services
        behind it. If a transparent device is being monitored, a destination IP address
        must be specified. The probe is sent to the specified IP address by using
        the MAC address of the transparent device.
    type: str
    default: 'NO'
  trofscode:
    description:
      - Code expected when the server is under maintenance
    type: float
  trofsstring:
    description:
      - String expected from the server for the service to be marked as trofs. Applicable
        to HTTP-ECV/TCP-ECV monitors.
    type: str
  type:
    choices:
      - PING
      - TCP
      - HTTP
      - TCP-ECV
      - HTTP-ECV
      - UDP-ECV
      - DNS
      - FTP
      - LDNS-PING
      - LDNS-TCP
      - LDNS-DNS
      - RADIUS
      - USER
      - HTTP-INLINE
      - SIP-UDP
      - SIP-TCP
      - LOAD
      - FTP-EXTENDED
      - SMTP
      - SNMP
      - NNTP
      - MYSQL
      - MYSQL-ECV
      - MSSQL-ECV
      - ORACLE-ECV
      - LDAP
      - POP3
      - CITRIX-XML-SERVICE
      - CITRIX-WEB-INTERFACE
      - DNS-TCP
      - RTSP
      - ARP
      - CITRIX-AG
      - CITRIX-AAC-LOGINPAGE
      - CITRIX-AAC-LAS
      - CITRIX-XD-DDC
      - ND6
      - CITRIX-WI-EXTENDED
      - DIAMETER
      - RADIUS_ACCOUNTING
      - STOREFRONT
      - APPC
      - SMPP
      - CITRIX-XNC-ECV
      - CITRIX-XDM
      - CITRIX-STA-SERVICE
      - CITRIX-STA-SERVICE-NHOP
      - MQTT
      - HTTP2
    description:
      - Type of monitor that you want to create.
    type: str
  units1:
    choices:
      - SEC
      - MSEC
      - MIN
    description:
      - Unit of measurement for the Deviation parameter. Cannot be changed after the
        monitor is created.
    type: str
    default: SEC
  units2:
    choices:
      - SEC
      - MSEC
      - MIN
    description:
      - Unit of measurement for the Down Time parameter. Cannot be changed after the
        monitor is created.
    type: str
    default: SEC
  units3:
    choices:
      - SEC
      - MSEC
      - MIN
    description:
      - monitor interval units
    type: str
    default: SEC
  units4:
    choices:
      - SEC
      - MSEC
      - MIN
    description:
      - monitor response timeout units
    type: str
    default: SEC
  username:
    description:
      - User name with which to probe the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL,
        MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC or CITRIX-XDM
        server.
    type: str
  validatecred:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Validate the credentials of the Xen Desktop DDC server user. Applicable to
        monitors of type CITRIX-XD-DDC.
    type: str
    default: 'NO'
  vendorid:
    description:
      - Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use
        for monitoring Diameter servers.
    type: float
  vendorspecificacctapplicationids:
    description:
      - List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to
        use for monitoring Diameter servers. A maximum of eight of these AVPs are
        supported in a monitoring message. The specified value is combined with the
        value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id
        AVP in the CER monitoring message.
    type: list
  vendorspecificauthapplicationids:
    description:
      - List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for
        the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter
        servers. A maximum of eight of these AVPs are supported in a monitoring message.
        The specified value is combined with the value of vendorSpecificVendorId to
        obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.
    type: list
  vendorspecificvendorid:
    description:
      - Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value
        pair (AVP) in the monitoring CER message. To specify Auth-Application-Id or
        Acct-Application-Id in Vendor-Specific-Application-Id, use vendorSpecificAuthApplicationIds
        or vendorSpecificAcctApplicationIds, respectively. Only one Vendor-Id is supported
        for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.
    type: float
  lbmonitor_metric_binding:
    type: dict
    description: Bindings for lbmonitor_metric_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  lbmonitor_sslcertkey_binding:
    type: dict
    description: Bindings for lbmonitor_sslcertkey_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
- name: Sample Playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Sample Task | lbmonitor
      delegate_to: localhost
      netscaler.adc.lbmonitor:
        state: present
        monitorname: ldns-dns
        type: LDNS-DNS
        query: .
        querytype: Address
        deviation: '0'
        interval: 6
        resptimeout: 3
        downtime: 20
    - name: Sample Task | lbmonitor | 2
      delegate_to: localhost
      netscaler.adc.lbmonitor:
        state: present
        monitorname: stasecure
        type: CITRIX-STA-SERVICE
        deviation: '0'
        interval: 2
        units3: MIN
        resptimeout: 4
        downtime: 5

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
