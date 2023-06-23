from .blueprint import profile_blueprint

@profile_blueprint.route('', methods=('GET',))
def get_active_profile():
    try:
        with open('.profile', 'r') as f:
            profile = f.read().strip()
            if profile is not None and profile in { 'small', 'medium', 'large' }:
                return { 'name': profile }
    except:
        pass
    
    return { 'name': 'small' }