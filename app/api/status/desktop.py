from app.api.status.utils import check_process_running


def get_desktop_status():
    is_up = check_process_running('xfce4-session') and check_process_running('Xvfb')
    return {
        'name': 'desktop',
        'status': 'up' if is_up else 'down',
        'info': []
    }