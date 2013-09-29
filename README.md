company_unique
==============

OpenERP 7.0 当Partner为公司时，其名称必须唯一。 而不限制联系人的名称重复（系统默认）。

Only when partner is a company, it's name shall be unique. Otherwise, contacts(partner) can have duplicate names.

How to disable/uninstall this module?

Uninstall from the OpenERP interface is not enough.
You have drop constraint and index manually.

ALTER TABLE res_partner DROP CONSTRAINT res_partner_name_is_company_unique;
DROP INDEX res_partner_name_is_company_unique_idx;
