from bs4 import BeautifulSoup
from ildar import get_link_from_menu_list_left
import tools


def gather_name_link_of_employess_it_licey(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    uls = soup.find_all('ul', class_='menu_list')

    employees = []
    for ul in uls:
        links = ul.find_all('a')
        for link in links:
            if "@" not in link.text:
                employees.append((link.text, link.get('href')))
    return employees


def parse_IT_licey(link):
    info_button_link = get_link_from_menu_list_left(link, 'Сведения об образовательной организации')
    info_prep_button_link = get_link_from_menu_list_left(info_button_link,
                                                         'Руководство. Педагогический (научно-педагогический) состав')
    employess = gather_name_link_of_employess_it_licey(info_prep_button_link)
    result = {"Педагогический состав":employess}
    return result

def gather_name_link_of_employess_licey_lobach(link):
    html = tools.get_html(link)
    soup = BeautifulSoup(html, 'lxml')

    uls = soup.find_all('ul', class_='menu_list')

    employees = []
    for ul in uls:
        links = ul.find_all('a')
        for link in links:
            if "@" not in link.text:
                employees.append((link.text, link.get('href')))
    return employees


def parse_lobach_licey(link):
    info_button_link = get_link_from_menu_list_left(link, 'Сведения об образовательной организации')
    info_prep_button_link = get_link_from_menu_list_left(info_button_link,
                                                         'Руководство. Педагогический (научно-педагогический) состав')
    employess = gather_name_link_of_employess_licey_lobach(info_prep_button_link)
    result = {"Педагогический состав": employess}
    return result