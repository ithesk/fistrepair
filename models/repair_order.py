# -*- coding: utf-8 -*-

from odoo import api, fields, models



class RepairP(models.Model):
    _inherit = 'repair.order'
    imei = fields.Char(string='IMEI SN')
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
    flash = fields.Boolean(string='Flash')
    powerstate = fields.Boolean(string='Power State')

    partner1_phone = fields.Char(string='Phone', related='partner_id.phone')
    company_phone = fields.Char(string='Phone', related='company_id.phone')
    partner1_email = fields.Char(string='Email', related='company_id.email')
    company_name = fields.Char(string='Company', related='company_id.name')
    address = fields.Char(string='Address', related='company_id.street')
    website1 = fields.Char(string='Website', related='company_id.website')
    condition = fields.Char(string='Condition')
    classific = fields.Char(compute="_compute_classific", string='Classific')
    evaluation = fields.Char(compute="_compute_evaluation", string='Evaluation')
    typerepair = fields.Selection([('cell', 'Cell'),
                                   ('tablet', 'Tablet'),
                                   ('smartwatch', 'SmartWatch'),
                                    ], string='Type Repair', default="cell")

    @api.depends('faceid', 'wifi', 'signal', 'screen', 'camera', 'speaker', 'microphone', 'charging', 'buttons', 'touch', 'sim', 'sd', 'camerafront', 'panic', 'screw', 'earphone', 'flash')
    def _compute_evaluation(self):
        for record in self:
            sum = 0
            if record.faceid:
                sum += 1
            if record.wifi:
                sum += 1
            if record.signal:
                sum += 1
            if record.screen:
                sum += 1
            if record.camera:
                sum += 1
            if record.speaker:
                sum += 1
            if record.microphone:
                sum += 1
            if record.charging:
                sum += 1
            if record.buttons:
                sum += 1
            if record.touch:
                sum += 1
            if record.sim:
                sum += 1
            if record.camerafront:
                sum += 1
            if record.panic:
                sum += 1
            if record.screw:
                sum += 1
            if record.earphone:
                sum += 1
            if record.flash:
                sum += 1  
            if sum == 16:
                record.evaluation = "2/10 Se Reinicia"    
            if sum == 15:
                record.evaluation = "10/10 NITIDO"
            elif sum >= 13:
                record.evaluation = "8/10 TA BUENO"
            elif sum >= 9:
                record.evaluation = "5/10 HAY"
            elif sum >= 5:
                record.evaluation = "3/10 REGULAR"
            elif sum >= 1:
                record.evaluation = "1/10 Maco"
            else: 
                record.evaluation = "No Probado"
    
    
    @api.depends('typerepair')
    def _compute_classific(self):
        for record in self:
            if record.typerepair == "cell":
                record.classific = "C"
            elif record.typerepair == "tablet":
                record.classific = "T"
            elif record.typerepair == "smartwatch":
                record.classific = "S"
            else:
                record.classific = "A"
                              
            
            
    



    
    # states = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('under_repair', 'Under Repair'), ('ready', 'Ready to Repair'), ('done', 'Repaired'), ('cancel', 'Cancelled')], string='State', readonly=True, default='draft', copy=False, track_visibility='onchange')
    done = fields.Boolean(string='Done')

    statecell = fields.Selection(string="State equipment" ,
                                 selection=[('in', 'In'), ('out', 'Out')]    )       
