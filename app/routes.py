from flask import Blueprint, jsonify
from .models import db, Campaign
import json

main = Blueprint("main", __name__)

@main.route("/sync", methods=["POST"])
def sync_campaigns():
    with open("mock_data/campaigns.json") as f:
        data = json.load(f)

    Campaign.query.delete()
    for entry in data:
        campaign = Campaign(
            name = entry["name"]
            impressions = entry["impressions"],
            clicks = entry["clicks"]
        )
        db.session.add(campaign)

    db.session.commit()
    return jsonify({"message": "Campaigns synced"}), 200

@main.route("/report", methods = ["GET"])
def report():
    campaigns = Campaign.query.all()
    result = []
    for c in campaigns:
        result.append({
            "name": c.name,
            "impressions": c.impressions,
            "clicks": c.clicks,
            "ctr": c.ctr()
        })
    return jsonify(result)