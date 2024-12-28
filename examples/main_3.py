def extract_data(credentials: dict, source: str) -> dict:
    """
    Downloads weather readings from ``source`` database.

    Parameters
    ----------
    credentials : dict
        Database credentials.

    source : str
        Database address.

    Returns
    -------
    : dict
    """
    return dict()


def load_credentials() -> dict:
    """
    Loads credentials.

    Returns
    -------
    : dict
    """
    return dict()


def load_settings() -> dict:
    """
    Process settings.

    Returns
    -------
    : dict
    """
    return dict()


if __name__ == '__main__':
    # Load settings and credentials
    credentials = load_credentials()
    settings = load_settings()

    # Get data
    ds = extract_data(credentials, source)
    # Transform
    ...
    # Upload
    ...
