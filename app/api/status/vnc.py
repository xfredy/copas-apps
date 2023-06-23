from app.api.status.utils import check_process_running


def get_vnc_status():
    is_up = check_process_running('x11vnc')
    return {
        'name': 'vnc',
        'status': 'up' if is_up else 'down',
        'info': []
    }