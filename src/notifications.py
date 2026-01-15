class NotificationService:
    """Dispatches alerts based on risk severity."""
    
    @staticmethod
    def notify_citizens(risk_score):
        if risk_score >= 85:
            return {
                "level": "CRITICAL",
                "title": " Urgent: High Odor Hazard",
                "body": "Toxic sulfide levels predicted. Avoid Kordon/Bay area.",
                "action": "Evacuate Coastline"
            }
        elif risk_score >= 70:
            return {
                "level": "WARNING",
                "title": " Odor Alert",
                "body": "Noticeable odor predicted in the next 2 hours.",
                "action": "Close windows near the bay"
            }
        return None
