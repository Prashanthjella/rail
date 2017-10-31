
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the "
        "header."),
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=_("Twitter link"),
    description=_("If present a Twitter icon linking here will be in the "
        "header."),
    editable=True,
    default="https://twitter.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_GOOGLE",
    label=_("Google Plus link"),
    description=_("If present a Google icon linking here will be in the "
        "header."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_LINKEDIN",
    label=_("Google Plus link"),
    description=_("If present a Google icon linking here will be in the "
        "header."),
    editable=True,
    default="",
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("SOCIAL_LINK_FACEBOOK",
             "SOCIAL_LINK_TWITTER",
             "SOCIAL_LINK_GOOGLE",
             "SOCIAL_LINK_LINKEDIN"),
)