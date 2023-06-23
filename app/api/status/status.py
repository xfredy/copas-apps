from .desktop import get_desktop_status
from .vnc import get_vnc_status
from .blueprint import status_blueprint

@status_blueprint.route('', methods=('GET',))
def get_status():
    return {
        'services': [
            get_desktop_status(),
            get_vnc_status()
        ]
    }
