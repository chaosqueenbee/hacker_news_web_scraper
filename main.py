from classes.combinator import Combinator

if __name__ == '__main__':
    combinator = Combinator()

    links = combinator.get_top_three_links()

    for link in links:
        print(f'{combinator.get_element_title(link)} - {combinator.get_element_link(link)}')