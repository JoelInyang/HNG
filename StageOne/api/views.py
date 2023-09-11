import json
import datetime
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

@require_GET
@csrf_exempt  
def endpoint1(request):
    slack_name = request.GET.get('slack_name', 'Joel Inyang')
    track = request.GET.get('track', 'backend')

    current_day = datetime.datetime.now().strftime('%A')
    current_utc_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"  # Replace with your actual GitHub file URL
    github_repo_url = "https://github.com/username/repo"  # Replace with your actual GitHub repo URL

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }

    return JsonResponse(response_data)
