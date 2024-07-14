from core.models import SocialModel

def social_link(request):
    soc_link = SocialModel.objects.all()
    return dict(soc_link=soc_link)