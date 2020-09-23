from fastapi import APIRouter

router = APIRouter()

user_info_dict = {'jdoe':{'username': 'jdoe',
    'globus_email': 'jdoe@bnl.gov'}}

@router.get("/{username_or_email}")
def get_user_info(username_or_email):
    for user, info in user_info_dict.items():
        if username_or_email in info.values():
            return info
    return None

@router.get("/")
def get_all_usernames():
    all_names = []
    for name in user_info_dict.keys():
        all_names.append(name)
    return {'users':all_names}
