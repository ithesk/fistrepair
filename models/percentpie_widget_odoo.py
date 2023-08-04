class gym_body_parts_config(models.Model):
    _name = 'gym.body.parts.config'

    sequence = fields.Integer(default=10,help="Gives the sequence order when displaying a list of records.")
    name = fields.Char(string="Name", required=True)
    progress_percentpie = fields.Integer(compute='_compute_progress_percentpie')	

    @api.depends('name','sequence')
    def _compute_progress_percentpie(self):
        for u in self:
            if u.name and u.sequence:
                progress = 100
            elif u.name:
                progress = 50
            else:
                progress = 0
            u.progress_percentpie = progress