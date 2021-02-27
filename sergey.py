from bs4 import BeautifulSoup
from ildar import get_link_from_menu_list_left

import tools


def gather_name_link_of_cathedras_of_psychology(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    ul = soup.find('ul', class_='menu_list_left')

    lis = ul.find_all('li')

    cathedras = []
    for li in lis:
        a = li.find('a')
        cathedras.append((a.text, a.get('href')))
    return cathedras


def gather_name_link_of_psychology_employee_engine(link):
    html = tools.get_html_with_engine(link)
    soup = BeautifulSoup(html, 'lxml')

    div = soup.find('div', class_='left_width')

    links = div.find_all('a')

    employees = []
    for link in links:
        if link:
            employees.append((link.text, link.get('href')))

    return employees


def gather_name_link_of_psychology_employees(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    div = soup.find('div', class_='visit_link')

    links = div.find_all('a')

    employees = []
    for link in links:
        if link:
            employees.append((link.text, link.get('href')))

    return employees


def parse_psychology(link):
    struct_button_link = get_link_from_menu_list_left(link, 'Структура')

    cathedras_button_link = get_link_from_menu_list_left(struct_button_link, 'Кафедры')

    cathedras = gather_name_link_of_cathedras_of_psychology(cathedras_button_link)

    result = {}

    for name, link in cathedras:
        stuff_link1 = get_link_from_menu_list_left(link, 'Сотрудники')
        stuff_link2 = get_link_from_menu_list_left(link, 'Сотрудники кафедры')
        if stuff_link1:
            result[name] = stuff_link1
        elif stuff_link2:
            result[name] = stuff_link2

    for name, stuff_link in result.items():
        if name == 'Кафедра дошкольного образования':
            result[name] = gather_name_link_of_psychology_employees(stuff_link)
        else:
            result[name] = gather_name_link_of_psychology_employee_engine(stuff_link)

    return result

