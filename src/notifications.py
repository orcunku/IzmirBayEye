class NotificationService:
    @staticmethod
    def get_alert(risk_score):
        if risk_score >= 80:
            return {"level": "CRITICAL", "title": " High Odor Hazard", "msg": "Avoid the coastline. H2S levels rising."}
        elif risk_score >= 60:
            return {"level": "WARNING", "title": " Odor Alert", "msg": "Localized odors expected near the bay."}
        return None

