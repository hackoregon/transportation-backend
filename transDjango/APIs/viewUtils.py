

def getMinDist(request, query_param, default):
    try:
        return int(request.query_params.get(query_param, default))
    except ValueError:
        return default
