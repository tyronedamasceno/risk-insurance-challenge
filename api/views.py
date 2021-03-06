from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from api.core import calculate_risk_profile
from api.serializers import UserInputSerializer, RiskProfileSerializer


class RiskProfileView(APIView):
    @swagger_auto_schema(request_body=UserInputSerializer,
                         responses={'200': RiskProfileSerializer})
    def post(self, request):
        serializer = UserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = serializer.validated_data
        risk_profile = calculate_risk_profile(**user_data)

        scores = RiskProfileSerializer(data=risk_profile)
        scores.is_valid(raise_exception=True)

        return Response(data=scores.data)
