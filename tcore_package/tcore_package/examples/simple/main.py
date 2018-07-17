# To correctly import tc_python and t_core, place this folder at the root

from tc_python.arule import ARule
from t_core.messages import Packet
from HA import HA
from HAb import HAb
from HTopClass2TableLHS import HTopClass2TableLHS
from HTopClass2TableRHS import HTopClass2TableRHS

r1 = ARule(HTopClass2TableLHS(), HTopClass2TableRHS())
p = Packet()
p.graph = HA()
p1 = r1.packet_in(p)
print p1

print r1.is_success

if r1.exception:
     raise r1.exception
 
r2 = ARule(HTopClass2TableLHS(), HTopClass2TableRHS())
p = Packet()
p.graph = HAb()
p2 = r2.packet_in(p)
print p2

print r2.is_success

if r2.exception:
     raise r2.exception