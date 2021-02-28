from bs4 import BeautifulSoup
import tools
import ildar


def gather_name_link_of_cathedras_of_imo(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    div = soup.find('div', class_='visit_link')

    links = div.find_all('a')

    cathedras = []
    for a in links:
        if 'Кафедра' in a.text:
            cathedras.append((a.text, a.get('href')))
    return cathedras


def gather_name_link_of_employees_imo(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    employees = []

    iframe = soup.find('iframe')
    if iframe:
        outer_src = iframe.get('src')

        html = tools.get_html(outer_src)
        soup = BeautifulSoup(html, 'lxml')

        spans = soup.find_all('span', class_='fio')

        employees = []
        for span in spans:
            a = span.find('a')
            if a:
                employees.append((a.text, a.get('href')))
    else:
        div = soup.find('div', class_='visit_link')
        p = div.find('p')
        for row in p.text.split('\r\n'):
            employees.append((row, None))
    return employees


def parse_imo(link):
    struct_button_link = ildar.get_link_from_menu_list_left(link, 'Структура')

    cathedras = gather_name_link_of_cathedras_of_imo(struct_button_link)
    result = {}

    for name, link in cathedras:
        stuff_link1 = ildar.get_link_from_menu_list_left(link, 'Сотрудники')
        stuff_link2 = ildar.get_link_from_menu_list_left(link, 'Состав кафедры')
        if stuff_link1:
            result[name] = stuff_link1
        if stuff_link2:
            result[name] = stuff_link2

    for name, stuff_link in result.items():
        result[name] = gather_name_link_of_employees_imo(stuff_link)
    i = 1
    return result


def gather_name_link_of_cathedras_of_mehmat(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    uls = soup.find_all('ul', class_='menu_list')

    list_links = []
    for ul in uls:
        list_links.append(ul.find_all('a'))

    cathedras = []
    for list in list_links:
        for link in list:
            if link.text.startswith('Кафедpа') or link.text.startswith('Кафедра'):
                cathedras.append((link.text, link.get('href')))
    return cathedras


def gather_name_link_of_employees_mehmat(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    employees = []

    iframe = soup.find('iframe')
    if iframe:
        outer_src = iframe.get('src')

        html = tools.get_html(outer_src)
        soup = BeautifulSoup(html, 'lxml')

        spans = soup.find_all('span', class_='fio')

        employees = []
        for span in spans:
            a = span.find('a')
            if a:
                employees.append((a.text, a.get('href')))
    else:
        tbody = soup.find_all('tbody')[0]
        trs = tbody.find_all('tr')
        for tr in trs:
            td = tr.find('td')
            p = td.find('p')
            a = p.find_all('a')[0]
            if a:
                employees.append((a.text, a.get('href')))
    return employees


def parse_mehmat(link):
    struct_button_link = ildar.get_link_from_menu_list_left(link, 'Структура')

    cathedras = gather_name_link_of_cathedras_of_mehmat(struct_button_link)
    result = {}
    for name, link in cathedras:
        stuff_link1 = ildar.get_link_from_menu_list_left(link, 'Сотрудники')
        stuff_link2 = ildar.get_link_from_menu_list_left(link, 'Состав кафедры')
        if stuff_link1:
            result[name] = stuff_link1
        elif stuff_link2:
            result[name] = stuff_link2
    for name, stuff_link in result.items():
        result[name] = gather_name_link_of_employees_mehmat(stuff_link)

    return result
