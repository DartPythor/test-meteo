# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from search.models import SearchHistory
from search.serializers import SearchHistorySerializer
from search.pagination import StandardResultsPagination


class UserSearchHistoryView(APIView):
    pagination_class = StandardResultsPagination

    def get(self, request):
        session_key = request.session.session_key

        if not session_key:
            return Response(
                {"error": "Session not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = SearchHistory.objects.filter(
            session_key=session_key
        ).order_by('-created_at')

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)

        if page is not None:
            serializer = SearchHistorySerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = SearchHistorySerializer(queryset, many=True)
        return Response(serializer.data)
