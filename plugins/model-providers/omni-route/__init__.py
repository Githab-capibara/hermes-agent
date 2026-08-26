"""OmniRoute provider profile."""

from hermes_cli import __version__ as _HERMES_VERSION
from providers import register_provider
from providers.base import ProviderProfile

omni_route = ProviderProfile(
    name="omni-route",
    aliases=("omnirouter", "9router", "omni"),
    display_name="OmniRoute",
    description="OmniRoute — unified model routing API (Sapiens AI models)",
    signup_url="https://sapiens.ai/",
    env_vars=("OMNIROUTER_API_KEY", "OMNIROUTER_BASE_URL"),
    base_url="https://api.sapiens.ai/v1",
    auth_type="api_key",
    default_headers={"User-Agent": f"HermesAgent/{_HERMES_VERSION}"},
    default_aux_model="hnc/auto",
    fallback_models=(
        "hnc/auto",
    ),
)

register_provider(omni_route)
