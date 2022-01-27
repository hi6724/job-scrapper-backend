from rest_framework.response import Response
from rest_framework.decorators import api_view
from .get_jobs import get_jobs


# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world")


@api_view(["GET"])
def getJobs(request, keyword, Page_No, careerType, careerMin, careerMax, edu,
            cotype, jobtype, payMin, payMax):
    jobs = get_jobs(keyword=keyword,
                    Page_No=Page_No,
                    careerType=careerType,
                    careerMin=careerMin,
                    careerMax=careerMax,
                    edu=edu,
                    cotype=cotype,
                    jobtype=jobtype,
                    payMin=payMin,
                    payMax=payMax)
    return Response(jobs)
