from rest_framework.views import APIView
from rest_framework.response import Response

class DashboardView(APIView):
    def get(self, request):
        data = [
            {"source": "SAP Fuel Data", "status": "Approved", "scope": "Scope 1"},
            {"source": "Utility Electricity", "status": "Pending", "scope": "Scope 2"},
            {"source": "Corporate Travel", "status": "Flagged", "scope": "Scope 3"}
        ]
        return Response(data)