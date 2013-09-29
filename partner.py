# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class res_partner(osv.osv):
    _inherit = 'res.partner'

    _sql_constraints = [
        # Empty constraint, complemented by unique index (see below)
        # Still useful to keep sql constraints because it provides a proper error message when a violation occurs.
        # Because the constraint and index share the same prefix so that IntegrityError triggered by the index will be caught
        # and reported to the user with the sql constraint's error message.
        ('name_is_company_unique', 'unique ()', 'Company names must be unique'),
    ]

    def init(self, cr, context=None):
        super(res_partner, self)._auto_init(cr, context)
        cr.execute("""SELECT indexname FROM pg_indexes WHERE indexname = 'res_partner_name_is_company_unique_idx'""")
        if not cr.fetchone():
            cr.execute("""CREATE UNIQUE INDEX "res_partner_name_is_company_unique_idx" ON res_partner (name) WHERE is_company IS True""")

res_partner()
