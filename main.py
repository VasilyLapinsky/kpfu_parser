import tools
import constants
from pprint import pprint

from ildar import gather_name_link_of_institutes_and_branches, parse_ivmiit, parse_geogr, parse_physical
from vasia import parse_higher_school_buisness, create_visualization
from sergey import parse_psychology
from maks import parse_ipot
from rama import parse_engineer
from alsu import parse_chill
from ilsiyar import parse_phys, parse_law, parse_chem
from timur import parse_mehmat, parse_imo
from regina import parse_philology
from anton import parse_lobach_licey, parse_IT_licey


def main():
    html = tools.get_html(constants.initial_url)
    institutes = gather_name_link_of_institutes_and_branches(html)
    print(f'институты: {institutes}')
    print(f'количество институтов: {len(institutes)}')

    parsing_dictionary = {
        'Институт экологии и природопользования': parse_geogr,
        'Институт геологии и нефтегазовых технологий': None,
        'Институт математики и механики им. Н.И. Лобачевского': parse_mehmat,
        'Институт физики': parse_phys,
        'Химический институт им. А.М. Бутлерова': parse_chem,
        'Юридический факультет': parse_law,
        'Институт вычислительной математики и информационных технологий': parse_ivmiit,
        'Институт филологии и межкультурной коммуникации': parse_philology,
        'Институт психологии и образования': parse_psychology,
        'Общеуниверситетская кафедра физического воспитания и спорта': parse_physical,
        'Институт информационных технологий и интеллектуальных систем': None,
        'Институт фундаментальной медицины и биологии': None,
        'Инженерный институт': parse_engineer,
        'Институт международных отношений': parse_imo,
        'Высшая школа бизнеса': parse_higher_school_buisness,
        'Институт социально-философских наук и массовых коммуникаций': None,
        'Институт управления, экономики и финансов': None,
        'Высшая школа государственного и муниципального управления': None,
        'Центр корпоративного обучения': None,
        'IT-лицей-интернат КФУ': parse_IT_licey,
        'Лицей имени Н.И.Лобачевского': parse_lobach_licey,
        'Подготовительный факультет для иностранных учащихся': None,
        'Приволжский центр повышения квалификации и профессиональной переподготовки работников образования': None,
        'Центр непрерывного повышения профессионального мастерства педагогических работников': None,
        'Медико-санитарная часть ФГАОУ ВО КФУ': None,
        'Центр цифровых трансформаций': None,
        'Институт передовых образовательных технологий': parse_ipot,
        'Набережночелнинский институт КФУ': parse_chill,
        'Елабужский институт КФУ': None}

    data = {}
    for name, link in institutes:
        func = parsing_dictionary.get(name)
        if func:
            data[name] = func(link)

    # pprint(data)
    create_visualization(data)


if __name__ == '__main__':
    main()
