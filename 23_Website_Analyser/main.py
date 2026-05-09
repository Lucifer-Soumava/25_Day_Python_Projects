import asyncio
from asyncio import TimeoutError
import requests
from requests import Response
from dataclasses import dataclass
import time

@dataclass
class WebsiteResponse:
    url: str
    status: int | None
    reason: str
    time: float | None

async def check_website(url: str, timeout: float) -> WebsiteResponse:
    if not url.startswith(('http://','https://')):
        url = f'https://{url}'

    try:
        start: float = time.perf_counter()
        response: Response = await asyncio.to_thread(requests.get, url)
        total_time: float = time.perf_counter() - start
        return WebsiteResponse(url, response.status_code, response.reason, total_time)
    except asyncio.TimeoutError:
        return WebsiteResponse(url, None, f'Timed out after {timeout}s', None)
    except Exception as e:
        return WebsiteResponse(url, None, str(e), None)
    
async def check_websites(urls: list[str], timeout: float = 5) -> None:
    tasks = [check_website(url, timeout) for url in urls]

    try:
        for completed_task in asyncio.as_completed(fs=tasks, timeout=timeout):
            response: WebsiteResponse = await completed_task

            if response.status is not None:
                print(
                    f'{response.url}: ✅ ONLINE ({response.status} {response.reason} [{response.time:.2f}s])'
                )
            else:
                print(f'Could not retrieve information for: "{response.url}"')

    except TimeoutError:
        print('Timeout reached — some websites took too long.')


async def main() -> None:
    urls: list[str] = [
        'www.indently.io',
        'www.apple.com',
        'www.facebook.com',
        'nonexistent-website-404.com',
        'www.instagram.com',
        'www.reddit.com',
        'www.wikipedia.org',
        'www.fail-website.com',
        'www.amazon.com',
        'www.linkedin.com',
        'www.microsoft.com',
        'www.github.com',
    ]

    print(f'Checking {len(urls)} websites...')
    await asyncio.gather(check_websites(urls))
    # print(type(time.time()))
    print('Done!')


if __name__ == '__main__':
    asyncio.run(main())