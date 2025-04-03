from fastapi import Request


def get_client_ip(request: Request) -> str:
    """
    Retrieves the IP address of the client making the request.

    Args:
        request (Request): The FastAPI request object.

    Returns:
        str: The client's IP address.
    """
    # Check for X-Forwarded-For header (used in proxies/load balancers)
    x_forwarded_for = request.headers.get("X-Forwarded-For")
    if x_forwarded_for:
        # Return the first IP in the list
        return x_forwarded_for.split(",")[0].strip()

    # Fallback to the client host from the request
    client_host = request.client.host if request.client else "Unknown"
    return client_host