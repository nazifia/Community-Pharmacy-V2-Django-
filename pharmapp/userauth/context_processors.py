

from userauth.models import Profile


def user_profile(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            if not profile.image:
                profile.image = 'images/undraw_profile.svg'  # Path to your default image
            return {'user_profile': profile}
        except Profile.DoesNotExist:
            return {'user_profile': None}
    return {'user_profile': None}
