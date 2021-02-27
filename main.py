import tools
import constants
from pprint import pprint

from ildar import gather_name_link_of_institutes_and_branches, parse_ivmiit, parse_geogr, parse_physical
from vasia import parse_higher_school_buisness
from sergey import parse_psychology
from maks import parse_ipot
from rama import parse_engineer
from alsu import parse_chill
from ilsiyar import parse_phys, parse_law, parse_chem
from regina import parse_philology

# def main():
#     html = tools.get_html(constants.initial_url)
#     institutes = gather_name_link_of_institutes_and_branches(html)
#     print(f'институты: {institutes}')
#     print(f'количество институтов: {len(institutes)}')
#
#     parsing_dictionary = {
#         'Институт экологии и природопользования': parse_geogr,
#         'Институт геологии и нефтегазовых технологий': None,
#         'Институт математики и механики им. Н.И. Лобачевского': None,
#         'Институт физики': parse_phys,
#         'Химический институт им. А.М. Бутлерова': parse_chem,
#         'Юридический факультет': parse_law,
#         'Институт вычислительной математики и информационных технологий': parse_ivmiit,
#         'Институт филологии и межкультурной коммуникации': parse_philology,
#         'Институт психологии и образования': parse_psychology,
#         'Общеуниверситетская кафедра физического воспитания и спорта': parse_physical,
#         'Институт информационных технологий и интеллектуальных систем': None,
#         'Институт фундаментальной медицины и биологии': None,
#         'Инженерный институт': parse_engineer,
#         'Институт международных отношений': None,
#         'Высшая школа бизнеса': parse_higher_school_buisness,
#         'Институт социально-философских наук и массовых коммуникаций': None,
#         'Институт управления, экономики и финансов': None,
#         'Высшая школа государственного и муниципального управления': None,
#         'Центр корпоративного обучения': None,
#         'IT-лицей-интернат КФУ': None,
#         'Лицей имени Н.И.Лобачевского': None,
#         'Подготовительный факультет для иностранных учащихся': None,
#         'Приволжский центр повышения квалификации и профессиональной переподготовки работников образования': None,
#         'Центр непрерывного повышения профессионального мастерства педагогических работников': None,
#         'Медико-санитарная часть ФГАОУ ВО КФУ': None,
#         'Центр цифровых трансформаций': None,
#         'Институт передовых образовательных технологий': parse_ipot,
#         'Набережночелнинский институт КФУ': parse_chill,
#         'Елабужский институт КФУ': None}
#
#     data = {}
#     for name, link in institutes:
#         func = parsing_dictionary.get(name)
#         if func:
#             data[name] = func(link)
#
#     pprint(data)


if __name__ == '__main__':
    # main()

    data = {'Высшая школа бизнеса': {'Основная кафедра школы': [('Ахметшина Алсу '
                                                                 'Ринатовна',
                                                                 'https://kpfu.ru/Alsu.Ahmetshina'),
                                                                ('Вагизова Венера '
                                                                 'Ильдусовна',
                                                                 'https://kpfu.ru/venera.vagizova'),
                                                                ('Галлямова Динара '
                                                                 'Хамитовна',
                                                                 'https://kpfu.ru/Dinara.Gallyamova'),
                                                                ('Каспина Роза '
                                                                 'Григорьевна',
                                                                 'https://kpfu.ru/roza.kaspina'),
                                                                ('Киршин Игорь '
                                                                 'Александрович',
                                                                 'https://kpfu.ru/Igor.Kirchine'),
                                                                ('Ягудин Рамил Хаевич',
                                                                 'https://kpfu.ru/ramil.yagudin'),
                                                                ('Тухватуллин Руслан '
                                                                 'Шавкатович',
                                                                 'https://kpfu.ru/ruslans.tuhvatullin'),
                                                                ('Арсланов Артур '
                                                                 'Шамильевич',
                                                                 'https://kpfu.ru/artur.arslanov'),
                                                                ('Захматов Дмитрий '
                                                                 'Юрьевич',
                                                                 'https://kpfu.ru/dmitrij.zahmatov'),
                                                                ('Рахманова Ильнара '
                                                                 'Ильнуровна',
                                                                 'https://kpfu.ru/ilnara.rahmanova'),
                                                                ('Абдуллина Лилия '
                                                                 'Габделахатовна',
                                                                 'https://kpfu.ru/1Liliya.Abdullina'),
                                                                ('Каюмова Ландыш '
                                                                 'Кадимовна',
                                                                 'https://kpfu.ru/landysh.kajumova'),
                                                                ('Роговская Наталия '
                                                                 'Геннадиевна',
                                                                 'https://kpfu.ru/nataliya.rogovskaya'),
                                                                ('Рахматуллин Ильдар '
                                                                 'Алмасович',
                                                                 'https://kpfu.ru/ildar.rakhmatullin'),
                                                                ('Кудрявцева Марина '
                                                                 'Геннадьевна',
                                                                 'https://kpfu.ru/Marina.Kudryavceva'),
                                                                ('Захарова Анна '
                                                                 'Николаевна',
                                                                 'https://kpfu.ru/Anna.Zaharova'),
                                                                ('Ахкямова Алсу '
                                                                 'Наргизовна',
                                                                 'https://kpfu.ru/alsun.valeeva'),
                                                                ('Валиева Зиля Ринатовна',
                                                                 'https://kpfu.ru/zilya.galimullina'),
                                                                ('Михалевич Полина '
                                                                 'Олеговна',
                                                                 'https://kpfu.ru/polina.mikhalevich')]},
            'Инженерный институт': {'Кафедра биомедицинской инженерии и управления инновациями': None,
                                    'Кафедра технической физики и энергетики': None,
                                    'Кафедра управления качеством': [('Бикмуллина Ильсияр '
                                                                      'Ильдаровна',
                                                                      'https://kpfu.ru/ilsiyar.bikmullina'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Воронцов Дмитрий '
                                                                      'Петрович',
                                                                      'https://kpfu.ru/dmitrij.voroncov'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Галеев Рустем '
                                                                      'Дамирович',
                                                                      'https://kpfu.ru/rustem.galeev'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Деваев Вячеслав '
                                                                      'Михайлович',
                                                                      'https://kpfu.ru/vyacheslav.devaev'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Елизарова Наталья '
                                                                      'Юрьевна',
                                                                      'https://kpfu.ru/natalya.elizarova'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Закирова Альфия '
                                                                      'Равильевна',
                                                                      'https://kpfu.ru/alfiya.zakirova'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Ильина Кристина '
                                                                      'Георгиевна',
                                                                      'https://kpfu.ru/kristina.ilina'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Конахина Ирина '
                                                                      'Александровна',
                                                                      'https://kpfu.ru/irina.konahina'),
                                                                     ('Кузьмина Ирина '
                                                                      'Александровна',
                                                                      'https://kpfu.ru/Irina.Kuzmina'),
                                                                     ('Сиразетдинов '
                                                                      'Рифкат Талгатович',
                                                                      'https://kpfu.ru/rifkat.sirazetdinov'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Смирнова Гульнара '
                                                                      'Сергеевна',
                                                                      'https://kpfu.ru/gulnara.smirnova'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Суркин Наиль '
                                                                      'Рашадович',
                                                                      'https://kpfu.ru/nail.surkin'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Фадеев Андрей '
                                                                      'Юрьевич',
                                                                      'https://kpfu.ru/andrej.fadeev'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Хамидуллина '
                                                                      'Гульнара '
                                                                      'Рафкатовна',
                                                                      'https://kpfu.ru/gulnara.hamidullina'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Хафизов Ильдар '
                                                                      'Ильсурович',
                                                                      'https://kpfu.ru/ildar.hafizov'),
                                                                     ('Храмов Юрий '
                                                                      'Владимирович',
                                                                      'https://kpfu.ru/yurij.khramov'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Хуснутдинова '
                                                                      'Эльвира '
                                                                      'Мусавировна',
                                                                      'https://kpfu.ru/elvira.husnutdinova'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Шихалёв Анатолий '
                                                                      'Михайлович',
                                                                      'https://kpfu.ru/anatolij.shihalev'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/'),
                                                                     ('Юнусова Гульназ '
                                                                      'Рашитовна',
                                                                      'https://kpfu.ru/gulnaz.gatina'),
                                                                     ('КФУ',
                                                                      'http://kpfu.ru/')]},
            'Институт вычислительной математики и информационных технологий': {
                'Кафедра анализа данных и исследования операций': [('Абдуллин '
                                                                    'Адель '
                                                                    'Ильдусович',
                                                                    'https://kpfu.ru/adeli.abdullin'),
                                                                   ('Бандеров '
                                                                    'Виктор '
                                                                    'Викторович',
                                                                    'https://kpfu.ru/Victor.Banderov'),
                                                                   ('Бикчентаев '
                                                                    'Айрат '
                                                                    'Мидхатович',
                                                                    'https://kpfu.ru/Airat.Bikchentaev'),
                                                                   ('Габидуллина '
                                                                    'Зульфия '
                                                                    'Равилевна',
                                                                    'https://kpfu.ru/Zulfiya.Gabidullina'),
                                                                   ('Заботин '
                                                                    'Игорь '
                                                                    'Ярославич',
                                                                    'https://kpfu.ru/Igor.Zabotin'),
                                                                   ('Казаева '
                                                                    'Ксения '
                                                                    'Евгеньевна',
                                                                    'https://kpfu.ru/kseniya.kazaeva'),
                                                                   ('Кораблев '
                                                                    'Анатолий '
                                                                    'Иванович',
                                                                    'https://kpfu.ru/Anatol.Korablev'),
                                                                   ('Лернер '
                                                                    'Эдуард '
                                                                    'Юльевич',
                                                                    'https://kpfu.ru/Edouard.Lerner'),
                                                                   ('Миссаров '
                                                                    'Мукадас '
                                                                    'Дмухтасибович',
                                                                    'https://kpfu.ru/Moukadas.Missarov'),
                                                                   ('Мухтарова '
                                                                    'Татьяна '
                                                                    'Маратовна',
                                                                    'https://kpfu.ru/Tatyana.Moukhtarova'),
                                                                   ('Остроумов '
                                                                    'Анатолий '
                                                                    'Павлович',
                                                                    'https://kpfu.ru/anatolij.ostroumov'),
                                                                   ('Пинягина '
                                                                    'Ольга '
                                                                    'Владиславовна',
                                                                    'https://kpfu.ru/Olga.Piniaguina'),
                                                                   ('Фофанов '
                                                                    'Вячеслав '
                                                                    'Борисович',
                                                                    'https://kpfu.ru/Viatcheslav.Fofanov'),
                                                                   ('Чебакова '
                                                                    'Виолетта '
                                                                    'Юрьевна',
                                                                    'https://kpfu.ru/violetta.chebakova'),
                                                                   ('Шульгина '
                                                                    'Оксана '
                                                                    'Николаевна',
                                                                    'https://kpfu.ru/Oksana.Shulgina'),
                                                                   ('Шустова '
                                                                    'Евгения '
                                                                    'Петровна',
                                                                    'https://kpfu.ru/Evgeniya.Shustova'),
                                                                   ('Яруллин '
                                                                    'Рашид '
                                                                    'Саматович',
                                                                    'https://kpfu.ru/rashid.yarullin')],
                'Кафедра вычислительной математики': [('Абдюшева '
                                                       'Гузель '
                                                       'Равильевна',
                                                       'https://kpfu.ru/Guzel.Abdusheva'),
                                                      ('Алексеев '
                                                       'Сергей '
                                                       'Сергеевич',
                                                       'https://kpfu.ru/Sergey.Alekseyev'),
                                                      ('Бадриев '
                                                       'Ильдар '
                                                       'Бурханович',
                                                       'https://kpfu.ru/Ildar.Badriev'),
                                                      ('Глазырина '
                                                       'Людмила '
                                                       'Леонидовна',
                                                       'https://kpfu.ru/Ludmila.Glazyrina'),
                                                      ('Глазырина '
                                                       'Ольга '
                                                       'Владимировна',
                                                       'https://kpfu.ru/olga.glazyrina'),
                                                      ('Гнеденкова '
                                                       'Валентина '
                                                       'Львовна',
                                                       'https://kpfu.ru/Valentina.Gnedenkova'),
                                                      ('Даутов '
                                                       'Рафаил '
                                                       'Замилович',
                                                       'https://kpfu.ru/Rafail.Dautov'),
                                                      ('Задворнов '
                                                       'Олег '
                                                       'Анатольевич',
                                                       'https://kpfu.ru/Oleg.Zadvornov'),
                                                      ('Макаров '
                                                       'Максим '
                                                       'Викторович',
                                                       'https://kpfu.ru/maksim.makarov'),
                                                      ('Павлова '
                                                       'Мария '
                                                       'Филипповна',
                                                       'https://kpfu.ru/Maria.Pavlova'),
                                                      ('Панкратова '
                                                       'Ольга '
                                                       'Владиславна',
                                                       'https://kpfu.ru/Olga.Pankratova'),
                                                      ('Соловьев '
                                                       'Сергей '
                                                       'Иванович',
                                                       'https://kpfu.ru/Sergei.Solovyev'),
                                                      ('Тимербаев '
                                                       'Марат '
                                                       'Равилевич',
                                                       'https://kpfu.ru/Marat.Timerbaev'),
                                                      ('Трифонова '
                                                       'Галина '
                                                       'Олеговна',
                                                       'https://kpfu.ru/galina.trifonova')],
                'Кафедра информационных систем': [('Аюпов '
                                                   'Мадехур '
                                                   'Масхутович',
                                                   'https://kpfu.ru/madehur.ajupov'),
                                                  ('Бронская '
                                                   'Вероника '
                                                   'Владимировна',
                                                   'https://kpfu.ru/veronika.bronskaya'),
                                                  ('Габдулхакова '
                                                   'Диляра '
                                                   'Рустемовна',
                                                   'https://kpfu.ru/dilyara.gabdulkhakova'),
                                                  ('Галимянов '
                                                   'Анис '
                                                   'Фуатович',
                                                   'https://kpfu.ru/Anis.Galimjanoff'),
                                                  ('Галиуллин '
                                                   'Дамир '
                                                   'Кахирович',
                                                   'https://kpfu.ru/Damir.Galiullin'),
                                                  ('Гатиатуллин '
                                                   'Айрат '
                                                   'Рафизович',
                                                   'https://kpfu.ru/Ajrat.Gatiatullin'),
                                                  ('Гафаров '
                                                   'Фаиль '
                                                   'Мубаракович',
                                                   'https://kpfu.ru/Fail.Gafarov'),
                                                  ('Гилемзянов '
                                                   'Алмаз '
                                                   'Фирдинантович',
                                                   'https://kpfu.ru/almaz.gilemzyanov'),
                                                  ('Гиниятуллина '
                                                   'Гульчачак '
                                                   'Ришатовна',
                                                   'https://kpfu.ru/gulchachak.giniyatullina'),
                                                  ('Голицына '
                                                   'Ирина '
                                                   'Николаевна',
                                                   'https://kpfu.ru/Irina.Golicyna'),
                                                  ('Маклецов '
                                                   'Сергей '
                                                   'Владиславович',
                                                   'https://kpfu.ru/Serge.Makletsov'),
                                                  ('Медведева '
                                                   'Ольга '
                                                   'Анатолиевна',
                                                   'https://kpfu.ru/olgaa.medvedeva'),
                                                  ('Миннегалиева '
                                                   'Чулпан '
                                                   'Бакиевна',
                                                   'https://kpfu.ru/Chulpan.Minnegalieva'),
                                                  ('Мухаметшина '
                                                   'Миляуша '
                                                   'Маратовна',
                                                   'https://kpfu.ru/milyausha.muhametshina'),
                                                  ('Невзорова '
                                                   'Ольга '
                                                   'Авенировна',
                                                   'https://kpfu.ru/Olga.Nevzorova'),
                                                  ('Сагдеева '
                                                   'Розалия '
                                                   'Фагмутдиновна',
                                                   'https://kpfu.ru/rozaliya.sagdeeva'),
                                                  ('Сулейманов '
                                                   'Джавдет '
                                                   'Шевкетович',
                                                   'https://kpfu.ru/Djavdet.Suleymanov'),
                                                  ('Сулейманов '
                                                   'Янис '
                                                   'Адисович',
                                                   'https://kpfu.ru/yanis.suleymanov'),
                                                  ('Тихомиров '
                                                   'Сергей '
                                                   'Игоревич',
                                                   'https://kpfu.ru/sergey.tikhomirov'),
                                                  ('Хайруллина '
                                                   'Лилия '
                                                   'Эмитовна',
                                                   'https://kpfu.ru/Liliya.Hajrullina'),
                                                  ('Широкова '
                                                   'Ольга '
                                                   'Александровна',
                                                   'https://kpfu.ru/Olga.Shirokova')],
                'Кафедра математической статистики': [('Асхатов '
                                                       'Радик '
                                                       'Мухаметгалеевич',
                                                       'https://kpfu.ru/Radik.Ashatov'),
                                                      ('Володин '
                                                       'Игорь '
                                                       'Николаевич',
                                                       'https://kpfu.ru/Igor.Volodin'),
                                                      ('Гимадеева '
                                                       'Динара '
                                                       'Айратовна',
                                                       'https://kpfu.ru/dinaraa.gimadeeva'),
                                                      ('Григорьева '
                                                       'Ирина '
                                                       'Сергеевна',
                                                       'https://kpfu.ru/Irina.Grigorieva'),
                                                      ('Дубровин '
                                                       'Вячеслав '
                                                       'Тимофеевич',
                                                       'https://kpfu.ru/Vyacheslav.Dubrovin'),
                                                      ('Заикин '
                                                       'Артем '
                                                       'Александрович',
                                                       'https://kpfu.ru/artem.zaikin'),
                                                      ('Игнатьева '
                                                       'Марина '
                                                       'Александровна',
                                                       'https://kpfu.ru/Marina.Ignatieva'),
                                                      ('Казанцев '
                                                       'Андрей '
                                                       'Витальевич',
                                                       'https://kpfu.ru/Andrei.Kazantsev'),
                                                      ('Кареев '
                                                       'Искандер '
                                                       'Амирович',
                                                       'https://kpfu.ru/iskander.kareev'),
                                                      ('Каштанова '
                                                       'Елена '
                                                       'Кирилловна',
                                                       'https://kpfu.ru/Elena.Kashtanova'),
                                                      ('Мавлявиев '
                                                       'Ринат '
                                                       'Мизхатович',
                                                       'https://kpfu.ru/Rinat.Mavlyaviev'),
                                                      ('Романенко '
                                                       'Артур '
                                                       'Данилевич',
                                                       'https://kpfu.ru/artur.romanenko'),
                                                      ('Салимов '
                                                       'Рустем '
                                                       'Фаридович',
                                                       'https://kpfu.ru/Rustem.Salimov'),
                                                      ('Сидоров '
                                                       'Анатолий '
                                                       'Михайлович',
                                                       'https://kpfu.ru/Anatoly.Sidorov'),
                                                      ('Симушкин '
                                                       'Дмитрий '
                                                       'Сергеевич',
                                                       'https://kpfu.ru/dmitrij.simushkin'),
                                                      ('Симушкин '
                                                       'Сергей '
                                                       'Владимирович',
                                                       'https://kpfu.ru/Sergey.Simushkin'),
                                                      ('Тихонов '
                                                       'Олег '
                                                       'Евгеньевич',
                                                       'https://kpfu.ru/Oleg.Tikhonov'),
                                                      ('Чебакова '
                                                       'Виолетта '
                                                       'Юрьевна',
                                                       'https://kpfu.ru/violetta.chebakova'),
                                                      ('Шерман '
                                                       'Евгений '
                                                       'Дмитриевич',
                                                       'https://kpfu.ru/Evgenyi.Sherman')],
                'Кафедра прикладной математики': [('Абгарян '
                                                   'Гарник '
                                                   'Владимирович',
                                                   'https://kpfu.ru/garnik.abgaryan'),
                                                  ('Александрова '
                                                   'Ирина '
                                                   'Леонидовна',
                                                   'https://kpfu.ru/1Irina.Alexandrova'),
                                                  ('Бахтиева '
                                                   'Ляля '
                                                   'Узбековна',
                                                   'https://kpfu.ru/Lyalya.Bakhtieva'),
                                                  ('Валеева '
                                                   'Алсу '
                                                   'Анваровна',
                                                   'https://kpfu.ru/alsua.valeeva'),
                                                  ('Гиниятова '
                                                   'Динара '
                                                   'Халиловна',
                                                   'https://kpfu.ru/Dinara.Ginijatova'),
                                                  ('Данилова '
                                                   'Анастасия '
                                                   'Вадимовна',
                                                   'https://kpfu.ru/anastasiya.anufrieva'),
                                                  ('Карчевский '
                                                   'Евгений '
                                                   'Михайлович',
                                                   'https://kpfu.ru/Evgenii.Karchevskii'),
                                                  ('Кокунин '
                                                   'Петр '
                                                   'Анатольевич',
                                                   'https://kpfu.ru/petr.kokunin'),
                                                  ('Конюхов '
                                                   'Владимир '
                                                   'Михайлович',
                                                   'https://kpfu.ru/Vladimir.Konyukhov'),
                                                  ('Кугураков '
                                                   'Владимир '
                                                   'Сергеевич',
                                                   'https://kpfu.ru/Vladimir.Kugurakov'),
                                                  ('Маркина '
                                                   'Ангелина '
                                                   'Геннадьевна',
                                                   'https://kpfu.ru/angelina.markina'),
                                                  ('Мокейчев '
                                                   'Валерий '
                                                   'Степанович',
                                                   'https://kpfu.ru/Valery.Mokeychev'),
                                                  ('Мосин '
                                                   'Сергей '
                                                   'Геннадьевич',
                                                   'https://kpfu.ru/sergej.mosin'),
                                                  ('Мусин '
                                                   'Фоат '
                                                   'Минегереевич',
                                                   'https://kpfu.ru/foat.musin'),
                                                  ('Мухачева '
                                                   'Наиля '
                                                   'Шарифовна',
                                                   'https://kpfu.ru/Nailya.Muhachyova'),
                                                  ('Насырова '
                                                   'Наиля '
                                                   'Халитовна',
                                                   'https://kpfu.ru/Nailya.Nasyrova'),
                                                  ('Осипов '
                                                   'Евгений '
                                                   'Александрович',
                                                   'https://kpfu.ru/Evgenij.Osipov'),
                                                  ('Плещинский '
                                                   'Николай '
                                                   'Борисович',
                                                   'https://kpfu.ru/Nikolai.Pleshchinskii'),
                                                  ('Рунг '
                                                   'Елена '
                                                   'Владимировна',
                                                   'https://kpfu.ru/Elena.Rung'),
                                                  ('Саламатин '
                                                   'Артур '
                                                   'Андреевич',
                                                   'https://kpfu.ru/artur.salamatin'),
                                                  ('Стехина '
                                                   'Кристина '
                                                   'Николаевна',
                                                   'https://kpfu.ru/Kristina.Stekhina'),
                                                  ('Тумаков '
                                                   'Дмитрий '
                                                   'Николаевич',
                                                   'https://kpfu.ru/Dmitri.Tumakov'),
                                                  ('Филиппов '
                                                   'Игорь '
                                                   'Евгеньевич',
                                                   'https://kpfu.ru/Igor.Filippov')],
                'Кафедра системного анализа и информационных технологий': [('Абайдуллин '
                                                                            'Равиль '
                                                                            'Нуралиевич',
                                                                            'https://kpfu.ru/Ravil.Abaydullin'),
                                                                           ('Андрианова '
                                                                            'Анастасия '
                                                                            'Александровна',
                                                                            'https://kpfu.ru/Anastasiya.Andrianova'),
                                                                           ('Багавеев '
                                                                            'Валерий '
                                                                            'Артурович',
                                                                            'https://kpfu.ru/valerij.bagaveev'),
                                                                           ('Васильев '
                                                                            'Александр '
                                                                            'Валерьевич',
                                                                            'https://kpfu.ru/Alexander.Vasiliev'),
                                                                           ('Гайнуллина '
                                                                            'Алина '
                                                                            'Рашидовна',
                                                                            'https://kpfu.ru/alinar.gajnullina'),
                                                                           ('Галанин '
                                                                            'Дмитрий '
                                                                            'Николаевич',
                                                                            'https://kpfu.ru/dmitrijn.galanin'),
                                                                           ('Галимова '
                                                                            'Гузель '
                                                                            'Ринатовна',
                                                                            'https://kpfu.ru/guzel.galimova'),
                                                                           ('Глазырина '
                                                                            'Ольга '
                                                                            'Владимировна',
                                                                            'https://kpfu.ru/olga.glazyrina'),
                                                                           ('Гостев '
                                                                            'Вадим '
                                                                            'Михайлович',
                                                                            'https://kpfu.ru/Vadim.Gostev'),
                                                                           ('Даулетзянова '
                                                                            'Сиреня '
                                                                            'Илгизовна',
                                                                            'https://kpfu.ru/sirena.yarullina'),
                                                                           ('Денисов '
                                                                            'Максим '
                                                                            'Павлович',
                                                                            'https://kpfu.ru/maksim.denisov'),
                                                                           ('Долгов '
                                                                            'Дмитрий '
                                                                            'Александрович',
                                                                            'https://kpfu.ru/Dmitrij.Dolgov'),
                                                                           ('Еникеев '
                                                                            'Разиль '
                                                                            'Радикович',
                                                                            'https://kpfu.ru/Razil.Enikeev'),
                                                                           ('Жуманиёзов '
                                                                            'Алишер '
                                                                            'Равшонбекович',
                                                                            'https://kpfu.ru/alisher.zhumaniezov'),
                                                                           ('Замов '
                                                                            'Наиль '
                                                                            'Калимович',
                                                                            'https://kpfu.ru/Nail.Zamov'),
                                                                           ('Захарова '
                                                                            'Ирина '
                                                                            'Александровна',
                                                                            'https://kpfu.ru/irina.bryzgalova'),
                                                                           ('Зиновьев '
                                                                            'Владислав '
                                                                            'Александрович',
                                                                            'https://kpfu.ru/vladislav.zinovev'),
                                                                           ('Зискин '
                                                                            'Владимир '
                                                                            'Фалкович',
                                                                            'https://kpfu.ru/vladimir.ziskin'),
                                                                           ('Ишмухаметов '
                                                                            'Шамиль '
                                                                            'Талгатович',
                                                                            'https://kpfu.ru/Shamil.Ishmukhametov'),
                                                                           ('Кашуба '
                                                                            'Алексей '
                                                                            'Юрьевич',
                                                                            'https://kpfu.ru/aleksej.kashuba'),
                                                                           ('Коннов '
                                                                            'Игорь '
                                                                            'Васильевич',
                                                                            'https://kpfu.ru/Igor.Konnov'),
                                                                           ('Куленева '
                                                                            'Юлиана '
                                                                            'Александровна',
                                                                            'https://kpfu.ru/juliana.kuleneva'),
                                                                           ('Курбангалеев '
                                                                            'Артур '
                                                                            'Аскарович',
                                                                            'https://kpfu.ru/artur.kurbangaleev'),
                                                                           ('Латыпов '
                                                                            'Рустам '
                                                                            'Хафизович',
                                                                            'https://kpfu.ru/Roustam.Latypov'),
                                                                           ('Михайлов '
                                                                            'Валерий '
                                                                            'Юрьевич',
                                                                            'https://kpfu.ru/Valery.Mikhailov'),
                                                                           ('Мубараков '
                                                                            'Булат '
                                                                            'Газинурович',
                                                                            'https://kpfu.ru/bulat.mubarakov'),
                                                                           ('Некрасова '
                                                                            'Юлия '
                                                                            'Александровна',
                                                                            'https://kpfu.ru/yuliya.nekrasova'),
                                                                           ('Нигматуллин '
                                                                            'Руслан '
                                                                            'Рафикович',
                                                                            'https://kpfu.ru/ruslan.nigmatullin'),
                                                                           ('Николаев '
                                                                            'Константин '
                                                                            'Сергеевич',
                                                                            'https://kpfu.ru/konstantin.nikolaev'),
                                                                           ('Нотфуллина '
                                                                            'Гульназ '
                                                                            'Рафаиловна',
                                                                            'https://kpfu.ru/gulnazr.safina'),
                                                                           ('Пшеничный '
                                                                            'Павел '
                                                                            'Витальевич',
                                                                            'https://kpfu.ru/Pavel.Pchenitchnyi'),
                                                                           ('Разинков '
                                                                            'Евгений '
                                                                            'Викторович',
                                                                            'https://kpfu.ru/Evgenij.Razinkov'),
                                                                           ('Репина '
                                                                            'Анна '
                                                                            'Игоревна',
                                                                            'https://kpfu.ru/anna.repina'),
                                                                           ('Рубцова '
                                                                            'Рамиля '
                                                                            'Гакилевна',
                                                                            'https://kpfu.ru/Ramilya.Rubtsova'),
                                                                           ('Свалова '
                                                                            'Ирина '
                                                                            'Евгеньевна',
                                                                            'https://kpfu.ru/irina.svalova'),
                                                                           ('Созутов '
                                                                            'Илья '
                                                                            'Георгиевич',
                                                                            'https://kpfu.ru/ilya.sozutov'),
                                                                           ('Степанова '
                                                                            'Анна '
                                                                            'Олеговна',
                                                                            'https://kpfu.ru/anna.soloduhina'),
                                                                           ('Тагиров '
                                                                            'Равиль '
                                                                            'Рафгатович',
                                                                            'https://kpfu.ru/Ravil.Tagirov'),
                                                                           ('Тихонова '
                                                                            'Нина '
                                                                            'Владимировна',
                                                                            'https://kpfu.ru/Nina.Tikhonova'),
                                                                           ('Тихонова '
                                                                            'Ольга '
                                                                            'Олеговна',
                                                                            'https://kpfu.ru/olga.tihonova'),
                                                                           ('Шаймухаметов '
                                                                            'Рамиль '
                                                                            'Рашитович',
                                                                            'https://kpfu.ru/Ramil.Shaimukhametov'),
                                                                           ('Шигапов '
                                                                            'Марат '
                                                                            'Ильясович',
                                                                            'https://kpfu.ru/Marat.Shigapov')],
                'Кафедра теоретической кибернетики': [('Аблаев '
                                                       'Фарид '
                                                       'Мансурович',
                                                       'https://kpfu.ru/Farid.Ablayev'),
                                                      ('Ахтямов '
                                                       'Рауф '
                                                       'Баграмович',
                                                       'https://kpfu.ru/Raouf.Akhtiamov'),
                                                      ('Байрашева '
                                                       'Венера '
                                                       'Рустамовна',
                                                       'https://kpfu.ru/Venera.Bajrasheva'),
                                                      ('Гайнутдинова '
                                                       'Аида '
                                                       'Фаритовна',
                                                       'https://kpfu.ru/Aida.Gainutdinova'),
                                                      ('Гусенков '
                                                       'Александр '
                                                       'Михайлович',
                                                       'https://kpfu.ru/Alexandr.Gusenkov'),
                                                      ('Кугураков '
                                                       'Владимир '
                                                       'Сергеевич',
                                                       'https://kpfu.ru/Vladimir.Kugurakov'),
                                                      ('Нурмеев '
                                                       'Наиль '
                                                       'Нуреевич',
                                                       'https://kpfu.ru/Nail.Nurmeev'),
                                                      ('Салимов '
                                                       'Фарид '
                                                       'Ибрагимович',
                                                       'https://kpfu.ru/Farid.Salimov'),
                                                      ('Хадиев '
                                                       'Камиль '
                                                       'Равилевич',
                                                       'https://kpfu.ru/Kamil.Hadiev'),
                                                      ('Хайруллин '
                                                       'Альфред '
                                                       'Фаридович',
                                                       'https://kpfu.ru/Alfred.Khairoullin'),
                                                      ('Шарафулисламова '
                                                       'Чулпан '
                                                       'Маратовна',
                                                       'https://kpfu.ru/chulpan.sharafulislamova')],
                'Кафедра технологий программирования': [('Ахмедова '
                                                         'Альфира '
                                                         'Мазитовна',
                                                         'https://kpfu.ru/Alfira.Ahmedova'),
                                                        ('Балафендиева '
                                                         'Ирина '
                                                         'Сергеевна',
                                                         'https://kpfu.ru/irina.balafendieva'),
                                                        ('Бурнашев '
                                                         'Рустам '
                                                         'Арифович',
                                                         'https://kpfu.ru/rustam.burnashev'),
                                                        ('Бухараев '
                                                         'Наиль '
                                                         'Раисович',
                                                         'https://kpfu.ru/Naille.Boukharaev'),
                                                        ('Вахитов '
                                                         'Галим '
                                                         'Зарибзянович',
                                                         'https://kpfu.ru/galim.vahitov'),
                                                        ('Галимуллин '
                                                         'Дамир '
                                                         'Зиннурович',
                                                         'https://kpfu.ru/Damir.Galimullin'),
                                                        ('Горбунов '
                                                         'Владислав '
                                                         'Маратович',
                                                         'https://kpfu.ru/vladislav.gorbunov'),
                                                        ('Еникеев '
                                                         'Арслан '
                                                         'Ильясович',
                                                         'https://kpfu.ru/Arslan.Enikeev'),
                                                        ('Еникеев '
                                                         'Искандер '
                                                         'Арсланович',
                                                         'https://kpfu.ru/iskander.enikeev'),
                                                        ('Еникеев '
                                                         'Камиль '
                                                         'Шамилевич',
                                                         'https://kpfu.ru/kamil.enikeev'),
                                                        ('Еникеева '
                                                         'Зульфира '
                                                         'Аснафовна',
                                                         'https://kpfu.ru/zulfira.enikeeva'),
                                                        ('Жуманиёзов '
                                                         'Алишер '
                                                         'Равшонбекович',
                                                         'https://kpfu.ru/alisher.zhumaniezov'),
                                                        ('Корчагин '
                                                         'Павел '
                                                         'Анатольевич',
                                                         'https://kpfu.ru/Pavel.Korchagin'),
                                                        ('Матренина '
                                                         'Ольга '
                                                         'Михайловна',
                                                         'https://kpfu.ru/olga.matrenina'),
                                                        ('Медведева '
                                                         'Ольга '
                                                         'Анатолиевна',
                                                         'https://kpfu.ru/olgaa.medvedeva'),
                                                        ('Прокопьев '
                                                         'Николай '
                                                         'Аркадьевич',
                                                         'https://kpfu.ru/nikolaj.prokopev'),
                                                        ('Сабитов '
                                                         'Шамиль '
                                                         'Рустэмович',
                                                         'https://kpfu.ru/shamil.sabitov'),
                                                        ('Ситдиков '
                                                         'Айрат '
                                                         'Салимович',
                                                         'https://kpfu.ru/ajrat.sitdikov'),
                                                        ('Хадиева '
                                                         'Алия '
                                                         'Ихсановна',
                                                         'https://kpfu.ru/aliya.hadieva')]},
            'Институт передовых образовательных технологий': {'Центр координации образовательных проектов': ['Руднева '
                                                                                                             'Яна '
                                                                                                             'Борисовна',
                                                                                                             'КФУ  '
                                                                                                             'Центр '
                                                                                                             'координации '
                                                                                                             'образовательных '
                                                                                                             'проектов '
                                                                                                             'КФУ,',
                                                                                                             'YBRudneva@kpfuru',
                                                                                                             'Тел '
                                                                                                             '2065080 '
                                                                                                             '(вн4201)',
                                                                                                             'Плотникова '
                                                                                                             'Луиза '
                                                                                                             'Альбертовна',
                                                                                                             'КФУ  '
                                                                                                             'Центр '
                                                                                                             'координации '
                                                                                                             'образовательных '
                                                                                                             'проектов '
                                                                                                             'КФУ,',
                                                                                                             'lplotnikova@kpfuru',
                                                                                                             'Тел '
                                                                                                             '2065080 '
                                                                                                             '(вн4200)',
                                                                                                             'Валиева '
                                                                                                             'Диляра '
                                                                                                             'Хикматулловна',
                                                                                                             'КФУ  '
                                                                                                             'Центр '
                                                                                                             'координации '
                                                                                                             'образовательных '
                                                                                                             'проектов '
                                                                                                             'КФУ,',
                                                                                                             'DKValieva@kpfuru',
                                                                                                             'Тел '
                                                                                                             '2065080 '
                                                                                                             '(вн4204)'],
                                                              'Центр корпоративного обучения': ['Заведующий '
                                                                                                'центром  '
                                                                                                'Бердникова '
                                                                                                'Ольга '
                                                                                                'Алексеевна',
                                                                                                'Сотрудники '
                                                                                                'ЦКОГлавный '
                                                                                                'специалист  '
                                                                                                'Масленникова '
                                                                                                'Екатерина '
                                                                                                'ЮрьевнаСпециалист '
                                                                                                'по '
                                                                                                'УМР '
                                                                                                'Токарева '
                                                                                                'Дарья '
                                                                                                'Сергеевна'],
                                                              'Центр развития онлайн-образования': ['Если '
                                                                                                    'у '
                                                                                                    'вас '
                                                                                                    'возник '
                                                                                                    'какойлибо '
                                                                                                    'вопрос '
                                                                                                    'или '
                                                                                                    'проблема, '
                                                                                                    'пишите '
                                                                                                    'или '
                                                                                                    'звоните '
                                                                                                    'по '
                                                                                                    'следующим '
                                                                                                    'контактам',
                                                                                                    'Пообщим '
                                                                                                    'вопросамтелефон '
                                                                                                    '(843) '
                                                                                                    '2337426, '
                                                                                                    'почтаcroo@kpfuru',
                                                                                                    'НАШИ '
                                                                                                    'СОТРУДНИКИ',
                                                                                                    'Сулейманова '
                                                                                                    'Елена '
                                                                                                    'Александровна',
                                                                                                    'главный '
                                                                                                    'специалист '
                                                                                                    'Центра '
                                                                                                    'развития '
                                                                                                    'онлайнобразованияИнститута '
                                                                                                    'передовых '
                                                                                                    'образовательных '
                                                                                                    'технологий '
                                                                                                    'КФУ',
                                                                                                    'Комната '
                                                                                                    '303, '
                                                                                                    'II '
                                                                                                    'учебнкорпус',
                                                                                                    'Emailes@kpfuru',
                                                                                                    'Телефон '
                                                                                                    '(843) '
                                                                                                    '2337426',
                                                                                                    'Назаров '
                                                                                                    'Алексей '
                                                                                                    'Николаевич',
                                                                                                    'специалист '
                                                                                                    '1 '
                                                                                                    'категории '
                                                                                                    'Центра '
                                                                                                    'развития '
                                                                                                    'онлайнобразованияИнститута '
                                                                                                    'передовых '
                                                                                                    'образовательных '
                                                                                                    'технологий '
                                                                                                    'КФУ',
                                                                                                    'Комната '
                                                                                                    '304, '
                                                                                                    'II '
                                                                                                    'учебнкорпус',
                                                                                                    'Emailnan@kpfuru',
                                                                                                    'Телефон '
                                                                                                    '(843) '
                                                                                                    '2337426',
                                                                                                    'Аухатова '
                                                                                                    'Юлия '
                                                                                                    'Валерьевна',
                                                                                                    'специалист '
                                                                                                    '2 '
                                                                                                    'категории '
                                                                                                    'Центра '
                                                                                                    'развития '
                                                                                                    'онлайнобразованияИнститута '
                                                                                                    'передовых '
                                                                                                    'образовательных '
                                                                                                    'технологий '
                                                                                                    'КФУ',
                                                                                                    'Комната '
                                                                                                    '303, '
                                                                                                    'II '
                                                                                                    'учебнкорпус',
                                                                                                    'Emailay@kpfuru',
                                                                                                    'Телефон '
                                                                                                    '(843) '
                                                                                                    '2337426',
                                                                                                    'По '
                                                                                                    'вопросам '
                                                                                                    'сотрудничества '
                                                                                                    'и '
                                                                                                    'технической '
                                                                                                    'поддержки',
                                                                                                    'Нурутдинов '
                                                                                                    'Султан '
                                                                                                    'Хамитович',
                                                                                                    'Заместитель '
                                                                                                    'руководителя '
                                                                                                    'по '
                                                                                                    'информационным '
                                                                                                    'системамИнженерного '
                                                                                                    'центра '
                                                                                                    'телекоммуникацийи '
                                                                                                    'информационных '
                                                                                                    'систем',
                                                                                                    'Комната '
                                                                                                    '205б, '
                                                                                                    'Здание '
                                                                                                    '17',
                                                                                                    'Emailsultan@kpfuru',
                                                                                                    'Телефон '
                                                                                                    '(843) '
                                                                                                    '2065084 '
                                                                                                    'доб '
                                                                                                    '2216',
                                                                                                    'Халитова '
                                                                                                    'Наталья '
                                                                                                    'Владимировна',
                                                                                                    'Программист '
                                                                                                    '1 '
                                                                                                    'категории '
                                                                                                    'отдела '
                                                                                                    'внедрения '
                                                                                                    'и '
                                                                                                    'сопровождения '
                                                                                                    'информационных '
                                                                                                    'системИнженерного '
                                                                                                    'центра '
                                                                                                    'телекоммуникаций\u200bи '
                                                                                                    'информационных '
                                                                                                    'систем',
                                                                                                    'Комната '
                                                                                                    '209, '
                                                                                                    'Здание '
                                                                                                    '17',
                                                                                                    'EmailNatalyaHalitova@kpfuru',
                                                                                                    'Телефон '
                                                                                                    '(843) '
                                                                                                    '2337330, '
                                                                                                    '2065085']},
            'Институт психологии и образования': {'Кафедра дошкольного образования': [('Твардовская '
                                                                                       'Алла '
                                                                                       'Александровна',
                                                                                       'https://kpfu.ru/Alla.Tvardovskaya'),
                                                                                      ('Габдулхаков '
                                                                                       'Валерьян '
                                                                                       'Фаритович',
                                                                                       'https://kpfu.ru/Valeryan.Gabdulhakov'),
                                                                                      ('Колетвинова '
                                                                                       'Наталья '
                                                                                       'Дмитриевна',
                                                                                       'https://kpfu.ru/Natalya.Koletvinova'),
                                                                                      ('Башинова '
                                                                                       'Светлана '
                                                                                       'Николаевна',
                                                                                       'https://kpfu.ru/Svetlana.Bashinova'),
                                                                                      ('Курбанова '
                                                                                       'Айслу '
                                                                                       'Тагировна',
                                                                                       'https://kpfu.ru/ajslu.kurbanova'),
                                                                                      ('Новик '
                                                                                       'Наталья '
                                                                                       'Николаевна',
                                                                                       'https://kpfu.ru/Natalya.Novik'),
                                                                                      (',',
                                                                                       'https://kpfu.ru/main?p_id=28803&p_lang=&p_type=12'),
                                                                                      ('Бичурина '
                                                                                       'Сеимбика '
                                                                                       'Усмановна',
                                                                                       'https://kpfu.ru/Seimbika.Bichurina'),
                                                                                      ('Салпыкова '
                                                                                       'Индира '
                                                                                       'Маратовна',
                                                                                       'https://kpfu.ru/Indira.Salpykova'),
                                                                                      (',',
                                                                                       'https://kpfu.ru/main?p_id=29375&p_type=14&p_lang='),
                                                                                      ('Веретенникова '
                                                                                       'Вероника '
                                                                                       'Борисовна',
                                                                                       'https://kpfu.ru/veronika.veretennikova'),
                                                                                      ('Гарифуллина '
                                                                                       'Альмира '
                                                                                       'Маратовна',
                                                                                       'https://kpfu.ru/almira.garifullina'),
                                                                                      ('Рафф-Ганачевский '
                                                                                       'Арсений '
                                                                                       'Михайлович',
                                                                                       'https://kpfu.ru/arsenij.raff-ganachevskij'),
                                                                                      ('Лазарева '
                                                                                       'Диана '
                                                                                       'Раисовна',
                                                                                       'https://kpfu.ru/diana.lazareva'),
                                                                                      ('Садретдинова '
                                                                                       'Эльвира '
                                                                                       'Азгамовна',
                                                                                       'https://kpfu.ru/elvira.sadretdinova'),
                                                                                      ('Пименова '
                                                                                       'Ольга '
                                                                                       'Александровна',
                                                                                       'https://kpfu.ru/olga.pimenova')],
                                                  'Кафедра клинической психологии и психологии личности': [
                                                      ('Хакимзянов '
                                                       'Руслан '
                                                       'Наильевич\xa0',
                                                       'http://kpfu.ru/Ruslan.Khakimzyanov'),
                                                      ('Попов '
                                                       'Леонид '
                                                       'Михайлович',
                                                       'http://kpfu.ru/main?p_id=10799'),
                                                      ('Абитов '
                                                       'Ильдар '
                                                       'Равильевич ',
                                                       'https://kpfu.ru/ildar.abitov'),
                                                      ('Валиуллина '
                                                       'Гульнара '
                                                       'Владимировна',
                                                       'https://kpfu.ru/gulnarav.valiullina'),
                                                      ('Фролова '
                                                       'Алла '
                                                       'Владимировна',
                                                       'http://kpfu.ru/Alla.Frolova'),
                                                      ('Степашкина '
                                                       'Валерия '
                                                       'Александровна',
                                                       'http://kpfu.ru/main?p_id=33677'),
                                                      ('Гурьянова '
                                                       'Ольга '
                                                       'Александровна',
                                                       'http://kpfu.ru/Olga.Guryanova'),
                                                      ('Менделевич '
                                                       'Владимир '
                                                       'Давыдович',
                                                       'https://kpfu.ru/Vladimir.Mendelevich'),
                                                      ('Ахметшина '
                                                       'Алина '
                                                       'Гусмановна',
                                                       'https://kpfu.ru/alina.akhmetshina')],
                                                  'Кафедра методологии обучения и воспитания': [('Хузиахметов '
                                                                                                 'Анвар '
                                                                                                 'Нуриахметович',
                                                                                                 'http://kpfu.ru/main?p_id=29275'),
                                                                                                ('Фахрутдинова '
                                                                                                 'Гузалия '
                                                                                                 'Жевдятовна ',
                                                                                                 'http://kpfu.ru/main?p_id=29446'),
                                                                                                ('Габдрахманова '
                                                                                                 'Рашида '
                                                                                                 'Габдельбакиевна ',
                                                                                                 'http://kpfu.ru/Rashida.Gabdrahmanova'),
                                                                                                ('Насибуллов '
                                                                                                 'Рамис '
                                                                                                 'Рафагатович',
                                                                                                 'http://kpfu.ru/main?p_id=28789'),
                                                                                                ('Яруллин '
                                                                                                 'Ильнар '
                                                                                                 'Фагимович',
                                                                                                 'http://kpfu.ru/main?p_id=31214'),
                                                                                                ('Салимзянова '
                                                                                                 'Эльмира '
                                                                                                 'Шавкатовна ',
                                                                                                 'https://kpfu.ru/elmira.salimzyanova'),
                                                                                                ('Яруллина '
                                                                                                 'Резеда '
                                                                                                 'Ильгизаровна ',
                                                                                                 'http://kpfu.ru/main?p_id=32782')],
                                                  'Кафедра начального образования': [('Закирова\xa0'
                                                                                      'Венера '
                                                                                      'Гильмхановна\xa0',
                                                                                      'http://kpfu.ru/main?p_id=28275'),
                                                                                     ('Григорьева '
                                                                                      'Стелла '
                                                                                      'Георгиевна',
                                                                                      'https://kpfu.ru/stella.grigoreva'),
                                                                                     ('Власова '
                                                                                      'Вера '
                                                                                      'Константиновна',
                                                                                      'http://kpfu.ru/main?p_id=28005'),
                                                                                     ('Садовая '
                                                                                      'Виктория '
                                                                                      'Владимировна',
                                                                                      'https://kpfu.ru/Viktoriya.Sadovaya'),
                                                                                     ('Хаирова '
                                                                                      'Ирина '
                                                                                      'Валентиновна',
                                                                                      'http://kpfu.ru/main?p_id=29525'),
                                                                                     ('Камалова '
                                                                                      'Лера '
                                                                                      'Ахтямовна',
                                                                                      'http://kpfu.ru/main?p_id=28446'),
                                                                                     ('Хайрутдинова '
                                                                                      'Резеда '
                                                                                      'Рафаилевна',
                                                                                      'http://kpfu.ru/main?p_id=29134'),
                                                                                     ('Громова '
                                                                                      'Чулпан '
                                                                                      'Раесовна',
                                                                                      'http://kpfu.ru/main?p_id=28226'),
                                                                                     ('Шарай '
                                                                                      'Татьяна '
                                                                                      'Петровна',
                                                                                      'http://kpfu.ru/tatyana.sharaj'),
                                                                                     ('Сабирова '
                                                                                      'Эльвира '
                                                                                      'Гильфановна',
                                                                                      'http://kpfu.ru/main?p_id=28996'),
                                                                                     ('Каюмова '
                                                                                      'Лейсан '
                                                                                      'Рафисовна',
                                                                                      'http://kpfu.ru/main?p_id=31417'),
                                                                                     ('Иванов '
                                                                                      'Динар '
                                                                                      'Валерьевич',
                                                                                      'http://kpfu.ru/dinar.ivanov'),
                                                                                     ('Хафизова '
                                                                                      'Айгуль '
                                                                                      'Айдаровна',
                                                                                      'https://kpfu.ru/ajgul.khafizova'),
                                                                                     ('Соколова '
                                                                                      'Валерия '
                                                                                      'Алексеевна',
                                                                                      'http://kpfu.ru/valeriya.sokolova')],
                                                  'Кафедра общей психологии': [('Прохоров '
                                                                                'Александр '
                                                                                'Октябринович',
                                                                                'http://kpfu.ru/main?p_id=10804'),
                                                                               ('Салихова '
                                                                                'Наиля '
                                                                                'Рустамовна',
                                                                                'http://kpfu.ru/main?p_id=10805'),
                                                                               ('Алишев '
                                                                                'Булат '
                                                                                'Салямович',
                                                                                'http://kpfu.ru/main?p_id=10800'),
                                                                               ('Фахрутдинова '
                                                                                'Лилия '
                                                                                'Раифовна',
                                                                                'http://kpfu.ru/Liliya.Fahrutdinova'),
                                                                               ('Валиуллина '
                                                                                'Марина '
                                                                                'Евгеньевна',
                                                                                'http://kpfu.ru/main?p_id=10801'),
                                                                               ('Афанасьев '
                                                                                'Павел '
                                                                                'Николаевич',
                                                                                'http://kpfu.ru/Pavel.Afanasev'),
                                                                               ('Юсупов '
                                                                                'Марк '
                                                                                'Геннадьевич',
                                                                                'http://kpfu.ru/main?p_id=26227'),
                                                                               ('Чернов '
                                                                                'Альберт '
                                                                                'Валентинович',
                                                                                'http://kpfu.ru/Albert.Chernov'),
                                                                               ('Пучкова '
                                                                                'Ирина '
                                                                                'Михайловна',
                                                                                'https://kpfu.ru/Irina.Puchkova'),
                                                                               ('Устин '
                                                                                'Павел '
                                                                                'Николаевич',
                                                                                'https://kpfu.ru/Pavel.Ustin'),
                                                                               ('Х',
                                                                                'http://kpfu.ru/margarita.antonova'),
                                                                               ('алфиева '
                                                                                'Алиса '
                                                                                'Рамилевна',
                                                                                'http://kpfu.ru/alisa.halfieva'),
                                                                               ('Мельников '
                                                                                'Андрей '
                                                                                'Владимирович',
                                                                                'http://kpfu.ru/andrej.melnikov'),
                                                                               ('Решетникова '
                                                                                'Ирина '
                                                                                'Сергеевна',
                                                                                'https://kpfu.ru/irinas.reshetnikova')],
                                                  'Кафедра педагогики': [('Валеева Роза '
                                                                          'Алексеевна',
                                                                          'http://kpfu.ru/Roza.Valeeva'),
                                                                         ('Добротворская '
                                                                          'Светлана '
                                                                          'Георгиевна',
                                                                          'http://kpfu.ru/main?p_id=10822'),
                                                                         ('Биктагирова '
                                                                          'Гульнара '
                                                                          'Фердинандовна',
                                                                          'http://kpfu.ru/main?p_id=27835'),
                                                                         ('Дроздикова-Зарипова '
                                                                          'Альбина '
                                                                          'Рафаиловна\xa0',
                                                                          'http://kpfu.ru/Albina.Drozdikova-Zaripova'),
                                                                         ('Калацкая '
                                                                          'Наталья '
                                                                          'Николаевна\xa0',
                                                                          'http://kpfu.ru/Natalya.Kalackaya'),
                                                                         ('Костюнина '
                                                                          'Надежда '
                                                                          'Юрьевна\xa0',
                                                                          'http://kpfu.ru/Nadezhda.Kostjunina'),
                                                                         ('Парфилова '
                                                                          'Гульфия '
                                                                          'Габдрахмановна\xa0',
                                                                          'http://kpfu.ru/main?p_id=28865'),
                                                                         ('Рыбакова '
                                                                          'Ляйсан '
                                                                          'Анатольевна\xa0',
                                                                          'http://kpfu.ru/main?p_id=28993'),
                                                                         ('Каримова Лилия '
                                                                          'Шамильевна\xa0',
                                                                          'http://kpfu.ru/3Liliya.Karimova'),
                                                                         ('Касимова '
                                                                          'Рамиля '
                                                                          'Шамилевна\xa0',
                                                                          'http://kpfu.ru/Ramilya.Kasimova'),
                                                                         ('Оренбурова '
                                                                          'Лиана '
                                                                          'Владимировна',
                                                                          'https://kpfu.ru/liana.orenburova')],
                                                  'Кафедра педагогики высшей школы': [('Масалимова '
                                                                                       'Альфия '
                                                                                       'Рафисовна',
                                                                                       'https://kpfu.ru/alfiya.masalimova'),
                                                                                      ('Калимуллин '
                                                                                       'Айдар '
                                                                                       'Минимансурович',
                                                                                       'http://kpfu.ru/main?p_id=27653'),
                                                                                      ('Ибрагимов '
                                                                                       'Гасан-Гусейн '
                                                                                       'Ибрагимович',
                                                                                       'http://kpfu.ru/Gasangusejn.Ibragimov'),
                                                                                      ('Кирилова '
                                                                                       'Галия '
                                                                                       'Ильдусовна',
                                                                                       'http://kpfu.ru/Galiya.Kirilova'),
                                                                                      ('Шайхелисламов '
                                                                                       'Раис '
                                                                                       'Фалихович',
                                                                                       'https://kpfu.ru/Rais.Shajhelislamov'),
                                                                                      ('Голованова '
                                                                                       'Инна '
                                                                                       'Игоревна',
                                                                                       'http://kpfu.ru/main?p_id=20711'),
                                                                                      ('Сахиева '
                                                                                       'Регина '
                                                                                       'Геннадьевна',
                                                                                       'http://kpfu.ru/regina.sahieva'),
                                                                                      ('Асафова '
                                                                                       'Елена '
                                                                                       'Владимировна',
                                                                                       'http://kpfu.ru/main?p_id=10809'),
                                                                                      ('Чиркина '
                                                                                       'Светлана '
                                                                                       'Евгеньевна ',
                                                                                       'http://kpfu.ru/Svetlana.Chirkina'),
                                                                                      ('Баклашова '
                                                                                       'Татьяна '
                                                                                       'Александровна',
                                                                                       'http://kpfu.ru/main?p_id=25132'),
                                                                                      ('Гайнутдинова '
                                                                                       'Татьяна '
                                                                                       'Юрьевна',
                                                                                       'https://kpfu.ru/Tatyana.Gajnutdinova'),
                                                                                      ('Кривоножкина '
                                                                                       'Екатерина '
                                                                                       'Геннадьевна',
                                                                                       'http://kpfu.ru/main?p_id=25187'),
                                                                                      ('Телегина '
                                                                                       'Надежда '
                                                                                       'Викторовна',
                                                                                       'http://kpfu.ru/main?p_id=10815'),
                                                                                      ('Вашетина '
                                                                                       'Оксана '
                                                                                       'Викторовна',
                                                                                       'http://kpfu.ru/oksana.vashetina'),
                                                                                      ('Галимова '
                                                                                       'Эльвира '
                                                                                       'Габдельбаровна',
                                                                                       'http://kpfu.ru/Elvira.Galimova'),
                                                                                      ('Маслова '
                                                                                       'Елена '
                                                                                       'Сергеевна',
                                                                                       'http://kpfu.ru/Elena.Grigoreva'),
                                                                                      ('Грунис '
                                                                                       'Максим '
                                                                                       'Леонидович',
                                                                                       'https://kpfu.ru/maksim.grunis'),
                                                                                      ('Павлов '
                                                                                       'Дмитрий '
                                                                                       'Николаевич',
                                                                                       'https://kpfu.ru/dmitrij.pavlov'),
                                                                                      ('Сибгатуллин '
                                                                                       'Искандер '
                                                                                       'Рамилевич',
                                                                                       'https://kpfu.ru/iskander.sibgatullin'),
                                                                                      ('Аракчеева '
                                                                                       'Ольга '
                                                                                       'Евгеньевна',
                                                                                       'https://kpfu.ru/olga.arakcheeva'),
                                                                                      ('Тухватуллина '
                                                                                       'Лейсан '
                                                                                       'Рустемовна',
                                                                                       'https://kpfu.ru/lejsan.tukhvatullina')],
                                                  'Кафедра педагогической психологии': [('Баянова '
                                                                                         'Лариса '
                                                                                         'Фаритовна',
                                                                                         'http://kpfu.ru/larisa.bayanova'),
                                                                                        ('Гарифуллин '
                                                                                         'Рамиль '
                                                                                         'Рамзиевич',
                                                                                         'https://kpfu.ru/ramil.garifullin'),
                                                                                        ('Хусаинова '
                                                                                         'Резеда '
                                                                                         'Мунировна',
                                                                                         'http://kpfu.ru/Rezeda.Husainova'),
                                                                                        ('Шишова '
                                                                                         'Евгения '
                                                                                         'Олеговна',
                                                                                         'http://kpfu.ru/main?p_id=29180'),
                                                                                        ('Муртазина '
                                                                                         'Эльмира '
                                                                                         'Ильдусовна',
                                                                                         'http://kpfu.ru/Elmira.Sahapova'),
                                                                                        ('Лопухова '
                                                                                         'Ольга '
                                                                                         'Геннадьевна',
                                                                                         'http://kpfu.ru/main?p_id=28602'),
                                                                                        ('Солобутина '
                                                                                         'Марина '
                                                                                         'Михайловна',
                                                                                         'http://kpfu.ru/main?p_id=28938'),
                                                                                        ('Федоренко '
                                                                                         'Марина '
                                                                                         'Владимировна',
                                                                                         'http://kpfu.ru/Marina.Fedorenko'),
                                                                                        ('Волчков '
                                                                                         'Эдуард '
                                                                                         'Григорьевич',
                                                                                         'http://kpfu.ru/Eduard.Volchkov'),
                                                                                        ('Гилемханова '
                                                                                         'Эльвира '
                                                                                         'Нурахматовна',
                                                                                         'http://kpfu.ru/elvira.gilemhanova'),
                                                                                        ('Шакирова '
                                                                                         'Гульшат '
                                                                                         'Фиразовна',
                                                                                         'http://kpfu.ru/main?p_id=29517'),
                                                                                        ('Хусаинова '
                                                                                         'Светлана '
                                                                                         'Владимировна',
                                                                                         'https://kpfu.ru/svetlana.khusainova'),
                                                                                        ('Попова '
                                                                                         'Резеда '
                                                                                         'Равилевна',
                                                                                         'http://kpfu.ru/rezeda.popova'),
                                                                                        ('Хаматвалеева '
                                                                                         'Динара '
                                                                                         'Гумаровна ',
                                                                                         'https://kpfu.ru/dinara.khamatvaleeva'),
                                                                                        ('Рязанова '
                                                                                         'Анастасия '
                                                                                         'Алексеевна ',
                                                                                         'https://kpfu.ru/anastasiya.ryazanova'),
                                                                                        ('Дуканова '
                                                                                         'Гульнара '
                                                                                         'Маратовна',
                                                                                         'http://kpfu.ru/gulnara.dukanova')],
                                                  'Кафедра психологии и педагогики специального образования': [
                                                      ('Ахметзянова '
                                                       'Анна '
                                                       'Ивановна',
                                                       'http://kpfu.ru/Anna.Ahmetzyanova'),
                                                      ('Артемьева '
                                                       'Татьяна '
                                                       'Васильевна',
                                                       'http://kpfu.ru/main?p_id=27750'),
                                                      ('Артищева '
                                                       'Лира '
                                                       'Владимировна',
                                                       'http://kpfu.ru/Lira.Artischeva'),
                                                      ('Васина '
                                                       'Вероника '
                                                       'Викторовна',
                                                       'https://kpfu.ru/veronika.vasina'),
                                                      ('Корнийченко '
                                                       'Татья',
                                                       'https://kpfu.ru/Tatyana.Kornijchenko'),
                                                      ('на '
                                                       'Юрьевна',
                                                       'https://kpfu.ru/Tatyana.Kornijchenko'),
                                                      ('Кротова '
                                                       'Инна '
                                                       'Владимировна',
                                                       'http://kpfu.ru/Inna.Balymova'),
                                                      ('Минуллина '
                                                       'Аида '
                                                       'Фаридовна',
                                                       'https://kpfu.ru/Aida.Minullina'),
                                                      ('Нигматуллина '
                                                       'Ирина '
                                                       'Александровна',
                                                       'http://kpfu.ru/main?p_id=28742'),
                                                      ('Болтакова '
                                                       'Наталья '
                                                       'Ивановна',
                                                       'https://kpfu.ru/1Natalya.Boltakova'),
                                                      ('Дадакина '
                                                       'Виктория '
                                                       'Юрьевна',
                                                       'https://kpfu.ru/viktoriya.dadakina'),
                                                      ('Кириллова '
                                                       'Екатерина '
                                                       'Александровна',
                                                       'https://kpfu.ru/ekaterina.kirillova'),
                                                      ('Охотникова '
                                                       'Валерия '
                                                       'Олеговна ',
                                                       'https://kpfu.ru/valeriya.okhotnikova'),
                                                      ('Халтурина '
                                                       'Елизавета '
                                                       'Романовна',
                                                       'https://kpfu.ru/elizaveta.halturina'),
                                                      ('Насретдинова '
                                                       'Ирина '
                                                       'Фарисовна',
                                                       'https://kpfu.ru/irina.nasretdinova')]},
            'Институт физики': {'Кафедра астрономии и космической геодезии': [('Безменов '
                                                                               'Владимир '
                                                                               'Михайлович',
                                                                               'https://kpfu.ru/Vladimir.Bezmenov'),
                                                                              ('Сахибуллин '
                                                                               'Наиль '
                                                                               'Абдуллович',
                                                                               'https://kpfu.ru/Nail.Sakhibullin'),
                                                                              ('Жучков '
                                                                               'Роман '
                                                                               'Яковлевич',
                                                                               'https://kpfu.ru/Roman.Zhuchkov'),
                                                                              ('Загретдинов '
                                                                               'Ренат '
                                                                               'Вагизович',
                                                                               'https://kpfu.ru/Renat.Zagretdinov'),
                                                                              ('Соколова '
                                                                               'Марина '
                                                                               'Геннадьевна',
                                                                               'https://kpfu.ru/Marina.Sokolova'),
                                                                              ('Шиманская '
                                                                               'Нелли '
                                                                               'Николаевна',
                                                                               'https://kpfu.ru/Nelli.Shimanskaya'),
                                                                              ('Шиманский '
                                                                               'Владислав '
                                                                               'Владимирович',
                                                                               'https://kpfu.ru/Slava.Shimansky'),
                                                                              ('Шпекин '
                                                                               'Михаил '
                                                                               'Иванович',
                                                                               'https://kpfu.ru/Michael.Shpekin'),
                                                                              ('Новлянская '
                                                                               'Инна '
                                                                               'Олеговна',
                                                                               'https://kpfu.ru/inna.novlyanskaya'),
                                                                              ('Сапронов '
                                                                               'Алексей '
                                                                               'Евгеньевич',
                                                                               'https://kpfu.ru/Aleksej.Sapronov'),
                                                                              ('Бикмаев '
                                                                               'Ильфан '
                                                                               'Фяритович',
                                                                               'https://kpfu.ru/Ilfan.Bikmaev'),
                                                                              ('Чезганова '
                                                                               'Светлана '
                                                                               'Геннадьевна',
                                                                               'https://kpfu.ru/svetlana.chezganova'),
                                                                              ('Белов '
                                                                               'Игорь '
                                                                               'Юрьевич',
                                                                               'https://kpfu.ru/Igor.Belov'),
                                                                              ('Колбин '
                                                                               'Александр '
                                                                               'Иванович',
                                                                               'https://kpfu.ru/aleksandr.kolbin'),
                                                                              ('Усанин '
                                                                               'Владимир '
                                                                               'Сергеевич',
                                                                               'https://kpfu.ru/Vladimir.Usanin'),
                                                                              ('Загидуллин '
                                                                               'Артур '
                                                                               'Александрович',
                                                                               'https://kpfu.ru/artur.zagidullin'),
                                                                              ('Комаров '
                                                                               'Руслан '
                                                                               'Викторович',
                                                                               'https://kpfu.ru/Ruslan.Komarov'),
                                                                              ('Николаева '
                                                                               'Евгения '
                                                                               'Александровна',
                                                                               'https://kpfu.ru/evgeniyaa.nikolaeva'),
                                                                              ('Мезрина '
                                                                               'Наталия '
                                                                               'Владимировна',
                                                                               'https://kpfu.ru/Natalia.Mezrina'),
                                                                              ('Королева '
                                                                               'Татьяна '
                                                                               'Леонидовна',
                                                                               'https://kpfu.ru/Tatyana.Koroleva'),
                                                                              ('Склянов '
                                                                               'Александр '
                                                                               'Сергеевич',
                                                                               'https://kpfu.ru/Aleksandr.Sklyanov'),
                                                                              ('Тутышкина '
                                                                               'Зоя '
                                                                               'Константиновна',
                                                                               'https://kpfu.ru/Zoja.Tutyshkina'),
                                                                              ('Пронина '
                                                                               'Валентина '
                                                                               'Дмитриевна',
                                                                               'https://kpfu.ru/valentina.pronina')],
                                'Кафедра вычислительной физики': [('Мокшин Анатолий '
                                                                   'Васильевич',
                                                                   'http://kpfu.ru/Anatolii.Mokshin'),
                                                                  ('Нефедьев Юрий '
                                                                   'Анатольевич',
                                                                   'http://kpfu.ru/Yuriy.Nefedev'),
                                                                  ('Хуснутдинов Рамиль '
                                                                   'Миннегаязович',
                                                                   'http://kpfu.ru/Ramil.Husnutdinov'),
                                                                  ('Галимзянов Булат '
                                                                   'Наилевич',
                                                                   'http://kpfu.ru/Bulat.Galimzyanov'),
                                                                  ('Демин Сергей '
                                                                   'Анатольевич',
                                                                   'http://kpfu.ru/Sergej.Djomin'),
                                                                  ('Файрушин Ильназ '
                                                                   'Изаилович',
                                                                   'https://kpfu.ru/ilnaz.fajrushin'),
                                                                  ('Вильф Яков Зиновьевич',
                                                                   'https://kpfu.ru/yakov.vilf'),
                                                                  ('Андреев Алексей '
                                                                   'Олегович',
                                                                   'http://kpfu.ru/aleksej.andreev'),
                                                                  ('Загидуллин\xa0'
                                                                   'Артур\xa0'
                                                                   'Александрович',
                                                                   'https://kpfu.ru/artur.zagidullin'),
                                                                  ('Ахматнабиева Лейла '
                                                                   'Булатовна',
                                                                   'https://kpfu.ru/lejla.akhmatnabieva'),
                                                                  ('Фархутдинов Альберт '
                                                                   'Ришатович',
                                                                   'https://kpfu.ru/pg/AlbRFarhutdinov'),
                                                                  ('Злищева Полина '
                                                                   'Андреевна',
                                                                   'https://kpfu.ru/pg/PoAZlischeva'),
                                                                  ('Куташова Екатерина '
                                                                   'Михайловна',
                                                                   'https://kpfu.ru/pg/EkMKutashova'),
                                                                  ('Ананьев Иван '
                                                                   'Федорович',
                                                                   'https://kpfu.ru/pg/IvFAnanev'),
                                                                  ('Яруллин Динар '
                                                                   'Тимурович',
                                                                   'https://kpfu.ru/student/DiTYarullin'),
                                                                  ('Хабибуллин Роман '
                                                                   'Альбертович',
                                                                   'https://kpfu.ru/roman.khabibullin'),
                                                                  ('Хайруллина Рания '
                                                                   'Рустамовна',
                                                                   'https://kpfu.ru/raniya.khajrullina'),
                                                                  ('Мирзиярова Диана '
                                                                   'Альбертовна',
                                                                   'https://kpfu.ru/Diana.mirziyarova')],
                                'Кафедра квантовой электроники и радиоспектроскопии': [('Абишев '
                                                                                        'Нурбулат ',
                                                                                        'https://kpfu.ru/nurbulat.abishev'),
                                                                                       ('Аглямов '
                                                                                        'Радик '
                                                                                        'Дависович',
                                                                                        'https://kpfu.ru/radik.aglyamov'),
                                                                                       ('Алакшин '
                                                                                        'Егор '
                                                                                        'Михайлович',
                                                                                        'https://kpfu.ru/Egor.Alakshin'),
                                                                                       ('Александров '
                                                                                        'Артем '
                                                                                        'Сергеевич',
                                                                                        'https://kpfu.ru/Artem.Aleksandrov'),
                                                                                       ('Андреев '
                                                                                        'Георгий '
                                                                                        'Юрьевич',
                                                                                        'https://kpfu.ru/georgiy.andreev'),
                                                                                       ('Батулин '
                                                                                        'Руслан '
                                                                                        'Германович',
                                                                                        'https://kpfu.ru/ruslan.batulin'),
                                                                                       ('Богайчук '
                                                                                        'Александр '
                                                                                        'Вячеславович',
                                                                                        'https://kpfu.ru/aleksandr.bogajchuk'),
                                                                                       ('Володина '
                                                                                        'Ирина '
                                                                                        'Павловна',
                                                                                        'https://kpfu.ru/Irina.Volodina'),
                                                                                       ('Гафуров '
                                                                                        'Марат '
                                                                                        'Ревгерович',
                                                                                        'https://kpfu.ru/Marat.Gafurov'),
                                                                                       ('Гнездилов '
                                                                                        'Олег '
                                                                                        'Иванович',
                                                                                        'https://kpfu.ru/oleg.gnezdilov'),
                                                                                       ('Грачева '
                                                                                        'Ирина '
                                                                                        'Николаевна',
                                                                                        'https://kpfu.ru/Irina.Gracheva'),
                                                                                       ('Долгоруков '
                                                                                        'Глеб '
                                                                                        'Александрович',
                                                                                        'https://kpfu.ru/gleb.dolgorukov'),
                                                                                       ('Дуглав '
                                                                                        'Александр '
                                                                                        'Васильевич',
                                                                                        'https://kpfu.ru/Alexander.Dooglav'),
                                                                                       ('Еремин '
                                                                                        'Михаил '
                                                                                        'Васильевич',
                                                                                        'https://kpfu.ru/Mikhail.Eremin'),
                                                                                       ('Ефимов '
                                                                                        'Сергей '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/Sergej.Efimov'),
                                                                                       ('Зверев '
                                                                                        'Дмитрий '
                                                                                        'Германович',
                                                                                        'https://kpfu.ru/1Dmitry.Zverev'),
                                                                                       ('Зиннатуллин '
                                                                                        'Алмаз '
                                                                                        'Линарович',
                                                                                        'https://kpfu.ru/almaz.zinnatullin'),
                                                                                       ('Кан '
                                                                                        'Денис ',
                                                                                        'https://kpfu.ru/denis.kan'),
                                                                                       ('Каратаева '
                                                                                        'Фарида '
                                                                                        'Хайдаровна',
                                                                                        'https://kpfu.ru/Farida.Karataeva'),
                                                                                       ('Клековкина '
                                                                                        'Вера '
                                                                                        'Вадимовна',
                                                                                        'https://kpfu.ru/Vera.Klekovkina'),
                                                                                       ('Клочков '
                                                                                        'Александр '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/Alexander.Klochkov'),
                                                                                       ('Кобчикова '
                                                                                        'Полина '
                                                                                        'Павловна',
                                                                                        'https://kpfu.ru/polina.kobchikova'),
                                                                                       ('Кондратьева '
                                                                                        'Екатерина '
                                                                                        'Ивановна',
                                                                                        'https://kpfu.ru/ekaterinai.kondrateva'),
                                                                                       ('Конькин '
                                                                                        'Алексей '
                                                                                        'Александрович',
                                                                                        'https://kpfu.ru/aleksej.konkin'),
                                                                                       ('Кузьмин '
                                                                                        'Вячеслав '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/Vjacheslav.Kuzmin'),
                                                                                       ('Лукинова '
                                                                                        'Елена ',
                                                                                        'https://kpfu.ru/elena.lukinova'),
                                                                                       ('Мадиров '
                                                                                        'Эдуард '
                                                                                        'Ильдарович',
                                                                                        'https://kpfu.ru/eduard.madirov'),
                                                                                       ('Макарченко '
                                                                                        'Александр '
                                                                                        'Сергеевич',
                                                                                        'https://kpfu.ru/aleksandr.makarchenko'),
                                                                                       ('Малкин '
                                                                                        'Борис '
                                                                                        'Залманович',
                                                                                        'https://kpfu.ru/Boris.Malkin'),
                                                                                       ('Мамин '
                                                                                        'Георгий '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/George.Mamin'),
                                                                                       ('Марисов '
                                                                                        'Михаил '
                                                                                        'Александрович',
                                                                                        'https://kpfu.ru/Mikhail.Marisov'),
                                                                                       ('Мотыгуллин '
                                                                                        'Ильдар '
                                                                                        'Гусманович',
                                                                                        'https://kpfu.ru/Ildar.Motygullin'),
                                                                                       ('Мумджи '
                                                                                        'Иван '
                                                                                        'Энверович',
                                                                                        'https://kpfu.ru/ivan.mumdzhi'),
                                                                                       ('Мурзаханов '
                                                                                        'Фадис '
                                                                                        'Фанилович',
                                                                                        'https://kpfu.ru/fadis.murzahanov'),
                                                                                       ('Низамутдинов '
                                                                                        'Алексей '
                                                                                        'Сергеевич',
                                                                                        'https://kpfu.ru/Alexey.Nizamutdinov'),
                                                                                       ('Орлинский '
                                                                                        'Сергей '
                                                                                        'Борисович',
                                                                                        'https://kpfu.ru/Sergei.Orlinskii'),
                                                                                       ('Парфишина '
                                                                                        'Арина '
                                                                                        'Сергеевна',
                                                                                        'https://kpfu.ru/arina.parfishina'),
                                                                                       ('Пудовкин '
                                                                                        'Максим '
                                                                                        'Сергеевич',
                                                                                        'https://kpfu.ru/maksim.pudovkin'),
                                                                                       ('Рахматуллин '
                                                                                        'Рафаиль '
                                                                                        'Мансурович',
                                                                                        'https://kpfu.ru/Rafail.Rakhmatullin'),
                                                                                       ('Родионов '
                                                                                        'Александр '
                                                                                        'Александрович',
                                                                                        'https://kpfu.ru/Alexander.Rodionov'),
                                                                                       ('Романова '
                                                                                        'Ирина '
                                                                                        'Владимировна',
                                                                                        'https://kpfu.ru/Irina.Romanova'),
                                                                                       ('Сайфуллин '
                                                                                        'Эмиль '
                                                                                        'Ринатович',
                                                                                        'https://kpfu.ru/emil.sajfullin'),
                                                                                       ('Сафиуллин '
                                                                                        'Каюм '
                                                                                        'Рафаилевич',
                                                                                        'https://kpfu.ru/Kajum.Safiullin'),
                                                                                       ('Семашко '
                                                                                        'Вадим '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/Vadim.Semashko'),
                                                                                       ('Солтамов '
                                                                                        'Виктор '
                                                                                        'Андреевич',
                                                                                        'https://kpfu.ru/viktor.soltamov'),
                                                                                       ('Станиславовас '
                                                                                        'Андрей '
                                                                                        'Андреевич',
                                                                                        'https://kpfu.ru/andrej.stanislavovas'),
                                                                                       ('Тагиров '
                                                                                        'Мурат '
                                                                                        'Салихович',
                                                                                        'https://kpfu.ru/Murat.Tagirov'),
                                                                                       ('Филиппов '
                                                                                        'Андрей '
                                                                                        'Васильевич',
                                                                                        'https://kpfu.ru/Andrey.Filippov'),
                                                                                       ('Хадиев '
                                                                                        'Амир '
                                                                                        'Рамилевич',
                                                                                        'https://kpfu.ru/amir.hadiev'),
                                                                                       ('Харахашьян '
                                                                                        'Георгий '
                                                                                        'Эдуардович',
                                                                                        'https://kpfu.ru/georgij.kharakhashyan'),
                                                                                       ('Черосов '
                                                                                        'Михаил '
                                                                                        'Андреевич',
                                                                                        'https://kpfu.ru/mikhail.cherosov'),
                                                                                       ('Шавельев '
                                                                                        'Алексей '
                                                                                        'Андреевич',
                                                                                        'https://kpfu.ru/aleksej.shavelev'),
                                                                                       ('Шуртакова '
                                                                                        'Дарья '
                                                                                        'Владимировна',
                                                                                        'https://kpfu.ru/darya.shurtakova'),
                                                                                       ('Юсупов '
                                                                                        'Роман '
                                                                                        'Валерьевич',
                                                                                        'https://kpfu.ru/Roman.Yusupov'),
                                                                                       ('Явкин '
                                                                                        'Борис '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/Boris.Yavkin')],
                                'Кафедра киберфизических технологий': [('Чикрин Дмитрий '
                                                                        'Евгеньевич',
                                                                        'https://kpfu.ru/dmitrij.chikrin'),
                                                                       ('Калабанов Сергей '
                                                                        'Александрович',
                                                                        'https://kpfu.ru/Sergei.Kalabanov')],
                                'Кафедра медицинской физики': [('Аганов Альберт '
                                                                'Вартанович',
                                                                'https://kpfu.ru/Albert.Aganov'),
                                                               ('Челышев Юрий '
                                                                'Александрович',
                                                                'https://kpfu.ru/jurij.chelyshev'),
                                                               ('Ильясов Камиль Ахатович',
                                                                'https://kpfu.ru/Kamil.Ilyasov'),
                                                               ('Котов Николай Викторович',
                                                                'https://kpfu.ru/Nicolaj.Kotov'),
                                                               ('Клочков Владимир '
                                                                'Васильевич',
                                                                'https://kpfu.ru/Vladimir.Klochkov'),
                                                               ('Рыжкин  Сергей '
                                                                'Александрович',
                                                                'https://kpfu.ru/sergej.ryzhkin'),
                                                               ('Гафуров Марат Ревгерович',
                                                                'https://kpfu.ru/Marat.Gafurov'),
                                                               ('Туранов Александр '
                                                                'Николаевич',
                                                                'https://kpfu.ru/aleksandr.turanov'),
                                                               ('Усачев Константин '
                                                                'Сергеевич',
                                                                'https://kpfu.ru/Konstantin.Usachev'),
                                                               ('Хайрутдинов Булат '
                                                                'Имамутдинович',
                                                                'https://kpfu.ru/Boulat.Khairoutdinov'),
                                                               ('Халиуллина Алия '
                                                                'Владимировна',
                                                                'https://kpfu.ru/aliya.haliullina'),
                                                               ('Блохин Дмитрий Сергеевич',
                                                                'https://kpfu.ru/Dmitrij.Blohin'),
                                                               ('Ефимов Сергей '
                                                                'Владимирович',
                                                                'https://kpfu.ru/Sergej.Efimov'),
                                                               ('Рахматуллин Ильфат '
                                                                'Зуфарович',
                                                                'https://kpfu.ru/ilfat.rahmatullin'),
                                                               ('Ходов Илья Анатольевич',
                                                                'https://kpfu.ru/ilya.hodov'),
                                                               ('Клочкова Эвелина '
                                                                'Андреевна',
                                                                'https://kpfu.ru/evelina.klochkova'),
                                                               ('Аганова Оксана '
                                                                'Вартановна',
                                                                'https://kpfu.ru/oksana.aganova'),
                                                               ('Гориева Виктория '
                                                                'Геннадьевна',
                                                                'https://kpfu.ru/viktoriya.gorieva'),
                                                               ('Валитова Айгуль '
                                                                'Фаниловна',
                                                                'https://kpfu.ru/ajgul.valitova'),
                                                               ('Гоенко Илья '
                                                                'Александрович',
                                                                'https://kpfu.ru/ilya.goenko'),
                                                               ('Кондратьева Екатерина '
                                                                'Ивановна',
                                                                'https://kpfu.ru/ekaterinai.kondrateva'),
                                                               ('Петрова Алина Артуровна',
                                                                'https://kpfu.ru/alina.mamatova'),
                                                               ('Русанова Инна '
                                                                'Александровна',
                                                                'https://kpfu.ru/inna.rusanova'),
                                                               ('Сучков Дмитрий Сергеевич',
                                                                'https://kpfu.ru/dmitrij.suchkov'),
                                                               ('Шуртакова Дарья '
                                                                'Владимировна',
                                                                'https://kpfu.ru/darya.shurtakova'),
                                                               ('Бикмуллин Айдар '
                                                                'Галимзанович',
                                                                'https://kpfu.ru/ajdar.bikmullin'),
                                                               ('Згадзай Юрий Олегович',
                                                                'https://kpfu.ru/jurij.zgadzaj'),
                                                               ('Кусова Александра '
                                                                'Михайловна',
                                                                'https://kpfu.ru/aleksandra.kusova'),
                                                               ('Шуршалова Гузель '
                                                                'Салаватовна',
                                                                'https://kpfu.ru/guzel.musabirova'),
                                                               ('Галиуллина Нурия '
                                                                'Файзрахмановна',
                                                                'https://kpfu.ru/Nurija.Galiullina'),
                                                               ('Малинина Юлия '
                                                                'Вячеславовна',
                                                                'https://kpfu.ru/Julia.Malinina'),
                                                               ('Юльметов Айдар '
                                                                'Рафаилевич',
                                                                'https://kpfu.ru/Ajdar.Julmetov'),
                                                               ('Липачев Никита Сергеевич',
                                                                'https://kpfu.ru/nikita.lipachev'),
                                                               ('Биктимиров Артём '
                                                                'Дмитриевич',
                                                                'https://kpfu.ru/artyom.biktimirov'),
                                                               ('Кобчикова Полина '
                                                                'Павловна',
                                                                'https://kpfu.ru/polina.kobchikova'),
                                                               ('Санчугова Дарья '
                                                                'Андреевна',
                                                                'https://kpfu.ru/darya.sanchugova'),
                                                               ('Тарасов Артем Сергеевич',
                                                                'https://kpfu.ru/artems.tarasov'),
                                                               ('Тимерова Айзира Флюсовна',
                                                                'https://kpfu.ru/ajzira.timerova')],
                                'Кафедра образовательных технологий в физике': [('Нефедьев '
                                                                                 'Леонид '
                                                                                 'Анатольевич',
                                                                                 'http://kpfu.ru/leonid.nefedev'),
                                                                                ('Гарнаева '
                                                                                 'Гузель '
                                                                                 'Ильдаровна',
                                                                                 'http://kpfu.ru/guzel.garnaeva'),
                                                                                ('Мингазов '
                                                                                 'Рамиль '
                                                                                 'Хаернасович',
                                                                                 'http://kpfu.ru/ramil.mingazov'),
                                                                                ('Низамова '
                                                                                 'Эльмира '
                                                                                 'Ильгамовна',
                                                                                 'http://kpfu.ru/elmira.nizamova'),
                                                                                ('Шигапова '
                                                                                 'Эльвера '
                                                                                 'Дамировна',
                                                                                 'http://kpfu.ru/elvera.shigapova'),
                                                                                ('Ахмедшина '
                                                                                 'Екатерина '
                                                                                 'Николаевна',
                                                                                 'http://kpfu.ru/ekaterina.ahmedshina'),
                                                                                ('Фадеева '
                                                                                 'Елена '
                                                                                 'Юрьевна',
                                                                                 'http://kpfu.ru/elena.fadeeva'),
                                                                                ('Спиридонов '
                                                                                 'Анатолий '
                                                                                 'Владимирович',
                                                                                 'http://kpfu.ru/anatolij.spiridonov')],
                                'Кафедра общей физики': [('Таюрский Дмитрий Альбертович',
                                                          'https://kpfu.ru/Dmitry.Tayurskii'),
                                                         ('Мингазов Рамиль Хаернасович',
                                                          'https://kpfu.ru/ramil.mingazov'),
                                                         ('Нефедьев Леонид Анатольевич',
                                                          'https://kpfu.ru/leonid.nefedev'),
                                                         ('Фишман Александр Израилович',
                                                          'https://kpfu.ru/Alexander.Fishman'),
                                                         ('Еремина Рушана Михайловна',
                                                          'https://kpfu.ru/rushana.eremina'),
                                                         ('Гарнаева Гузель Ильдаровна',
                                                          'https://kpfu.ru/Guzel.Garnaeva'),
                                                         ('Даминов Рустам Валиевич',
                                                          'https://kpfu.ru/Rustam.Daminov'),
                                                         ('Захаров Юрий Анатольевич',
                                                          'https://kpfu.ru/Yuri.Zakharov'),
                                                         ('Мутыгуллина Айгуль '
                                                          'Ахмадулловна',
                                                          'https://kpfu.ru/Aigul.Mutygullina'),
                                                         ('Налетов Владимир Вениаминович',
                                                          'https://kpfu.ru/Vladimir.Naletov'),
                                                         ('Скворцов Андрей Иванович',
                                                          'https://kpfu.ru/Andrei.Skvortzov'),
                                                         ('Усеинов Ниазбек Хамзович',
                                                          'https://kpfu.ru/Niazbeck.Useinov'),
                                                         ('Батулин Руслан Германович',
                                                          'https://kpfu.ru/ruslan.batulin'),
                                                         ('Волошин Александр Викторович',
                                                          'https://kpfu.ru/Alexandr.Voloshin'),
                                                         ('Грачева Ирина Николаевна',
                                                          'https://kpfu.ru/Irina.Gracheva'),
                                                         ('Киямов Айрат Газинурович',
                                                          'https://kpfu.ru/Ajrat.Kiyamov'),
                                                         ('Недопекин Олег Владимирович',
                                                          'https://kpfu.ru/Oleg.Nedopekin'),
                                                         ('Романова Ирина Владимировна',
                                                          'https://kpfu.ru/Irina.Romanova'),
                                                         ('Фазлижанов Ильшат '
                                                          'Имаметдинович',
                                                          'https://kpfu.ru/ilshat.fazlizhanov'),
                                                         ('Яцык Иван Владимирович',
                                                          'https://kpfu.ru/ivan.yacyk'),
                                                         ('Монахова Наталья Ивановна',
                                                          'https://kpfu.ru/Natalia.Monakhova'),
                                                         ('Салихова Олеся Борисовна',
                                                          'https://kpfu.ru/Olesia.Kokorina'),
                                                         ('Филиппова Елена Алексеевна',
                                                          'https://kpfu.ru/Elena.Filippova'),
                                                         ('Низамова Эльмира Ильгамовна',
                                                          'https://kpfu.ru/elmira.nizamova'),
                                                         ('Русанова Инна Александровна',
                                                          'https://kpfu.ru/inna.rusanova'),
                                                         ('Хакимзянова Эльза Ильдаровна',
                                                          'https://kpfu.ru/elza.hakimzyanova'),
                                                         ('Шигапова Эльвера Дамировна',
                                                          'https://kpfu.ru/elvera.shigapova'),
                                                         ('Ахмедшина Екатерина Николаевна',
                                                          'https://kpfu.ru/ekaterina.ahmedshina'),
                                                         ('Харитонов Антон Викторович',
                                                          'https://kpfu.ru/antonv.haritonov'),
                                                         ('Ирисов Денис Сергеевич',
                                                          'https://kpfu.ru/Denis.Irisov'),
                                                         ('Сукоркина Алина Валерьевна',
                                                          'https://kpfu.ru/alina.sukorkina'),
                                                         ('Фадеева Елена Юрьевна',
                                                          'https://kpfu.ru/elena.fadeeva'),
                                                         ('Бакунина Гузяль Вазиховна',
                                                          'https://kpfu.ru/guzyal.bakunina'),
                                                         ('Гафиятуллин Линар Гадилович',
                                                          'https://kpfu.ru/linar.gafiyatullin'),
                                                         ('Гильмутдинов Ильдар Фаритович',
                                                          'https://kpfu.ru/ildar.gilmutdinov'),
                                                         ('Косенков Николай Иванович',
                                                          'https://kpfu.ru/nikolaji.kosenkov'),
                                                         ('Кочемасов Иван Николаевич',
                                                          'https://kpfu.ru/ivan.kochemasov'),
                                                         ('Мугинов Марат Ринатович',
                                                          'https://kpfu.ru/marat.muginov'),
                                                         ('Петров Андрей Вячеславович',
                                                          'https://kpfu.ru/andrej.petrov'),
                                                         ('Сахарова Надежда Петровна',
                                                          'https://kpfu.ru/nadezhda.saharova'),
                                                         ('Скворцов Евгений Николаевич',
                                                          'https://kpfu.ru/evgenijn.skvorcov'),
                                                         ('Спиридонов Анатолий '
                                                          'Владимирович',
                                                          'https://kpfu.ru/anatolij.spiridonov'),
                                                         ('Базановас Антонина Николаевна',
                                                          'https://kpfu.ru/antonina.bazanovas'),
                                                         ('Андреев Георгий Юрьевич',
                                                          'https://kpfu.ru/georgiy.andreev'),
                                                         ('Закиров Амир Ильдарович',
                                                          'https://kpfu.ru/amir.zakirov'),
                                                         ('Золина Карина Альфредовна',
                                                          'https://kpfu.ru/karina.zolina'),
                                                         ('Парфишина Арина Сергеевна',
                                                          'https://kpfu.ru/arina.parfishina'),
                                                         ('Полукеев Игорь Георгиевич',
                                                          'https://kpfu.ru/igor.polukeev'),
                                                         ('Сираев Фаиль Мансурович',
                                                          'https://kpfu.ru/fail.siraev'),
                                                         ('Спиридонова Ангелина '
                                                          'Вячеславовна',
                                                          'https://kpfu.ru/angelina.spiridonova'),
                                                         ('Цыганков Артем Алексеевич',
                                                          'https://kpfu.ru/artem.cygankov'),
                                                         ('Новеньков Анатолий Николаевич',
                                                          'https://kpfu.ru/Anatolij.Novenkov'),
                                                         ('Попова Галина Константиновна',
                                                          'https://kpfu.ru/Galina.Popova'),
                                                         ('Хамидуллин Линар Фирдусович',
                                                          'https://kpfu.ru/linar.hamidullin'),
                                                         ('Шарипова Гулия Ильгамовна',
                                                          'https://kpfu.ru/guliya.sharipova')],
                                'Кафедра оптики и нанофотоники': [('Калачев Алексей '
                                                                   'Алексеевич',
                                                                   'http://kpfu.ru/main?p_id=10907'),
                                                                  ('Харинцев Сергей '
                                                                   'Сергеевич',
                                                                   'http://kpfu.ru/main?p_id=10911'),
                                                                  ('Гайнутдинов Ренат '
                                                                   'Хамитович -\xa0',
                                                                   'http://kpfu.ru/main?p_id=10905'),
                                                                  ('Камалова Дина Илевна',
                                                                   'http://kpfu.ru/Dina.Kamalova'),
                                                                  ('Хамадеев Марат '
                                                                   'Актасович',
                                                                   'http://kpfu.ru/main?p_id=25527'),
                                                                  ('Корюкин Артем '
                                                                   'Валерьевич',
                                                                   'http://kpfu.ru/main?p_id=33168'),
                                                                  ('Гарифуллин Адель '
                                                                   'Ильдусович',
                                                                   'https://kpfu.ru/adel.garifullin'),
                                                                  ('Щербаков Виктор '
                                                                   'Дмитриевич',
                                                                   'http://kpfu.ru/Victor.Shcherbakov')],
                                'Кафедра радиоастрономии': [('Акчурин Адель Джавидович',
                                                             'http://kpfu.ru/main?p_id=10912'),
                                                            ('Закиров Ринат Камилевич',
                                                             'http://kpfu.ru/Rinat.Zakirov'),
                                                            ('Зыков Евгений Юрьевич',
                                                             'http://kpfu.ru/main?p_id=10914'),
                                                            ('Колчев Алексей Анатольевич',
                                                             'https://kpfu.ru/main?p_id=39638'),
                                                            ('Михайлова Ляля Фердинатовна',
                                                             'http://kpfu.ru/Lyalya.Mihaylova'),
                                                            ('Сапаев Андрей Львович',
                                                             'http://kpfu.ru/andrej.sapaev'),
                                                            ('Скобельцын Константин '
                                                             'Владимирович',
                                                             'http://kpfu.ru/konstantin.skobelcyn'),
                                                            ('Хуторова Ольга Германовна',
                                                             'http://kpfu.ru/main?p_id=10921'),
                                                            ('Шорников Всеволод Олегович',
                                                             'http://kpfu.ru/Vsevolod.Shornikov'),
                                                            ('Юсупов Камиль Маратович',
                                                             'http://kpfu.ru/main?p_id=26166')],
                                'Кафедра радиофизики': [('Шерстюков Олег Николаевич',
                                                         'https://kpfu.ru/Oleg.Sherstyukov'),
                                                        ('Карпов Аркадий Васильевич',
                                                         'https://kpfu.ru/Arkadi.Karpov'),
                                                        ('Тюрин Владимир Александрович',
                                                         'https://kpfu.ru/Vladimir.Tiourin'),
                                                        ('Шемахин Александр Юрьевич',
                                                         'https://kpfu.ru/Aleksandr.Shemahin'),
                                                        ('Калабанов Сергей Александрович',
                                                         'https://kpfu.ru/Sergei.Kalabanov'),
                                                        ('Латыпов Руслан Рустемович',
                                                         'https://kpfu.ru/Ruslan.Latypov'),
                                                        ('Рябченко Евгений Юрьевич',
                                                         'https://kpfu.ru/Eugene.Ryabchenko'),
                                                        ('Корчагин Павел Анатольевич',
                                                         'https://kpfu.ru/Pavel.Korchagin'),
                                                        ('Коротышкин Дмитрий Викторович',
                                                         'https://kpfu.ru/Dmitry.Korotyshkin'),
                                                        ('Данилов Евгений Валерьянович',
                                                         'https://kpfu.ru/Evgenij.Danilov'),
                                                        ('Панищев Олег Юрьевич',
                                                         'https://kpfu.ru/Oleg.Panischev'),
                                                        ('Смоляков Алексей Дмитриевич',
                                                         'https://kpfu.ru/aleksej.smolyakov'),
                                                        ('Галиев Айдар Ахатович',
                                                         'https://kpfu.ru/ajdar.galiev'),
                                                        ('Бочкарев Владимир Владимирович',
                                                         'https://kpfu.ru/Vladimir.Bochkarev'),
                                                        ('Гатина Роза Шамилевна',
                                                         'https://kpfu.ru/roza.gatina'),
                                                        ('Кашникова Наталья Викторовна',
                                                         'https://kpfu.ru/natalya.kashnikova'),
                                                        ('Куклин Владимир Александрович',
                                                         'https://kpfu.ru/vladimir.kuklin'),
                                                        ('Назмиев Фарид Масгутович',
                                                         'https://kpfu.ru/farid.nazmiev'),
                                                        ('Попова Татьяна Михайловна',
                                                         'https://kpfu.ru/Tanya.Popova'),
                                                        ('Сафонов Максим Николаевич',
                                                         'https://kpfu.ru/Maxim.Safonov'),
                                                        ('Марамзин Владимир Михайлович',
                                                         'https://kpfu.ru/vladimir.maramzin'),
                                                        ('Некрасов Игорь Константинович',
                                                         'https://kpfu.ru/igor.nekrasov'),
                                                        ('Самсонова Екатерина Сергеевна',
                                                         'https://kpfu.ru/ekaterinas.samsonova'),
                                                        ('Ситников Юрий Кириллович',
                                                         'https://kpfu.ru/Jury.Sitnikov'),
                                                        ('Терентьев Тимур Николаевич',
                                                         'https://kpfu.ru/timur.terentev'),
                                                        ('Якимова Людмила Михайловна',
                                                         'https://kpfu.ru/L.Yakimova')],
                                'Кафедра радиоэлектроники': [('Овчинников Марат '
                                                              'Николаевич',
                                                              'http://kpfu.ru/main?p_id=11004'),
                                                             ('Насыров Игорь '
                                                              'Альбертович\xa0',
                                                              'http://kpfu.ru/main?p_id=10942'),
                                                             ('Гумеров Рустем Исхакович ',
                                                              'http://kpfu.ru/main?p_id=11001'),
                                                             ('Гаврилов Александр '
                                                              'Геннадьевич ',
                                                              'http://kpfu.ru/main?p_id=20646'),
                                                             ('Лунев Иван '
                                                              'Владимирович\xa0',
                                                              'http://kpfu.ru/main?p_id=20939'),
                                                             ('Марфин Евгений '
                                                              'Александрович',
                                                              'http://kpfu.ru/main?p_id=30217'),
                                                             ('Когогин Денис '
                                                              'Александрович',
                                                              'http://kpfu.ru/Denis.Kogogin'),
                                                             ('Васильева Мария '
                                                              'Александровна ',
                                                              'http://kpfu.ru/main?p_id=21715')],
                                'Кафедра теоретической физики': [('список без фотографий',
                                                                  'http://kpfu.ru/main_page?p_cid=2394&p_random=054'),
                                                                 ('Авдеев Максим '
                                                                  'Викторович',
                                                                  'http://kpfu.ru/Maksim.Avdeev')],
                                'Кафедра теории относительности и гравитации': [('Альпин '
                                                                                 'Тимур '
                                                                                 'Юрьевич',
                                                                                 'https://kpfu.ru/Timur.Alpin'),
                                                                                ('Аминова '
                                                                                 'Ася '
                                                                                 'Васильевна',
                                                                                 'https://kpfu.ru/Asya.Aminova'),
                                                                                ('Балакин '
                                                                                 'Александр '
                                                                                 'Борисович',
                                                                                 'https://kpfu.ru/Alexander.Balakin'),
                                                                                ('Грошев '
                                                                                 'Дмитрий '
                                                                                 'Евгеньевич',
                                                                                 'https://kpfu.ru/dmitrij.groshev'),
                                                                                ('Даишев '
                                                                                 'Ринат '
                                                                                 'Абдурашидович',
                                                                                 'https://kpfu.ru/Rinat.Daishev'),
                                                                                ('Кашаргин '
                                                                                 'Павел '
                                                                                 'Евгеньевич',
                                                                                 'https://kpfu.ru/Pavel.Kashargin'),
                                                                                ('Кропотова '
                                                                                 'Татьяна '
                                                                                 'Владимировна',
                                                                                 'https://kpfu.ru/Tatyana.Kropotova'),
                                                                                ('Кузнецова '
                                                                                 'Алла '
                                                                                 'Юрьевна',
                                                                                 'https://kpfu.ru/Alla.Kuznetsova'),
                                                                                ('Мухарлямов '
                                                                                 'Руслан '
                                                                                 'Камилевич',
                                                                                 'https://kpfu.ru/Ruslan.Muharlyamov'),
                                                                                ('Патрин '
                                                                                 'Евгений '
                                                                                 'Владимирович',
                                                                                 'https://kpfu.ru/Evgeny.Patrin'),
                                                                                ('Попов '
                                                                                 'Владимир '
                                                                                 'Александрович',
                                                                                 'https://kpfu.ru/Vladimir.Popov'),
                                                                                ('Серякин '
                                                                                 'Георгий '
                                                                                 'Анатольевич',
                                                                                 'https://kpfu.ru/George.Seryakin'),
                                                                                ('Сушков '
                                                                                 'Сергей '
                                                                                 'Владимирович',
                                                                                 'https://kpfu.ru/Sergey.Sushkov'),
                                                                                ('Хабибуллина '
                                                                                 'Гузель '
                                                                                 'Забировна',
                                                                                 'https://kpfu.ru/guzel.habibullina')],
                                'Кафедра физики молекулярных систем': [('Скирда Владимир '
                                                                        'Дмитриевич',
                                                                        'https://kpfu.ru/Vladimir.Skirda'),
                                                                       ('Фаткуллин Наиль '
                                                                        'Фидаиевич',
                                                                        'http://kpfu.ru/Nail.Fatkullin'),
                                                                       ('Филиппов Андрей '
                                                                        'Васильевич',
                                                                        'http://kpfu.ru/Andrey.Filippov'),
                                                                       ('Савинков Андрей '
                                                                        'Владимирович\xa0',
                                                                        'http://kpfu.ru/Andrey.Savinkov'),
                                                                       ('Савостина '
                                                                        'Людмила Ивановна',
                                                                        'https://kpfu.ru/Liudmila.Savostina'),
                                                                       ('Александров '
                                                                        'Артем Сергеевич',
                                                                        'https://kpfu.ru/main?p_id=29680'),
                                                                       ('Тумакаева Люзия '
                                                                        'Хафизовна',
                                                                        'https://kpfu.ru/ljuziya.tumakaeva'),
                                                                       ('Мельникова Дарья '
                                                                        'Леонидовна',
                                                                        'https://kpfu.ru/darya.melnikova'),
                                                                       ('Иванов Анатолий '
                                                                        'Александрович',
                                                                        'https://kpfu.ru/Anatoly.Ivanov'),
                                                                       ('Иванов Дмитрий '
                                                                        'Сергеевич',
                                                                        'https://kpfu.ru/dmitrijs.ivanov'),
                                                                       ('Савинкова Юлия '
                                                                        'Рафаиловна',
                                                                        'https://kpfu.ru/juliya.savinkova')],
                                'Кафедра физики твердого тела': [('Воронина Елена '
                                                                  'Валентиновна',
                                                                  'https://kpfu.ru/Elena.Voronina'),
                                                                 ('Парфенов Виктор '
                                                                  'Всеволодович',
                                                                  'https://kpfu.ru/Viktor.Parfenov'),
                                                                 ('Вагизов Фарит '
                                                                  'Габдулхакович',
                                                                  'https://kpfu.ru/Farit.Vagizov'),
                                                                 ('Никитин Сергей '
                                                                  'Иванович',
                                                                  'https://kpfu.ru/Sergey.Nikitin'),
                                                                 ('Дулов Евгений '
                                                                  'Николаевич',
                                                                  'https://kpfu.ru/Evgeny.Dulov'),
                                                                 ('Зарипова Ландыш '
                                                                  'Дамировна',
                                                                  'https://kpfu.ru/landysh.zaripova'),
                                                                 ('Иванова Анна '
                                                                  'Геннадьевна',
                                                                  'https://kpfu.ru/annag.ivanova'),
                                                                 ('Бикчантаев Масгут '
                                                                  'Махмутович',
                                                                  'https://kpfu.ru/Masgut.Bikchantaev'),
                                                                 ('Закиров Ринат '
                                                                  'Камилевич',
                                                                  'https://kpfu.ru/Rinat.Zakirov'),
                                                                 ('Пятаев Андрей '
                                                                  'Васильевич',
                                                                  'https://kpfu.ru/Andrey.Pyataev'),
                                                                 ('Абдуллин Аяз '
                                                                  'Фернатович',
                                                                  'https://kpfu.ru/ayaz.abdullin'),
                                                                 ('Куташова Екатерина '
                                                                  'Михайловна',
                                                                  'https://kpfu.ru/ekaterina.kutashova')],
                                'Кафедра ядерно-физического материаловедения': [('Болтакова '
                                                                                 'Наталья '
                                                                                 'Викторовна',
                                                                                 'https://kpfu.ru/Natalya.Boltakova'),
                                                                                ('Ахматнабиева '
                                                                                 'Лейля '
                                                                                 'Булатовна',
                                                                                 'https://kpfu.ru/lejla.akhmatnabieva')]},
            'Институт филологии и межкультурной коммуникации': {
                'Кафедра билингвального и цифрового образования': [('Галимянов '
                                                                    'Анис '
                                                                    'Фуатович',
                                                                    'https://kpfu.ru/Anis.Galimjanoff'),
                                                                   ('Фахрутдинова '
                                                                    'Резида '
                                                                    'Ахатовна',
                                                                    'https://kpfu.ru/Rezida.Fahrutdinova'),
                                                                   ('Ялалов '
                                                                    'Фарит '
                                                                    'Габтелович',
                                                                    'https://kpfu.ru/farit.yalalov'),
                                                                   ('Ярмакеев '
                                                                    'Искандер '
                                                                    'Энгелевич',
                                                                    'https://kpfu.ru/Iskander.Yarmakeev'),
                                                                   ('Салехова '
                                                                    'Ляйля '
                                                                    'Леонардовна',
                                                                    'https://kpfu.ru/Lyajlya.Salehova'),
                                                                   ('Абдрафикова '
                                                                    'Альбина '
                                                                    'Ринатовна',
                                                                    'https://kpfu.ru/Albina.Abdrafikova'),
                                                                   ('Гарипов '
                                                                    'Ильнур '
                                                                    'Бурханович',
                                                                    'https://kpfu.ru/Ilnur.Garipov'),
                                                                   ('Григорьева '
                                                                    'Ксения '
                                                                    'Сергеевна',
                                                                    'https://kpfu.ru/Kseniya.Grigoreva'),
                                                                   ('Данилов '
                                                                    'Андрей '
                                                                    'Владимирович',
                                                                    'https://kpfu.ru/andrej.danilov'),
                                                                   ('Лукоянова '
                                                                    'Марина '
                                                                    'Александровна',
                                                                    'https://kpfu.ru/marina.lukoyanova'),
                                                                   ('Хакимов '
                                                                    'Булат '
                                                                    'Эрнстович',
                                                                    'https://kpfu.ru/Boulat.Hakimov'),
                                                                   ('Батрова '
                                                                    'Наиля '
                                                                    'Ильдусовна',
                                                                    'https://kpfu.ru/nailya.batrova'),
                                                                   ('Зарипова '
                                                                    'Рината '
                                                                    'Раисовна',
                                                                    'https://kpfu.ru/Rinata.Zaripova'),
                                                                   ('Пименова '
                                                                    'Татьяна '
                                                                    'Сергеевна',
                                                                    'https://kpfu.ru/Tatyana.Pimenova'),
                                                                   ('Валеев '
                                                                    'Ильмир '
                                                                    'Ирекович',
                                                                    'https://kpfu.ru/ilmir.valeev'),
                                                                   ('Мухаметшин '
                                                                    'Ленар '
                                                                    'Миннеханович',
                                                                    'https://kpfu.ru/Lenar.Muhametshin'),
                                                                   ('Плотникова '
                                                                    'Луиза '
                                                                    'Альбертовна',
                                                                    'https://kpfu.ru/luiza.plotnikova'),
                                                                   ('Фазлиахметов '
                                                                    'Тимур '
                                                                    'Рафикович',
                                                                    'https://kpfu.ru/timur.fazliakhmetov'),
                                                                   ('Ибрагимов '
                                                                    'Тавзих '
                                                                    'Ибрагимович',
                                                                    'https://kpfu.ru/Tavzikh.Ibragimov'),
                                                                   ('Шангареев '
                                                                    'Евгений '
                                                                    'Ринатович',
                                                                    'https://kpfu.ru/evgenij.shangareev'),
                                                                   ('Ижевских '
                                                                    'Елена '
                                                                    'Рудольфовна',
                                                                    'https://kpfu.ru/elena.izhevskih')],
                'Кафедра дизайна и национальных искусств': [('Ахметшина '
                                                             'Эльмира '
                                                             'Габдулловна',
                                                             'https://kpfu.ru/elmira.ahmetshina'),
                                                            ('Яо '
                                                             'Любовь '
                                                             'Маркеловна',
                                                             'https://kpfu.ru/lyubov.yao'),
                                                            ('Гаджиев '
                                                             'Имаш '
                                                             'Адыширин '
                                                             'оглы',
                                                             'https://kpfu.ru/imash.gadzhiev'),
                                                            ('Еманова '
                                                             'Юлиана '
                                                             'Геннадьевна',
                                                             'https://kpfu.ru/Juliana.Emanova'),
                                                            ('Кадыйрова '
                                                             'Ляйсан '
                                                             'Хабибулхаковна',
                                                             'https://kpfu.ru/lyajsan.kadyjrova'),
                                                            ('Мубаракшина '
                                                             'Фирдания '
                                                             'Дамировна',
                                                             'https://kpfu.ru/firdaniya.mubarakshina'),
                                                            ('Насибуллов '
                                                             'Рамис '
                                                             'Рафагатович',
                                                             'https://kpfu.ru/Ramis.Nasibullov'),
                                                            ('Яо '
                                                             'Михаил '
                                                             'Константинович',
                                                             'https://kpfu.ru/Mihail.Yao'),
                                                            ('Карамова '
                                                             'Клара '
                                                             'Хакимовна',
                                                             'https://kpfu.ru/klara.karamova'),
                                                            ('Махмутова '
                                                             'Мадина '
                                                             'Мухаметовна',
                                                             'https://kpfu.ru/Madina.Mahmutova'),
                                                            ('Мухаметзянова '
                                                             'Лилия '
                                                             'Ринатовна',
                                                             'https://kpfu.ru/Liliya.Ahmetova'),
                                                            ('Юмагулова '
                                                             'Венера '
                                                             'Маратовна',
                                                             'https://kpfu.ru/venera.yumagulova'),
                                                            ('Валиуллин '
                                                             'Фарит '
                                                             'Рашидович',
                                                             'https://kpfu.ru/Farit.Valiullin'),
                                                            ('Силуянычев '
                                                             'Андрей '
                                                             'Михайлович',
                                                             'https://kpfu.ru/andrej.siluyanychev'),
                                                            ('Ахметшина '
                                                             'Гульназ '
                                                             'Радиковна',
                                                             'https://kpfu.ru/Gulnaz.Hasanzyanova'),
                                                            ('Мирхасанов '
                                                             'Рустем '
                                                             'Фаритович',
                                                             'https://kpfu.ru/rustem.mirkhasanov'),
                                                            ('Нуруллин '
                                                             'Айдар '
                                                             'Фаритович',
                                                             'https://kpfu.ru/ajdar.nurullin'),
                                                            ('Раузеев '
                                                             'Искандер '
                                                             'Зиннурович',
                                                             'https://kpfu.ru/iskander.rauzeev'),
                                                            ('Сафин '
                                                             'Айрат '
                                                             'Равилевич',
                                                             'https://kpfu.ru/ayrat.safin'),
                                                            ('Зарипова '
                                                             'Лилия '
                                                             'Ренатовна',
                                                             'https://kpfu.ru/liliya.ishmakova'),
                                                            ('Мухаметшин '
                                                             'Александр '
                                                             'Альбертович',
                                                             'https://kpfu.ru/aleksandr.mukhametshin'),
                                                            ('Сафина '
                                                             'Гульнара '
                                                             'Ильдаровна',
                                                             'https://kpfu.ru/gulnarai.safina'),
                                                            ('Юсупова '
                                                             'Эльвира '
                                                             'Рстамовна',
                                                             'https://kpfu.ru/elvira.yusupova'),
                                                            ('Шайдуллина '
                                                             'Дина '
                                                             'Насиховна',
                                                             'https://kpfu.ru/dina.shajdullina'),
                                                            ('Аниферова '
                                                             'Виолетта '
                                                             'Витальевна',
                                                             'https://kpfu.ru/violetta.aniferova')],
                'Кафедра контрастивной лингвистики': [('Шакирова '
                                                       'Диляра '
                                                       'Шамилевна',
                                                       'https://kpfu.ru/Dilyara.Israfilova'),
                                                      ('Абдрафикова '
                                                       'Альбина '
                                                       'Ринатовна',
                                                       'https://kpfu.ru/Albina.Abdrafikova'),
                                                      ('Вагнер '
                                                       'Кира '
                                                       'Рустемовна',
                                                       'https://kpfu.ru/kira.vagner'),
                                                      ('Нурутдинова '
                                                       'Аида '
                                                       'Рустамовна',
                                                       'https://kpfu.ru/aidar.nurutdinova'),
                                                      ('Фазлыева '
                                                       'Зульфия '
                                                       'Ханифовна',
                                                       'https://kpfu.ru/Zulfiya.Fazlyeva'),
                                                      ('Григорьева '
                                                       'Ксения '
                                                       'Сергеевна',
                                                       'https://kpfu.ru/Kseniya.Grigoreva'),
                                                      ('Исмагилова '
                                                       'Гулюса '
                                                       'Курбангалиевна',
                                                       'https://kpfu.ru/guljusa.ismagilova'),
                                                      ('Насибуллова '
                                                       'Гузель '
                                                       'Ришатовна',
                                                       'https://kpfu.ru/Guzel.Nasibullova'),
                                                      ('Туганова '
                                                       'Светлана '
                                                       'Владимировна',
                                                       'https://kpfu.ru/svetlana.tuganova'),
                                                      ('Гагарина '
                                                       'Вилена '
                                                       'Рустемовна',
                                                       'https://kpfu.ru/vilena.gagarina'),
                                                      ('Шейнина '
                                                       'Дина '
                                                       'Петровна',
                                                       'https://kpfu.ru/Dina.Shejnina'),
                                                      ('Акташ '
                                                       'Айгуль '
                                                       'Ильдаровна',
                                                       'https://kpfu.ru/ajgul.farhaeva'),
                                                      ('Бадур '
                                                       'Фархад ',
                                                       'https://kpfu.ru/farkhad.badur'),
                                                      ('Бикмуллина '
                                                       'Эльвира '
                                                       'Рамильевна',
                                                       'https://kpfu.ru/elvira.bikmullina'),
                                                      ('Богданова '
                                                       'Анна '
                                                       'Романовна',
                                                       'https://kpfu.ru/anna.bogdanova'),
                                                      ('Измайлова '
                                                       'Гузель '
                                                       'Алексеевна',
                                                       'https://kpfu.ru/guzel.izmajlova'),
                                                      ('Ильминбетова '
                                                       'Сабина '
                                                       'Альбертовна',
                                                       'https://kpfu.ru/sabina.ilminbetova'),
                                                      ('Литвиненко '
                                                       'Елена '
                                                       'Владимировна',
                                                       'https://kpfu.ru/elena.litvinenko'),
                                                      ('Ло '
                                                       'Ли ',
                                                       'https://kpfu.ru/li.lo'),
                                                      ('Сарачоглу '
                                                       'Хатидже ',
                                                       'https://kpfu.ru/khatidzhe.sarachoglu'),
                                                      ('Хасанзянова '
                                                       'Гульнара '
                                                       'Илгизовна',
                                                       'https://kpfu.ru/gulnara.hasanzyanova'),
                                                      ('Чжэн '
                                                       'Чжуньи ',
                                                       'https://kpfu.ru/chzhuni.chzhen'),
                                                      ('Шангареев '
                                                       'Мустафа '
                                                       'Мансурович',
                                                       'https://kpfu.ru/mustafa.shangareev'),
                                                      ('Ши '
                                                       'Даньдань ',
                                                       'https://kpfu.ru/dandan.shi'),
                                                      ('Чжэн '
                                                       'Милана '
                                                       'Фаридовна',
                                                       'https://kpfu.ru/milanaf.chzhen')],
                'Кафедра общего языкознания и тюркологии': [('',
                                                             'http://kpfu.ru/Radif.Zamaletdinov'),
                                                            ('Замалетдинов '
                                                             'Радиф '
                                                             'Рифкатович',
                                                             'http://kpfu.ru/Radif.Zamaletdinov'),
                                                            ('Аюпова '
                                                             'Айгуль '
                                                             'Ринатовна',
                                                             'http://kpfu.ru/Ajgul.Ajupova'),
                                                            ('Болгарова '
                                                             'Рамзия '
                                                             'Марсовна',
                                                             'http://kpfu.ru/Ramziya.Bolgarova'),
                                                            ('Гайнутдинова '
                                                             'Алина '
                                                             'Салимовна',
                                                             'https://kpfu.ru/alina.gajnutdinova'),
                                                            ('Гилазетдинова '
                                                             'Гелиня '
                                                             'Хайретдиновна',
                                                             'http://kpfu.ru/main?p_id=11115'),
                                                            ('Денмухаметова '
                                                             'Эльвира '
                                                             'Николаевна',
                                                             'http://kpfu.ru/Ilvira.Denmukhametova'),
                                                            ('Закиев '
                                                             'Мирфатых '
                                                             'Закиевич',
                                                             'https://kpfu.ru/Mirfatyh.Zakiev'),
                                                            ('Замалетдинова '
                                                             'Гульнара '
                                                             'Фандасовна',
                                                             'http://kpfu.ru/Gulnara.Zamaletdinova'),
                                                            ('Исламова '
                                                             'Эльвира '
                                                             'Альбертовна',
                                                             'http://kpfu.ru/Ealvira.Islamova'),
                                                            ('Кириллова '
                                                             'Зоя '
                                                             'Николаевна',
                                                             'http://kpfu.ru/Zoja.Kirillova'),
                                                            ('Латыпов '
                                                             'Ренат '
                                                             'Исламгаряевич',
                                                             'https://kpfu.ru/renat.latypov'),
                                                            ('Мугтасимова '
                                                             'Гульназ '
                                                             'Ринатовна',
                                                             'http://kpfu.ru/Gulnaz.Mugtasimova'),
                                                            ('Набиуллина '
                                                             'Гузель '
                                                             'Амировна',
                                                             'http://kpfu.ru/Guzel.Nabiullina'),
                                                            ('Нурмухаметова '
                                                             'Раушания '
                                                             'Сагдатзяновна',
                                                             'http://kpfu.ru/Raushaniya.Nurmuhametova'),
                                                            ('Салахова '
                                                             'Рузиля '
                                                             'Рашитовна',
                                                             'http://kpfu.ru/Ruzilya.Salahova'),
                                                            ('Саттарова '
                                                             'Мадина '
                                                             'Рашидовна',
                                                             'http://kpfu.ru/Madina.Sattarova'),
                                                            ('Сибгаева '
                                                             'Фируза '
                                                             'Рамзеловна',
                                                             'http://kpfu.ru/Firuza.Sibgaeva'),
                                                            ('Фатхуллова '
                                                             'Кадрия '
                                                             'Сунгатовна',
                                                             'http://kpfu.ru/Kadria.Fatxullova'),
                                                            ('Юсупова '
                                                             'Альфия '
                                                             'Шавкетовна',
                                                             'http://kpfu.ru/Alfiia.Iousoupova'),
                                                            ('Сафина '
                                                             'Гульгена '
                                                             'Нурисламовна',
                                                             'http://kpfu.ru/Gulgena.Husnullina')],
                'Кафедра прикладной и экспериментальной лингвистики': [('Горобец '
                                                                        'Елена '
                                                                        'Анатольевна',
                                                                        'http://kpfu.ru/Elena.Gorobets'),
                                                                       ('Бакшаева '
                                                                        'Алёна '
                                                                        'Андреевна',
                                                                        'https://kpfu.ru/alyona.bakshaeva'),
                                                                       ('Виноградова '
                                                                        'Татьяна '
                                                                        'Юрьевна',
                                                                        'http://kpfu.ru/Tatyana.Vinogradova'),
                                                                       ('Вольская '
                                                                        'Юлия '
                                                                        'Александровна',
                                                                        'https://kpfu.ru/juliya.volskaya'),
                                                                       ('Галиуллин '
                                                                        'Камиль '
                                                                        'Рахимович',
                                                                        'http://kpfu.ru/k.galiullin'),
                                                                       ('Гараева '
                                                                        'Виктория '
                                                                        'Юрьевна',
                                                                        'https://kpfu.ru/main?p_id=42832'),
                                                                       ('Гизатуллина '
                                                                        'Азалия '
                                                                        'Ришатовна',
                                                                        'http://kpfu.ru/Azaliya.Gizatullina'),
                                                                       ('Есин '
                                                                        'Олег '
                                                                        'Радиевич',
                                                                        'http://kpfu.ru/oleg.esin'),
                                                                       ('Жолобов '
                                                                        'Олег '
                                                                        'Феофанович',
                                                                        'http://kpfu.ru/Oleg.Jolobov'),
                                                                       ('Каримуллина '
                                                                        'Гузель '
                                                                        'Нурутдиновна',
                                                                        'http://kpfu.ru/Guzel.Karimullina'),
                                                                       ('Каримуллина '
                                                                        'Резеда '
                                                                        'Нурутдиновна',
                                                                        'https://kpfu.ru/Rezeda.Karimullina'),
                                                                       ('Лещиньска '
                                                                        'Анна '
                                                                        'Магдалена',
                                                                        'https://kpfu.ru/anna_magdalena.leshhinska'),
                                                                       ('Луканкина '
                                                                        'Татьяна '
                                                                        'Александровна',
                                                                        'https://kpfu.ru/tatyana.alehina'),
                                                                       ('Мардиева '
                                                                        'Ляйля '
                                                                        'Агьдасовна',
                                                                        'https://kpfu.ru/Lejla.Mardieva'),
                                                                       ('Мартьянов '
                                                                        'Денис '
                                                                        'Андреевич',
                                                                        'https://kpfu.ru/Denis.Martyanov'),
                                                                       ('Николаева '
                                                                        'Наталия '
                                                                        'Геннадьевна',
                                                                        'http://kpfu.ru/Natalia.Nikolaeva'),
                                                                       ('Соловьёв '
                                                                        'Валерий '
                                                                        'Дмитриевич',
                                                                        'https://kpfu.ru/Valery.Solovyev'),
                                                                       ('Фатхутдинова '
                                                                        'Венера '
                                                                        'Габдулхаковна',
                                                                        'https://kpfu.ru/Venera.Fatkhoutdinova'),
                                                                       ('Шайхутдинова '
                                                                        'Рузалина '
                                                                        'Ильясовна',
                                                                        'https://kpfu.ru/main?p_id=41870'),
                                                                       ('Щуклина '
                                                                        'Татьяна '
                                                                        'Ювенальевна',
                                                                        'https://kpfu.ru/Tatyana.Schuklina')],
                'Кафедра романо-германской филологии': [('Арсентьева '
                                                         'Елена '
                                                         'Фридриховна',
                                                         'https://kpfu.ru/Elena.Arsentyeva'),
                                                        ('Аюпова '
                                                         'Роза '
                                                         'Алляметдиновна',
                                                         'https://kpfu.ru/Roza.Ayupova'),
                                                        ('Тарасова '
                                                         'Фануза '
                                                         'Харисовна',
                                                         'https://kpfu.ru/fanuza.tarasova'),
                                                        ('Амурская '
                                                         'Оксана '
                                                         'Юрьевна',
                                                         'https://kpfu.ru/Oksana.Amurskaya'),
                                                        ('Варламова '
                                                         'Елена '
                                                         'Валерьевна',
                                                         'https://kpfu.ru/Elena.Varlamova'),
                                                        ('Гаврилов '
                                                         'Аллен '
                                                         'Владимирович',
                                                         'https://kpfu.ru/allen.gavrilov'),
                                                        ('Газизова '
                                                         'Лилия '
                                                         'Гумаровна',
                                                         'https://kpfu.ru/Lilija.Gazizova'),
                                                        ('Гималетдинова '
                                                         'Гульнара '
                                                         'Камилевна',
                                                         'https://kpfu.ru/Gulnara.Gimaletdinova'),
                                                        ('Каюмова '
                                                         'Альбина '
                                                         'Рамилевна',
                                                         'https://kpfu.ru/Albina.Kayumova'),
                                                        ('Носкова '
                                                         'Анна '
                                                         'Ильинична',
                                                         'https://kpfu.ru/anna.vlasova'),
                                                        ('Плеухова '
                                                         'Елена '
                                                         'Алексеевна',
                                                         'https://kpfu.ru/Elena.Pleuchova'),
                                                        ('Садыкова '
                                                         'Гульнара '
                                                         'Василевна',
                                                         'https://kpfu.ru/Gulnara.Sadykova'),
                                                        ('Салиева '
                                                         'Римма '
                                                         'Наильевна',
                                                         'https://kpfu.ru/Rimma.Saileva'),
                                                        ('Сафина '
                                                         'Римма '
                                                         'Абельхаеровна',
                                                         'https://kpfu.ru/Rimma.Safina'),
                                                        ('Сафиуллина '
                                                         'Гульшат '
                                                         'Рафаилевна',
                                                         'https://kpfu.ru/Gulshat.Safiullina'),
                                                        ('Халитова '
                                                         'Лилия '
                                                         'Камилевна',
                                                         'https://kpfu.ru/Liliya.Halitova'),
                                                        ('Якубова '
                                                         'Диляра '
                                                         'Джавдетовна',
                                                         'https://kpfu.ru/Dilyara.Sulejmanova'),
                                                        ('Гарипова '
                                                         'Эльза '
                                                         'Вильдановна',
                                                         'https://kpfu.ru/elza.garipova'),
                                                        ('Гурьянов '
                                                         'Игорь '
                                                         'Олегович',
                                                         'https://kpfu.ru/igor.guryanov'),
                                                        ('Дуняшева '
                                                         'Лилия '
                                                         'Гаффаровна',
                                                         'https://kpfu.ru/liliya.dunyasheva'),
                                                        ('Колабинова '
                                                         'Татьяна '
                                                         'Ивановна',
                                                         'https://kpfu.ru/Tatyana.Kolabinova'),
                                                        ('Планкина '
                                                         'Регина '
                                                         'Маратовна',
                                                         'https://kpfu.ru/regina.plankina'),
                                                        ('Гарсия '
                                                         'Муньос '
                                                         'Рикардо',
                                                         'https://kpfu.ru/Rikardo.Garsiya'),
                                                        ('Мамаева '
                                                         'Алена '
                                                         'Дмитриевна',
                                                         'https://kpfu.ru/alena.mamaeva'),
                                                        ('Сиразова '
                                                         'Лилия '
                                                         'Саимовна',
                                                         'https://kpfu.ru/liliya.sirazova'),
                                                        ('Диас '
                                                         'Етсанет '
                                                         'Дель '
                                                         'Валье',
                                                         'https://kpfu.ru/etsanet.dias'),
                                                        ('Давитова '
                                                         'Нурия '
                                                         'Рустэмовна',
                                                         'https://kpfu.ru/nuriya.davitova'),
                                                        ('Кайгородова '
                                                         'Лира '
                                                         'Николаевна',
                                                         'https://kpfu.ru/lira.kaygorodova'),
                                                        ('Серкадильо '
                                                         'Бланко '
                                                         'Соня ',
                                                         'https://kpfu.ru/sonya.serkadilo_blanko'),
                                                        ('Васильева-Шальнева '
                                                         'Татьяна '
                                                         'Борисовна',
                                                         'https://kpfu.ru/Tatyana.Vasileva-Shalneva')],
                'Кафедра русского языка и методики его преподавания': [('Юсупова '
                                                                        'Зульфия '
                                                                        'Фирдинатовна',
                                                                        'https://kpfu.ru/Zulfiya.Jusupova'),
                                                                       ('Аминова '
                                                                        'Альмира\xa0 '
                                                                        'Асхатовна',
                                                                        'https://kpfu.ru/Almira.Aminova'),
                                                                       ('Байрамова '
                                                                        'Луиза '
                                                                        'Каримовна',
                                                                        'https://kpfu.ru/Luiza.Bairamova'),
                                                                       ('Ерофеева '
                                                                        'Ирина '
                                                                        'Валерьевна',
                                                                        'https://kpfu.ru/Irina.Erofeeva'),
                                                                       ('Фаттахова '
                                                                        'Наиля '
                                                                        'Нурыйхановна',
                                                                        'https://kpfu.ru/Nailya.Fattahova'),
                                                                       ('Хайрутдинова '
                                                                        'Гульшат '
                                                                        'Ахматхановна',
                                                                        'https://kpfu.ru/Gulshat.Hairutdinova'),
                                                                       ('Корнеева '
                                                                        'Татьяна '
                                                                        'Александровна',
                                                                        'https://kpfu.ru/Tatyana.Korneeva'),
                                                                       ('Лукоянова '
                                                                        'Юлия '
                                                                        'Константиновна',
                                                                        'https://kpfu.ru/Julia.Lukojanova'),
                                                                       ('Нуруллина '
                                                                        'Гузель '
                                                                        'Миннезуфаровна',
                                                                        'https://kpfu.ru/Guzel.Nurullina'),
                                                                       ('Рахимова '
                                                                        'Динара '
                                                                        'Ирековна',
                                                                        'https://kpfu.ru/Dinara.Rahimova'),
                                                                       ('Сафонова '
                                                                        'Светлана '
                                                                        'Сергеевна',
                                                                        'https://kpfu.ru/Svetlana.Safonova'),
                                                                       ('Усманова '
                                                                        'Лилия '
                                                                        'Абраровна',
                                                                        'https://kpfu.ru/Liliya.Usmanova'),
                                                                       ('Чупрякова '
                                                                        'Ольга '
                                                                        'Анатольевна',
                                                                        'https://kpfu.ru/Olga.Chupryakova'),
                                                                       ('Файзуллина '
                                                                        'Наиля '
                                                                        'Ивановна',
                                                                        'https://kpfu.ru/Najlya.Fedorova'),
                                                                       ('Давлатова\xa0 '
                                                                        'Мансура '
                                                                        'Мансуровна',
                                                                        'https://kpfu.ru/mansura.davlatova')],
                'Кафедра русского языка как иностранного': [('Бочина '
                                                             'Татьяна '
                                                             'Геннадьевна ',
                                                             '\t'
                                                             'http://kpfu.ru/Tatyana.Bochina\t'),
                                                            ('Бурцева '
                                                             'Татьяна '
                                                             'Альбертовна ',
                                                             '\t'
                                                             'http://kpfu.ru/Tatyana.Burceva\t'),
                                                            ('Гимранова '
                                                             'Татьяна '
                                                             'Александровна',
                                                             'http://kpfu.ru/Tatjana.Bychkova'),
                                                            ('Хабибуллина '
                                                             'Елена '
                                                             'Викторовна ',
                                                             '\t'
                                                             'http://kpfu.ru/main?p_id=29521\t'),
                                                            ('Садыкова '
                                                             'Илсояр '
                                                             'Афтахована ',
                                                             '\t'
                                                             'http://kpfu.ru/main?p_id=24915\t'),
                                                            ('Колосова '
                                                             'Елена '
                                                             'Ивановна',
                                                             '\t'
                                                             'http://kpfu.ru/Helena.Kolosova\t'),
                                                            ('Косова '
                                                             'Вера '
                                                             'Алексеевна ',
                                                             '\t'
                                                             'http://kpfu.ru/main?p_id=11116&p_lang=&p_type=1\t'),
                                                            ('Бастрикова '
                                                             'Елена '
                                                             'Михайловна ',
                                                             '\t'
                                                             'http://kpfu.ru/pec_print?p_id=11110&p_lang=\t'),
                                                            ('Бастриков '
                                                             'Алексей '
                                                             'Васильевич ',
                                                             '\t'
                                                             'http://kpfu.ru/pec_print?p_id=11109&p_lang=\t'),
                                                            ('Москалева '
                                                             'Лада '
                                                             'Алексеевна',
                                                             'http://kpfu.ru/lada.moskaleva'),
                                                            ('Мифтахова '
                                                             'Алия '
                                                             'Наилевна ',
                                                             '\t'
                                                             'http://kpfu.ru/Aliya.Miftahova\t'),
                                                            ('Ахмерова '
                                                             'Лилия '
                                                             'Ринадовна',
                                                             '\t'
                                                             'http://kpfu.ru/liliya.Akhmerova\t'),
                                                            ('Агеева '
                                                             'Юлия '
                                                             'Викторовна',
                                                             'http://kpfu.ru/Juliya.Ageeva'),
                                                            ('Салахова '
                                                             'Айгуль '
                                                             'Рестамовна ',
                                                             '\t'
                                                             'http://kpfu.ru/Aygul.Salakhova\t'),
                                                            ('Спиридонов '
                                                             'Александр '
                                                             'Владимирович',
                                                             '\t'
                                                             'http://kpfu.ru/pec_print?p_id=30106&p_lang=\t'),
                                                            ('Галеев '
                                                             'Тимур '
                                                             'Ильдарович ',
                                                             '\t'
                                                             'http://kpfu.ru/timur.galeev\t'),
                                                            ('Яппарова '
                                                             'Венера '
                                                             'Нагимовна ',
                                                             '\t'
                                                             'http://kpfu.ru/main?p_id=29461\t'),
                                                            ('Старостина '
                                                             'Ольга '
                                                             'Вячеславовна ',
                                                             '\t'
                                                             'http://kpfu.ru/Olga.Starostina\t'),
                                                            ('Маклеева '
                                                             'Елена '
                                                             'Александровна ',
                                                             '\t'
                                                             'http://kpfu.ru/Elena.Makleeva\t'),
                                                            ('Рахимова '
                                                             'Алия '
                                                             'Рамилевна',
                                                             'http://kpfu.ru/aliya.rahimova'),
                                                            ('Капустина '
                                                             'Елена '
                                                             'Владимировна',
                                                             'http://kpfu.ru/elena.kapustina'),
                                                            ('Капралова '
                                                             'Юлия '
                                                             'Владимировна',
                                                             'http://kpfu.ru/juliya.kapralova'),
                                                            ('Штырлина '
                                                             'Екатерина '
                                                             'Геннадьевна',
                                                             'http://kpfu.ru/pec_print?p_id=30352&p_lang='),
                                                            ('Варламова '
                                                             'Марина '
                                                             'Юрьевна',
                                                             'http://kpfu.ru/Marina.Varlamova'),
                                                            ('Гузаерова '
                                                             'Регина '
                                                             'Рустемовна',
                                                             'http://kpfu.ru/regina.guzaerova'),
                                                            ('Ахметзянова\xa0'
                                                             'Лиана\xa0'
                                                             'Михайловна',
                                                             'http://kpfu.ru/main?p_id=42875'),
                                                            ('Ершова '
                                                             'Алина '
                                                             'Андреевна',
                                                             'https://kpfu.ru/alina.ershova'),
                                                            ('Казанцева '
                                                             'Аида '
                                                             'Марсовна\xa0',
                                                             'https://kpfu.ru/main?p_id=43552'),
                                                            ('Музуров '
                                                             'Виталий '
                                                             'Николаевич',
                                                             'https://kpfu.ru/vitalij.muzurov'),
                                                            ('Макришина '
                                                             'Надежда '
                                                             'Владимировна',
                                                             'https://kpfu.ru/nadezhda.makrishina'),
                                                            ('Коршунова '
                                                             'Анастасия '
                                                             'Александровна',
                                                             'https://kpfu.ru/anastasiya.korshunova'),
                                                            ('Зигангирова '
                                                             'Ляйсяния '
                                                             'Башировна',
                                                             'https://kpfu.ru/lyajsyaniya.zigangirova'),
                                                            ('Некрасова '
                                                             'Инна '
                                                             'Дмитриевна',
                                                             'https://kpfu.ru/inna.nekrasova'),
                                                            ('Смоленцева '
                                                             'Людмила '
                                                             'Александровна',
                                                             'https://kpfu.ru/lyudmila.smolenceva'),
                                                            ('Чэнь '
                                                             'Няньцзу',
                                                             'https://kpfu.ru/nyanczu.chen'),
                                                            ('Ван '
                                                             'Мо',
                                                             'https://kpfu.ru/pec_print?p_id=46329')],
                'Кафедра русской и зарубежной литературы': [('Несмелова '
                                                             'Ольга '
                                                             'Олеговна',
                                                             'https://kpfu.ru/Olga.Nesmelova'),
                                                            ('Крылов '
                                                             'Вячеслав '
                                                             'Николаевич',
                                                             'https://kpfu.ru/Vjatsheslav.Krylov'),
                                                            ('Мухаметшина '
                                                             'Резеда '
                                                             'Фаилевна',
                                                             'https://kpfu.ru/Rezeda.Muhametshina'),
                                                            ('Пашкуров '
                                                             'Алексей '
                                                             'Николаевич',
                                                             'https://kpfu.ru/Aleksey.Pashkurov'),
                                                            ('Хабибуллина '
                                                             'Лилия '
                                                             'Фуатовна',
                                                             'https://kpfu.ru/Liliya.Habibullina'),
                                                            ('Шамина '
                                                             'Вера '
                                                             'Борисовна',
                                                             'https://kpfu.ru/Vera.Shamina'),
                                                            ('Аминева '
                                                             'Венера '
                                                             'Рудалевна',
                                                             'https://kpfu.ru/Venera.Amineva'),
                                                            ('Бекметов '
                                                             'Ринат '
                                                             'Ферганович',
                                                             'https://kpfu.ru/Rinat.Bekmetov'),
                                                            ('Бреева '
                                                             'Татьяна '
                                                             'Николаевна',
                                                             'https://kpfu.ru/Tatyana.Breeva'),
                                                            ('Галимуллина '
                                                             'Альфия '
                                                             'Фоатовна',
                                                             'https://kpfu.ru/Alfiya.Galimullina'),
                                                            ('Карасик '
                                                             'Ольга '
                                                             'Борисовна',
                                                             'https://kpfu.ru/Olga.Karasik'),
                                                            ('Скворцов '
                                                             'Артем '
                                                             'Эдуардович',
                                                             'https://kpfu.ru/Artem.Scvortsov'),
                                                            ('Афанасьев '
                                                             'Антон '
                                                             'Сергеевич',
                                                             'https://kpfu.ru/Anton.Afanasev'),
                                                            ('Вафина '
                                                             'Алсу '
                                                             'Хадиевна',
                                                             'https://kpfu.ru/Alsu.Vafina'),
                                                            ('Зиннатуллина '
                                                             'Зульфия '
                                                             'Рафисовна',
                                                             'https://kpfu.ru/Zulfiya.Zinnatullina'),
                                                            ('Махинина '
                                                             'Наталья '
                                                             'Георгиевна',
                                                             'https://kpfu.ru/Natalia.Mahinina'),
                                                            ('Нагуманова '
                                                             'Эльвира '
                                                             'Фирдавильевна',
                                                             'https://kpfu.ru/Elvira.Nagumanova'),
                                                            ('Насрутдинова '
                                                             'Лилия '
                                                             'Харисовна',
                                                             'https://kpfu.ru/Liliya.Nasroutdinova'),
                                                            ('Хабибуллина '
                                                             'Алсу '
                                                             'Зарифовна',
                                                             'https://kpfu.ru/Alsu.Habibullina'),
                                                            ('Зуева '
                                                             'Екатерина '
                                                             'Владимировна',
                                                             'https://kpfu.ru/Ekaterina.Zueva'),
                                                            ('Бакиров '
                                                             'Ринат '
                                                             'Альбертович',
                                                             'https://kpfu.ru/rinat.bakirov'),
                                                            ('Мирасова '
                                                             'Камила '
                                                             'Наиловна',
                                                             'https://kpfu.ru/kamila.mirasova'),
                                                            ('Мелихов '
                                                             'Алексей '
                                                             'Германович',
                                                             'https://kpfu.ru/aleksey.melikhov'),
                                                            ('Шевченко '
                                                             'Арина '
                                                             'Рафаильевна',
                                                             'https://kpfu.ru/arina.shevchenko'),
                                                            ('Щепачева '
                                                             'Инна '
                                                             'Владимировна',
                                                             'https://kpfu.ru/inna.schepacheva')],
                'Кафедра татаристики и культуроведения': [('Батыршина '
                                                           'Гульнара '
                                                           'Ибрагимовна',
                                                           'http://kpfu.ru/main?p_id=27885'),
                                                          ('Акбарова '
                                                           'Гульназ '
                                                           'Наилевна',
                                                           'https://kpfu.ru/Gulnaz.Akbarova'),
                                                          ('Ахмадуллина '
                                                           'Римма '
                                                           'Маратовна',
                                                           'http://kpfu.ru/main?p_id=27759'),
                                                          ('Сингх '
                                                           'Балвант',
                                                           'https://kpfu.ru/singkh.balvant'),
                                                          ('Блинова '
                                                           'Юлия '
                                                           'Лорэнсовна',
                                                           'http://kpfu.ru/Juliya.Blinova'),
                                                          ('Валиахметова '
                                                           'Нелли '
                                                           'Раисовна',
                                                           'http://kpfu.ru/main?p_id=27922'),
                                                          ('Гайнетдин '
                                                           'Дамира '
                                                           'Магсумовна',
                                                           'http://kpfu.ru/main?p_id=27980'),
                                                          ('Дыганова '
                                                           'Елена '
                                                           'Александровна',
                                                           'http://kpfu.ru/Elena.Dyganova'),
                                                          ('Камалова '
                                                           'Ильмира '
                                                           'Фуатовна',
                                                           'http://kpfu.ru/main?p_id=28425'),
                                                          ('Каркина '
                                                           'Светлана '
                                                           'Владимировна',
                                                           'http://kpfu.ru/main?p_id=28457'),
                                                          ('Мишина '
                                                           'Анастасия '
                                                           'Валентиновна',
                                                           'http://kpfu.ru/main?p_id=36719'),
                                                          ('Нургаянова '
                                                           'Неля '
                                                           'Хабибулловна',
                                                           'http://kpfu.ru/main?p_id=28838'),
                                                          ('Файзрахманова '
                                                           'Ляля '
                                                           'Тагировна',
                                                           'https://kpfu.ru/Lyalya.Fajzrahmanova'),
                                                          ('Фахрутдинова '
                                                           'Резида '
                                                           'Ахатовна',
                                                           'http://kpfu.ru/main?p_id=29468'),
                                                          ('Хабибулина '
                                                           'Лилия '
                                                           'Фэатовна',
                                                           'https://kpfu.ru/main?p_id=31091'),
                                                          ('Ялалов '
                                                           'Фарит '
                                                           'Габтелович',
                                                           'http://kpfu.ru/farit.yalalov'),
                                                          ('Гатауллина '
                                                           'Венера '
                                                           'Дамировна',
                                                           'https://kpfu.ru/main?p_id=28164'),
                                                          ('Ибрагимова '
                                                           'Зульфия '
                                                           'Ахметовна',
                                                           'https://kpfu.ru/1Zulfiya.Ibragimova'),
                                                          ('Ильяшенко '
                                                           'Николай '
                                                           'Васильевич',
                                                           'https://kpfu.ru/Nikolaj.Ilyashenko'),
                                                          ('Коварская '
                                                           'Маргарита '
                                                           'Яковлевна',
                                                           'https://kpfu.ru/main?p_id=28546'),
                                                          ('Красноперова '
                                                           'Вероника '
                                                           'Николаевна',
                                                           'https://kpfu.ru/veronika.krasnoperova'),
                                                          ('Яворский '
                                                           'Василий '
                                                           'Анатольевич',
                                                           'https://kpfu.ru/Vasilij.Yavorskij')],
                'Кафедра татарского языкознания': [('Галиуллина '
                                                    'Гульшат '
                                                    'Раисовна',
                                                    'https://kpfu.ru/Gulshat.Galiullina'),
                                                   ('Нуриева '
                                                    'Фануза '
                                                    'Шакуровна',
                                                    'https://kpfu.ru/Fenuze.Nurieva'),
                                                   ('Харисов '
                                                    'Фираз '
                                                    'Фахразович',
                                                    'https://kpfu.ru/Firaz.Harisov'),
                                                   ('Юсупов '
                                                    'Рузаль '
                                                    'Абдуллазянович',
                                                    'https://kpfu.ru/Ruzal.Jusupov'),
                                                   ('Кузьмина '
                                                    'Халиса '
                                                    'Хатиповна',
                                                    'https://kpfu.ru/Khalisa.Kuzmina'),
                                                   ('Сагдиева '
                                                    'Рамиля '
                                                    'Камиловна',
                                                    'https://kpfu.ru/Ramilya.Sagdieva'),
                                                   ('Хадиева '
                                                    'Гульфия '
                                                    'Камиловна',
                                                    'https://kpfu.ru/Gulfiya.Khadieva'),
                                                   ('Хуснутдинов '
                                                    'Дамир '
                                                    'Хайдарович',
                                                    'https://kpfu.ru/Damir.Husnutdinov'),
                                                   ('Юсупов '
                                                    'Айрат '
                                                    'Фаикович',
                                                    'https://kpfu.ru/Ajrat.Jusupov'),
                                                   ('Шакирова '
                                                    'Гульнара '
                                                    'Расиховна',
                                                    'https://kpfu.ru/Gulnara.Shakirova')],
                'Кафедра татарской литературы': [('Сайфулина '
                                                  'Флера '
                                                  'Сагитовна ',
                                                  '\t'
                                                  'http://kpfu.ru/Flera.Sajfulina\t'),
                                                 ('Миннегулов '
                                                  'Хатип '
                                                  'Юсупович ',
                                                  'https://kpfu.ru/main?p_id=10793'),
                                                 ('Галимуллин '
                                                  'Фоат '
                                                  'Галимуллинович',
                                                  '\t'
                                                  'http://kpfu.ru/Foat.Galimullin\t'),
                                                 ('Мингазова '
                                                  'Ляйля '
                                                  'Ихсановна',
                                                  '\t'
                                                  'http://kpfu.ru/Lyajlya.Mingazova\t'),
                                                 ('Юсупова '
                                                  'Нурфия '
                                                  'Марсовна ',
                                                  '\t'
                                                  'http://kpfu.ru/Nurfija.Jusupova\t'),
                                                 ('Гайнуллина '
                                                  'Гульфия '
                                                  'Расилевна',
                                                  '\t'
                                                  'http://kpfu.ru/Gulfia.Gaynyllina\t'),
                                                 ('Гилазов '
                                                  'Тагир '
                                                  'Шамсегалиевич ',
                                                  '\t'
                                                  'http://kpfu.ru/Tagir.Gilazov\t'),
                                                 ('Хабутдинова '
                                                  'Милеуша '
                                                  'Мухаметзяновна ',
                                                  '\t'
                                                  'http://kpfu.ru/Mileusha.Habutdinova\t'),
                                                 ('Замалиева '
                                                  'Луиза '
                                                  'Фирдусовна',
                                                  '\t'
                                                  'http://kpfu.ru/Luiza.Zamalieva\t'),
                                                 ('Каюмова '
                                                  'Гелюса '
                                                  'Фаридовна',
                                                  'https://kpfu.ru/main?p_id=28073')],
                'Кафедра теории и практики преподавания иностранных языков': [('Гафиятова '
                                                                               'Эльзара '
                                                                               'Василовна',
                                                                               'https://kpfu.ru/Elzara.Gafiyatova'),
                                                                              ('Давлетбаева '
                                                                               'Диана '
                                                                               'Няилевна',
                                                                               'https://kpfu.ru/Diana.Davletbaeva'),
                                                                              ('Каюмова '
                                                                               'Диана '
                                                                               'Фердинандовна',
                                                                               'https://kpfu.ru/Diana.Kajumova'),
                                                                              ('Кулькова '
                                                                               'Мария '
                                                                               'Александровна',
                                                                               'https://kpfu.ru/Mariya.Kulkova'),
                                                                              ('Садыкова '
                                                                               'Аида '
                                                                               'Гумеровна',
                                                                               'https://kpfu.ru/Aida.Sadykova'),
                                                                              ('Солнышкина '
                                                                               'Марина '
                                                                               'Ивановна',
                                                                               'https://kpfu.ru/Marina.Solnyshkina'),
                                                                              ('Васильева '
                                                                               'Валентина '
                                                                               'Николаевна',
                                                                               'https://kpfu.ru/Valentina.Vasileva'),
                                                                              ('Алеева '
                                                                               'Гульнара '
                                                                               'Халирахмановна',
                                                                               'https://kpfu.ru/Gulnara.Aleeva'),
                                                                              ('Гильмутдинова '
                                                                               'Айгуль '
                                                                               'Раисовна',
                                                                               'https://kpfu.ru/Ajgul.Gilmutdinova'),
                                                                              ('Мерзлякова '
                                                                               'Амина '
                                                                               'Фариковна\u200b',
                                                                               'https://kpfu.ru/amina.merzlyakova'),
                                                                              ('Зарипова '
                                                                               'Зарема '
                                                                               'Мухтаровна',
                                                                               'https://kpfu.ru/Zarema.Zaripova'),
                                                                              ('Каримова '
                                                                               'Анна '
                                                                               'Анатольевна',
                                                                               'https://kpfu.ru/1Anna.Karimova'),
                                                                              ('Назарова '
                                                                               'Гульнара '
                                                                               'Ильсуровна',
                                                                               'https://kpfu.ru/Gulnara.Nazarova'),
                                                                              ('Низамиева '
                                                                               'Лилия '
                                                                               'Рафхатовна',
                                                                               'https://kpfu.ru/Liliya.Nizamieva'),
                                                                              ('Остроумова '
                                                                               'Ольга '
                                                                               'Федоровна',
                                                                               'https://kpfu.ru/Olga.Ostroumova'),
                                                                              ('Рахимова '
                                                                               'Алина '
                                                                               'Эдуардовна',
                                                                               'https://kpfu.ru/Alina.Rahimova'),
                                                                              ('Кузнецова '
                                                                               'Ирина '
                                                                               'Алексеевна',
                                                                               'https://kpfu.ru/main?p_id=40013&p_lang=&p_type=1'),
                                                                              ('Харькова '
                                                                               'Елена '
                                                                               'Владимировна',
                                                                               'https://kpfu.ru/Elena.Harkova'),
                                                                              ('Хасанова '
                                                                               'Оксана '
                                                                               'Владимировна',
                                                                               'https://kpfu.ru/Oksana.Hasanova'),
                                                                              ('Яшина '
                                                                               'Марианна '
                                                                               'Евгеньевна',
                                                                               'https://kpfu.ru/Marianna.Yashina'),
                                                                              ('Андрианова '
                                                                               'Наталия '
                                                                               'Сергеевна',
                                                                               'https://kpfu.ru/nataliya.andrianova'),
                                                                              ('Денисова '
                                                                               'Елена '
                                                                               'Александровна',
                                                                               'https://kpfu.ru/main?p_id=41245'),
                                                                              ('Максимова '
                                                                               'Юлия '
                                                                               'Олеговна',
                                                                               'https://kpfu.ru/main?p_id=48434&p_lang=&p_type=1'),
                                                                              ('Маланчева '
                                                                               'Оксана '
                                                                               'Олеговна',
                                                                               'https://kpfu.ru/main?p_id=47527&p_lang=&p_type=1'),
                                                                              ('Тулусина '
                                                                               'Елена '
                                                                               'Антоновна',
                                                                               'https://kpfu.ru/Elena.Tulusina'),
                                                                              ('Струкова '
                                                                               'Александра '
                                                                               'Владимировна',
                                                                               'https://kpfu.ru/main?p_id=42756&p_lang=&p_type=1'),
                                                                              ('Шемшуренко '
                                                                               'Оксана '
                                                                               'Владимировна',
                                                                               'https://kpfu.ru/Oksana.Shemshurenko'),
                                                                              ('Галеева '
                                                                               'Гульнара '
                                                                               'Ирековна',
                                                                               'https://kpfu.ru/Gulnara.Galeeva'),
                                                                              ('Мингазова '
                                                                               'Раушания '
                                                                               'Разуловна',
                                                                               'https://kpfu.ru/Raushaniya.Mingazova'),
                                                                              ('Сафин '
                                                                               'Ильдар '
                                                                               'Хамзович',
                                                                               'https://kpfu.ru/Ildar.Safin'),
                                                                              ('Башкирова '
                                                                               'Карина '
                                                                               'Александровна',
                                                                               'https://kpfu.ru/karina.bashkirova'),
                                                                              ('Гатиятуллина '
                                                                               'Галия '
                                                                               'Маратовна',
                                                                               'https://kpfu.ru/galiya.gatiyatullina'),
                                                                              ('Мухамадьярова '
                                                                               'Альбина '
                                                                               'Фанилевна',
                                                                               'https://kpfu.ru/albina.muhamadyarova'),
                                                                              ('Ройтер '
                                                                               'Кирстен\xa0',
                                                                               'https://kpfu.ru/kirsten.rojter'),
                                                                              ('Павлова '
                                                                               'Юлия '
                                                                               'Игоревна\xa0',
                                                                               'https://kpfu.ru/yuliya.pavlova'),
                                                                              ('Гатиятуллина '
                                                                               'Лиана '
                                                                               'Фаргатовна\xa0',
                                                                               'https://kpfu.ru/liana.gatiyatullina'),
                                                                              ('Коноплева '
                                                                               'Наталья '
                                                                               'Вячеславовна',
                                                                               'https://kpfu.ru/main?p_id=11051'),
                                                                              ('Галиханова '
                                                                               'Фарзания '
                                                                               'Ульмасовна',
                                                                               'https://kpfu.ru/main?p_id=42009'),
                                                                              ('Мартынова '
                                                                               'Екатерина '
                                                                               'Владимировна',
                                                                               'https://kpfu.ru/main?p_id=40572'),
                                                                              ('Низамиев '
                                                                               'Рустам '
                                                                               'Асхатович',
                                                                               'https://kpfu.ru/rustam.nizamiev'),
                                                                              ('Булина '
                                                                               'Евгения '
                                                                               'Николаевна',
                                                                               'https://kpfu.ru/main?p_id=46413'),
                                                                              ('Кудрявцева '
                                                                               'Елена '
                                                                               'Анатольевна',
                                                                               'https://kpfu.ru/elena.kudryavceva'),
                                                                              ('Другов '
                                                                               'Артём '
                                                                               'Викторович',
                                                                               'https://kpfu.ru/artyom.drugov'),
                                                                              ('Герасимова '
                                                                               'Екатерина '
                                                                               'Сергеевна',
                                                                               'https://kpfu.ru/main?p_id=48769&p_lang=&p_type=1'),
                                                                              ('Буслаева '
                                                                               'Тамила '
                                                                               'Хабировна',
                                                                               'https://kpfu.ru/main?p_id=48522&p_lang=&p_type=1'),
                                                                              ('Кузнецова '
                                                                               'Ирина '
                                                                               'Алексеевна',
                                                                               'https://kpfu.ru/main?p_id=40013'),
                                                                              ('Павлова '
                                                                               'Юлия '
                                                                               'Игоревна\u200b',
                                                                               'https://kpfu.ru/main?p_id=46433&p_lang=&p_type=1'),
                                                                              ('Марико '
                                                                               'Мохамед '
                                                                               'Ламин',
                                                                               'https://kpfu.ru/mokhamed.mariko'),
                                                                              ('Шелестова '
                                                                               'Ольга '
                                                                               'Вадимовна',
                                                                               'https://kpfu.ru/Olga.Shelestova'),
                                                                              ('',
                                                                               'https://kpfu.ru/mokhamed.mariko'),
                                                                              ('',
                                                                               'https://kpfu.ru/mokhamed.mariko')],
                'Кафедра языковой и межкультурной коммуникации': [('Ашрапова '
                                                                   'Алсу '
                                                                   'Халиловна',
                                                                   'https://kpfu.ru/Alsu.Ashrapova'),
                                                                  ('Садыкова '
                                                                   'Гульнара '
                                                                   'Василевна',
                                                                   'https://kpfu.ru/Gulnara.Sadykova'),
                                                                  ('Сайфулина '
                                                                   'Нафиля '
                                                                   'Шакирчановна',
                                                                   'https://kpfu.ru/nafilya.sayfullina'),
                                                                  ('Сафиуллина '
                                                                   'Гульшат '
                                                                   'Рафаилевна',
                                                                   'https://kpfu.ru/Gulshat.Safiullina'),
                                                                  ('Свирина '
                                                                   'Людмила '
                                                                   'Олеговна',
                                                                   'https://kpfu.ru/Ljudmila.Svirina'),
                                                                  ('Халитова '
                                                                   'Лилия '
                                                                   'Камилевна',
                                                                   'https://kpfu.ru/Liliya.Halitova'),
                                                                  ('Шаяхметова '
                                                                   'Лейсан '
                                                                   'Хабировна',
                                                                   'https://kpfu.ru/Lejsan.Shayahmetova'),
                                                                  ('Закирова '
                                                                   'Роза '
                                                                   'Рафаиловна',
                                                                   'https://kpfu.ru/rozar.zakirova'),
                                                                  ('Мухарлямова '
                                                                   'Лилия '
                                                                   'Рашидовна',
                                                                   'https://kpfu.ru/Liliya.Muharlyamova'),
                                                                  ('Шакирова '
                                                                   'Гульнара '
                                                                   'Расиховна',
                                                                   'https://kpfu.ru/Gulnara.Shakirova'),
                                                                  ('Безуглова '
                                                                   'Ольга '
                                                                   'Андреевна',
                                                                   'https://kpfu.ru/olga.bezuglova'),
                                                                  ('Габитова '
                                                                   'Лилия '
                                                                   'Хабировна',
                                                                   'https://kpfu.ru/liliya.shayahmetova'),
                                                                  ('Ильясова '
                                                                   'Лилия '
                                                                   'Галиевна',
                                                                   'https://kpfu.ru/liliya.ilyasova'),
                                                                  ('Нигматуллина '
                                                                   'Алина '
                                                                   'Фасировна',
                                                                   'https://kpfu.ru/alina.nigmatullina'),
                                                                  ('Важорова '
                                                                   'Евгения '
                                                                   'Валерьевна',
                                                                   'https://kpfu.ru/evgeniya.vazhorova'),
                                                                  ('Ван '
                                                                   'Синчан ',
                                                                   'https://kpfu.ru/sinchan.van'),
                                                                  ('Галиуллина '
                                                                   'Лиана '
                                                                   'Ильдаровна',
                                                                   'https://kpfu.ru/liana.galiullina'),
                                                                  ('Замалетдинова '
                                                                   'Гулюса '
                                                                   'Рафаэлевна',
                                                                   'https://kpfu.ru/guljusa.zamaletdinova'),
                                                                  ('Хасанзянова '
                                                                   'Гульнара '
                                                                   'Илгизовна',
                                                                   'https://kpfu.ru/gulnara.hasanzyanova')]},
            'Институт экологии и природопользования': {'Кафедра ландшафтной экологии': [('Мальцев '
                                                                                         'Кирилл '
                                                                                         'Александрович',
                                                                                         'https://kpfu.ru/Kirill.Malcev'),
                                                                                        ('Ермолаев '
                                                                                         'Олег '
                                                                                         'Петрович',
                                                                                         'https://kpfu.ru/Oleg.Yermolaev'),
                                                                                        ('Сироткин '
                                                                                         'Вячеслав '
                                                                                         'Владимирович',
                                                                                         'https://kpfu.ru/Vyacheslav.Sirotkin'),
                                                                                        ('Куржанова '
                                                                                         'Анна '
                                                                                         'Алексеевна',
                                                                                         'https://kpfu.ru/Anna.Kurzhanova'),
                                                                                        ('Сафина '
                                                                                         'Гузель '
                                                                                         'Рашитовна',
                                                                                         'https://kpfu.ru/Guzel.Safina'),
                                                                                        ('Федорова '
                                                                                         'Виктория '
                                                                                         'Алексеевна',
                                                                                         'https://kpfu.ru/1Victoria.Fedorova'),
                                                                                        ('Гайнутдинова '
                                                                                         'Гульшат '
                                                                                         'Флюровна',
                                                                                         'https://kpfu.ru/gulshat.gajnutdinova'),
                                                                                        ('Двинских '
                                                                                         'Александр '
                                                                                         'Петрович',
                                                                                         'https://kpfu.ru/Aleksandr.Dvinskih'),
                                                                                        ('Иванов '
                                                                                         'Максим '
                                                                                         'Андреевич',
                                                                                         'https://kpfu.ru/Maksim.Ivanov'),
                                                                                        ('Петрова '
                                                                                         'Елена '
                                                                                         'Витальевна',
                                                                                         'https://kpfu.ru/1Elena.Petrova'),
                                                                                        ('Шарифуллин '
                                                                                         'Айдар '
                                                                                         'Гамисович',
                                                                                         'https://kpfu.ru/ajdar.sharifullin'),
                                                                                        ('Усманов '
                                                                                         'Булат '
                                                                                         'Мансурович',
                                                                                         'https://kpfu.ru/Bulat.Usmanoff'),
                                                                                        ('Гафуров '
                                                                                         'Артур '
                                                                                         'Маратович',
                                                                                         'https://kpfu.ru/artur.gafurov'),
                                                                                        ('Хайруллина '
                                                                                         'Динара '
                                                                                         'Николаевна',
                                                                                         'https://kpfu.ru/Dinara.Hajrullina'),
                                                                                        ('Хомяков '
                                                                                         'Петр '
                                                                                         'Валериевич',
                                                                                         'https://kpfu.ru/Petr.Khomyakov'),
                                                                                        ('Аввакумова '
                                                                                         'Алина '
                                                                                         'Олеговна',
                                                                                         'https://kpfu.ru/Alina.Avvakumova'),
                                                                                        ('Медведева '
                                                                                         'Регина '
                                                                                         'Азатовна',
                                                                                         'https://kpfu.ru/regina.gajfutdinova')],
                                                       'Кафедра метеорологии, климатологии и экологии атмосферы': [
                                                           ('Переведенцев '
                                                            'Юрий '
                                                            'Петрович',
                                                            'https://kpfu.ru/Yuri.Perevedentsev'),
                                                           ('Гурьянов '
                                                            'Владимир '
                                                            'Владимирович',
                                                            'https://kpfu.ru/Vladimir.Guryanov'),
                                                           ('Исмагилов '
                                                            'Наиль '
                                                            'Вагизович',
                                                            'https://kpfu.ru/1Nail.Ismagilov'),
                                                           ('Мирсаева '
                                                            'Надежда '
                                                            'Александровна',
                                                            'https://kpfu.ru/Nadezhda.Vazhnova'),
                                                           ('Николаев '
                                                            'Александр '
                                                            'Анатольевич',
                                                            'https://kpfu.ru/Aleksandr.Nikolaev'),
                                                           ('Шанталинский '
                                                            'Константин '
                                                            'Михайлович',
                                                            'https://kpfu.ru/Konstantin.Shantalinsky'),
                                                           ('Аухадеев '
                                                            'Тимур '
                                                            'Ринатович',
                                                            'https://kpfu.ru/timur.auhadeev'),
                                                           ('Сабирова '
                                                            'Марина '
                                                            'Валериевна',
                                                            'https://kpfu.ru/1Marina.Isaeva'),
                                                           ('Антонова '
                                                            'Альбина '
                                                            'Владимировна',
                                                            'https://kpfu.ru/albina.antonova'),
                                                           ('Арсланова '
                                                            'Зарина '
                                                            'Ленаровна',
                                                            'https://kpfu.ru/zarina.arslanova')],
                                                       'Кафедра моделирования экологических систем': [('Зарипов '
                                                                                                       'Шамиль '
                                                                                                       'Хузеевич',
                                                                                                       'https://kpfu.ru/Shamil.Zaripov'),
                                                                                                      ('Савельев '
                                                                                                       'Анатолий '
                                                                                                       'Александрович',
                                                                                                       'https://kpfu.ru/Anatoly.Saveliev'),
                                                                                                      ('Мухарамова '
                                                                                                       'Светлана '
                                                                                                       'Саясовна',
                                                                                                       'https://kpfu.ru/Svetlana.Mukharamova'),
                                                                                                      ('Гильфанов '
                                                                                                       'Артур '
                                                                                                       'Камилевич',
                                                                                                       'https://kpfu.ru/Artur.Gilfanov'),
                                                                                                      ('Никоненкова '
                                                                                                       'Татьяна '
                                                                                                       'Владимировна',
                                                                                                       'https://kpfu.ru/Tatjna.Nikonenkova'),
                                                                                                      ('Чижикова '
                                                                                                       'Нелли '
                                                                                                       'Александровна',
                                                                                                       'https://kpfu.ru/Nelly.Chizhikova'),
                                                                                                      ('Пилюгин '
                                                                                                       'Александр '
                                                                                                       'Геннадиевич',
                                                                                                       'https://kpfu.ru/Alexander.Piliouguine'),
                                                                                                      ('Марданова '
                                                                                                       'Александра '
                                                                                                       'Евгеньевна',
                                                                                                       'https://kpfu.ru/aleksandra.mardanova'),
                                                                                                      ('Газизова '
                                                                                                       'Светлана '
                                                                                                       'Евгеньевна',
                                                                                                       'https://kpfu.ru/svetlana.gazizova'),
                                                                                                      ('Залялетдинова '
                                                                                                       'Розалия '
                                                                                                       'Фаридовна',
                                                                                                       'https://kpfu.ru/Rozalia.Zalialetdinova')],
                                                       'Кафедра общей экологии': [('Рогова '
                                                                                   'Татьяна '
                                                                                   'Владимировна',
                                                                                   'https://kpfu.ru/Tatiana.Rogova'),
                                                                                  ('Фардеева '
                                                                                   'Марина '
                                                                                   'Борисовна',
                                                                                   'https://kpfu.ru/Marina.Fardeeva'),
                                                                                  ('Шайхутдинова '
                                                                                   'Галия '
                                                                                   'Адхатовна',
                                                                                   'https://kpfu.ru/Galiya.Shaykhutdinova'),
                                                                                  ('Прохоров '
                                                                                   'Вадим '
                                                                                   'Евгеньевич',
                                                                                   'https://kpfu.ru/Vadim.Prokhorov'),
                                                                                  ('Тишин '
                                                                                   'Денис '
                                                                                   'Владимирович',
                                                                                   'https://kpfu.ru/Denis.Tishin'),
                                                                                  ('Шафигуллина '
                                                                                   'Надия '
                                                                                   'Рустэмовна',
                                                                                   'https://kpfu.ru/Nadiya.Shafigullina'),
                                                                                  ('Потапов '
                                                                                   'Ким '
                                                                                   'Олегович',
                                                                                   'https://kpfu.ru/Kim.Potapov'),
                                                                                  ('Кочанов '
                                                                                   'Михаил '
                                                                                   'Алексеевич',
                                                                                   'https://kpfu.ru/Michail.Kochanov'),
                                                                                  ('Короткова '
                                                                                   'Галина '
                                                                                   'Георгиевна',
                                                                                   'https://kpfu.ru/Galina.Korotkova'),
                                                                                  ('Сауткин '
                                                                                   'Илья '
                                                                                   'Сергеевич',
                                                                                   'https://kpfu.ru/ilya.sautkin')],
                                                       'Кафедра почвоведения': [('Смирнова '
                                                                                 'Елена '
                                                                                 'Васильевна',
                                                                                 'https://kpfu.ru/Elena.Smirnova'),
                                                                                ('Ковалева '
                                                                                 'Наталия '
                                                                                 'Олеговна',
                                                                                 'https://kpfu.ru/nataliya.kovaleva'),
                                                                                ('Гиниятуллин '
                                                                                 'Камиль '
                                                                                 'Гашикович',
                                                                                 'https://kpfu.ru/Kamil.Ginijatullin'),
                                                                                ('Александрова '
                                                                                 'Асель '
                                                                                 'Биляловна',
                                                                                 'https://kpfu.ru/asel.aleksandrova'),
                                                                                ('Ибатуллина '
                                                                                 'Римма '
                                                                                 'Петровна',
                                                                                 'https://kpfu.ru/rimma.ibatullina'),
                                                                                ('Кожевникова '
                                                                                 'Мария '
                                                                                 'Владимировна',
                                                                                 'https://kpfu.ru/mariya.kozhevnikova'),
                                                                                ('Окунев '
                                                                                 'Родион '
                                                                                 'Владимирович',
                                                                                 'https://kpfu.ru/rodion.okunev'),
                                                                                ('Рыжих '
                                                                                 'Людмила '
                                                                                 'Юрьевна',
                                                                                 'https://kpfu.ru/ljudmila.ryzhih'),
                                                                                ('Сахабиев '
                                                                                 'Ильназ '
                                                                                 'Алимович',
                                                                                 'https://kpfu.ru/ilnaz.sahabiev'),
                                                                                ('Кадырова '
                                                                                 'Резеда '
                                                                                 'Габдулловна',
                                                                                 'https://kpfu.ru/Rezeda.Kadyrova'),
                                                                                ('Гордеева '
                                                                                 'Карина '
                                                                                 'Андреевна',
                                                                                 'https://kpfu.ru/karina.gordeeva'),
                                                                                ('Гусманова '
                                                                                 'Альфия '
                                                                                 'Кирамовна',
                                                                                 'https://kpfu.ru/alfiya.gusmanova'),
                                                                                ('Латыпова '
                                                                                 'Лейсан '
                                                                                 'Илдаровна',
                                                                                 'https://kpfu.ru/lejsan.latypova')],
                                                       'Кафедра прикладной экологии': [('Зобов '
                                                                                        'Владимир '
                                                                                        'Васильевич',
                                                                                        'https://kpfu.ru/Vladimir.Zobov'),
                                                                                       ('Латыпова '
                                                                                        'Венера '
                                                                                        'Зиннатовна',
                                                                                        'https://kpfu.ru/Venera.Latipova'),
                                                                                       ('Мукминов '
                                                                                        'Малик '
                                                                                        'Нилович',
                                                                                        'https://kpfu.ru/malikn.mukminov'),
                                                                                       ('Селивановская '
                                                                                        'Светлана '
                                                                                        'Юрьевна',
                                                                                        'https://kpfu.ru/Svetlana.Selivanovskaya'),
                                                                                       ('Степанова '
                                                                                        'Надежда '
                                                                                        'Юльевна',
                                                                                        'https://kpfu.ru/Nadezhda.Stepanova'),
                                                                                       ('Галицкая '
                                                                                        'Полина '
                                                                                        'Юрьевна',
                                                                                        'https://kpfu.ru/Polina.Galitskaya'),
                                                                                       ('Шагидуллина '
                                                                                        'Раиса '
                                                                                        'Абдулловна',
                                                                                        'https://kpfu.ru/raisa.shagidullina'),
                                                                                       ('Бадрутдинов '
                                                                                        'Олег '
                                                                                        'Рауфович',
                                                                                        'https://kpfu.ru/Oleg.Badrutdinov'),
                                                                                       ('Никитин '
                                                                                        'Олег '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/Oleg.Nikitin'),
                                                                                       ('Шуралев '
                                                                                        'Эдуард '
                                                                                        'Аркадьевич',
                                                                                        'https://kpfu.ru/Eaduard.Shuralev'),
                                                                                       ('Валеева '
                                                                                        'Гузель '
                                                                                        'Равильевна',
                                                                                        'https://kpfu.ru/Guzel.Valeeva'),
                                                                                       ('Курынцева '
                                                                                        'Полина '
                                                                                        'Александровна',
                                                                                        'https://kpfu.ru/polina.zvereva'),
                                                                                       ('Ахметзянова '
                                                                                        'Лейсан '
                                                                                        'Габбасовна',
                                                                                        'https://kpfu.ru/Leisan.Ahmetzyanova'),
                                                                                       ('Гайфутдинова '
                                                                                        'Наиля '
                                                                                        'Равилевна',
                                                                                        'https://kpfu.ru/nailya.gajfutdinova'),
                                                                                       ('Новикова '
                                                                                        'Людмила '
                                                                                        'Викторовна',
                                                                                        'https://kpfu.ru/Ljudmila.Gureva'),
                                                                                       ('Мальцева '
                                                                                        'Татьяна '
                                                                                        'Сергеевна',
                                                                                        'https://kpfu.ru/tatyana.elkina'),
                                                                                       ('Сабанаев '
                                                                                        'Руслан '
                                                                                        'Николаевич',
                                                                                        'https://kpfu.ru/ruslan.sabanaev'),
                                                                                       ('Салихов '
                                                                                        'Дамир '
                                                                                        'Габдульбарович',
                                                                                        'https://kpfu.ru/damir.salikhov')]},
            'Набережночелнинский институт КФУ': {'кафедра автоматизации и управления': [('Симонова '
                                                                                         'Лариса '
                                                                                         'Анатольевна',
                                                                                         'https://kpfu.ru/larisa.simonova'),
                                                                                        ('Ганиев '
                                                                                         'Махмут '
                                                                                         'Масхутович',
                                                                                         'https://kpfu.ru/mahmut.ganiev'),
                                                                                        ('Абрамова '
                                                                                         'Вера '
                                                                                         'Викторовна',
                                                                                         'https://kpfu.ru/vera.abramova'),
                                                                                        ('Балабанов '
                                                                                         'Игорь '
                                                                                         'Петрович',
                                                                                         'https://kpfu.ru/igor.balabanov'),
                                                                                        ('Валиахметов '
                                                                                         'Равиль '
                                                                                         'Рафкатович',
                                                                                         'https://kpfu.ru/ravil.valiahmetov'),
                                                                                        ('Гумерова '
                                                                                         'Лилия '
                                                                                         'Зуфаровна',
                                                                                         'https://kpfu.ru/liliya.gumerova'),
                                                                                        ('Заморский '
                                                                                         'Валерий '
                                                                                         'Валентинович',
                                                                                         'https://kpfu.ru/valerij.zamorskij'),
                                                                                        ('Зиятдинов '
                                                                                         'Рустем '
                                                                                         'Раисович',
                                                                                         'https://kpfu.ru/rustem.ziyatdinov'),
                                                                                        ('Лукьянова '
                                                                                         'Ангелина '
                                                                                         'Викторовна',
                                                                                         'https://kpfu.ru/angelina.lukyanova'),
                                                                                        ('Романовский '
                                                                                         'Эдуард '
                                                                                         'Анатольевич',
                                                                                         'https://kpfu.ru/eduard.romanovskij'),
                                                                                        ('Шабаев '
                                                                                         'Александр '
                                                                                         'Аликович',
                                                                                         'https://kpfu.ru/aleksandr.shabaev'),
                                                                                        ('Сабиров '
                                                                                         'Ильдар '
                                                                                         'Салихзянович',
                                                                                         'https://kpfu.ru/ildar.sabirov'),
                                                                                        ('Гильман '
                                                                                         'Виталий '
                                                                                         'Николаевич',
                                                                                         'https://kpfu.ru/vitaliy.gilman'),
                                                                                        ('Хайдарова '
                                                                                         'Глуса '
                                                                                         'Васильевна',
                                                                                         'https://kpfu.ru/glusa.hajdarova'),
                                                                                        ('Газетдинов '
                                                                                         'Фидаэл '
                                                                                         'Миргаязович',
                                                                                         'https://kpfu.ru/main?p_id=34128'),
                                                                                        ('Тимофеева '
                                                                                         'Татьяна '
                                                                                         'Сергеевна',
                                                                                         'https://kpfu.ru/tatyana.timofeeva')],
                                                 'кафедра автомобилей, автомобильных двигателей и дизайна': [
                                                     ('Дмитриев '
                                                      'Сергей '
                                                      'Васильевич',
                                                      'https://kpfu.ru/sergej.dmitriev'),
                                                     ('Никишин '
                                                      'Вячеслав '
                                                      'Николаевич',
                                                      'https://kpfu.ru/vyacheslav.nikishin'),
                                                     ('Акимов '
                                                      'Владимир '
                                                      'Яковлевич',
                                                      'https://kpfu.ru/vladimir.akimov'),
                                                     ('Басыров '
                                                      'Руслан '
                                                      'Рамилевич',
                                                      'https://kpfu.ru/ruslan.basyrov'),
                                                     ('Мавлеев '
                                                      'Ильдус '
                                                      'Рифович',
                                                      'https://kpfu.ru/ildus.mavleev'),
                                                     ('Павленко '
                                                      'Алексей '
                                                      'Петрович',
                                                      'https://kpfu.ru/aleksej.pavlenko'),
                                                     ('Румянцев '
                                                      'Валерий '
                                                      'Владимирович',
                                                      'https://kpfu.ru/valerij.rumyancev'),
                                                     ('Салахов '
                                                      'Ильдар '
                                                      'Ильгизарович',
                                                      'https://kpfu.ru/ildar.salahov'),
                                                     ('Шамсутдинов '
                                                      'Ильдар '
                                                      'Рафисович',
                                                      'https://kpfu.ru/ildar.shamsutdinov'),
                                                     ('Валеев '
                                                      'Данис '
                                                      'Хадиевич',
                                                      'https://kpfu.ru/danis.valeev'),
                                                     ('Валеев '
                                                      'Игорь '
                                                      'Данисович',
                                                      'https://kpfu.ru/igor.valeev'),
                                                     ('Лущеко '
                                                      'Василий '
                                                      'Александрович',
                                                      'https://kpfu.ru/vasilij.lushheko'),
                                                     ('Хлюпин '
                                                      'Виктор '
                                                      'Борисович',
                                                      'https://kpfu.ru/viktor.hljupin'),
                                                     ('Анютина '
                                                      'Галина '
                                                      'Павловна',
                                                      'https://kpfu.ru/galina.anjutina'),
                                                     ('Ахметова '
                                                      'Альбина '
                                                      'Маратовна',
                                                      'https://kpfu.ru/albinam.ahmetova'),
                                                     ('Лоншакова '
                                                      'Марина '
                                                      'Михайловна',
                                                      'https://kpfu.ru/marina.lonshakova'),
                                                     ('Валеев '
                                                      'Нияз '
                                                      'Рашитович',
                                                      'https://kpfu.ru/niyaz.valeev'),
                                                     ('Ханнанов '
                                                      'Марат '
                                                      'Дамирович',
                                                      'https://kpfu.ru/marat.khannanov'),
                                                     ('Хасанов '
                                                      'Альберт '
                                                      'Абелхалилович',
                                                      'https://kpfu.ru/albert.khasanov'),
                                                     ('Мухамедзянова '
                                                      'Гульсина '
                                                      'Ясавеевна',
                                                      'https://kpfu.ru/gulsina.muhamedzyanova')],
                                                 'кафедра бизнес информатики и математических методов в экономике': [
                                                     ('Павликов '
                                                      'Сергей '
                                                      'Владимирович',
                                                      'https://kpfu.ru/sergej.pavlikov'),
                                                     ('Розенцвайг '
                                                      'Александр '
                                                      'Куртович',
                                                      'https://kpfu.ru/aleksandr.rozencvajg'),
                                                     ('Еремина '
                                                      'Ирина '
                                                      'Ильинична',
                                                      'https://kpfu.ru/irina.eremina'),
                                                     ('Лысанов '
                                                      'Денис '
                                                      'Михайлович',
                                                      'https://kpfu.ru/denis.lysanov'),
                                                     ('Ишмурадова '
                                                      'Изида '
                                                      'Илдаровна',
                                                      'https://kpfu.ru/izida.ishmuradova'),
                                                     ('Фархутдинов '
                                                      'Ильнур '
                                                      'Илдусович',
                                                      'https://kpfu.ru/ilnur.farhutdinov')],
                                                 'кафедра высокоэнергетических процессов и агрегатов': [('Исрафилов '
                                                                                                         'Ирек '
                                                                                                         'Хуснемарданович',
                                                                                                         'https://kpfu.ru/irek.israfilov'),
                                                                                                        ('Кузнецов '
                                                                                                         'Борис '
                                                                                                         'Леонидович',
                                                                                                         'https://kpfu.ru/boris.kuznecov'),
                                                                                                        ('Звездин '
                                                                                                         'Валерий '
                                                                                                         'Васильевич',
                                                                                                         'https://kpfu.ru/valerij.zvezdin'),
                                                                                                        ('Алеев '
                                                                                                         'Рафиль '
                                                                                                         'Мухтарович',
                                                                                                         'https://kpfu.ru/rafil.aleev'),
                                                                                                        ('Болдырев '
                                                                                                         'Алексей '
                                                                                                         'Владимирович',
                                                                                                         'https://kpfu.ru/aleksej.boldyrev'),
                                                                                                        ('Волков '
                                                                                                         'Денис '
                                                                                                         'Александрович',
                                                                                                         'https://kpfu.ru/denis.volkov'),
                                                                                                        ('Габдрахманов '
                                                                                                         'Азат '
                                                                                                         'Талгатович',
                                                                                                         'https://kpfu.ru/azat.gabdrahmanov'),
                                                                                                        ('Галиакбаров '
                                                                                                         'Азат '
                                                                                                         'Талгатович',
                                                                                                         'https://kpfu.ru/azat.galiakbarov'),
                                                                                                        ('Гумеров '
                                                                                                         'Азат '
                                                                                                         'Флорович',
                                                                                                         'https://kpfu.ru/azat.gumerov'),
                                                                                                        ('Исрафилов '
                                                                                                         'Данис '
                                                                                                         'Ирекович',
                                                                                                         'https://kpfu.ru/danis.israfilov'),
                                                                                                        ('Карелин '
                                                                                                         'Дмитрий '
                                                                                                         'Леонидович',
                                                                                                         'https://kpfu.ru/dmitrij.karelin'),
                                                                                                        ('Болдырев '
                                                                                                         'Сергей '
                                                                                                         'Владимирович',
                                                                                                         'https://kpfu.ru/sergej.boldyrev'),
                                                                                                        ('Портнов '
                                                                                                         'Сергей '
                                                                                                         'Михайлович',
                                                                                                         'https://kpfu.ru/sergej.portnov'),
                                                                                                        ('Саубанов '
                                                                                                         'Рузиль '
                                                                                                         'Рашитович',
                                                                                                         'https://kpfu.ru/ruzil.saubanov'),
                                                                                                        ('Арсланов '
                                                                                                         'Ильяс '
                                                                                                         'Миргарифович',
                                                                                                         'https://kpfu.ru/ilyas.arslanov'),
                                                                                                        ('Рахимов '
                                                                                                         'Радик '
                                                                                                         'Рафисович',
                                                                                                         'https://kpfu.ru/radik.rahimov'),
                                                                                                        ('Гайсин '
                                                                                                         'Ирек '
                                                                                                         'Анасович',
                                                                                                         'https://kpfu.ru/irek.gajsin'),
                                                                                                        ('Самигуллин '
                                                                                                         'Алмаз '
                                                                                                         'Динаисович',
                                                                                                         'https://kpfu.ru/almaz.samigullin'),
                                                                                                        ('Хазиев '
                                                                                                         'Марат '
                                                                                                         'Люцерович',
                                                                                                         'https://kpfu.ru/marat.haziev'),
                                                                                                        ('Галиакбарова '
                                                                                                         'Разиля '
                                                                                                         'Рауфовна',
                                                                                                         'https://kpfu.ru/razilya.galiakbarova')],
                                                 'кафедра иностранных языков': [('Айдаева '
                                                                                 'Гьюнай '
                                                                                 'Фируддиновна',
                                                                                 'https://kpfu.ru/gjunaj.ajdaeva'),
                                                                                ('Бакланов '
                                                                                 'Павел '
                                                                                 'Алексеевич',
                                                                                 'https://kpfu.ru/pavel.baklanov'),
                                                                                ('Гатауллина '
                                                                                 'Камила '
                                                                                 'Наилевна',
                                                                                 'https://kpfu.ru/kamila.gataullina'),
                                                                                ('Дердизова '
                                                                                 'Фарида '
                                                                                 'Валиевна',
                                                                                 'https://kpfu.ru/farida.derdizova'),
                                                                                ('Жданов '
                                                                                 'Дмитрий '
                                                                                 'Олегович',
                                                                                 'https://kpfu.ru/dmitrij.zhdanov'),
                                                                                ('Ишмурадова '
                                                                                 'Альфия '
                                                                                 'Миннемухтаровна',
                                                                                 'https://kpfu.ru/alfiya.ishmuradova'),
                                                                                ('Калашникова '
                                                                                 'Миляуша '
                                                                                 'Миннерависовна',
                                                                                 'https://kpfu.ru/milyausha.kalashnikova'),
                                                                                ('Калинина '
                                                                                 'Галина '
                                                                                 'Сергеевна',
                                                                                 'https://kpfu.ru/galina.kalinina'),
                                                                                ('Маклакова '
                                                                                 'Евгения '
                                                                                 'Михайловна',
                                                                                 'https://kpfu.ru/evgeniya.maklakova'),
                                                                                ('Максимова '
                                                                                 'Эльвира '
                                                                                 'Владимировна',
                                                                                 'https://kpfu.ru/elvira.maksimova'),
                                                                                ('Мусина '
                                                                                 'Лейсан '
                                                                                 'Марсовна',
                                                                                 'https://kpfu.ru/leysan.musina'),
                                                                                ('Мустафина '
                                                                                 'Джамиля '
                                                                                 'Насыховна',
                                                                                 'https://kpfu.ru/dzhamilya.mustafina'),
                                                                                ('Мустафина '
                                                                                 'Лилия '
                                                                                 'Рашидовна',
                                                                                 'https://kpfu.ru/liliya.mustafina'),
                                                                                ('Нурутдинова '
                                                                                 'Наиля '
                                                                                 'Ривгатевна',
                                                                                 'https://kpfu.ru/nailya.nurutdinova'),
                                                                                ('Славина '
                                                                                 'Лилия '
                                                                                 'Рустамовна',
                                                                                 'https://kpfu.ru/liliya.slavina'),
                                                                                ('Соколова '
                                                                                 'Инесса '
                                                                                 'Альбертовна',
                                                                                 'https://kpfu.ru/inessa.sokolova'),
                                                                                ('Ханова '
                                                                                 'Айгуль '
                                                                                 'Филусовна',
                                                                                 'https://kpfu.ru/ajgul.hanova'),
                                                                                ('Чернова '
                                                                                 'Наталья '
                                                                                 'Айратовна',
                                                                                 'https://kpfu.ru/natalya.chernova')],
                                                 'кафедра информационных систем': [('Валиев '
                                                                                    'Рустам '
                                                                                    'Асгатович',
                                                                                    'https://kpfu.ru/rustam.valiev'),
                                                                                   ('Габбасов '
                                                                                    'Назим '
                                                                                    'Салихович',
                                                                                    'https://kpfu.ru/nazim.gabbasov'),
                                                                                   ('Галиуллин '
                                                                                    'Ленар '
                                                                                    'Айратович',
                                                                                    'https://kpfu.ru/lenar.galiullin'),
                                                                                   ('Зубков '
                                                                                    'Евгений '
                                                                                    'Витальевич',
                                                                                    'https://kpfu.ru/evgenij.zubkov'),
                                                                                   ('Илюхин '
                                                                                    'Алексей '
                                                                                    'Николаевич',
                                                                                    'https://kpfu.ru/aleksej.iljuhin'),
                                                                                   ('Тазмеев '
                                                                                    'Алмаз '
                                                                                    'Харисович',
                                                                                    'https://kpfu.ru/almaz.tazmeev'),
                                                                                   ('Хамадеев '
                                                                                    'Шамиль '
                                                                                    'Актасович',
                                                                                    'https://kpfu.ru/shamil.hamadeev'),
                                                                                   ('Хузятов '
                                                                                    'Шафик '
                                                                                    'Шаехович',
                                                                                    'https://kpfu.ru/shafik.huzyatov'),
                                                                                   ('Галиуллин '
                                                                                    'Ильнар '
                                                                                    'Айратович',
                                                                                    'https://kpfu.ru/ilnar.galiullin'),
                                                                                   ('Хазиев '
                                                                                    'Эмиль '
                                                                                    'Люцерович',
                                                                                    'https://kpfu.ru/emil.haziev'),
                                                                                   ('Чернов '
                                                                                    'Владимир '
                                                                                    'Владимирович',
                                                                                    'https://kpfu.ru/vladimir.chernov'),
                                                                                   ('Гибадуллина '
                                                                                    'Гузель '
                                                                                    'Рустамовна',
                                                                                    'https://kpfu.ru/guzel.gibadullina'),
                                                                                   ('Каримов '
                                                                                    'Тимур '
                                                                                    'Наилевич',
                                                                                    'https://kpfu.ru/timur.karimov'),
                                                                                   ('Хузятова '
                                                                                    'Ляля '
                                                                                    'Бакиевна',
                                                                                    'https://kpfu.ru/lyalya.huzyatova'),
                                                                                   ('Валиева '
                                                                                    'Лайсания '
                                                                                    'Акрамовна',
                                                                                    'https://kpfu.ru/lajsaniya.valieva'),
                                                                                   ('Хазиева '
                                                                                    'Гюзаль '
                                                                                    'Фидаевна',
                                                                                    'https://kpfu.ru/gjuzal.hazieva')],
                                                 'кафедра конституционного, административного и международного права': [
                                                     ('Курочкин '
                                                      'Анатолий '
                                                      'Васильевич',
                                                      'https://kpfu.ru/anatolij.kurochkin'),
                                                     ('Валиев '
                                                      'Габдрахман '
                                                      'Хаматханович',
                                                      'https://kpfu.ru/gabdrahman.valiev'),
                                                     ('Табольская '
                                                      'Виктория '
                                                      'Валерьевна',
                                                      'https://kpfu.ru/viktoriya.tabolskaya'),
                                                     ('Шакирова '
                                                      'Индира '
                                                      'Абдулхаковна',
                                                      'https://kpfu.ru/indira.shakirova'),
                                                     ('Ахмадуллина '
                                                      'Ирина '
                                                      'Ахсановна',
                                                      'https://kpfu.ru/irina.akhmadullina'),
                                                     ('Недорезова '
                                                      'Ольга '
                                                      'Юрьевна',
                                                      'https://kpfu.ru/olga.nedorezova'),
                                                     ('Хайруллина '
                                                      'Резеда '
                                                      'Газинуровна',
                                                      'https://kpfu.ru/rezeda.hajrullina'),
                                                     ('Кравченко '
                                                      'Ольга '
                                                      'Дмитриевна',
                                                      'https://kpfu.ru/olga.kravchenko'),
                                                     ('Фардеева '
                                                      'Ирина '
                                                      'Николаевна',
                                                      'https://kpfu.ru/irina.fardeeva'),
                                                     ('Хаертдинова '
                                                      'Альбина '
                                                      'Харисовна',
                                                      'https://kpfu.ru/albina.khaertdinova')],
                                                 'кафедра конструкторско-технологического обеспечения машиностроительных производств': [
                                                     ('Астащенко '
                                                      'Владимир '
                                                      'Иванович',
                                                      'https://kpfu.ru/vladimir.astaschenko'),
                                                     ('Глинина '
                                                      'Гульназ '
                                                      'Фидаэловна',
                                                      'https://kpfu.ru/gulnaz.glinina'),
                                                     ('Давлетшина '
                                                      'Галия '
                                                      'Камиловна',
                                                      'https://kpfu.ru/galiya.davletshina'),
                                                     ('Кенжабоев '
                                                      'Шукуржон '
                                                      'Шарипович',
                                                      'https://kpfu.ru/shukurzhon.kenzhaboev'),
                                                     ('Кондрашов '
                                                      'Алексей '
                                                      'Геннадьевич',
                                                      'https://kpfu.ru/aleksej.kondrashov'),
                                                     ('Петров '
                                                      'Сергей '
                                                      'Михайлович',
                                                      'https://kpfu.ru/sergej.petrov'),
                                                     ('Рябов '
                                                      'Евгений '
                                                      'Александрович',
                                                      'https://kpfu.ru/evgenij.ryabov'),
                                                     ('Сабиров '
                                                      'Айдар '
                                                      'Рамазанович',
                                                      'https://kpfu.ru/ajdarr.sabirov'),
                                                     ('Сафаров '
                                                      'Дамир '
                                                      'Тамасович',
                                                      'https://kpfu.ru/damir.safarov'),
                                                     ('Ступко '
                                                      'Виталий '
                                                      'Борисович',
                                                      'https://kpfu.ru/vitalij.stupko'),
                                                     ('Фасхутдинов '
                                                      'Айрат '
                                                      'Ибрагимович',
                                                      'https://kpfu.ru/ajrat.fashutdinov'),
                                                     ('Хисамутдинов '
                                                      'Равиль '
                                                      'Миргалимович',
                                                      'https://kpfu.ru/ravil.hisamutdinov'),
                                                     ('Хусаинов '
                                                      'Рустем '
                                                      'Мухаметович',
                                                      'https://kpfu.ru/rustem.husainov'),
                                                     ('Юрасова '
                                                      'Ольга '
                                                      'Игоревна',
                                                      'https://kpfu.ru/olga.jurasova')],
                                                 'кафедра математики': [('Габбасов Назим '
                                                                         'Салихович',
                                                                         'https://kpfu.ru/nazim.gabbasov'),
                                                                        ('Зайцева Жанна '
                                                                         'Ильинична',
                                                                         'https://kpfu.ru/zhanna.zajceva'),
                                                                        ('Матвеев Семен '
                                                                         'Николаевич',
                                                                         'https://kpfu.ru/semen.matveev'),
                                                                        ('Углов Александр '
                                                                         'Николаевич',
                                                                         'https://kpfu.ru/aleksandr.uglov'),
                                                                        ('Антропова '
                                                                         'Гюзель '
                                                                         'Равильевна',
                                                                         'https://kpfu.ru/gjuzel.antropova'),
                                                                        ('Губочкина '
                                                                         'Наталья '
                                                                         'Ивановна',
                                                                         'https://kpfu.ru/natalya.gubochkina'),
                                                                        ('Харасова Лилия '
                                                                         'Сергеевна',
                                                                         'https://kpfu.ru/liliya.harasova'),
                                                                        ('Халимова Алсу '
                                                                         'Файзулхаковна',
                                                                         'https://kpfu.ru/alsu.halimova')],
                                                 'кафедра материалов, технологий и качества': None,
                                                 'кафедра машиностроения': [('Шибаков '
                                                                             'Владимир '
                                                                             'Георгиевич',
                                                                             'https://kpfu.ru/vladimir.shibakov'),
                                                                            ('Сафронов '
                                                                             'Николай  '
                                                                             'Николаевич',
                                                                             'https://kpfu.ru/nikolaj.safronov'),
                                                                            ('Панкратов '
                                                                             'Дмитрий '
                                                                             'Леонидович',
                                                                             'https://kpfu.ru/dmitrij.pankratov'),
                                                                            ('Харисов '
                                                                             'Ленар '
                                                                             'Рустамович',
                                                                             'https://kpfu.ru/lenar.harisov'),
                                                                            ('Андреев '
                                                                             'Антон '
                                                                             'Павлович',
                                                                             'https://kpfu.ru/anton.andreev'),
                                                                            ('Валиев '
                                                                             'Айнур '
                                                                             'Миннегаянович',
                                                                             'https://kpfu.ru/ajnur.valiev'),
                                                                            ('Низамов '
                                                                             'Равиль '
                                                                             'Салимович',
                                                                             'https://kpfu.ru/ravil.nizamov'),
                                                                            ('Кужагильдин '
                                                                             'Рим '
                                                                             'Салихович',
                                                                             'https://kpfu.ru/rim.kuzhagildin'),
                                                                            ('Шутова '
                                                                             'Любовь '
                                                                             'Александровна',
                                                                             'https://kpfu.ru/ljubov.shutova'),
                                                                            ('Юмадилов '
                                                                             'Валерий '
                                                                             'Нуриевич',
                                                                             'https://kpfu.ru/valerij.jumadilov'),
                                                                            ('Клочкова '
                                                                             'Ксения '
                                                                             'Валерьевна',
                                                                             'https://kpfu.ru/kseniya.klochkova'),
                                                                            ('Яковлева '
                                                                             'Динара '
                                                                             'Маратовна',
                                                                             'https://kpfu.ru/dinara.galina')],
                                                 'кафедра механики и конструирования': [('Ахметов '
                                                                                         'Наил '
                                                                                         'Дамирович',
                                                                                         'https://kpfu.ru/nail.ahmetov'),
                                                                                        ('Байрамов '
                                                                                         'Фарит '
                                                                                         'Давлетович',
                                                                                         'https://kpfu.ru/farit.bajramov'),
                                                                                        ('Галимянов '
                                                                                         'Ильнур '
                                                                                         'Динаесович',
                                                                                         'https://kpfu.ru/ilnur.galimyanov'),
                                                                                        ('Гимадеев '
                                                                                         'Минахмет '
                                                                                         'Минхайдарович',
                                                                                         'https://kpfu.ru/minahmet.gimadeev'),
                                                                                        ('Кривошеев '
                                                                                         'Вячеслав '
                                                                                         'Александрович',
                                                                                         'https://kpfu.ru/vyacheslav.krivosheev'),
                                                                                        ('Тазмеева '
                                                                                         'Рамиля '
                                                                                         'Нуриахметовна',
                                                                                         'https://kpfu.ru/ramilya.tazmeeva'),
                                                                                        ('Талипова '
                                                                                         'Ирина '
                                                                                         'Петровна',
                                                                                         'https://kpfu.ru/irina.talipova'),
                                                                                        ('Фардеев '
                                                                                         'Альберт '
                                                                                         'Рифович',
                                                                                         'https://kpfu.ru/albert.fardeev'),
                                                                                        ('Феоктистова '
                                                                                         'Лида '
                                                                                         'Александровна',
                                                                                         'https://kpfu.ru/lida.feoktistova'),
                                                                                        ('Фролов '
                                                                                         'Алексей '
                                                                                         'Марксович',
                                                                                         'https://kpfu.ru/aleksej.frolov'),
                                                                                        ('Байрамов  '
                                                                                         'Булат '
                                                                                         'Фаритович',
                                                                                         'https://kpfu.ru/bulat.bajramov'),
                                                                                        ('Юнусов '
                                                                                         'Ганишер '
                                                                                         'Гафирович',
                                                                                         'https://kpfu.ru/ganisher.yunusov'),
                                                                                        ('Галимова '
                                                                                         'Гульназ '
                                                                                         'Ильгизовна',
                                                                                         'https://kpfu.ru/gulnaz.nabiullina'),
                                                                                        ('Коробова '
                                                                                         'Алла '
                                                                                         'Геннадьевна',
                                                                                         'https://kpfu.ru/alla.korobova'),
                                                                                        ('Рзаева '
                                                                                         'Татьяна '
                                                                                         'Васильевна',
                                                                                         'https://kpfu.ru/tatyana.rzaeva'),
                                                                                        ('Шарифуллина '
                                                                                         'Миляуша '
                                                                                         'Инсафовна',
                                                                                         'https://kpfu.ru/main?p_id=36311'),
                                                                                        ('Кирилова '
                                                                                         'Клара '
                                                                                         'Ивановна',
                                                                                         'https://kpfu.ru/klara.kirilova')],
                                                 'кафедра производственного менеджмента': [('Бикулов  '
                                                                                            'Ринат '
                                                                                            'Абдуллаевич',
                                                                                            'https://kpfu.ru/rinat.bikulov'),
                                                                                           ('Пуряев '
                                                                                            'Айдар '
                                                                                            'Султангалиевич',
                                                                                            'https://kpfu.ru/ajdar.puryaev'),
                                                                                           ('Аетдинова '
                                                                                            'Расуля '
                                                                                            'Рифкатовна',
                                                                                            'https://kpfu.ru/rasulya.aetdinova'),
                                                                                           ('Вячина '
                                                                                            'Ирина '
                                                                                            'Николаевна',
                                                                                            'https://kpfu.ru/irina.vyachina'),
                                                                                           ('Габдуллин '
                                                                                            'Ленар '
                                                                                            'Вакифович',
                                                                                            'https://kpfu.ru/lenar.gabdullin'),
                                                                                           ('Любова '
                                                                                            'Ольга '
                                                                                            'Витальевна',
                                                                                            'https://kpfu.ru/olga.ljubova'),
                                                                                           ('Сафаргалиев '
                                                                                            'Эрнст '
                                                                                            'Раисович',
                                                                                            'https://kpfu.ru/ernst.safargaliev'),
                                                                                           ('Сотников '
                                                                                            'Михаил '
                                                                                            'Иванович',
                                                                                            'https://kpfu.ru/mihail.sotnikov'),
                                                                                           ('Ефремова '
                                                                                            'Оксана '
                                                                                            'Ильинична',
                                                                                            'https://kpfu.ru/oksana.efremova')],
                                                 'кафедра промышленного, гражданского и строительных материалов': [
                                                     ('Галеев '
                                                      'Руслан '
                                                      'Разинович',
                                                      'https://kpfu.ru/ruslan.galeev'),
                                                     (
                                                         'Сибгатуллин '
                                                         'Эмер '
                                                         'Сулейманович',
                                                         'https://kpfu.ru/emer.sibgatullin'),
                                                     ('Бобрышев '
                                                      'Александр '
                                                      'Анатольевич',
                                                      'https://kpfu.ru/aleksandr.bobryshev'),
                                                     ('Исламов '
                                                      'Камиль '
                                                      'Фаритович',
                                                      'https://kpfu.ru/kamil.islamov'),
                                                     (
                                                         'Исрафилов '
                                                         'Данис '
                                                         'Ирекович',
                                                         'https://kpfu.ru/danis.israfilov'),
                                                     ('Корчагин '
                                                      'Олег '
                                                      'Павлович',
                                                      'https://kpfu.ru/oleg.korchagin'),
                                                     (
                                                         'Сибгатуллин '
                                                         'Камиль '
                                                         'Эмерович',
                                                         'https://kpfu.ru/kamil.sibgatullin'),
                                                     (
                                                         'Шафигуллин '
                                                         'Ленар '
                                                         'Нургалеевич',
                                                         'https://kpfu.ru/lenar.shafigullin'),
                                                     ('Ахметов '
                                                      'Фриль '
                                                      'Мирзанурович',
                                                      'https://kpfu.ru/fril.ahmetov'),
                                                     ('Мурузина '
                                                      'Елена '
                                                      'Васильевна',
                                                      'https://kpfu.ru/elena.muruzina'),
                                                     ('Мухин '
                                                      'Александр '
                                                      'Михайлович',
                                                      'https://kpfu.ru/aleksandr.mukhin'),
                                                     ('Буятова '
                                                      'Светлана '
                                                      'Геннадьевна',
                                                      'https://kpfu.ru/svetlana.buyatova'),
                                                     ('Зонина '
                                                      'Светлана '
                                                      'Викторовна',
                                                      'https://kpfu.ru/svetlana.zonina'),
                                                     ('Казакова '
                                                      'Ирина '
                                                      'Геннадьевна',
                                                      'https://kpfu.ru/irina.kazakova'),
                                                     (
                                                         'Мурзагалина '
                                                         'Элина '
                                                         'Ириковна',
                                                         'https://kpfu.ru/elina.murzagalina')],
                                                 'кафедра сервиса транспортных систем': [('Макарова '
                                                                                          'Ирина '
                                                                                          'Викторовна',
                                                                                          'https://kpfu.ru/irina.makarova'),
                                                                                         ('Ахметзянова '
                                                                                          'Гулия '
                                                                                          'Наильевна',
                                                                                          'https://kpfu.ru/guliya.ahmetzyanova'),
                                                                                         ('Басыров '
                                                                                          'Руслан '
                                                                                          'Рамилевич',
                                                                                          'https://kpfu.ru/ruslan.basyrov'),
                                                                                         ('Беляев '
                                                                                          'Эдуард '
                                                                                          'Ирекович',
                                                                                          'https://kpfu.ru/Eduard.Belyaev'),
                                                                                         ('Буйвол '
                                                                                          'Полина '
                                                                                          'Александровна',
                                                                                          'https://kpfu.ru/polina.bujvol'),
                                                                                         ('Габсалихова '
                                                                                          'Лариса '
                                                                                          'Мухаматзакиевна',
                                                                                          'https://kpfu.ru/larisa.gabsalihova'),
                                                                                         ('Маврин '
                                                                                          'Вадим '
                                                                                          'Геннадьевич',
                                                                                          'https://kpfu.ru/vadim.mavrin'),
                                                                                         ('Мухаметдинов '
                                                                                          'Эдуард '
                                                                                          'Мухаматзакиевич',
                                                                                          'https://kpfu.ru/eduard.muhametdinov'),
                                                                                         ('Павленко '
                                                                                          'Алексей '
                                                                                          'Петрович',
                                                                                          'https://kpfu.ru/aleksej.pavlenko'),
                                                                                         ('Фатихова '
                                                                                          'Лариса '
                                                                                          'Энгельсовна',
                                                                                          'https://kpfu.ru/larisa.fatihova'),
                                                                                         ('Цыбунов '
                                                                                          'Эдуард '
                                                                                          'Николаевич',
                                                                                          'https://kpfu.ru/eduard.cybunov'),
                                                                                         ('Барыкин '
                                                                                          'Алексей '
                                                                                          'Юрьевич',
                                                                                          'https://kpfu.ru/aleksej.barykin'),
                                                                                         ('Галиев '
                                                                                          'Радик '
                                                                                          'Мирзашаехович',
                                                                                          'https://kpfu.ru/radik.galiev'),
                                                                                         ('Гафиятуллин '
                                                                                          'Асхат '
                                                                                          'Асадуллович',
                                                                                          'https://kpfu.ru/ashat.gafiyatullin'),
                                                                                         ('Малаховецкий '
                                                                                          'Андрей '
                                                                                          'Федорович',
                                                                                          'https://kpfu.ru/andrej.malahoveckij'),
                                                                                         ('Нуретдинов '
                                                                                          'Дамир '
                                                                                          'Имамутдинович',
                                                                                          'https://kpfu.ru/damir.nuretdinov'),
                                                                                         ('Сулейманов '
                                                                                          'Ильнар '
                                                                                          'Фаргатович',
                                                                                          'https://kpfu.ru/ilnar.sulejmanov'),
                                                                                         ('Шубенкова '
                                                                                          'Ксения '
                                                                                          'Андреевна',
                                                                                          'https://kpfu.ru/kseniya.shubenkova'),
                                                                                         ('Мавляутдинова '
                                                                                          'Гульназ '
                                                                                          'Рашидовна',
                                                                                          'https://kpfu.ru/gulnaz.sadygova'),
                                                                                         ('Тахавиев '
                                                                                          'Раяз '
                                                                                          'Халимович',
                                                                                          'https://kpfu.ru/rayaz.tahaviev'),
                                                                                         ('Якупова '
                                                                                          'Гульнара '
                                                                                          'Анваровна',
                                                                                          'https://kpfu.ru/gulnara.yakupova'),
                                                                                         ('Бадриев '
                                                                                          'Айрат '
                                                                                          'Ирекович',
                                                                                          'https://kpfu.ru/ajrat.badriev'),
                                                                                         ('Бойко '
                                                                                          'Алексей '
                                                                                          'Дмитриевич',
                                                                                          'https://kpfu.ru/aleksej.bojko'),
                                                                                         ('Сафина '
                                                                                          'Лилия '
                                                                                          'Рафисовна',
                                                                                          'https://kpfu.ru/liliyara.safina'),
                                                                                         ('Парсин '
                                                                                          'Глеб '
                                                                                          'Артурович',
                                                                                          'https://kpfu.ru/gleb.parsin')],
                                                 'кафедра системного анализа и информатики': [('Карабцев '
                                                                                               'Владимир '
                                                                                               'Сергеевич',
                                                                                               'https://kpfu.ru/vladimir.karabcev'),
                                                                                              ('Ахатов '
                                                                                               'Акмал '
                                                                                               'Рустамович',
                                                                                               'https://kpfu.ru/akmal.akhatov'),
                                                                                              ('Ахметзянов '
                                                                                               'Инсур '
                                                                                               'Завдятович',
                                                                                               'https://kpfu.ru/insur.ahmetzyanov'),
                                                                                              ('Гумерова '
                                                                                               'Лилия '
                                                                                               'Зуфаровна',
                                                                                               'https://kpfu.ru/liliya.gumerova'),
                                                                                              ('Демьянов '
                                                                                               'Дмитрий '
                                                                                               'Николаевич',
                                                                                               'https://kpfu.ru/dmitrij.demyanov'),
                                                                                              ('Марданшин '
                                                                                               'Рифкат '
                                                                                               'Галимович',
                                                                                               'https://kpfu.ru/rifkat.mardanshin'),
                                                                                              ('Товштейн '
                                                                                               'Марк '
                                                                                               'Яковлевич',
                                                                                               'https://kpfu.ru/mark.tovshtejn'),
                                                                                              ('Мышкина '
                                                                                               'Ирина '
                                                                                               'Юрьевна',
                                                                                               'https://kpfu.ru/irina.myshkina'),
                                                                                              ('Волков '
                                                                                               'Василий '
                                                                                               'Геннадьевич',
                                                                                               'https://kpfu.ru/vasilij.volkov'),
                                                                                              ('Грудцына '
                                                                                               'Лариса '
                                                                                               'Юрьевна',
                                                                                               'https://kpfu.ru/larisa.grudcyna'),
                                                                                              ('Хаматьянов '
                                                                                               'Руслан '
                                                                                               'Винерович',
                                                                                               'https://kpfu.ru/ruslan.khamatyanov')],
                                                 'кафедра социально-гуманитарных наук': [('Хайруллин '
                                                                                          'Аскар '
                                                                                          'Гафиятуллович',
                                                                                          'https://kpfu.ru/askar.hajrullin'),
                                                                                         ('Бессонова '
                                                                                          'Татьяна '
                                                                                          'Викторовна',
                                                                                          'https://kpfu.ru/tatyana.bessonova'),
                                                                                         ('Бурганова '
                                                                                          'Нафиса '
                                                                                          'Тагировна',
                                                                                          'https://kpfu.ru/nafisa.burganova'),
                                                                                         ('Горячева '
                                                                                          'Ольга '
                                                                                          'Николаевна',
                                                                                          'https://kpfu.ru/olga.goryacheva'),
                                                                                         ('Задворнов '
                                                                                          'Андрей '
                                                                                          'Николаевич',
                                                                                          'https://kpfu.ru/andrej.zadvornov'),
                                                                                         ('Закирова '
                                                                                          'Лейсан '
                                                                                          'Мударисовна',
                                                                                          'https://kpfu.ru/lejsan.zakirova'),
                                                                                         ('Патенко '
                                                                                          'Гульчачак '
                                                                                          'Ринатовна',
                                                                                          'https://kpfu.ru/gulchachak.patenko'),
                                                                                         ('Яковлева '
                                                                                          'Марина '
                                                                                          'Геннадьевна',
                                                                                          'https://kpfu.ru/marina.yakovleva'),
                                                                                         ('Исмагилова '
                                                                                          'Регина '
                                                                                          'Рифгатовна',
                                                                                          'https://kpfu.ru/regina.ismagilova'),
                                                                                         ('Комарова '
                                                                                          'Любовь '
                                                                                          'Юрьевна',
                                                                                          'https://kpfu.ru/ljubov.komarova'),
                                                                                         ('Шайсултанова '
                                                                                          'Эльмира '
                                                                                          'Ильдаровна',
                                                                                          'https://kpfu.ru/elmira.shajsultanova'),
                                                                                         ('Халиуллина '
                                                                                          'Эльмира '
                                                                                          'Марсовна',
                                                                                          'https://kpfu.ru/elmira.haliullina')],
                                                 'кафедра технологии строительства и управления недвижимостью': [
                                                     ('Исламов '
                                                      'Камиль '
                                                      'Фаритович',
                                                      'https://kpfu.ru/kamil.islamov'),
                                                     ('Игтисамов '
                                                      'Рафаэль '
                                                      'Сазитович',
                                                      'https://kpfu.ru/rafael.igtisamov'),
                                                     ('Чернов '
                                                      'Виктор '
                                                      'Александрович',
                                                      'https://kpfu.ru/viktor.chernov'),
                                                     ('Ахметов '
                                                      'Фриль '
                                                      'Мирзанурович',
                                                      'https://kpfu.ru/fril.ahmetov'),
                                                     ('Тедеева '
                                                      'Татьяна '
                                                      'Олеговна',
                                                      'https://kpfu.ru/tatyana.tedeeva'),
                                                     ('Сафиуллин '
                                                      'Ринат '
                                                      'Талгатович',
                                                      'https://kpfu.ru/rinatt.safiullin'),
                                                     ('Совков '
                                                      'Сергей '
                                                      'Анатольевич',
                                                      'https://kpfu.ru/sergey.sovkov'),
                                                     ('Тимиров '
                                                      'Эскандер '
                                                      'Вязирович',
                                                      'https://kpfu.ru/eskander.timirov'),
                                                     ('Новоселов '
                                                      'Олег '
                                                      'Геннадьевич',
                                                      'https://kpfu.ru/oleg.novoselov'),
                                                     ('Хораськин '
                                                      'Станислав '
                                                      'Александрович',
                                                      'https://kpfu.ru/stanislav.khoraskin'),
                                                     ('Сайфуллина '
                                                      'Юлия '
                                                      'Витальевна',
                                                      'https://kpfu.ru/juliya.sajfullina')],
                                                 'кафедра уголовного права, уголовного процесса и криминалистики': [
                                                     ('Хамитов '
                                                      'Радик '
                                                      'Накимович',
                                                      'https://kpfu.ru/radik.hamitov'),
                                                     (
                                                         'Камалиева '
                                                         'Лиана '
                                                         'Александровна',
                                                         'https://kpfu.ru/liana.kamalieva'),
                                                     (
                                                         'Аглямова '
                                                         'Гульназ '
                                                         'Махияновна',
                                                         'https://kpfu.ru/gulnaz.aglyamova'),
                                                     ('Следь '
                                                      'Юрий '
                                                      'Генадьевич',
                                                      'https://kpfu.ru/jurijg.sled'),
                                                     ('Ахметов '
                                                      'Рустем '
                                                      'Рифович',
                                                      'https://kpfu.ru/rustemr.ahmetov'),
                                                     ('Акрамов '
                                                      'Ульфат '
                                                      'Камильевич',
                                                      'https://kpfu.ru/ulfat.akramov'),
                                                     (
                                                         'Харисова '
                                                         'Эльвира '
                                                         'Анваровна',
                                                         'https://kpfu.ru/elvira.harisova'),
                                                     (
                                                         'Шакирова '
                                                         'Альбина '
                                                         'Абдулхаковна',
                                                         'https://kpfu.ru/albinaa.shakirova')],
                                                 'кафедра физики': [('Галиакбаров Азат '
                                                                     'Талгатович',
                                                                     'https://kpfu.ru/azat.galiakbarov'),
                                                                    ('Акст Евгений '
                                                                     'Рудольфович',
                                                                     'https://kpfu.ru/evgenij.akst'),
                                                                    ('Тазмеев Харис '
                                                                     'Каюмович',
                                                                     'https://kpfu.ru/haris.tazmeev'),
                                                                    ('Шайхуллина Равия '
                                                                     'Масгутовна',
                                                                     'https://kpfu.ru/raviya.shajhullina'),
                                                                    ('Рамазанов Фарит '
                                                                     'Фатихович',
                                                                     'https://kpfu.ru/farit.ramazanov'),
                                                                    ('Тазмеев Гаяз '
                                                                     'Харисович',
                                                                     'https://kpfu.ru/gayaz.tazmeev'),
                                                                    ('Карпова Марина '
                                                                     'Николаевна',
                                                                     'https://kpfu.ru/marina.karpova'),
                                                                    ('Ряднинская Лейсан '
                                                                     'Фанисовна',
                                                                     'https://kpfu.ru/lejsan.ryadninskaya')],
                                                 'кафедра филологии': [('Айдарова Алсу '
                                                                        'Мирзаяновна',
                                                                        'https://kpfu.ru/alsu.ajdarova'),
                                                                       ('Багатеева '
                                                                        'Ангелина '
                                                                        'Олеговна',
                                                                        'https://kpfu.ru/angelina.bagateeva'),
                                                                       ('Базарова  Лилия  '
                                                                        'Вязировна',
                                                                        'https://kpfu.ru/liliya.bazarova'),
                                                                       ('Билялова Альбина '
                                                                        'Анваровна',
                                                                        'https://kpfu.ru/albinaa.bilyalova'),
                                                                       ('Вильданова '
                                                                        'Эльмира '
                                                                        'Минекасимовна',
                                                                        'https://kpfu.ru/elmira.vildanova'),
                                                                       ('Геворкян Ирина '
                                                                        'Арцруновна',
                                                                        'https://kpfu.ru/irina.gevorkyan'),
                                                                       ('Гильфанова '
                                                                        'Гульнара '
                                                                        'Тавкильевна',
                                                                        'https://kpfu.ru/gulnara.gilfanova'),
                                                                       ('Гилязева Эмма '
                                                                        'Николаевна',
                                                                        'https://kpfu.ru/emma.gilyazeva'),
                                                                       ('Евграфова Ольга '
                                                                        'Геннадьевна',
                                                                        'https://kpfu.ru/olga.evgrafova'),
                                                                       ('Зиганшина Чулпан '
                                                                        'Рифовна',
                                                                        'https://kpfu.ru/chulpan.ziganshina'),
                                                                       ('Кемалова Миляуша '
                                                                        'Назимовна',
                                                                        'https://kpfu.ru/milyausha.kemalova'),
                                                                       ('Мазаева Татьяна '
                                                                        'Викторовна',
                                                                        'https://kpfu.ru/tatyana.mazaeva'),
                                                                       ('Патенко '
                                                                        'Гульчачак '
                                                                        'Ринатовна',
                                                                        'https://kpfu.ru/gulchachak.patenko'),
                                                                       ('Салимзанова '
                                                                        'Диляра Айратовна',
                                                                        'https://kpfu.ru/dilyara.gilfanova'),
                                                                       ('Сахапова Фарида '
                                                                        'Ханифовна',
                                                                        'https://kpfu.ru/farida.sahapova'),
                                                                       ('Сингатуллова '
                                                                        'Дина Ибрагимовна',
                                                                        'https://kpfu.ru/dina.singatullova'),
                                                                       ('Хайруллина '
                                                                        'Динара '
                                                                        'Дилшатовна',
                                                                        'https://kpfu.ru/dinarad.hajrullina'),
                                                                       ('Хузин Ильнур '
                                                                        'Рафисович',
                                                                        'https://kpfu.ru/ilnurr.khuzin'),
                                                                       ('Шарипова Эльвира '
                                                                        'Зямиловна',
                                                                        'https://kpfu.ru/elviraz.sharipova')],
                                                 'кафедра химии и экологии': [('Маврин '
                                                                               'Геннадий '
                                                                               'Витальевич',
                                                                               'https://kpfu.ru/gennadij.mavrin'),
                                                                              ('Ахмадиев '
                                                                               'Габдулахат '
                                                                               'Маликович',
                                                                               'https://kpfu.ru/gabdulahat.ahmadiev'),
                                                                              ('Соколов '
                                                                               'Михаил '
                                                                               'Павлович',
                                                                               'https://kpfu.ru/mihail.sokolov'),
                                                                              ('Мифтахов '
                                                                               'Мунир '
                                                                               'Нафисович',
                                                                               'https://kpfu.ru/munir.miftahov'),
                                                                              ('Сиппель '
                                                                               'Ирина '
                                                                               'Яковлевна',
                                                                               'https://kpfu.ru/irina.sippel'),
                                                                              ('Смирнова '
                                                                               'Нина '
                                                                               'Николаевна',
                                                                               'https://kpfu.ru/nina.smirnova'),
                                                                              ('Фазуллин '
                                                                               'Динар '
                                                                               'Дильшатович',
                                                                               'https://kpfu.ru/dinar.fazullin'),
                                                                              ('Шарафутдинов '
                                                                               'Рафик '
                                                                               'Низамутдинович',
                                                                               'https://kpfu.ru/rafik.sharafutdinov'),
                                                                              ('Ахметов '
                                                                               'Вильнюс '
                                                                               'Мирзахметович',
                                                                               'https://kpfu.ru/vilnjus.ahmetov'),
                                                                              ('Сулейманов '
                                                                               'Ильнар '
                                                                               'Фаргатович',
                                                                               'https://kpfu.ru/ilnar.sulejmanov'),
                                                                              ('Трушков '
                                                                               'Сергей '
                                                                               'Михайлович',
                                                                               'https://kpfu.ru/sergey.trushkov'),
                                                                              ('Харлямов '
                                                                               'Дамир '
                                                                               'Афгатович',
                                                                               'https://kpfu.ru/damir.harlyamov'),
                                                                              ('Терентьева '
                                                                               'Валерия '
                                                                               'Валерьевна',
                                                                               'https://kpfu.ru/valeriya.terenteva')],
                                                 'кафедра экономики предприятий\xa0и организаций': [('Махмутов '
                                                                                                     'Ильнур '
                                                                                                     'Ильязович',
                                                                                                     'https://kpfu.ru/ilnur.mahmutov'),
                                                                                                    ('Ваславская '
                                                                                                     'Ирина '
                                                                                                     'Юрьевна',
                                                                                                     'https://kpfu.ru/irina.vaslavskaya'),
                                                                                                    ('Насыров '
                                                                                                     'Искандар '
                                                                                                     'Наилович',
                                                                                                     'https://kpfu.ru/iskandar.nasyrov'),
                                                                                                    ('Габидинова '
                                                                                                     'Гульназ '
                                                                                                     'Сабирзяновна',
                                                                                                     'https://kpfu.ru/gulnaz.gabidinova'),
                                                                                                    ('Григорьева '
                                                                                                     'Диана '
                                                                                                     'Рамилевна',
                                                                                                     'https://kpfu.ru/diana.grigoreva'),
                                                                                                    ('Елакова '
                                                                                                     'Алла '
                                                                                                     'Александровна',
                                                                                                     'https://kpfu.ru/alla.elakova'),
                                                                                                    ('Жарина '
                                                                                                     'Наталья '
                                                                                                     'Анатольевна',
                                                                                                     'https://kpfu.ru/natalya.zharina'),
                                                                                                    ('Зиятдинов '
                                                                                                     'Артур '
                                                                                                     'Фаридович',
                                                                                                     'https://kpfu.ru/artur.ziyatdinov'),
                                                                                                    ('Карамышев '
                                                                                                     'Антон '
                                                                                                     'Николаевич',
                                                                                                     'https://kpfu.ru/anton.karamyshev'),
                                                                                                    ('Кузнецова '
                                                                                                     'Светлана '
                                                                                                     'Борисовна',
                                                                                                     'https://kpfu.ru/svetlanab.kuznecova'),
                                                                                                    ('Хайруллин '
                                                                                                     'Булат '
                                                                                                     'Аскарович',
                                                                                                     'https://kpfu.ru/bulat.hajrullin'),
                                                                                                    ('Руднева '
                                                                                                     'Наталья '
                                                                                                     'Валентиновна',
                                                                                                     'https://kpfu.ru/natalya.rudneva'),
                                                                                                    ('Тюхалкина '
                                                                                                     'Евгения '
                                                                                                     'Евгениевна',
                                                                                                     'https://kpfu.ru/evgeniya.tjuhalkina')],
                                                 'кафедра экономической теории и экономической политики': [('Макаров '
                                                                                                            'Анатолий '
                                                                                                            'Николаевич',
                                                                                                            'https://kpfu.ru/Anatoliy.Makarov'),
                                                                                                           ('Абдуллина '
                                                                                                            'Эльвира '
                                                                                                            'Ирековна',
                                                                                                            'https://kpfu.ru/elvira.abdullina'),
                                                                                                           (
                                                                                                               'Галиуллина '
                                                                                                               'Гыльия '
                                                                                                               'Фагимовна',
                                                                                                               'https://kpfu.ru/gyliya.galiullina'),
                                                                                                           ('Максютина '
                                                                                                            'Елена '
                                                                                                            'Владимировна',
                                                                                                            'https://kpfu.ru/elena.maksjutina'),
                                                                                                           ('Мансурова '
                                                                                                            'Татьяна '
                                                                                                            'Геннадьевна',
                                                                                                            'https://kpfu.ru/tatyana.mansurova')],
                                                 'кафедра эксплуатации автомобильного транспорта': [('Кулаков '
                                                                                                     'Александр '
                                                                                                     'Тихонович',
                                                                                                     'https://kpfu.ru/aleksandr.kulakov'),
                                                                                                    ('Барыкин '
                                                                                                     'Алексей '
                                                                                                     'Юрьевич',
                                                                                                     'https://kpfu.ru/aleksej.barykin'),
                                                                                                    ('Барыльникова '
                                                                                                     'Елена '
                                                                                                     'Петровна',
                                                                                                     'https://kpfu.ru/elena.barylnikova'),
                                                                                                    ('Галиев '
                                                                                                     'Радик '
                                                                                                     'Мирзашаехович',
                                                                                                     'https://kpfu.ru/radik.galiev'),
                                                                                                    ('Илдарханов '
                                                                                                     'Радик '
                                                                                                     'Фанисович',
                                                                                                     'https://kpfu.ru/radik.ildarhanov'),
                                                                                                    ('Нуретдинов '
                                                                                                     'Дамир '
                                                                                                     'Имамутдинович',
                                                                                                     'https://kpfu.ru/damir.nuretdinov'),
                                                                                                    ('Сахапов '
                                                                                                     'Ирек '
                                                                                                     'Анасович',
                                                                                                     'https://kpfu.ru/irek.sahapov'),
                                                                                                    ('Шайхутдинов '
                                                                                                     'Илнар '
                                                                                                     'Фанилевич',
                                                                                                     'https://kpfu.ru/ilnar.shajhutdinov'),
                                                                                                    ('Шакуров '
                                                                                                     'Дилус '
                                                                                                     'Кавыевич',
                                                                                                     'https://kpfu.ru/dilus.shakurov'),
                                                                                                    ('Аюкин '
                                                                                                     'Зульфат '
                                                                                                     'Ахатович',
                                                                                                     'https://kpfu.ru/zulfat.ajukin'),
                                                                                                    ('Нигметзянова '
                                                                                                     'Венера '
                                                                                                     'Марсовна',
                                                                                                     'https://kpfu.ru/venera.nigmetzyanova'),
                                                                                                    ('Курдин '
                                                                                                     'Петр '
                                                                                                     'Геннадьевич',
                                                                                                     'https://kpfu.ru/petr.kurdin'),
                                                                                                    ('Тахавиев '
                                                                                                     'Раяз '
                                                                                                     'Халимович',
                                                                                                     'https://kpfu.ru/rayaz.tahaviev'),
                                                                                                    ('Щигарцов '
                                                                                                     'Иван '
                                                                                                     'Михайлович',
                                                                                                     'https://kpfu.ru/main?p_id=36316'),
                                                                                                    ('Хуснетдинов '
                                                                                                     'Шамиль '
                                                                                                     'Сабирович',
                                                                                                     'https://kpfu.ru/shamil.husnetdinov'),
                                                                                                    ('Смирнова '
                                                                                                     'Рамзия '
                                                                                                     'Хамитовна',
                                                                                                     'https://kpfu.ru/ramziya.ahmadeeva')],
                                                 'кафедра электроэнергетики и электротехники': [('Башмаков '
                                                                                                 'Дмитрий '
                                                                                                 'Александрович',
                                                                                                 'https://kpfu.ru/dmitrij.bashmakov'),
                                                                                                ('Сафронов '
                                                                                                 'Николай  '
                                                                                                 'Николаевич',
                                                                                                 'https://kpfu.ru/nikolaj.safronov'),
                                                                                                ('Насибуллин '
                                                                                                 'Рамиль '
                                                                                                 'Тахирович',
                                                                                                 'https://kpfu.ru/ramilt.nasibullin'),
                                                                                                ('Ахметсагиров '
                                                                                                 'Рамиль '
                                                                                                 'Ильясович',
                                                                                                 'https://kpfu.ru/ramil.ahmetsagirov'),
                                                                                                ('Ахметшин '
                                                                                                 'Роберт '
                                                                                                 'Султанович',
                                                                                                 'https://kpfu.ru/robert.ahmetshin'),
                                                                                                ('Галиакбаров '
                                                                                                 'Азат '
                                                                                                 'Талгатович',
                                                                                                 'https://kpfu.ru/azat.galiakbarov'),
                                                                                                ('Галимов '
                                                                                                 'Наиль '
                                                                                                 'Салихович',
                                                                                                 'https://kpfu.ru/nail.galimov'),
                                                                                                ('Гумеров '
                                                                                                 'Айрат '
                                                                                                 'Завдатович',
                                                                                                 'https://kpfu.ru/ajrat.gumerov'),
                                                                                                ('Ильин '
                                                                                                 'Владимир '
                                                                                                 'Иванович',
                                                                                                 'https://kpfu.ru/vladimir.ilin'),
                                                                                                ('Савицкий '
                                                                                                 'Сергей '
                                                                                                 'Константинович',
                                                                                                 'https://kpfu.ru/sergej.savickij'),
                                                                                                ('Садриев '
                                                                                                 'Рамиль '
                                                                                                 'Шамилевич',
                                                                                                 'https://kpfu.ru/ramils.sadriev'),
                                                                                                ('Шакиров '
                                                                                                 'Юнус '
                                                                                                 'Идрисович',
                                                                                                 'https://kpfu.ru/junus.shakirov'),
                                                                                                ('Заболотская '
                                                                                                 'Нина '
                                                                                                 'Николаевна',
                                                                                                 'https://kpfu.ru/nina.zabolotskaya'),
                                                                                                ('Фатыхов '
                                                                                                 'Камиль '
                                                                                                 'Закирович',
                                                                                                 'https://kpfu.ru/kamil.fatyhov'),
                                                                                                ('Анчугова '
                                                                                                 'Алевтина '
                                                                                                 'Флегентьевна',
                                                                                                 'https://kpfu.ru/alevtina.anchugova'),
                                                                                                ('Дрогайлова '
                                                                                                 'Людмила '
                                                                                                 'Николаевна',
                                                                                                 'https://kpfu.ru/ljudmila.drogajlova'),
                                                                                                ('Закирова '
                                                                                                 'Лилия '
                                                                                                 'Петровна',
                                                                                                 'https://kpfu.ru/liliyape.zakirova'),
                                                                                                ('Багавова '
                                                                                                 'Альбина '
                                                                                                 'Рифовна',
                                                                                                 'https://kpfu.ru/albina.bagavova'),
                                                                                                ('Валиев '
                                                                                                 'Рамиль '
                                                                                                 'Ильдарович',
                                                                                                 'https://kpfu.ru/ramil.valiev'),
                                                                                                ('Журавлева '
                                                                                                 'Гульшат '
                                                                                                 'Фаридовна',
                                                                                                 'https://kpfu.ru/main?p_id=39092'),
                                                                                                ('Хафизов '
                                                                                                 'Алмаз '
                                                                                                 'Анзяпович',
                                                                                                 'https://kpfu.ru/almaz.hafizov')],
                                                 'кафедра юридических дисциплин': [('Магизов '
                                                                                    'Рустем '
                                                                                    'Робертович',
                                                                                    'https://kpfu.ru/rustem.magizov'),
                                                                                   ('Комадорова '
                                                                                    'Ирина '
                                                                                    'Владимировна',
                                                                                    'https://kpfu.ru/irina.komadorova'),
                                                                                   ('Кабанов '
                                                                                    'Павел '
                                                                                    'Александрович',
                                                                                    'https://kpfu.ru/pavel.kabanov'),
                                                                                   ('Юнусов '
                                                                                    'Ахат '
                                                                                    'Ахнафович',
                                                                                    'https://kpfu.ru/akhat.yunusov'),
                                                                                   ('Валиуллина '
                                                                                    'Динара '
                                                                                    'Анваровна',
                                                                                    'https://kpfu.ru/dinara.musabirova'),
                                                                                   ('Гайфутдинова '
                                                                                    'Розалия '
                                                                                    'Закиевна',
                                                                                    'https://kpfu.ru/rozaliya.gajfutdinova'),
                                                                                   ('Гильманов '
                                                                                    'Идрис '
                                                                                    'Мухаматюнусович',
                                                                                    'https://kpfu.ru/idris.gilmanov'),
                                                                                   ('Кривенкова '
                                                                                    'Мария '
                                                                                    'Витальевна',
                                                                                    'https://kpfu.ru/mariya.krivenkova'),
                                                                                   ('Сахапов '
                                                                                    'Ринат '
                                                                                    'Раисович',
                                                                                    'https://kpfu.ru/rinat.sahapov'),
                                                                                   ('Туманов '
                                                                                    'Дмитрий '
                                                                                    'Юрьевич',
                                                                                    'https://kpfu.ru/dmitrij.tumanov'),
                                                                                   ('Хасимова '
                                                                                    'Лейсан '
                                                                                    'Нафисовна',
                                                                                    'https://kpfu.ru/lejsan.hasimova'),
                                                                                   ('Шакирова '
                                                                                    'Индира '
                                                                                    'Абдулхаковна',
                                                                                    'https://kpfu.ru/indira.shakirova'),
                                                                                   ('Ющенко '
                                                                                    'Наталья '
                                                                                    'Анатольевна',
                                                                                    'https://kpfu.ru/natalyaa.juschenko'),
                                                                                   ('Неганов '
                                                                                    'Дмитрий '
                                                                                    'Александрович',
                                                                                    'https://kpfu.ru/dmitrij.neganov'),
                                                                                   ('Кузнецов '
                                                                                    'Сергей '
                                                                                    'Владимирович',
                                                                                    'https://kpfu.ru/sergej.kuznecov'),
                                                                                   ('Мальцева '
                                                                                    'Елена '
                                                                                    'Николаевна',
                                                                                    'https://kpfu.ru/elena.malceva'),
                                                                                   ('Андреева '
                                                                                    'Ирина '
                                                                                    'Анатольевна',
                                                                                    'https://kpfu.ru/irinaa.andreeva')]},
            'Общеуниверситетская кафедра физического воспитания и спорта': {'Основная кафедра': [('Двоеносов '
                                                                                                  'Владимир '
                                                                                                  'Георгиевич',
                                                                                                  'https://kpfu.ru/Vladimir.Dvoenosov'),
                                                                                                 ('Жданов '
                                                                                                  'Ренад '
                                                                                                  'Ибрагимович',
                                                                                                  'https://kpfu.ru/Renad.Zhdanov'),
                                                                                                 ('Волкова '
                                                                                                  'Кадрия '
                                                                                                  'Рафиковна',
                                                                                                  'https://kpfu.ru/kadriya.volkova'),
                                                                                                 ('Пасмуров '
                                                                                                  'Григорий '
                                                                                                  'Иванович',
                                                                                                  'https://kpfu.ru/grigorij.pasmurov'),
                                                                                                 ('Фазлеева '
                                                                                                  'Елена '
                                                                                                  'Вячеславовна',
                                                                                                  'https://kpfu.ru/elena.fazleeva'),
                                                                                                 ('Шалавина '
                                                                                                  'Анна '
                                                                                                  'Сергеевна',
                                                                                                  'https://kpfu.ru/anna.shalavina'),
                                                                                                 ('Касатова '
                                                                                                  'Людмила '
                                                                                                  'Васильевна',
                                                                                                  'https://kpfu.ru/Ljudmila.Kasatova'),
                                                                                                 ('Галиев '
                                                                                                  'Ришат '
                                                                                                  'Ринатович',
                                                                                                  'https://kpfu.ru/Rishat.Galiev'),
                                                                                                 ('Рахимов '
                                                                                                  'Марат '
                                                                                                  'Ильшатович',
                                                                                                  'https://kpfu.ru/marat.rahimov'),
                                                                                                 ('Тагирова '
                                                                                                  'Наталия '
                                                                                                  'Петровна',
                                                                                                  'https://kpfu.ru/nataliya.tagirova'),
                                                                                                 ('Абдрашитова '
                                                                                                  'Татьяна '
                                                                                                  'Викторовна',
                                                                                                  'https://kpfu.ru/tatyana.abdrashitova'),
                                                                                                 ('Авдеева '
                                                                                                  'Лариса '
                                                                                                  'Викторовна',
                                                                                                  'https://kpfu.ru/larisa.avdeeva'),
                                                                                                 ('Азизова '
                                                                                                  'Ирина '
                                                                                                  'Николаевна',
                                                                                                  'https://kpfu.ru/irina.azizova'),
                                                                                                 ('Арбеева '
                                                                                                  'Милэуша '
                                                                                                  'Шамилевна',
                                                                                                  'https://kpfu.ru/Milyausha.Arbeeva'),
                                                                                                 ('Арсланова '
                                                                                                  'Татьяна '
                                                                                                  'Леонидовна',
                                                                                                  'https://kpfu.ru/Tatyana.Arslanova'),
                                                                                                 ('Белов '
                                                                                                  'Александр '
                                                                                                  'Михайлович',
                                                                                                  'https://kpfu.ru/Aleksandr.Belov'),
                                                                                                 ('Бикмуллина '
                                                                                                  'Аделя '
                                                                                                  'Рашитовна',
                                                                                                  'https://kpfu.ru/adelya.bikmullina'),
                                                                                                 ('Бухтоярова '
                                                                                                  'Луиза '
                                                                                                  'Васильевна',
                                                                                                  'https://kpfu.ru/Luiza.Bukhtoyarova'),
                                                                                                 ('Власова '
                                                                                                  'Татьяна '
                                                                                                  'Станиславовна',
                                                                                                  'https://kpfu.ru/tatyanas.vlasova'),
                                                                                                 ('Волкова '
                                                                                                  'Резеда '
                                                                                                  'Фатхрахмановна',
                                                                                                  'https://kpfu.ru/Rezeda.Volkova'),
                                                                                                 ('Воробьева '
                                                                                                  'Ирина '
                                                                                                  'Владимировна',
                                                                                                  'https://kpfu.ru/Irina.Vorobeva'),
                                                                                                 ('Галиуллин '
                                                                                                  'Равиль '
                                                                                                  'Масхутович',
                                                                                                  'https://kpfu.ru/ravil.galiullin'),
                                                                                                 ('Григорьев '
                                                                                                  'Артем '
                                                                                                  'Павлович',
                                                                                                  'https://kpfu.ru/artem.grigorev'),
                                                                                                 ('Диц '
                                                                                                  'Сергей '
                                                                                                  'Георгиевич',
                                                                                                  'https://kpfu.ru/sergej.dic'),
                                                                                                 ('Журавлева '
                                                                                                  'Марина '
                                                                                                  'Станиславовна',
                                                                                                  'https://kpfu.ru/marina.zhuravleva'),
                                                                                                 ('Зайцев '
                                                                                                  'Вячеслав '
                                                                                                  'Александрович',
                                                                                                  'https://kpfu.ru/vyacheslav.zajcev'),
                                                                                                 ('Закирова '
                                                                                                  'Найля '
                                                                                                  'Минкаримовна',
                                                                                                  'https://kpfu.ru/najlya.zakirova'),
                                                                                                 ('Залялиева '
                                                                                                  'Ольга '
                                                                                                  'Владимировна',
                                                                                                  'https://kpfu.ru/Olga.Zalyalieva'),
                                                                                                 ('Залялова '
                                                                                                  'Эльмира '
                                                                                                  'Равилевна',
                                                                                                  'https://kpfu.ru/elmira.zalyalova'),
                                                                                                 ('Зарипова '
                                                                                                  'Фарида '
                                                                                                  'Хадиулловна',
                                                                                                  'https://kpfu.ru/Farida.Chemodanova'),
                                                                                                 ('Имамиев '
                                                                                                  'Алмаз '
                                                                                                  'Ильфатович',
                                                                                                  'https://kpfu.ru/almaz.imamiev'),
                                                                                                 ('Кашафутдинов '
                                                                                                  'Владислав '
                                                                                                  'Ренартович',
                                                                                                  'https://kpfu.ru/Vladislav.Kashafutdinov'),
                                                                                                 ('Коржева '
                                                                                                  'Александра '
                                                                                                  'Геннадьевна',
                                                                                                  'https://kpfu.ru/aleksandra.korzheva'),
                                                                                                 ('Курмаев '
                                                                                                  'Зуфар '
                                                                                                  'Фатыхович',
                                                                                                  'https://kpfu.ru/Zufar.Kurmaev'),
                                                                                                 ('Лифанов '
                                                                                                  'Александр '
                                                                                                  'Александрович',
                                                                                                  'https://kpfu.ru/aleksandr.lifanov'),
                                                                                                 ('Лихачев '
                                                                                                  'Владислав '
                                                                                                  'Эдуардович',
                                                                                                  'https://kpfu.ru/Vladislav.Lihachev'),
                                                                                                 ('Макришин '
                                                                                                  'Владимир '
                                                                                                  'Николаевич',
                                                                                                  'https://kpfu.ru/vladimir.makrishin'),
                                                                                                 ('Марахтанова '
                                                                                                  'Валентина '
                                                                                                  'Ивановна',
                                                                                                  'https://kpfu.ru/Valentina.Marachtanova'),
                                                                                                 ('Маслова '
                                                                                                  'Лариса '
                                                                                                  'Петровна',
                                                                                                  'https://kpfu.ru/larisa.maslova'),
                                                                                                 ('Меркулов '
                                                                                                  'Александр '
                                                                                                  'Николаевич',
                                                                                                  'https://kpfu.ru/Aleksandr.Merkulov'),
                                                                                                 ('Минебаев '
                                                                                                  'Наиль '
                                                                                                  'Карамович',
                                                                                                  'https://kpfu.ru/nail.minebaev'),
                                                                                                 ('Мифтахов '
                                                                                                  'Ильдус '
                                                                                                  'Юнусович',
                                                                                                  'https://kpfu.ru/Ildus.Miftahov'),
                                                                                                 ('Мухаметсафин '
                                                                                                  'Рамиль '
                                                                                                  'Сунгатович',
                                                                                                  'https://kpfu.ru/ramil.muhametsafin'),
                                                                                                 ('Никитина '
                                                                                                  'Лилия '
                                                                                                  'Мидхатовна',
                                                                                                  'https://kpfu.ru/liliya.nikitina'),
                                                                                                 ('Нуруллин '
                                                                                                  'Ильшат '
                                                                                                  'Фаридович',
                                                                                                  'https://kpfu.ru/Ilshat.Nurullin'),
                                                                                                 ('Петров '
                                                                                                  'Александр '
                                                                                                  'Евгеньевич',
                                                                                                  'https://kpfu.ru/aleksandre.petrov'),
                                                                                                 ('Ратова '
                                                                                                  'Елена '
                                                                                                  'Николаевна',
                                                                                                  'https://kpfu.ru/elena.ratova'),
                                                                                                 ('Ряузов '
                                                                                                  'Владимир '
                                                                                                  'Григорьевич',
                                                                                                  'https://kpfu.ru/Vladimir.Ryuzov'),
                                                                                                 ('Сабирзянова '
                                                                                                  'Фарида '
                                                                                                  'Фаридовна',
                                                                                                  'https://kpfu.ru/farida.sabirzyanova'),
                                                                                                 ('Садыкова '
                                                                                                  'Альбина '
                                                                                                  'Мидхатовна',
                                                                                                  'https://kpfu.ru/albina.sadykova'),
                                                                                                 ('Салахиев '
                                                                                                  'Ринат '
                                                                                                  'Расифович',
                                                                                                  'https://kpfu.ru/rinat.salahiev'),
                                                                                                 ('Сверигина '
                                                                                                  'Лариса '
                                                                                                  'Аркадьевна',
                                                                                                  'https://kpfu.ru/Larisa.Sverigina'),
                                                                                                 ('Селиванова '
                                                                                                  'Ирина '
                                                                                                  'Владимировна',
                                                                                                  'https://kpfu.ru/Irina.Selivanova'),
                                                                                                 ('Серазетдинова '
                                                                                                  'Лариса '
                                                                                                  'Ильбарсовна',
                                                                                                  'https://kpfu.ru/Larisa.Serazetdinova'),
                                                                                                 ('Сергеева '
                                                                                                  'Наталья '
                                                                                                  'Борисовна',
                                                                                                  'https://kpfu.ru/natalya.sergeeva'),
                                                                                                 ('Сергина '
                                                                                                  'Татьяна '
                                                                                                  'Игоревна',
                                                                                                  'https://kpfu.ru/tatyana.sergina'),
                                                                                                 ('Сунгатуллин '
                                                                                                  'Рафаэль '
                                                                                                  'Иршатович',
                                                                                                  'https://kpfu.ru/rafaeli.sungatullin'),
                                                                                                 ('Сырова '
                                                                                                  'Ирина '
                                                                                                  'Николаевна',
                                                                                                  'https://kpfu.ru/Irina.Syrova'),
                                                                                                 ('Усманова '
                                                                                                  'Светлана '
                                                                                                  'Федоровна',
                                                                                                  'https://kpfu.ru/svetlana.usmanova'),
                                                                                                 ('Утегенова '
                                                                                                  'Нармина '
                                                                                                  'Рашитовна',
                                                                                                  'https://kpfu.ru/Narmina.Utegenova'),
                                                                                                 ('Фомина '
                                                                                                  'Евгения '
                                                                                                  'Владимировна',
                                                                                                  'https://kpfu.ru/evgeniya.fomina'),
                                                                                                 ('Хасанзянов '
                                                                                                  'Ильнар '
                                                                                                  'Исмагилович',
                                                                                                  'https://kpfu.ru/ilnar.hasanzyanov'),
                                                                                                 ('Чумарин '
                                                                                                  'Наиль '
                                                                                                  'Ахметович',
                                                                                                  'https://kpfu.ru/nail.chumarin'),
                                                                                                 ('Шамгунова '
                                                                                                  'Гузель '
                                                                                                  'Марселевна',
                                                                                                  'https://kpfu.ru/Guzel.Shamgunova'),
                                                                                                 ('Шафикова '
                                                                                                  'Наталья '
                                                                                                  'Юрьевна',
                                                                                                  'https://kpfu.ru/Natalia.Schafikova'),
                                                                                                 ('Шашков '
                                                                                                  'Александр '
                                                                                                  'Анатольевич',
                                                                                                  'https://kpfu.ru/aleksandr.shashkov'),
                                                                                                 ('Шершунова '
                                                                                                  'Вера '
                                                                                                  'Николаевна',
                                                                                                  'https://kpfu.ru/vera.shershunova'),
                                                                                                 ('Эмирусайинов '
                                                                                                  'Бекир '
                                                                                                  'Ибрагимович',
                                                                                                  'https://kpfu.ru/Bekir.Emirusainov'),
                                                                                                 ('Халитов '
                                                                                                  'Карим '
                                                                                                  'Фаритович',
                                                                                                  'https://kpfu.ru/karim.khalitov'),
                                                                                                 ('Габдрахманов '
                                                                                                  'Разил '
                                                                                                  'Фанзилович',
                                                                                                  'https://kpfu.ru/razil.gabdrakhmanov'),
                                                                                                 ('Галимов '
                                                                                                  'Динар '
                                                                                                  'Рашитович',
                                                                                                  'https://kpfu.ru/dinar.galimov'),
                                                                                                 ('Данилевская '
                                                                                                  'Дарья '
                                                                                                  'Олеговна',
                                                                                                  'https://kpfu.ru/darya.danilevskaya'),
                                                                                                 ('Данилов '
                                                                                                  'Вадим '
                                                                                                  'Александрович',
                                                                                                  'https://kpfu.ru/vadim.danilov'),
                                                                                                 ('Зимин '
                                                                                                  'Александр '
                                                                                                  'Сергеевич',
                                                                                                  'https://kpfu.ru/aleksandr.zimin'),
                                                                                                 ('Искаков '
                                                                                                  'Никита '
                                                                                                  'Георгиевич',
                                                                                                  'https://kpfu.ru/nikita.iskakov'),
                                                                                                 ('Камалиева '
                                                                                                  'Наталья '
                                                                                                  'Юрьевна',
                                                                                                  'https://kpfu.ru/natalya.kamalieva'),
                                                                                                 ('Леванов '
                                                                                                  'Алексей '
                                                                                                  'Николаевич',
                                                                                                  'https://kpfu.ru/Aleksej.Levanov'),
                                                                                                 ('Леонов '
                                                                                                  'Николай '
                                                                                                  'Владиславович',
                                                                                                  'https://kpfu.ru/nikolaj.leonov'),
                                                                                                 ('Лифанов '
                                                                                                  'Евгений '
                                                                                                  'Валерьевич',
                                                                                                  'https://kpfu.ru/evgenij.lifanov'),
                                                                                                 ('Минигалеева '
                                                                                                  'Альбина '
                                                                                                  'Зуфаровна',
                                                                                                  'https://kpfu.ru/Albina.Minigaleeva'),
                                                                                                 ('Муртазина '
                                                                                                  'Алсу '
                                                                                                  'Ильхамовна',
                                                                                                  'https://kpfu.ru/alsui.murtazina'),
                                                                                                 ('Никитин '
                                                                                                  'Сергей '
                                                                                                  'Валерьевич',
                                                                                                  'https://kpfu.ru/sergej.nikitin'),
                                                                                                 ('Петрова '
                                                                                                  'Валентина '
                                                                                                  'Ивановна',
                                                                                                  'https://kpfu.ru/valentinai.petrova'),
                                                                                                 ('Рихтер '
                                                                                                  'Илья '
                                                                                                  'Константинович',
                                                                                                  'https://kpfu.ru/ilya.rihter'),
                                                                                                 ('Салахова '
                                                                                                  'Наталья '
                                                                                                  'Олеговна',
                                                                                                  'https://kpfu.ru/natalya.salahova'),
                                                                                                 ('Самойленко '
                                                                                                  'Петр '
                                                                                                  'Михайлович',
                                                                                                  'https://kpfu.ru/petr.samoylenko'),
                                                                                                 ('Тевяшова '
                                                                                                  'Венера '
                                                                                                  'Гапасовна',
                                                                                                  'https://kpfu.ru/Venera.Tevjashova'),
                                                                                                 ('Усманова '
                                                                                                  'Елена '
                                                                                                  'Александровна',
                                                                                                  'https://kpfu.ru/Elena.Golovina'),
                                                                                                 ('Файзериев '
                                                                                                  'Ленар '
                                                                                                  'Равилевич',
                                                                                                  'https://kpfu.ru/lenar.fayzeriev'),
                                                                                                 ('Фомина '
                                                                                                  'Елизавета '
                                                                                                  'Борисовна',
                                                                                                  'https://kpfu.ru/elizaveta.fomina'),
                                                                                                 ('Хайруллин '
                                                                                                  'Данис '
                                                                                                  'Рафакатович',
                                                                                                  'https://kpfu.ru/danis.hajrullin'),
                                                                                                 ('Исмагилова '
                                                                                                  'Любовь '
                                                                                                  'Михайловна',
                                                                                                  'https://kpfu.ru/Liubov.Ismagilova'),
                                                                                                 ('Фалеева '
                                                                                                  'Светлана '
                                                                                                  'Александровна',
                                                                                                  'https://kpfu.ru/svetlana.faleeva'),
                                                                                                 ('Ахметшина '
                                                                                                  'Фарида '
                                                                                                  'Рафкатовна',
                                                                                                  'https://kpfu.ru/Farida.Akhmetshina'),
                                                                                                 ('Мазлова '
                                                                                                  'Наталья '
                                                                                                  'Олеговна',
                                                                                                  'https://kpfu.ru/natalya.mazlova'),
                                                                                                 ('Хайруллина '
                                                                                                  'Гельсария '
                                                                                                  'Васильевна',
                                                                                                  'https://kpfu.ru/Gelsaria.Hairullina')]},
            'Химический институт им. А.М. Бутлерова': {'Кафедра аналитической химии': [('Евтюгин '
                                                                                        'Геннадий '
                                                                                        'Артурович',
                                                                                        'https://kpfu.ru/Gennady.Evtugyn'),
                                                                                       ('Будников '
                                                                                        'Герман '
                                                                                        'Константинович',
                                                                                        'https://kpfu.ru/Herman.Budnikov'),
                                                                                       ('Медянцева '
                                                                                        'Эльвина '
                                                                                        'Павловна',
                                                                                        'https://kpfu.ru/Elvina.Medyantseva'),
                                                                                       ('Шайдарова '
                                                                                        'Лариса '
                                                                                        'Геннадиевна',
                                                                                        'https://kpfu.ru/Larisa.Shaidarova'),
                                                                                       ('Зиятдинова '
                                                                                        'Гузель '
                                                                                        'Камилевна',
                                                                                        'https://kpfu.ru/Guzel.Ziyatdinova'),
                                                                                       ('Гарифзянов '
                                                                                        'Айрат '
                                                                                        'Ризванович',
                                                                                        'https://kpfu.ru/Airat.Garifzyanov'),
                                                                                       ('Гедмина '
                                                                                        'Анна '
                                                                                        'Владимировна',
                                                                                        'https://kpfu.ru/Anna.Gedmina'),
                                                                                       ('Челнокова '
                                                                                        'Ирина '
                                                                                        'Александровна',
                                                                                        'https://kpfu.ru/Irina.Chelnokova'),
                                                                                       ('Порфирьева '
                                                                                        'Анна '
                                                                                        'Вениаминовна',
                                                                                        'https://kpfu.ru/Anna.Porfireva'),
                                                                                       ('Брусницын '
                                                                                        'Даниил '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/daniil.brusnicyn'),
                                                                                       ('Ильина '
                                                                                        'Марина '
                                                                                        'Андреевна',
                                                                                        'https://kpfu.ru/marina.degteva'),
                                                                                       ('Белякова '
                                                                                        'Светлана '
                                                                                        'Викторовна',
                                                                                        'https://kpfu.ru/Svetlana.Belyakova'),
                                                                                       ('Кузин '
                                                                                        'Юрий '
                                                                                        'Иванович',
                                                                                        'https://kpfu.ru/jurij.kuzin'),
                                                                                       ('Гафиатова '
                                                                                        'Ильвина '
                                                                                        'Азатовна',
                                                                                        'https://kpfu.ru/ilvina.abzalova'),
                                                                                       ('Лексина '
                                                                                        'Юлия '
                                                                                        'Александровна',
                                                                                        'https://kpfu.ru/juliya.leksina'),
                                                                                       ('Сорвин '
                                                                                        'Михаил '
                                                                                        'Игоревич',
                                                                                        'https://kpfu.ru/mihail.sorvin'),
                                                                                       ('Чибирев '
                                                                                        'Егор '
                                                                                        'Олегович',
                                                                                        'https://kpfu.ru/egor.chibirev'),
                                                                                       ('Бейлинсон '
                                                                                        'Регина '
                                                                                        'Марковна',
                                                                                        'https://kpfu.ru/Regina.Varlamova'),
                                                                                       ('Хонина '
                                                                                        'Ирина '
                                                                                        'Вадимовна',
                                                                                        'https://kpfu.ru/irina.honina'),
                                                                                       ('Зиганшина '
                                                                                        'Эндже '
                                                                                        'Ришатовна',
                                                                                        'https://kpfu.ru/Endzhe.Ziganshina'),
                                                                                       ('Чистова '
                                                                                        'Валентина '
                                                                                        'Александровна',
                                                                                        'https://kpfu.ru/valentina.chistova'),
                                                                                       ('Ласкина '
                                                                                        'Элина '
                                                                                        'Фларидовна',
                                                                                        'https://kpfu.ru/elina.laskina'),
                                                                                       ('Кашапова '
                                                                                        'Ирина '
                                                                                        'Ильязовна',
                                                                                        'https://kpfu.ru/Irina.Kashapova'),
                                                                                       ('Якупова '
                                                                                        'Эльвира '
                                                                                        'Наилевна',
                                                                                        'https://kpfu.ru/elvira.yakupova')],
                                                       'Кафедра высокомолекулярных и элементоорганических соединений': [
                                                           ('Галкина '
                                                            'Ирина '
                                                            'Васильевна',
                                                            'https://kpfu.ru/1Irina.Galkina'),
                                                           ('Низамов '
                                                            'Ильяс '
                                                            'Саидович',
                                                            'https://kpfu.ru/Ilyas.Nizamov'),
                                                           ('Черкасов '
                                                            'Рафаэль '
                                                            'Асхатович',
                                                            'https://kpfu.ru/Rafael.Cherkasov'),
                                                           ('Катаева '
                                                            'Ольга '
                                                            'Николаевна',
                                                            'https://kpfu.ru/Olga.Kataeva'),
                                                           ('Бахтиярова '
                                                            'Юлия '
                                                            'Валерьевна',
                                                            'https://kpfu.ru/Julia.Bakhtiyarova'),
                                                           ('Ивкова '
                                                            'Гульнара '
                                                            'Аскаровна',
                                                            'https://kpfu.ru/Gulnara.Ivkova'),
                                                           ('Салин '
                                                            'Алексей '
                                                            'Валерьевич',
                                                            'https://kpfu.ru/Alexey.Salin'),
                                                           ('Ильин '
                                                            'Антон '
                                                            'Викторович',
                                                            'https://kpfu.ru/Anton.Ilin'),
                                                           ('Тудрий '
                                                            'Елена '
                                                            'Вадимовна',
                                                            'https://kpfu.ru/elena.tudrij'),
                                                           ('Давлетшин '
                                                            'Рустам '
                                                            'Рифхатович',
                                                            'https://kpfu.ru/rustamr.davletshin'),
                                                           ('Колпакова '
                                                            'Елена '
                                                            'Владимировна',
                                                            'https://kpfu.ru/elena.kolpakova'),
                                                           ('Ямалиева '
                                                            'Луиза '
                                                            'Нурмухаметовна',
                                                            'https://kpfu.ru/Luisa.Yamaliewa'),
                                                           ('Давлетшина '
                                                            'Наталья '
                                                            'Викторовна',
                                                            'https://kpfu.ru/natalya.davletshina'),
                                                           ('Хаяров '
                                                            'Хасан '
                                                            'Рафаэлевич',
                                                            'https://kpfu.ru/Khasan.Khayarov'),
                                                           ('Романов '
                                                            'Семен '
                                                            'Романович',
                                                            'https://kpfu.ru/semenr.romanov'),
                                                           ('Гайнеев '
                                                            'Айдар '
                                                            'Маратович',
                                                            'https://kpfu.ru/aydar.gayneev'),
                                                           ('Ежова '
                                                            'Галина '
                                                            'Викторовна',
                                                            'https://kpfu.ru/galina.ezhova'),
                                                           ('Шильникова '
                                                            'Ольга '
                                                            'Викторовна',
                                                            'https://kpfu.ru/olga.shilnikova')],
                                                       'Кафедра медицинской химии': [('Племенков '
                                                                                      'Виталий '
                                                                                      'Владимирович',
                                                                                      'https://kpfu.ru/vitalij.plemenkov'),
                                                                                     ('Агафонова '
                                                                                      'Мария '
                                                                                      'Николаевна',
                                                                                      'https://kpfu.ru/Mariya.Agafonova'),
                                                                                     ('Шурпик '
                                                                                      'Дмитрий '
                                                                                      'Николаевич',
                                                                                      'https://kpfu.ru/main?p_id=36684'),
                                                                                     ('Газизова '
                                                                                      'Асия '
                                                                                      'Фаниловна',
                                                                                      'https://kpfu.ru/asiyaf.gazizova'),
                                                                                     ('Назарова '
                                                                                      'Анастасия '
                                                                                      'Александровна',
                                                                                      'https://kpfu.ru/anastasiya.nazarova'),
                                                                                     ('Шибаева '
                                                                                      'Ксения '
                                                                                      'Сергеевна',
                                                                                      'https://kpfu.ru/kseniya.shibaeva'),
                                                                                     ('Пономарев '
                                                                                      'Денис '
                                                                                      'Вячеславович',
                                                                                      'https://kpfu.ru/denis.ponomarev'),
                                                                                     ('Сайгитбаталова '
                                                                                      'Елена '
                                                                                      'Шириповна',
                                                                                      'https://kpfu.ru/elena.sajgitbatalova'),
                                                                                     ('Мирзаянов '
                                                                                      'Ильдар '
                                                                                      'Ирекович',
                                                                                      'https://kpfu.ru/ildar.mirzayanov'),
                                                                                     ('Ахмадуллина '
                                                                                      'Лилия '
                                                                                      'Ильгизовна',
                                                                                      'https://kpfu.ru/liliya.akhmadullina')],
                                                       'Кафедра неорганической химии': [('Амиров '
                                                                                         'Рустэм '
                                                                                         'Рафаэльевич',
                                                                                         'https://kpfu.ru/Rustem.Amirov'),
                                                                                        ('Амирова '
                                                                                         'Лилия '
                                                                                         'Миниахмедовна',
                                                                                         'https://kpfu.ru/liliya.amirova'),
                                                                                        ('Девятов '
                                                                                         'Федор '
                                                                                         'Владимирович',
                                                                                         'https://kpfu.ru/Fedor.Devyatov'),
                                                                                        ('Улахович '
                                                                                         'Николай '
                                                                                         'Алексеевич',
                                                                                         'https://kpfu.ru/Nikolay.Ulakhovich'),
                                                                                        ('Чевела '
                                                                                         'Владимир '
                                                                                         'Всеволодович',
                                                                                         'https://kpfu.ru/Vladimir.Chevela'),
                                                                                        ('Бычкова '
                                                                                         'Тамара '
                                                                                         'Ильинична',
                                                                                         'https://kpfu.ru/Tamara.Bychkova'),
                                                                                        ('Гатаулина '
                                                                                         'Альфия '
                                                                                         'Ринатовна',
                                                                                         'https://kpfu.ru/Alfiya.Gataulina'),
                                                                                        ('Журавлева '
                                                                                         'Юлия '
                                                                                         'Игоревна',
                                                                                         'https://kpfu.ru/Yulia.Zyavkina'),
                                                                                        ('Зиятдинова '
                                                                                         'Анна '
                                                                                         'Булатовна',
                                                                                         'https://kpfu.ru/Anna.Ziyatdinova'),
                                                                                        ('Кутырева '
                                                                                         'Марианна '
                                                                                         'Петровна',
                                                                                         'https://kpfu.ru/Marianna.Kutyreva'),
                                                                                        ('Штырлин '
                                                                                         'Валерий '
                                                                                         'Григорьевич',
                                                                                         'https://kpfu.ru/Valery.Shtyrlin'),
                                                                                        ('Андрианова '
                                                                                         'Кристина '
                                                                                         'Александровна',
                                                                                         'https://kpfu.ru/kristina.andrianova'),
                                                                                        ('Бухаров '
                                                                                         'Михаил '
                                                                                         'Сергеевич',
                                                                                         'https://kpfu.ru/Mihail.Buharov'),
                                                                                        ('Иванова '
                                                                                         'Валентина '
                                                                                         'Юрьевна',
                                                                                         'https://kpfu.ru/Valentina.Ivanova'),
                                                                                        ('Гоголашвили '
                                                                                         'Эдуард '
                                                                                         'Лаврентьевич',
                                                                                         'https://kpfu.ru/eduard.gogolashvili'),
                                                                                        ('Бурилова '
                                                                                         'Евгения '
                                                                                         'Александровна',
                                                                                         'https://kpfu.ru/evgeniya.burilova'),
                                                                                        ('Игнатьева '
                                                                                         'Клара '
                                                                                         'Александровна',
                                                                                         'https://kpfu.ru/Klara.Ignatyeva'),
                                                                                        ('Ханнанов '
                                                                                         'Артур '
                                                                                         'Айдарович',
                                                                                         'https://kpfu.ru/artur.hannanov'),
                                                                                        ('Ахмерова '
                                                                                         'Рякибя '
                                                                                         'Султановна',
                                                                                         'https://kpfu.ru/Ryakibya.Ahmerova'),
                                                                                        ('Ибрагимова '
                                                                                         'Зиля '
                                                                                         'Зайтуновна',
                                                                                         'https://kpfu.ru/zilya.ibragimova'),
                                                                                        ('Кукушкина '
                                                                                         'Ольга '
                                                                                         'Викторовна',
                                                                                         'https://kpfu.ru/Olga.Kukushckina'),
                                                                                        ('Рубанов '
                                                                                         'Алексей '
                                                                                         'Владимирович',
                                                                                         'https://kpfu.ru/Alexey.Rubanov'),
                                                                                        ('Шайымова '
                                                                                         'Юлия '
                                                                                         'Рахманкуловна',
                                                                                         'https://kpfu.ru/juliya.shajymova'),
                                                                                        ('Захаров '
                                                                                         'Алексей '
                                                                                         'Васильевич',
                                                                                         'https://kpfu.ru/Alexey.Zakharov'),
                                                                                        ('Балькаев '
                                                                                         'Динар '
                                                                                         'Ансарович',
                                                                                         'https://kpfu.ru/dinar.balkaev'),
                                                                                        ('Боос '
                                                                                         'Галина '
                                                                                         'Арведовна',
                                                                                         'https://kpfu.ru/Galina.Boos'),
                                                                                        ('Серов '
                                                                                         'Никита '
                                                                                         'Юрьевич',
                                                                                         'https://kpfu.ru/Nikita.Serov')],
                                                       'Кафедра органической химии': [('Антипин '
                                                                                       'Игорь '
                                                                                       'Сергеевич',
                                                                                       'https://kpfu.ru/Igor.Antipin'),
                                                                                      ('Каратаева '
                                                                                       'Фарида '
                                                                                       'Хайдаровна',
                                                                                       'https://kpfu.ru/Farida.Karataeva'),
                                                                                      ('Коновалов '
                                                                                       'Александр '
                                                                                       'Иванович',
                                                                                       'https://kpfu.ru/aleksandr.konovalov'),
                                                                                      ('Миронов '
                                                                                       'Владимир '
                                                                                       'Федорович',
                                                                                       'https://kpfu.ru/Vladimir.Mironov'),
                                                                                      ('Стойков '
                                                                                       'Иван '
                                                                                       'Иванович',
                                                                                       'https://kpfu.ru/Ivan.Stoikov'),
                                                                                      ('Чмутова '
                                                                                       'Галина '
                                                                                       'Алексеевна',
                                                                                       'https://kpfu.ru/Galina.Tschmutowa'),
                                                                                      ('Соловьева '
                                                                                       'Светлана '
                                                                                       'Евгеньевна',
                                                                                       'https://kpfu.ru/svetlanae.soloveva'),
                                                                                      ('Балакина '
                                                                                       'Марина '
                                                                                       'Юрьевна',
                                                                                       'https://kpfu.ru/marina.balakina'),
                                                                                      ('Бурилов '
                                                                                       'Владимир '
                                                                                       'Александрович',
                                                                                       'https://kpfu.ru/Vladimir.Burilov'),
                                                                                      ('Казымова '
                                                                                       'Марина '
                                                                                       'Александровна',
                                                                                       'https://kpfu.ru/Marina.Kazymova'),
                                                                                      ('Курбангалиева '
                                                                                       'Альмира '
                                                                                       'Рафаэловна',
                                                                                       'https://kpfu.ru/Almira.Kurbangalieva'),
                                                                                      ('Немтарев '
                                                                                       'Андрей '
                                                                                       'Владимирович',
                                                                                       'https://kpfu.ru/andrej.nemtarev'),
                                                                                      ('Татаринов '
                                                                                       'Дмитрий '
                                                                                       'Анатольевич',
                                                                                       'https://kpfu.ru/dmitrij.tatarinov'),
                                                                                      ('Якимова '
                                                                                       'Людмила '
                                                                                       'Сергеевна',
                                                                                       'https://kpfu.ru/Luidmila.Savelyeva'),
                                                                                      ('Маджидов '
                                                                                       'Тимур '
                                                                                       'Исмаилович',
                                                                                       'https://kpfu.ru/Timur.Madzhidov'),
                                                                                      ('Нугманов '
                                                                                       'Рамиль '
                                                                                       'Ирекович',
                                                                                       'https://kpfu.ru/ramil.nugmanov'),
                                                                                      ('Бочкова '
                                                                                       'Ольга '
                                                                                       'Дмитриевна',
                                                                                       'https://kpfu.ru/olga.bochkova'),
                                                                                      ('Вавилова '
                                                                                       'Алёна '
                                                                                       'Артёмовна',
                                                                                       'https://kpfu.ru/Aljona.Jantemirova'),
                                                                                      ('Латыпова '
                                                                                       'Лилия '
                                                                                       'Зиннуровна',
                                                                                       'https://kpfu.ru/Lilija.Latypova'),
                                                                                      ('Макшакова '
                                                                                       'Ольга '
                                                                                       'Николаевна',
                                                                                       'https://kpfu.ru/olga.makshakova'),
                                                                                      ('Миронова '
                                                                                       'Диана '
                                                                                       'Александровна',
                                                                                       'https://kpfu.ru/diana.mironova'),
                                                                                      ('Султанова '
                                                                                       'Эльза '
                                                                                       'Дамировна',
                                                                                       'https://kpfu.ru/elza.sultanova'),
                                                                                      ('Агарков '
                                                                                       'Артем '
                                                                                       'Сергеевич',
                                                                                       'https://kpfu.ru/artem.agarkov'),
                                                                                      ('Афонина '
                                                                                       'Валентина '
                                                                                       'Александровна',
                                                                                       'https://kpfu.ru/valentina.afonina'),
                                                                                      ('Шалин '
                                                                                       'Никита '
                                                                                       'Иванович',
                                                                                       'https://kpfu.ru/nikita.shalin'),
                                                                                      ('Мостовая '
                                                                                       'Ольга '
                                                                                       'Александровна',
                                                                                       'https://kpfu.ru/Olga.Mostovaya'),
                                                                                      ('Мухамедшина '
                                                                                       'Маршида '
                                                                                       'Ильдусовна',
                                                                                       'https://kpfu.ru/Marchida.Muhamedchina'),
                                                                                      ('Харахашьян '
                                                                                       'Георгий '
                                                                                       'Эдуардович',
                                                                                       'https://kpfu.ru/georgij.kharakhashyan')],
                                                       'Кафедра физической химии': [('Соломонов '
                                                                                     'Борис '
                                                                                     'Николаевич',
                                                                                     'https://kpfu.ru/Boris.Solomonov'),
                                                                                    ('Верещагина '
                                                                                     'Яна '
                                                                                     'Александровна',
                                                                                     'https://kpfu.ru/Jana.Vereschagina'),
                                                                                    ('Горбачук '
                                                                                     'Валерий '
                                                                                     'Виленович',
                                                                                     'https://kpfu.ru/Valery.Gorbatchuk'),
                                                                                    ('Киселев '
                                                                                     'Владимир '
                                                                                     'Дмитриевич',
                                                                                     'https://kpfu.ru/Vladimir.Kiselev'),
                                                                                    ('Ламберов '
                                                                                     'Александр '
                                                                                     'Адольфович',
                                                                                     'https://kpfu.ru/Alexander.Lamberov'),
                                                                                    ('Егорова '
                                                                                     'Светлана '
                                                                                     'Робертовна',
                                                                                     'https://kpfu.ru/Svetlana.Egorova'),
                                                                                    ('Зиганшин '
                                                                                     'Марат '
                                                                                     'Ахмедович',
                                                                                     'https://kpfu.ru/Marat.Ziganshin'),
                                                                                    ('Седов '
                                                                                     'Игорь '
                                                                                     'Алексеевич',
                                                                                     'https://kpfu.ru/Igor.Sedov'),
                                                                                    ('Варфоломеев '
                                                                                     'Михаил '
                                                                                     'Алексеевич',
                                                                                     'https://kpfu.ru/Mikhail.Varfolomeev'),
                                                                                    ('Лисицын '
                                                                                     'Юрий '
                                                                                     'Анатольевич',
                                                                                     'https://kpfu.ru/Yuri.Lisitsyn'),
                                                                                    ('Новиков '
                                                                                     'Владимир '
                                                                                     'Борисович',
                                                                                     'https://kpfu.ru/Vladimir.Novikov'),
                                                                                    ('Сироткин '
                                                                                     'Владимир '
                                                                                     'Александрович',
                                                                                     'https://kpfu.ru/Vladimir.Sirotkin'),
                                                                                    ('Галухин '
                                                                                     'Андрей '
                                                                                     'Владимирович',
                                                                                     'https://kpfu.ru/Andrej.Galuhin'),
                                                                                    ('Герасимов '
                                                                                     'Александр '
                                                                                     'Владимирович',
                                                                                     'https://kpfu.ru/Alexander.Gerasimov'),
                                                                                    ('Заиров '
                                                                                     'Рустэм '
                                                                                     'Равилевич',
                                                                                     'https://kpfu.ru/rustem.zairov'),
                                                                                    ('Ильясов '
                                                                                     'Ильдар '
                                                                                     'Равилевич',
                                                                                     'https://kpfu.ru/Ildar.Ilyasov'),
                                                                                    ('Мухаметзянов '
                                                                                     'Тимур '
                                                                                     'Анварович',
                                                                                     'https://kpfu.ru/Timur.Mukhametzyanov'),
                                                                                    ('Нагриманов '
                                                                                     'Руслан '
                                                                                     'Наильевич',
                                                                                     'https://kpfu.ru/ruslan.nagrimanov'),
                                                                                    ('Гатиатулин '
                                                                                     'Аскар '
                                                                                     'Камилевич',
                                                                                     'https://kpfu.ru/Askar.Gatiatulin'),
                                                                                    ('Климовицкий '
                                                                                     'Александр '
                                                                                     'Евгеньевич',
                                                                                     'https://kpfu.ru/Alexander.Klimovitskii'),
                                                                                    ('Корнилов '
                                                                                     'Дмитрий '
                                                                                     'Анатольевич',
                                                                                     'https://kpfu.ru/dmitrij.kornilov'),
                                                                                    ('Носов '
                                                                                     'Роман '
                                                                                     'Валериевич',
                                                                                     'https://kpfu.ru/roman.nosov'),
                                                                                    ('Ракипов '
                                                                                     'Ильназ '
                                                                                     'Тагирович',
                                                                                     'https://kpfu.ru/Ilnaz.Rakipov'),
                                                                                    ('Сухов '
                                                                                     'Александр '
                                                                                     'Вячеславович',
                                                                                     'https://kpfu.ru/Aleksandr.Suhov'),
                                                                                    ('Хачатрян '
                                                                                     'Арташес '
                                                                                     'Абраамович',
                                                                                     'https://kpfu.ru/artashes.hachatryan'),
                                                                                    ('Ягофаров '
                                                                                     'Михаил '
                                                                                     'Искандерович',
                                                                                     'https://kpfu.ru/mihail.yagofarov'),
                                                                                    ('Болматенков '
                                                                                     'Дмитрий  '
                                                                                     'Николаевич',
                                                                                     'https://kpfu.ru/dmitrij.bolmatenkov'),
                                                                                    ('Лукин '
                                                                                     'Руслан '
                                                                                     'Юрьевич',
                                                                                     'https://kpfu.ru/ruslan.lukin'),
                                                                                    ('Магсумов '
                                                                                     'Тимур '
                                                                                     'Ильнурович',
                                                                                     'https://kpfu.ru/timur.magsumov'),
                                                                                    ('Хайбрахманова '
                                                                                     'Диляра '
                                                                                     'Раисовна',
                                                                                     'https://kpfu.ru/dilyara.hajbrahmanova'),
                                                                                    ('Саматов '
                                                                                     'Айзат '
                                                                                     'Алмазович',
                                                                                     'https://kpfu.ru/ajzat.samatov'),
                                                                                    ('Бусыгина '
                                                                                     'Наталья '
                                                                                     'Владимировна',
                                                                                     'https://kpfu.ru/Natalya.Busygina'),
                                                                                    ('Воронцова '
                                                                                     'Людмила '
                                                                                     'Михайловна',
                                                                                     'https://kpfu.ru/ljudmila.voroncova'),
                                                                                    ('Загуменнов '
                                                                                     'Владимир '
                                                                                     'Александрович',
                                                                                     'https://kpfu.ru/Vladimir.Zagumennov'),
                                                                                    ('Манапова '
                                                                                     'Лаура '
                                                                                     'Закиевна',
                                                                                     'https://kpfu.ru/Laura.Manapova'),
                                                                                    ('Сафиуллина '
                                                                                     'Айсылу '
                                                                                     'Сибгатовна',
                                                                                     'https://kpfu.ru/ajsylu.safiullina'),
                                                                                    ('Фатхутдинова '
                                                                                     'Алиса '
                                                                                     'Амировна',
                                                                                     'https://kpfu.ru/alisa.fatkhutdinova'),
                                                                                    ('Кузнецова '
                                                                                     'Анастасия '
                                                                                     'Андреевна',
                                                                                     'https://kpfu.ru/anastasiyaa.kuznecova'),
                                                                                    ('Осельская '
                                                                                     'Виктория '
                                                                                     'Юрьевна',
                                                                                     'https://kpfu.ru/viktoriya.oselskaya')],
                                                       'Кафедра химического образования': [('Гильманшина '
                                                                                            'Сурия '
                                                                                            'Ирековна',
                                                                                            'https://kpfu.ru/suriya.gilmanshina'),
                                                                                           ('Ямбушев '
                                                                                            'Фарид '
                                                                                            'Джамалетдинович',
                                                                                            'https://kpfu.ru/farid.yambushev'),
                                                                                           ('Камалеева '
                                                                                            'Алсу '
                                                                                            'Рауфовна',
                                                                                            'https://kpfu.ru/alsu.kamaleeva'),
                                                                                           ('Журавлева '
                                                                                            'Юлия '
                                                                                            'Игоревна',
                                                                                            'https://kpfu.ru/Yulia.Zyavkina'),
                                                                                           ('Космодемьянская '
                                                                                            'Светлана '
                                                                                            'Сергеевна',
                                                                                            'https://kpfu.ru/svetlana.kosmodemyanskaya'),
                                                                                           ('Низамов '
                                                                                            'Ильнар '
                                                                                            'Дамирович',
                                                                                            'https://kpfu.ru/ilnar.nizamov'),
                                                                                           ('Сагитова '
                                                                                            'Римма '
                                                                                            'Надыровна',
                                                                                            'https://kpfu.ru/rimma.sagitova'),
                                                                                           ('Махмутова '
                                                                                            'Гузель '
                                                                                            'Фаргатовна',
                                                                                            'https://kpfu.ru/1Guzel.Mahmutova'),
                                                                                           ('Халикова '
                                                                                            'Фидалия '
                                                                                            'Дамировна',
                                                                                            'https://kpfu.ru/fidaliya.halikova'),
                                                                                           ('Гилязетдинов '
                                                                                            'Эдуард '
                                                                                            'Махмутович',
                                                                                            'https://kpfu.ru/Eduard.Gilyazetdinov'),
                                                                                           ('Мельникова '
                                                                                            'Гульнар '
                                                                                            'Фаритовна',
                                                                                            'https://kpfu.ru/Gulnar.Valitova'),
                                                                                           ('Арентова '
                                                                                            'Рамзия '
                                                                                            'Сэнжэловна',
                                                                                            'https://kpfu.ru/ramziya.arentova'),
                                                                                           ('Гайфуллина '
                                                                                            'Айгуль '
                                                                                            'Закизяновна',
                                                                                            'https://kpfu.ru/ajgul.gajfullina'),
                                                                                           ('Дарземанова '
                                                                                            'Диляра '
                                                                                            'Ленаровна',
                                                                                            'https://kpfu.ru/dilyara.darzemanova'),
                                                                                           ('Кадырова '
                                                                                            'Илюза '
                                                                                            'Айдаровна',
                                                                                            'https://kpfu.ru/ilyuza.kadyrova'),
                                                                                           ('Миннахметова '
                                                                                            'Виктория '
                                                                                            'Андреевна',
                                                                                            'https://kpfu.ru/viktoriya.minnakhmetova'),
                                                                                           ('Гумерова '
                                                                                            'Фирюза '
                                                                                            'Муллаяновна',
                                                                                            'https://kpfu.ru/firjuza.gumerova'),
                                                                                           ('Хамидуллина '
                                                                                            'Гузель '
                                                                                            'Гайнановна',
                                                                                            'https://kpfu.ru/guzelg.hamidullina'),
                                                                                           ('Акчурина '
                                                                                            'Айгуль '
                                                                                            'Ренатовна',
                                                                                            'https://kpfu.ru/aygul.akchurina'),
                                                                                           ('Назарова '
                                                                                            'Валерия '
                                                                                            'Сергеевна',
                                                                                            'https://kpfu.ru/valeriya.nazarova'),
                                                                                           ('Шульга '
                                                                                            'Виктория '
                                                                                            'Андреевна',
                                                                                            'https://kpfu.ru/viktoriya.shulga')]},
            'Юридический факультет': {'Кафедра гражданского права': [('Альмиева Лейсан '
                                                                      'Ильдусовна',
                                                                      'https://kpfu.ru/Leysan.Husnutdinova'),
                                                                     ('Арсланов Камиль '
                                                                      'Маратович',
                                                                      'http://kpfu.ru/main?p_id=10119'),
                                                                     ('Ахметьянова Замира '
                                                                      'Асраровна',
                                                                      'http://kpfu.ru/main?p_id=26221'),
                                                                     ('Гараева Гелюса '
                                                                      'Хадиевна',
                                                                      'http://kpfu.ru/Geljusa.Garaeva'),
                                                                     ('Гафиятуллина Дарья '
                                                                      'Дмитриевна',
                                                                      'https://kpfu.ru/darya.firsova'),
                                                                     ('Гилязова Екатерина '
                                                                      'Евгеньевна',
                                                                      'https://kpfu.ru/ekaterina.gilyazova'),
                                                                     ('Давлетшин Айрат '
                                                                      'Рамилевич',
                                                                      'http://kpfu.ru/ayrat.davletshin'),
                                                                     ('Давыдова Гузель '
                                                                      'Наилевна',
                                                                      'https://kpfu.ru/guzel.davydova'),
                                                                     ('Демиева Айнур '
                                                                      'Габдульбаровна',
                                                                      'http://kpfu.ru/main?p_id=23188'),
                                                                     ('Егоров Константин '
                                                                      'Валентинович',
                                                                      'https://kpfu.ru/konstantin.egorov'),
                                                                     ('Карягин Николай '
                                                                      'Егорович',
                                                                      'http://kpfu.ru/main?p_id=10124'),
                                                                     ('Кобчикова Елена '
                                                                      'Васильевна',
                                                                      'http://kpfu.ru/main?p_id=32650'),
                                                                     ('Макаров Тимофей '
                                                                      'Григорьевич',
                                                                      'http://kpfu.ru/main?p_id=23186'),
                                                                     ('Низамиева Ольга '
                                                                      'Николаевна',
                                                                      'http://kpfu.ru/main?p_id=10127'),
                                                                     ('Опыхтина Елена '
                                                                      'Генриховна',
                                                                      'http://kpfu.ru/main?p_id=27136'),
                                                                     ('Салихов Ильсур '
                                                                      'Ильгизович',
                                                                      'http://kpfu.ru/main?p_id=10130'),
                                                                     ('Самигуллина Айгуль '
                                                                      'Фаритовна',
                                                                      'http://kpfu.ru/main?p_id=20932'),
                                                                     ('Серкова Юлия '
                                                                      'Анатольевна',
                                                                      'http://kpfu.ru/main?p_id=10132'),
                                                                     ('Хабиров Артур '
                                                                      'Ильфарович',
                                                                      'http://kpfu.ru/artur.habirov'),
                                                                     ('Хамидуллина Фарида '
                                                                      'Ильдаровна',
                                                                      'http://kpfu.ru/main?p_id=10133')],
                                      'Кафедра конституционного и административного права': [('Адамова '
                                                                                              'Элла '
                                                                                              'Роландовна',
                                                                                              'http://kpfu.ru/main?p_id=20461'),
                                                                                             ('Алиуллов '
                                                                                              'Рашид '
                                                                                              'Рахимуллович',
                                                                                              'http://kpfu.ru/main?p_id=27289'),
                                                                                             ('Амирова '
                                                                                              'Римма '
                                                                                              'Рашитовна',
                                                                                              'http://kpfu.ru/main?p_id=10136'),
                                                                                             ('Барабанова '
                                                                                              'Светлана '
                                                                                              'Васильевна',
                                                                                              'https://kpfu.ru/svetlana.barabanova'),
                                                                                             ('Бухмин '
                                                                                              'Сергей '
                                                                                              'Владимирович ',
                                                                                              'http://kpfu.ru/main?p_id=22285'),
                                                                                             ('Валиуллин '
                                                                                              'Динар '
                                                                                              'Айратович',
                                                                                              'https://kpfu.ru/dinar.valiullin'),
                                                                                             ('Валиуллин '
                                                                                              'Фидаиль '
                                                                                              'Фаридович',
                                                                                              'http://kpfu.ru/fidail.valiullin'),
                                                                                             ('Гадыльшина '
                                                                                              'Зухра '
                                                                                              'Ильдаровна',
                                                                                              'http://kpfu.ru/main?p_id=10138'),
                                                                                             ('Гатауллин '
                                                                                              'Анас '
                                                                                              'Газизович',
                                                                                              'http://kpfu.ru/main?p_id=27575'),
                                                                                             ('Железнов '
                                                                                              'Борис '
                                                                                              'Леонидович',
                                                                                              'http://kpfu.ru/main?p_id=10139'),
                                                                                             ('Кириллова '
                                                                                              'Юлия '
                                                                                              'Владимировна',
                                                                                              'http://kpfu.ru/main?p_id=22794&p_lang=&p_type=1'),
                                                                                             ('Курманов '
                                                                                              'Мидхат '
                                                                                              'Мазгутович',
                                                                                              'http://kpfu.ru/main?p_id=22715'),
                                                                                             ('Малый '
                                                                                              'Александр '
                                                                                              'Федорович',
                                                                                              'http://kpfu.ru/main?p_id=30238'),
                                                                                             ('Мустафина '
                                                                                              'Ляйсан '
                                                                                              'Ринатовна',
                                                                                              'https://kpfu.ru/Leisan.Mirsaeva'),
                                                                                             ('Нигметзянов\xa0'
                                                                                              'Алмаз '
                                                                                              'Альбертович',
                                                                                              'https://kpfu.ru/almaz.nigmetzyanov'),
                                                                                             ('Никитенко '
                                                                                              'Игорь '
                                                                                              'Геннадиевич',
                                                                                              'http://kpfu.ru/main?p_id=22202'),
                                                                                             ('Султанов '
                                                                                              'Евгений '
                                                                                              'Батырович',
                                                                                              'http://kpfu.ru/main?p_id=10146'),
                                                                                             ('Тарасов '
                                                                                              'Артем '
                                                                                              'Сергеевич',
                                                                                              'http://kpfu.ru/artem.tarasov'),
                                                                                             ('Файзрахманова '
                                                                                              'Лейсан '
                                                                                              'Миннуровна',
                                                                                              'http://kpfu.ru/Lejsan.Fajzrahmanova'),
                                                                                             ('Хабибуллина '
                                                                                              'Гульнара '
                                                                                              'Рушановна',
                                                                                              'http://kpfu.ru/main?p_id=10149'),
                                                                                             ('Хурматуллина '
                                                                                              'Алсу '
                                                                                              'Махмутовна',
                                                                                              'http://kpfu.ru/main?p_id=36462'),
                                                                                             ('Хусаинов '
                                                                                              'Зуфар '
                                                                                              'Фаатович',
                                                                                              'http://kpfu.ru/main?p_id=10150'),
                                                                                             ('Чулюкин '
                                                                                              'Илья '
                                                                                              'Львович',
                                                                                              'http://kpfu.ru/main?p_id=10151'),
                                                                                             ('Шмелева '
                                                                                              'Ольга '
                                                                                              'Геннадьевна',
                                                                                              'https://kpfu.ru/olga.shmeleva')],
                                      'Кафедра международного и европейского права': [('Абдуллин '
                                                                                       'Адель '
                                                                                       'Ильсиярович',
                                                                                       'http://kpfu.ru/main?p_id=27193'),
                                                                                      ('Афхазава '
                                                                                       'Дурмишхан '
                                                                                       'Гивиевич',
                                                                                       'http://kpfu.ru/durmishhan.afhazava'),
                                                                                      ('Баширов '
                                                                                       'Эльдар '
                                                                                       'Гюльмирзаевич',
                                                                                       'https://kpfu.ru/eldar.bashirov'),
                                                                                      ('Бодурова '
                                                                                       'Гулшан '
                                                                                       'Гурезовна',
                                                                                       'https://kpfu.ru/gulshan.bodurova'),
                                                                                      ('Валеев '
                                                                                       'Револь '
                                                                                       'Миргалимович',
                                                                                       'http://kpfu.ru/main?p_id=10137'),
                                                                                      ('Валиуллина '
                                                                                       'Ксения '
                                                                                       'Борисовна',
                                                                                       'https://kpfu.ru/main?p_id=27927'),
                                                                                      ('Гараев '
                                                                                       'Марсель '
                                                                                       'Ильгамович',
                                                                                       'https://kpfu.ru/marsel.garaev'),
                                                                                      ('Кешнер '
                                                                                       'Мария '
                                                                                       'Валерьевна\xa0',
                                                                                       'http://kpfu.ru/mariya.keshner'),
                                                                                      ('Климовская '
                                                                                       'Ленара '
                                                                                       'Робертовна',
                                                                                       'https://kpfu.ru/main?p_id=46397'),
                                                                                      ('Курдюков '
                                                                                       'Геннадий '
                                                                                       'Иринархович',
                                                                                       'http://kpfu.ru/main?p_id=10141'),
                                                                                      ('Маммадов '
                                                                                       'Узейир '
                                                                                       'Юсуф '
                                                                                       'оглу',
                                                                                       'http://kpfu.ru/main?p_id=26293'),
                                                                                      ('Мингазов '
                                                                                       'Ленарис '
                                                                                       'Харисович',
                                                                                       'http://kpfu.ru/main?p_id=10142'),
                                                                                      ('Низамиев '
                                                                                       'Альфред '
                                                                                       'Шамилович',
                                                                                       'http://kpfu.ru/main?p_id=10144'),
                                                                                      ('Тюрина '
                                                                                       'Наталия '
                                                                                       'Евгеньевна',
                                                                                       'http://kpfu.ru/main?p_id=10148'),
                                                                                      ('Шайхутдинова '
                                                                                       'Гульнара '
                                                                                       'Раифовна',
                                                                                       'http://kpfu.ru/main?p_id=26297'),
                                                                                      ('Шестакова '
                                                                                       'Венера '
                                                                                       'Габдулловна',
                                                                                       'http://kpfu.ru/main?p_id=29887'),
                                                                                      ('Буташнова '
                                                                                       'Ирина '
                                                                                       'Вадимовна',
                                                                                       'http://kpfu.ru/irina.shlyapkina')],
                                      'Кафедра предпринимательского и энергетического права': [('Барышев '
                                                                                                'Сергей '
                                                                                                'Александрович',
                                                                                                'http://kpfu.ru/main?p_id=41693'),
                                                                                               ('Васькевич '
                                                                                                'Владимир '
                                                                                                'Петрович',
                                                                                                'http://kpfu.ru/main?p_id=10120'),
                                                                                               ('Измайлов '
                                                                                                'Роберт '
                                                                                                'Ринатович',
                                                                                                'https://kpfu.ru/robert.izmajlov'),
                                                                                               ('Иванишин '
                                                                                                'Павел '
                                                                                                'Зеновьевич',
                                                                                                'http://kpfu.ru/main?p_id=27391'),
                                                                                               ('Ильина '
                                                                                                'Этери '
                                                                                                'Хайдаровна',
                                                                                                'https://kpfu.ru/eteri.ilina'),
                                                                                               ('Камалетдинова '
                                                                                                'Айгуль '
                                                                                                'Владимировна',
                                                                                                'http://kpfu.ru/main?p_id=32943'),
                                                                                               ('Кашапова '
                                                                                                'Эльвина '
                                                                                                'Рустемовна',
                                                                                                'https://kpfu.ru/elvina.kashapova'),
                                                                                               ('Ковшова '
                                                                                                'Анна '
                                                                                                'Игоревна',
                                                                                                'http://kpfu.ru/anna.kovshova'),
                                                                                               ('Клименко '
                                                                                                'Оксана '
                                                                                                'Юсуповна',
                                                                                                'http://kpfu.ru/main?p_id=20535'),
                                                                                               ('Михайлов '
                                                                                                'Андрей '
                                                                                                'Валерьевич',
                                                                                                'http://kpfu.ru/main?p_id=10126'),
                                                                                               ('Салиева '
                                                                                                'Роза '
                                                                                                'Наилевна',
                                                                                                'http://kpfu.ru/Roza.Salieva'),
                                                                                               ('Селецкая '
                                                                                                'Стелла '
                                                                                                'Борисовна',
                                                                                                'http://kpfu.ru/main?p_id=10131'),
                                                                                               ('Ситдикова '
                                                                                                'Роза '
                                                                                                'Иосифовна',
                                                                                                'http://kpfu.ru/main?p_id=10200'),
                                                                                               ('Старостина '
                                                                                                'Екатерина '
                                                                                                'Сергеевна',
                                                                                                'https://kpfu.ru/ekaterina.starostina'),
                                                                                               ('Сунгатуллина '
                                                                                                'Лилия '
                                                                                                'Азатовна',
                                                                                                'http://kpfu.ru/liliyaa.sungatullina'),
                                                                                               ('Хабибуллина '
                                                                                                'Альбина '
                                                                                                'Шамиловна',
                                                                                                'http://kpfu.ru/main?p_id=36667'),
                                                                                               ('Хасанов '
                                                                                                'Ришат '
                                                                                                'Аухатович',
                                                                                                'http://kpfu.ru/main?p_id=24911'),
                                                                                               ('Чепарина '
                                                                                                'Ольга '
                                                                                                'Александровна',
                                                                                                'http://kpfu.ru/main?p_id=20331'),
                                                                                               ('Шпагонов '
                                                                                                'Александр '
                                                                                                'Николаевич',
                                                                                                'http://kpfu.ru/main?p_id=32941'),
                                                                                               ('Эйдельман '
                                                                                                'Ибрагим '
                                                                                                'Борисович',
                                                                                                'http://kpfu.ru/ibragim.ejdelman')],
                                      'Кафедра теории и истории государства и права\xa0': [('Бакулина '
                                                                                            'Лилия '
                                                                                            'Талгатовна',
                                                                                            'http://kpfu.ru/main?p_id=10152%20'),
                                                                                           ('Валиев '
                                                                                            'Рафаиль '
                                                                                            'Газизуллович',
                                                                                            'http://kpfu.ru/main?p_id=10154'),
                                                                                           ('Васин '
                                                                                            'Александр '
                                                                                            'Львович',
                                                                                            'http://kpfu.ru/aleksandr.vasin'),
                                                                                           ('Воронин '
                                                                                            'Максим '
                                                                                            'Валерьевич',
                                                                                            'http://kpfu.ru/main?p_id=26257'),
                                                                                           ('Гильмуллин '
                                                                                            'Айнур '
                                                                                            'Разифович',
                                                                                            'https://kpfu.ru/main?p_id=38990'),
                                                                                           ('Губайдуллин '
                                                                                            'Айдар '
                                                                                            'Рушанович',
                                                                                            'http://kpfu.ru/main?p_id=22108'),
                                                                                           ('Губайдуллина '
                                                                                            'Эльвира '
                                                                                            'Магнавиевна',
                                                                                            'http://kpfu.ru/elvira.gubajdullina'),
                                                                                           ('Давлетгильдеев '
                                                                                            'Рустем '
                                                                                            'Шамилевич',
                                                                                            'https://kpfu.ru/main?p_id=22637'),
                                                                                           ('Исаев '
                                                                                            'Эдуард '
                                                                                            'Евгеньевич',
                                                                                            'http://kpfu.ru/Eduard.Isaev'),
                                                                                           ('Ибрагимов '
                                                                                            'Марат '
                                                                                            'Гасангусейнович',
                                                                                            'http://kpfu.ru/Marat.Ibragimov'),
                                                                                           ('Краснов '
                                                                                            'Эдуард '
                                                                                            'Владимирович\xa0',
                                                                                            'http://kpfu.ru/eduard.krasnov'),
                                                                                           ('Курносова '
                                                                                            'Валерия '
                                                                                            'Витальевна\xa0',
                                                                                            'http://kpfu.ru/valeriya.kurnosova'),
                                                                                           ('Лукин '
                                                                                            'Юрий '
                                                                                            'Михайлович',
                                                                                            'http://kpfu.ru/main?p_id=22727'),
                                                                                           ('Минаева '
                                                                                            'Мария '
                                                                                            'Георгиевна\xa0',
                                                                                            'http://kpfu.ru/mariya.minaeva'),
                                                                                           ('Окриашвили '
                                                                                            'Тимур '
                                                                                            'Гиоргиевич',
                                                                                            'http://kpfu.ru/main?p_id=26251'),
                                                                                           ('Погодин '
                                                                                            'Александр '
                                                                                            'Витальевич',
                                                                                            'http://kpfu.ru/Aleksandr.Pogodin'),
                                                                                           ('Пономарев '
                                                                                            'Булат '
                                                                                            'Аскарович',
                                                                                            'https://kpfu.ru/bulat.ponomarev'),
                                                                                           ('Путинцев '
                                                                                            'Андрей '
                                                                                            'Владимирович',
                                                                                            'https://kpfu.ru/andrey.putincev'),
                                                                                           ('Сибаева '
                                                                                            'Ольга '
                                                                                            'Владимировна',
                                                                                            'http://kpfu.ru/main?p_id=20500'),
                                                                                           ('Сабирова '
                                                                                            'Лидия '
                                                                                            'Леонидовна',
                                                                                            'http://kpfu.ru/main?p_id=33074'),
                                                                                           ('Степаненко '
                                                                                            'Равия '
                                                                                            'Фаритовна',
                                                                                            'https://kpfu.ru/main?p_id=42025'),
                                                                                           ('Ходжиев '
                                                                                            'Алишер '
                                                                                            'Рауфович',
                                                                                            'http://kpfu.ru/main?p_id=26292'),
                                                                                           ('Хусаинова '
                                                                                            'Ольга '
                                                                                            'Владимировна',
                                                                                            'http://kpfu.ru/main?p_id=29316'),
                                                                                           ('Чулюкин '
                                                                                            'Лев '
                                                                                            'Дмитриевич',
                                                                                            'http://kpfu.ru/main?p_id=10184'),
                                                                                           ('Шарифуллин '
                                                                                            'Вадим '
                                                                                            'Рифович',
                                                                                            'http://kpfu.ru/main?p_id=10162'),
                                                                                           ('Шигабутдинова '
                                                                                            'Алина '
                                                                                            'Леонидовна',
                                                                                            'http://kpfu.ru/main?p_id=26250')],
                                      'Кафедра теории и методики обучения праву': [('Баширова '
                                                                                    'Садагат '
                                                                                    'Гюльмирзаевна',
                                                                                    'http://kpfu.ru/sadagat.bashirova'),
                                                                                   ('Валеева '
                                                                                    'Гузель '
                                                                                    'Анваровна',
                                                                                    'http://kpfu.ru/guzela.valeeva'),
                                                                                   ('Губайдуллин '
                                                                                    'Артур '
                                                                                    'Альбертович',
                                                                                    'https://kpfu.ru/artur.gubajdullin'),
                                                                                   ('Даянова '
                                                                                    'Динара '
                                                                                    'Павловна',
                                                                                    'https://kpfu.ru/dinara.dayanova'),
                                                                                   ('Ибрагимова '
                                                                                    'Елена '
                                                                                    'Михайловна',
                                                                                    'http://kpfu.ru/main?p_id=28410'),
                                                                                   ('Мулюков '
                                                                                    'Фархад '
                                                                                    'Батуевич',
                                                                                    'https://kpfu.ru/Farhad.Muljukov'),
                                                                                   ('Идиятов '
                                                                                    'Ильяс '
                                                                                    'Эльбрусович',
                                                                                    'https://kpfu.ru/ilyas.idiyatov'),
                                                                                   ('Насибуллина '
                                                                                    'Гульчачак '
                                                                                    'Мухаматовна',
                                                                                    'https://kpfu.ru/Gulchachak.Nasibullina'),
                                                                                   ('Стригулина '
                                                                                    'Светлана '
                                                                                    'Сергеевна',
                                                                                    'https://kpfu.ru/Svetlana.Strigulina'),
                                                                                   ('Хамдеев '
                                                                                    'Айдар '
                                                                                    'Рузалинович',
                                                                                    'https://kpfu.ru/Ajdar.Hamdeev'),
                                                                                   ('Юсупов '
                                                                                    'Фарит '
                                                                                    'Масгутович',
                                                                                    'http://kpfu.ru/main?p_id=29192')],
                                      'Кафедра уголовного права': [('Бакулин Валерий '
                                                                    'Константинович',
                                                                    'http://kpfu.ru/Valerij.Bakulin'),
                                                                   ('Бакулина Лидия '
                                                                    'Васильевна ',
                                                                    'http://kpfu.ru/main?p_id=10164'),
                                                                   ('Балафендиев Арсен '
                                                                    'Мирзебегович ',
                                                                    'http://kpfu.ru/main?p_id=10165'),
                                                                   ('Балеев Сергей '
                                                                    'Александрович',
                                                                    'http://kpfu.ru/main?p_id=10166'),
                                                                   ('Боковня Александра '
                                                                    'Юрьевна',
                                                                    'http://kpfu.ru/Alexandra.Timofeeva'),
                                                                   ('Гараев Магнави '
                                                                    'Тимершович',
                                                                    'http://kpfu.ru/Magnavi.Garaev'),
                                                                   ('Герфанова Елизавета '
                                                                    'Игоревна',
                                                                    'http://kpfu.ru/elizaveta.gerfanova'),
                                                                   ('Гизатуллина Елена '
                                                                    'Владимировна',
                                                                    'http://kpfu.ru/Elena.Akhmadeeva'),
                                                                   ('Голубев Станислав '
                                                                    'Игоревич',
                                                                    'http://kpfu.ru/stanislav.golubev'),
                                                                   ('Дунин Олег '
                                                                    'Николаевич',
                                                                    'https://kpfu.ru/oleg.dunin'),
                                                                   ('Мазитова Гузель '
                                                                    'Ильсуровна',
                                                                    'http://kpfu.ru/Guzel.Mazitova'),
                                                                   ('Рыбушкин Николай '
                                                                    'Николаевич',
                                                                    'http://kpfu.ru/main?p_id=10170'),
                                                                   ('Сундуров Федор '
                                                                    'Романович',
                                                                    'http://kpfu.ru/main?p_id=10174'),
                                                                   ('Талан Мария '
                                                                    'Вячеславовна',
                                                                    'http://kpfu.ru/main?p_id=10175'),
                                                                   ('Тарханов Ильдар '
                                                                    'Абдулхакович',
                                                                    'http://kpfu.ru/Ildar.Tarhanov'),
                                                                   ('Хабибуллин Наиль '
                                                                    'Эрикович',
                                                                    'http://kpfu.ru/1Nail.Khabibullin'),
                                                                   ('Халилов Рафик '
                                                                    'Нуруллович',
                                                                    'http://kpfu.ru/Rafik.Halilov')],
                                      'Кафедра уголовного процесса и криминалистики': [('Андреев '
                                                                                        'Эдуард '
                                                                                        'Алексеевич',
                                                                                        'http://kpfu.ru/eduard.andreev'),
                                                                                       ('Антонов '
                                                                                        'Игорь '
                                                                                        'Олегович',
                                                                                        'http://kpfu.ru/main?p_id=10177'),
                                                                                       ('Бурганова '
                                                                                        'Гузель '
                                                                                        'Вилсуровна',
                                                                                        'http://kpfu.ru/guzelv.burganova'),
                                                                                       ('Вавилин '
                                                                                        'Михаил '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/mihail.vavilin'),
                                                                                       ('Верин '
                                                                                        'Андрей '
                                                                                        'Юрьевич',
                                                                                        'http://kpfu.ru/main?p_id=33588&p_lang=&p_type=1%20'),
                                                                                       ('Гарипова '
                                                                                        'Кристина '
                                                                                        'Витальевна',
                                                                                        'https://kpfu.ru/kristina.garipova'),
                                                                                       ('Епихин '
                                                                                        'Александр '
                                                                                        'Юрьевич',
                                                                                        'http://kpfu.ru/main?p_id=32862'),
                                                                                       ('Ибрагимов '
                                                                                        'Артур '
                                                                                        'Гасангусейнович',
                                                                                        'http://kpfu.ru/artur.ibragimov'),
                                                                                       ('Клюкова '
                                                                                        'Марина '
                                                                                        'Евгеньевна',
                                                                                        'http://kpfu.ru/main?p_id=10180'),
                                                                                       ('Красильников '
                                                                                        'Валерий '
                                                                                        'Владимирович',
                                                                                        'https://kpfu.ru/valerij.krasilnikov'),
                                                                                       ('Мазуренко '
                                                                                        'Павел '
                                                                                        'Николаевич',
                                                                                        'https://kpfu.ru/pavel.mazurenko'),
                                                                                       ('Мишин '
                                                                                        'Андрей '
                                                                                        'Викторович',
                                                                                        'http://kpfu.ru/main?p_id=10181'),
                                                                                       ('Муратова '
                                                                                        'Надежда '
                                                                                        'Георгиевна',
                                                                                        'http://kpfu.ru/main?p_id=10182'),
                                                                                       ('Нестеренко '
                                                                                        'Майя '
                                                                                        'Владимировна',
                                                                                        'http://kpfu.ru/Maiya.Ignateva'),
                                                                                       ('Рахимов '
                                                                                        'Салават '
                                                                                        'Фоатович',
                                                                                        'https://kpfu.ru/salavat.rahimov'),
                                                                                       ('Рахматуллин '
                                                                                        'Рамиль '
                                                                                        'Рашитович',
                                                                                        'http://kpfu.ru/main?p_id=29232'),
                                                                                       ('Романов '
                                                                                        'Валерий '
                                                                                        'Иванович',
                                                                                        'http://kpfu.ru/main?p_id=10183'),
                                                                                       ('Сабирзянова '
                                                                                        'Аида '
                                                                                        'Азатовна',
                                                                                        'https://kpfu.ru/aida.sabirzyanova'),
                                                                                       ('Самитов '
                                                                                        'Эльдар '
                                                                                        'Оскарович',
                                                                                        'http://kpfu.ru/eldar.samitov'),
                                                                                       ('Сафин '
                                                                                        'Ильдус '
                                                                                        'Файзрахманович',
                                                                                        'http://kpfu.ru/Uldus.Safin'),
                                                                                       ('Сафонов '
                                                                                        'Эдуард '
                                                                                        'Евгеньевич',
                                                                                        'http://kpfu.ru/main?p_id=30066'),
                                                                                       ('Тихонова '
                                                                                        'Ольга '
                                                                                        'Александровна',
                                                                                        'http://kpfu.ru/olgaa.tihonova'),
                                                                                       ('Шалимов '
                                                                                        'Анатолий '
                                                                                        'Николаевич',
                                                                                        'http://kpfu.ru/main?p_id=10185'),
                                                                                       ('Шамсутдинов '
                                                                                        'Марат '
                                                                                        'Минефаетович',
                                                                                        'http://kpfu.ru/maratm.shamsutdinov')],
                                      'Кафедра экологического, трудового права и гражданского процесса': [('Авдонина '
                                                                                                           'Юлия '
                                                                                                           'Николаевна',
                                                                                                           'http://kpfu.ru/Juliya.Avdonina'),
                                                                                                          ('Бикеев '
                                                                                                           'Асхат '
                                                                                                           'Ахатович',
                                                                                                           'http://kpfu.ru/main?p_id=10190'),
                                                                                                          ('Валеев '
                                                                                                           'Дамир '
                                                                                                           'Хамитович ',
                                                                                                           'http://kpfu.ru/main?p_id=10191'),
                                                                                                          ('Васильев '
                                                                                                           'Максим '
                                                                                                           'Владимирович',
                                                                                                           'http://kpfu.ru/main?p_id=10192'),
                                                                                                          ('Загидуллин '
                                                                                                           'Марат '
                                                                                                           'Рашидович ',
                                                                                                           'http://kpfu.ru/main?p_id=10193'),
                                                                                                          (
                                                                                                              'Зиннатуллин '
                                                                                                              'Артур '
                                                                                                              'Зуфарович',
                                                                                                              'http://kpfu.ru/main?p_id=10194'),
                                                                                                          (
                                                                                                              'Каримуллина',
                                                                                                              'https://kpfu.ru/main?p_id=47570&p_lang=&p_type=1'),
                                                                                                          ('Кириллова '
                                                                                                           'Лариса '
                                                                                                           'Сергеевна',
                                                                                                           'http://kpfu.ru/Larisa.Kirillova'),
                                                                                                          ('Королев '
                                                                                                           'Иван '
                                                                                                           'Игоревич',
                                                                                                           'https://kpfu.ru/ivan.korolev'),
                                                                                                          ('Костин '
                                                                                                           'Илья '
                                                                                                           'Михайлович',
                                                                                                           'http://kpfu.ru/ilya.kostin'),
                                                                                                          ('Лунева '
                                                                                                           'Елена '
                                                                                                           'Викторовна',
                                                                                                           'http://kpfu.ru/elena.luneva'),
                                                                                                          ('Нагуманова '
                                                                                                           'Гузель '
                                                                                                           'Фирдинантовна',
                                                                                                           'http://kpfu.ru/Guzel.Nagumanova'),
                                                                                                          (
                                                                                                              'Нигматуллина '
                                                                                                              'Эльмира '
                                                                                                              'Фаатовна',
                                                                                                              'http://kpfu.ru/main?p_id=22249'),
                                                                                                          ('Нуриев '
                                                                                                           'Анас '
                                                                                                           'Гаптрауфович',
                                                                                                           'http://kpfu.ru/main?p_id=22294'),
                                                                                                          ('Сагитов '
                                                                                                           'Сергей '
                                                                                                           'Марселевич',
                                                                                                           'http://kpfu.ru/sergej.sagitov'),
                                                                                                          ('Сафин '
                                                                                                           'Завдат '
                                                                                                           'Файзрахманович',
                                                                                                           'http://kpfu.ru/main?p_id=10197'),
                                                                                                          ('Ситдиков '
                                                                                                           'Руслан '
                                                                                                           'Борисович',
                                                                                                           'http://kpfu.ru/main?p_id=26918'),
                                                                                                          ('Тагирова '
                                                                                                           'Гузель '
                                                                                                           'Ахметовна',
                                                                                                           'https://kpfu.ru/guzel.tagirova'),
                                                                                                          ('Хасаншин '
                                                                                                           'Рамиль '
                                                                                                           'Илгизович',
                                                                                                           'https://kpfu.ru/ramil.khasanshin'),
                                                                                                          ('Шакирьянов '
                                                                                                           'Рафаиль '
                                                                                                           'Валиевич',
                                                                                                           'https://kpfu.ru/main?p_id=29294')]}}

    general_counter = {}
    for institute_name, cathedras in data.items():
        cathedra_counter = {}
        for cathedra_name, stuff in cathedras.items():
            if stuff:
                cathedra_counter[cathedra_name] = len(stuff)
        general_counter[institute_name] = cathedra_counter

    pprint(general_counter)
