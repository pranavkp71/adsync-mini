from . import db

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    impressions = db.Column(db.Integer, default = 0)
    clicks = db.Column(db.Integer, default = 0)

    def ctr(self):
        return round(self.clicks / self.impressions, 2)if self.impressions > 0 else 0