Отчет по Теме #9 выполнил:
Сахно Александр Сергеевич, АИС-21-1
| Задание | Сам_раб | Лаб_раб | 
| ------ | ------ | ------ | 
| Задание 1 | + | + |  
| Задание 2 |  | + | 
| Задание 3 |  | + | 
| Задание 4 |  | + | 
| Задание 5 |  | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

# Лабораторная работа №9
## Задание 1
### Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию __init__(), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.
![1](https://github.com/Alexsergh/Engineering/assets/134552389/c944b4de-f813-4e76-b00a-0d0ec5b1fbc8)

## Задание 2
### Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором Михаил А. Панов будет определяться изменили ли состав мороженого или нет. В этом классе реализуйте метод, выводящий на печать «Мороженое с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.
![2](https://github.com/Alexsergh/Engineering/assets/134552389/f510f7d3-da48-4e3b-8a65-01b5bdd4a989)

## задание 3
### Петя – начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также вас необходимо объяснить Пете почему на скриншоте ниже в консоли выводится ошибка.
![3](https://github.com/Alexsergh/Engineering/assets/134552389/ce2b360f-17a5-4141-b584-e83198454b30)

## Задание 4
### Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи Михаил А. Панов “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.
![4](https://github.com/Alexsergh/Engineering/assets/134552389/f91f64cc-1121-4ca8-9ae7-09e13f581df2)

## Задание 5
### На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках. А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются. Заметьте, что для решения поставленной задачи мы использовали декоратор @staticmethod, поскольку нам не нужны обязательные параметры-ссылки вроде self.
![5](https://github.com/Alexsergh/Engineering/assets/134552389/11978439-ba29-4f7b-ac1e-cf4b61752123)


# Самостоятельная работа №9
## Задание 1
### Задания для самостоятельного выполнения:
Задание Садовник и помидоры.
Классовая структура: Есть Помидор со следующими характеристиками:
• Индекс
• Стадия созревания (стадии: отсутствует, цветение, зеленый, красный)
Помидор может:
• Расти(переходить на следующую стадию созревания) •
Предоставлять информацию о своей зрелости Есть Куст с помидорами, который: •
Содержит список томатов, которые на нем растут
А также может: 
• Расти вместе с томатами 
• Предоставлять информацию о зрелости всех томатов 
• Предоставлять урожай 
И также есть Садовник, который имеет:
• Имя 
• Растение, за которым он ухаживает
Он может:
• Ухаживать за растением 
• Собирать с него урожай
Задание:
Класс Tomato:
1) Создайте класс Tomato
2) Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
3) Создайте метод __init__(), внутри которого будут определены два динамических свойства: _index (передается параметром) и _state (принимает первое значение из словаря states). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства
4) Создайте метод grow(), который будет переводить томат на следующую стадию созревания
5) Создайте метод is_ripe(), который будет проверять, что томат созрел
   
Класс TomatoBush:
1) Создайте класс TomatoBush
2) Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes
3) Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
4) Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми.
5) Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая

Класс Gardener:
1) Создайте класс Gardener
2) Создайте метод __init__(), внутри которого будут определены два динамических свойства: name (передается параметром, является публичным) и _plant (принимает объект класса TomatoBush). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства
3) Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
4) Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все, то садовник собирает урожай. Если нет, то метод печатает предупреждение
5) Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству

Тесты:
1) Вызовите справку по садоводству
2) Создайте объекты классов TomatoBush и Gardener
3) Используя объект класса Gardener, поухаживайте за кустом с помидорами
4) Попробуйте собрать урожай, когда томаты еще не дозрели. Продолжайте ухаживать за ними
5) Соберите урожай
Результатом работы вашей программы будет листинг кода с подробными комментариями и скриншоты выполенния всех тестов.
![1](https://github.com/Alexsergh/Engineering/assets/134552389/6dc70d9a-a9a5-4db8-baf1-74071ac22779)
![2](https://github.com/Alexsergh/Engineering/assets/134552389/4db9d73f-5e89-4068-b14d-e9d64c4793f9)
![3](https://github.com/Alexsergh/Engineering/assets/134552389/a1413f37-c4d5-4058-a1a2-852d62954d16)
![4](https://github.com/Alexsergh/Engineering/assets/134552389/e373818e-31f0-431e-b656-353b38512c6d)

## Вывод
Выполняя данное задание, я окончательно убедился, что далее хочу учиться развиваться и работать в данной сфере. Благодаря самостоятельной работе я усвоил весь изученный материал и научился применять его на практике








