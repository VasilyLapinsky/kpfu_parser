from bs4 import BeautifulSoup
from ildar import get_link_from_menu_list_left
import tools


def gather_name_link_of_employees(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    employees = []

    iframe = soup.find('iframe')
    div = soup.find('div', class_='visit_link')
    if iframe:

        outer_src = iframe.get('src')

        html = tools.get_html(outer_src)
        soup = BeautifulSoup(html, 'lxml')

        spans = soup.find_all('span', class_='fio')

        for span in spans:
            a = span.find('a')
            if a:
                employees.append((a.text, a.get('href')))
    elif div:
        ps = div.find_all('p')

        for p in ps:
            a = p.find('a')
            if a:
                if 'КФУ' != a.text and 'Институт' not in a.text:
                    employees.append((a.text, a.get('href')))
    return employees


def gather_name_link_of_cathedras_of_school(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    ul = soup.find('ul', class_='menu_list_left')
    lis = ul.find_all('li')

    cathedras = []
    for li in lis:
        a = li.find('a')
        if a.text.startswith('Кафедра'):
            cathedras.append((a.text, a.get('href')))
    return cathedras


def gather_link_of_schools(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    ul = soup.find('ul', class_='menu_list_left')
    lis = ul.find_all('li')

    schools = []
    for li in lis:
        a = li.find('a')
        if a.text.startswith('Высшая школа'):
            schools.append(a.get('href'))
    return schools


def parse_philology(link):
    structure_button_link = get_link_from_menu_list_left(link, 'Структура')

    school_links = gather_link_of_schools(structure_button_link)

    cathedras = []
    for school in school_links:
        cathedras += gather_name_link_of_cathedras_of_school(school)

    result = {}

    for name, link in cathedras:
        stuff_link = get_link_from_menu_list_left(link, 'Сотрудники')
        result[name] = stuff_link

    for name, stuff_link in result.items():
        result[name] = gather_name_link_of_employees(stuff_link)

    return result


if __name__ == '__main__':
    parse_philology('https://kpfu.ru/philology-culture')
