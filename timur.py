from bs4 import BeautifulSoup
import tools
import ildar

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
        ps = div.find('p')
        for p in ps.contents:
            if '<br/>' not in str(p):
                employees.append((str(p)))
    return employees

def parse_imo(link):
    struct_buton_link = ildar.get_link_from_menu_list_left(link,'Структура')

    cathedras = ildar.gather_name_link_of_cathedras_of_geogr(struct_buton_link)
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

    lis = []
    for ul in uls:
        lis += ul.find_all('li', class_='li_spec')
    print(lis)
    cathedras = []
    for li in lis:
        a = li.find('a')
        print(a)
        print('_______')
        if a.text.startswith('Кафедpа'):
            cathedras.append((a.text, a.get('href')))
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
        tbody = soup.find_all('tbody')[1]
        trs = tbody.find_all('tr')
        for tr in trs:
            td = tr.find('td')
            p = td.find('p')
            a = p.find_all('a')[0]
            if a:
                employees.append((a.text, a.get('href')))
    return employees


def parse_mehmat(link):
    struct_buton_link = ildar.get_link_from_menu_list_left(link,'Структура')

    cathedras = gather_name_link_of_cathedras_of_mehmat(struct_buton_link)
    result = {}
    print(cathedras)
    for name, link in cathedras:
        stuff_link1 = ildar.get_link_from_menu_list_left(link, 'Сотрудники')
        stuff_link2 = ildar.get_link_from_menu_list_left(link, 'Сотрудники кафедры')
        if stuff_link1:
            result[name] = stuff_link1
        if stuff_link2:
            result[name] = stuff_link2

    for name, stuff_link in result.items():
        result[name] = gather_name_link_of_employees_mehmat(stuff_link)
    i = 1
    return result