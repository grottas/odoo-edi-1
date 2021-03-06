"""EDI stock transfer report records"""

from odoo import api, fields, models


class EdiPickReportRecord(models.Model):
    """EDI stock transfer report record

    This is the base model for EDI stock transfer report records.
    Each row represents a completed stock transfer that will be
    reported upon when the document is executed.

    The fields within each record represent the fields within the
    produced document, which may not exactly correspond to fields of
    the ``stock.picking`` model.  For example: the document may
    include a column reporting the number of days taken to dispatch
    the item, calculated from the picking's creation and completion
    dates.

    Derived models should implement either :meth:`~.record_values` or
    :meth:`~.prepare`.
    """

    _name = 'edi.pick.report.record'
    _inherit = 'edi.record'
    _description = "Stock Transfer Report"

    pick_id = fields.Many2one('stock.picking', string="Transfer",
                              required=True, readonly=True, index=True)

    _sql_constraints = [('doc_name_uniq', 'unique (doc_id, name)',
                         "Each name may appear at most once per document")]

    @api.model
    def record_values(self, pick):
        """Construct EDI record value dictionary

        Accepts a ``stock.picking`` record and constructs a
        corresponding value dictionary for an EDI stock transfer
        report record.
        """
        return {
            'name': pick.name,
            'pick_id': pick.id,
        }

    @api.model
    def prepare(self, doc, picks):
        """Prepare records"""
        for pick in picks:
            record_vals = self.record_values(pick)
            record_vals['doc_id'] = doc.id
            self.create(record_vals)
