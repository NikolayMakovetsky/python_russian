Python Russian Channel

Конкурентность (concurrency) - запуск на выполнение сразу нескольких задач
(не обязательно в 1 момент времени выполняется несколько).
Зависит от ПО. Первые ОС с процессором без ядер -использовали только ее.

Параллельность (parallel) - конкурентность,
когда 2+ задачи выполняются одновременно. Зависит от железа.
(Если ядро только одно, то ни о какой параллельности речи быть не может!)
Вы не можете одновременно (!) выполнять больше задач, чем есть ядер в системе.

thread-safe - потокобезопасность, означает что при работе с объектом не возникают
известные проблемы при работе с конкурентностью
ПРОБЛЕМЫ:
Взаимоблокировка - когда 2 потока ждут завершения друг друга и т.о. навечно заблочены
Гонка - когда несколько потоков хватаются за один ресурс
...
Объект, который защищен от таких проблем называется thread-safe объект или 
потобезопасный объект. Например в питоне есть потокобезопасные очереди.

Важно понимать, что изначально сам интерпретатор питона не является потокобезопасным!!!
Например, счетчик ссылок в питоне устроен непотокобезопасно...
Именно поэтому в питоне появился GIL 
GIL (Global Interpreter Lock) - глобальная блокировка интерпретатора,
механизм гарантирующий,
что в любой момент времени выполняется только 1 инструкция в питоне. (1 поток)

Интересно, что Numpy, Pandas написаны на языке С, и они лежат отдельно от питона,
и соответственно GIL на них не распространяется...отчасти еще и поэтому они быстрые

Задачи для Python могут быть:
CPU-bound - зависит от мощности процессора
IO-bound - зависит от системы ввода/вывода


threading - IO-bound задачи (многопоточность)
asyncio - IO-bound задачи (асинхронность в одном потоке)
multiprocessing - любые задачи (многопроцессорность)

Читать!
Фаулер М. "Asyncio и конкурентное программирование на Python"