def get_users_install():
    return ['mondoir', 'mondoir.users']


def get_users_middleware():
    return [
        'mondoir.users.middleware.UserInformationMiddleware',
    ]
