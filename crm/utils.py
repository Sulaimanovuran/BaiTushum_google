from django.db.models import Count


def get_dashboard_data(mdl,ordr:str, cnt:str):
    data = mdl.objects.all().values(ordr).annotate(total=Count(cnt)).order_by(ordr)
    return data