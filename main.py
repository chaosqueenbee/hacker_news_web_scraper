from classes.web_scraper import WebScraper

class Combinator:
    def __init__(self):
        web_scraper = WebScraper()

        combinator_page = web_scraper.get_page('https://news.ycombinator.com/best')
        
        if combinator_page.status_code != 200:
            raise ValueError("Error retrieving page.")
        
        self.combinator_html = web_scraper.scrape(combinator_page.content)

    def prettify(self):
        return self.combinator_html.prettify()
        
    def get_top_three_links(self):
        # body = list(self.combinator_html.children)[0]
        # return list(body)
        links = self.combinator_html.find_all(class_='titlelink')
        return links[0:3]
    
    def get_element_title(self, element):
        return element.get_text()
    
    def get_element_link(self, element):
        return element['href']

if __name__ == '__main__':
    combinator = Combinator()

    links = combinator.get_top_three_links()

    for link in links:
        print(f'{combinator.get_element_title(link)} - {combinator.get_element_link(link)}')