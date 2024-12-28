import logging


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


def get_data_source(settings: dict) -> str:
    """
    Function returns data source from settings dictionary.

    Parameters
    ----------
    settings : dict
        Dictionary, it must contain ``DATASOURCE`` key.

    Returns
    -------
    : str
    """
    return ""


if __name__ == '__main__':
    logging.info('START')

    # Load settings and credentials
    logging.info('Loading credentials')
    credentials = load_credentials()

    logging.info('Loading settings')
    settings = load_settings()

    source = get_data_source(settings)

    # Get data
    logging.info('Getting data')
    ds = extract_data(credentials, source)
    logging.debug(f'Retrived {len(ds)} records')

    # Transform
    logging.info('Data processing: step a')
    transformed_a = ...

    logging.info('Data processing: step b')
    transformed_b = ...

    # Upload
    logging.info('Data uploading')
    ...

    logging.info('DONE')
