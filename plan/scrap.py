import asyncio
import aiohttp
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, link_list):
        self.link_list = set(link_list)
        self.html_list = set()

    def __str__(self):
        string = ''
        for link in self.link_list:
            string = f'{link} {string}'
        return string

    def __add__(self, other):
        return self.link_list | other.link_list

    def __enter__(self):
        self.main()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    async def __download_site(self, session, url):
        try:
            async with session.get(url) as response:
                self.html_list.add(await response.text())
        except Exception as e:
            print(e)

    async def download_all_sites(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            # proggres bar would be nice but i don't know how to force async tqdm to behave correctly
            print('Downloading sites')
            for url in self.link_list:
                task = asyncio.ensure_future(
                    self.__download_site(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)

    def main(self):
        asyncio.get_event_loop().run_until_complete(self.download_all_sites())
