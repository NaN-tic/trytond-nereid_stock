#This file is part nereid_stock module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .shipment import *


def register():
    Pool.register(
        ShipmentOut,
        module='nereid_stock', type_='model')
