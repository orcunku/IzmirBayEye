class NotificationService:
    @staticmethod
    def notify_citizens(risk_score):
        if risk_score > 75:
            return {
                "title": " High Odor Risk",
                "body": f"Risk level at {risk_score}%. Avoid the coastline.",
                "channel": "Firebase_Push"
            }
        return None