import subprocess
from flask import request, current_app as app
from .blueprint import profile_blueprint

def get_resolution(size: str):
    if size == 'small':
        return '1920x1080'
    elif size == 'medium':
        return '1280x720_60.00'
    return '856x480_60.00'

def change_icons(size: str):
    r = subprocess.run(['xrandr', '-s', get_resolution(size)])
    return r.returncode == 0


@profile_blueprint.route('', methods=('POST',))
def update_profile():    
    profile = request.json

    if profile is None:
        return { 'error': 'no json body provided' }, 400

    if 'name' not in profile:
        return { 'error': 'missing property \'name\'' }, 400
    
    profile_name = profile['name']

    if profile_name not in { 'small', 'medium', 'large' }:
        return { 'error': f'unknown profile with name \'{profile_name}\'' }, 400

    try:
        with open('.profile', 'w') as f:
            if change_icons(profile_name):
                f.write(profile_name)
                app.logger.info('successfully updated profile to \'%s\'', profile_name)
                return {}
            app.logger.error('failed to update profile to \'%s\'', profile_name)
            return { 'error': f'failed to update profile to \'{profile_name}\'' }, 500

    except:
        app.logger.error('failed to update profile to \'%s\'', profile_name, exc_info=True)
        return { 'error': f'failed to update profile to \'{profile_name}\'' }, 500