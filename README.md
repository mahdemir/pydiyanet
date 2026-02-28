# pydiyanet

Python client library for the Diyanet prayer times API.

## Features

- Async/await support using aiohttp
- Full type hints with py.typed for mypy compatibility
- Authentication and token refresh handling
- Access to prayer times, countries, states, and cities
- Comprehensive error handling

## Installation

```bash
pip install pydiyanet
```

## Usage

```python
import asyncio
from aiohttp import ClientSession
from pydiyanet import DiyanetApiClient, DiyanetAuthError, DiyanetConnectionError

async def main():
    async with ClientSession() as session:
        client = DiyanetApiClient(session, "your-email@example.com", "your-password")

        try:
            # Authenticate
            await client.authenticate()

            # Get prayer times for a location
            prayer_times = await client.get_prayer_times(location_id=9146)
            print(f"Fajr: {prayer_times['fajr']}")
            print(f"Dhuhr: {prayer_times['dhuhr']}")

            # Get countries
            countries = await client.get_countries()

            # Get states for a country
            states = await client.get_states(country_id=2)

            # Get cities for a state
            cities = await client.get_cities(state_id=9)

        except DiyanetAuthError as err:
            print(f"Authentication failed: {err}")
        except DiyanetConnectionError as err:
            print(f"Connection error: {err}")

asyncio.run(main())
```

## API Reference

### DiyanetApiClient

#### `__init__(session: ClientSession, email: str, password: str)`

Initialize the API client with an aiohttp session and credentials.

#### `async authenticate() -> bool`

Authenticate with the Diyanet API and obtain access/refresh tokens.

Raises:

- `DiyanetAuthError`: If authentication fails
- `DiyanetConnectionError`: If there's a network error

#### `async get_prayer_times(location_id: int) -> dict[str, Any]`

Get prayer times for a specific location.

Returns a dictionary containing prayer times for the current day.

#### `async get_countries() -> list[dict[str, Any]]`

Get list of all available countries.

#### `async get_states(country_id: int) -> list[dict[str, Any]]`

Get list of states for a given country.

#### `async get_cities(state_id: int) -> list[dict[str, Any]]`

Get list of cities for a given state.

#### `async get_city_detail(city_id: int) -> dict[str, Any] | None`

Get detailed information for a specific city.

## Exceptions

- `DiyanetApiError`: Base exception for all API errors
- `DiyanetAuthError`: Raised when authentication fails
- `DiyanetConnectionError`: Raised when there's a network/connection error

## Token Management

The client automatically handles token expiration and refresh:

- Access tokens expire after 30 minutes
- Refresh tokens expire after 45 minutes
- Tokens are automatically refreshed when needed
- Full re-authentication occurs when refresh token expires

## Requirements

- Python 3.11+
- aiohttp >= 3.9.0

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
