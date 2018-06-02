import vk
import getpass

APP_ID = 6498088


def get_user_login():
    return input('Enter your VK login')


def get_user_password():
    return getpass.getpass(prompt='Enter VK password: ')


def connect_vk(login, password, vk_api_version=5.74):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )

    return vk.API(session, v=vk_api_version, timeout=10)


def get_friends_online(vk_api):
    friends_id_online = vk_api.friends.getOnline()
    return vk_api.users.get(user_ids=friends_id_online)


def output_friends_to_console(friends_online):
    if not friends_online:
        print('There are no friends online')
        return

    print('\nYour friends online:')
    for friend in friends_online:
        print('{} {}'.format(
            friend.get('last_name'), friend.get('first_name'))
        )


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()

    try:
        vk_api = connect_vk(login, password)
    except vk.exceptions.VkAuthError as auth_exception:
        exit('{}. Leaving...'.format(auth_exception))

    friends_online = get_friends_online(vk_api)
    output_friends_to_console(friends_online)
