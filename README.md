# Python package "toxicity"
**Мой дипломная работа "Выявление токсичного контента в русскоязычных текстах".**

Дипломная программа "Анализ больших данных в бизнесе, экономике и обществе".<br>
НИУ "Высшая Школа Экономики" (СПб).<br>

Текст работы представлен [на сайте НИУ ВШЭ](https://www.hse.ru/edu/vkr/47708555). <br>
В работе подробно объяснено, почему были выбраны данные алгоритмы машинного обучения, и расписаны все детали реализации полученных алгоритмов.

В данном репозитории собрана вся история разработки модели по классификации токсичного контента
на русском языке. В конце лучшая модель (с наилучшим соотношением качества и размера)
опубликована в форме python-пакета [**toxicity**](https://pypi.org/project/toxicity/).

Показатели метрик точности на тестовой выборке у модели (внутри пакета **toxicity**):

Accuracy | Recall | Precision | F1
-------- | ------ | --------- | ------ |
90.6%    | 83.86% | 87.24%    | 85.52% |

## Пример использования python-библиотеки
Установи пакет
```shell
pip3 install toxicity
```
и сразу пробуй
```python
from toxicity import ToxicCommentsDetector

test_raw_texts = [
    'ты чего берега попутал?',
    'это правый берег реки, не путай с левым'
]

toxicDetector = ToxicCommentsDetector()
print(toxicDetector.predict(test_raw_texts)) # [0.9521822  0.18336123]
```
В данном примере показывается, что модель с 95% вероятностью уверена,
что текст
>ты чего берега попутал?

является токсичным,
а уверенность модели, что текст
>это правый берег реки, не путай с левым

может быть токсичным составляет лишь 18%.

_Примечание:_ Выбор пограничного значения вероятности,
при котором причислять коммент к токсичному остается на усмотрение пользователя библиотеки.
Но, если нет представления, какое значение использовать, то бери `0.5`.

## Структура проекта
```
├── data # Используемые данные
│
├── dev # Набор констант и утилит для разработки
│   ├── constants
|   └── utils
│
├── models # различные модели для решения главной задачи классификации  
│
├── publishPackageUtils # инструменты для публикации пакета
│    
├── textPreprocessing # набор утилит для предобработки русскоязычных текстов
│   ├── text_utils # набор маленьких утилит по очистке текста
│   └── preprocess_text.py # собирает все утилиты из text_utils в одну функцию
│
└── wordEmbeddingsLayers # различные способы векторизации слов
```

## Навигация по проекту
- [Используемые данные](/data)
- [Предварительная очистка текстовых данных](/textPreprocessing)<br>
Как обрабатывались сырые текстовые данные перед их дальнейшим использованием в построении моделей машинного обучения.
- [Какие способы векторизации слов применялись](/wordEmbeddingsLayers)
- [Какие модели ML были опробованы для решения поставленной главной задачи классификации](/models)
- [Как опубликовать новую версию python-пакета](/publishPackageUtils/how-publish-package-instruction.md)
