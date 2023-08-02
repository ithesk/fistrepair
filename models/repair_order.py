# -*- coding: utf-8 -*-

from odoo import api, fields, models



class RepairP(models.Model):
    _inherit = 'repair.order'
    imei = fields.Char(string='IMEI')
    serial = fields.Char(string='Serial')
    passcode = fields.Char(string='Passcode')
    battery = fields.Integer(string='Battery')
    faceid = fields.Boolean(string='Face ID')
    wifi = fields.Boolean(string='Wifi')
    signal = fields.Boolean(string='Signal')
    screen = fields.Boolean(string='Screen')
    camera = fields.Boolean(string='Camera')
    speaker = fields.Boolean(string='Speaker')
    microphone = fields.Boolean(string='Microphone')
    charging = fields.Boolean(string='Charging')
    buttons = fields.Boolean(string='Buttons')
    touch = fields.Boolean(string='Touch')
    sim = fields.Boolean(string='SIM')
    sd = fields.Boolean(string='SD')
    camerafront = fields.Boolean(string='Front Camera')
    panic = fields.Boolean(string='Panic')
    screw = fields.Boolean(string='Screw')
    earphone = fields.Boolean(string='Earphone')
    
    # states = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('under_repair', 'Under Repair'), ('ready', 'Ready to Repair'), ('done', 'Repaired'), ('cancel', 'Cancelled')], string='State', readonly=True, default='draft', copy=False, track_visibility='onchange')
    done = fields.Boolean(string='Done')

    statecell = fields.Selection(string="State equipment" ,
                                 selection=[('in', 'In'), ('out', 'Out')]
                                 
                                 )
