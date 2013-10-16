#This file is part nereid_stock module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from nereid import render_template, request, login_required
from nereid.helpers import url_for
from nereid.contrib.pagination import Pagination
from werkzeug.exceptions import NotFound

from trytond.pool import PoolMeta

__all__ = ['ShipmentOut']
__metaclass__ = PoolMeta


class ShipmentOut:
    __name__ = 'stock.shipment.out'

    per_page = 10

    @classmethod
    @login_required
    def render_list(cls):
        """
        Get shipments
        """
        page = request.args.get('page', 1, int)

        clause = []
        clause.append(('customer', '=', request.nereid_user.party))
        order = [('effective_date', 'DESC'), ('id', 'DESC')]

        shipments = Pagination(
            cls, clause, page, cls.per_page, order
        )

        return render_template('shipments.jinja', shipments=shipments)

    @classmethod
    @login_required
    def render(cls, uri):
        """
        Get shipment detail
        """
        try:
            shipment, = cls.search([
                ('id', '=', int(uri)),
                ('customer', '=', request.nereid_user.party),
                ])
        except ValueError:
            return NotFound()
        return render_template('shipment.jinja', shipment=shipment)

    def get_absolute_url(self, **kwargs):
        return url_for(
            'stock.shipment.out.render', uri=self.id, **kwargs
            )
