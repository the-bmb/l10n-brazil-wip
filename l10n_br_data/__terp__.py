# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Brazilian Localisation Data Extension",
    "description" : "Brazilian Localisation Data Extension",
    "author" : "OpenERP Brasil",
    "version" : "0.1",
    "depends" : ["l10n_br"],
    'init_xml': [
        #Arquivos com dados Fiscais
        'l10n_br.cfop.csv',
        'l10n_br.fiscal.document.csv',
        'account.tax.csv',
        'l10n_br.ncm.csv',
        'l10n_br.st.source.csv',
        'l10n_br.st.csv',
        'res.country.state.csv',
        'l10n_br.city.csv'],
    "update_xml" : [],
    "category" : "Localisation",
    "active": False,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
