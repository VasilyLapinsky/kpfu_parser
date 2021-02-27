from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from ildar import get_link_from_menu_list_left, gather_name_link_of_employees, gather_name_link_of_cathedras_of_ivmiit


def parse_higher_school_buisness(link):
    employees_link = get_link_from_menu_list_left(link, 'Список сотрудников')
    return {'Основная кафедра школы': gather_name_link_of_employees(employees_link)}


def parse_economics(link):
    struct_link = get_link_from_menu_list_left(link, 'Структура')
    cathedras_link = get_link_from_menu_list_left(struct_link, 'Кафедры')

    cathedras = gather_name_link_of_cathedras_of_ivmiit(cathedras_link)
    result = {}

    for name, link in cathedras:
        stuff_link = get_link_from_menu_list_left(link, 'Сотрудники')
        result[name] = stuff_link

    return result


def create_vizualization(data):
    general_counter = {}
    for institute_name, cathedras in data.items():
        cathedra_counter = {}
        for cathedra_name, stuff in cathedras.items():
            if stuff:
                cathedra_counter[cathedra_name] = len(stuff)
        general_counter[institute_name] = cathedra_counter
    # pprint(general_counter)

    # Считаем по институтам
    institutes = [institute_name for institute_name, cathedras in general_counter.items()]
    institutes_counter = [sum([counter for cathedras_name, counter in cathedras.items()])
                          for institute_name, cathedras in general_counter.items()]
    # Создаем фигуру
    fig = plt.figure(constrained_layout=True)
    fig.set_size_inches(20, 10 * ((len(institutes) + 1) // 2))
    # Размечаем фигуру
    gs = GridSpec(2 + (len(institutes) + 1) // 2, 2, figure=fig)

    ax = fig.add_subplot(gs[:1, :])
    ax.set_title("Распределение сотрудников по инcтитутам")
    ax.pie(institutes_counter, labels=institutes,
           autopct=lambda pct: f"{int(pct * sum(institutes_counter) / 100)}", shadow=False)

    for i, institute in enumerate(institutes):
        ax = fig.add_subplot(gs[1 + (i // 2), i % 2])
        ax.set_title(f"Распределение сотрудников в {institute}\n "
                     f"с общим числом сотрудников: {institutes_counter[i]}")
        cathedras = [cathedras_name for cathedras_name, counter in general_counter[institute].items()]
        cathedras_counter = [counter for cathedras_name, counter in general_counter[institute].items()]
        ax.pie(cathedras_counter, labels=cathedras,
               autopct=lambda pct: f"{int(pct * sum(cathedras_counter) / 100)}", shadow=False)

    plt.show()
