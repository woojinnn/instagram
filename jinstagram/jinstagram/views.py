from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        print("Call as get")
        return render(request, '../templates/jinstagram/main.html')

