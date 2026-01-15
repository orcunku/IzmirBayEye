class NotificationService:
    @staticmethod
    def get_alert(risk_score):
        if risk_score >= 80:
            return {
                "level": "CRITICAL",
                "color": "#FF0000",
                "title": " High H2S Risk Detected",
                "message": "Atmospheric conditions suggest high odor accumulation. Municipality notified."
            }
        elif risk_score >= 60:
            return {
                "level": "WARNING",
                "color": "#FFA500",
                "title": " Moderate Odor Risk",
                "message": "Potential for localized odors in coastal areas."
            }
        return None

