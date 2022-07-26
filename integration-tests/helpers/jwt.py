from environs import Env
from jose import jwt as jose_jwt


def get_system_token() -> str:
    env: Env = Env()
    hs_issuer: str = env.str("HS_ISSUER")
    proxy_url: str = env.str("PROXY_URL")
    return jose_jwt.encode(
        {
            "metadata": {"system_id": "dhos-robot"},
            "iss": hs_issuer,
            "aud": proxy_url + "/",
            "scope": env.str("SYSTEM_JWT_SCOPE"),
            "exp": 9_999_999_999,
        },
        key=Env().str("HS_KEY"),
        algorithm="HS512",
    )
