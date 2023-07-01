from mondoir.users.install import (
    get_users_install,
    get_users_middleware,
)
from mondoir.core.install import get_core_install


def get_mondoir_app_list_install():
    return list(
        set(
            get_users_install()
            + get_core_install()
            )
    )


def get_mondoir_middleware_list():
    return (
        get_users_middleware()
    )