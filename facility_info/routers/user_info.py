from fastapi import APIRouter

router = APIRouter()

@router.get("/{username_or_email}")
def get_user_info(username_or_email):
    user_info_dict = {'jdoe':{'username': 'jdoe',
            'globus_email': 'jdoe@bnl.gov'}}
    for user, info in user_info_dict.items():
        if username_or_email in info.values():
            return info
    return None
