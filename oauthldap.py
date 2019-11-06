import logging

from laurelin.ldap import LDAP

LDAP.enable_logging()
logger = logging.getLogger('laurelin.ldap')
LDAP.log_warnings()
LDAP.disable_warnings()
with LDAP('ldap://ldap:389') as ldap:
    people = ldap.base.get_child('ou=tilda.center')
    print(people['objectClass'])
