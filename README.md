<h4>Реализованная функциональность</h4>
<ul>
    <li>test.py - Исполняемый файл системы распознавания.</li>
    <li>Принимает на вход видео в популярных форматах MP4, MOV, AVI, Y4M, MKV </li>
    <li>После обраболтки создаёт JSON файл с таким же именем, как у видеофайла, в котором содержится распознанный текст, ключевые слова,
    упоминания людей, мест, организаций</li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Качественный разбор звука текста</li>
 <li>Выделение имен людей, названий городов и организаций</li>
 <li>Возможность обрабатывать видео многопоточно, передавая список файлов в multi.py</li>
 <li>Нам очень интересно его развивать))</li>
 </ul>
 
<h4>Основной стек технологий:</h4>
<ul>
	<li>Python</li>
	<li>Vosk</li>
	<li>KaldiRecognizer</li>
	<li>SpaCy</li>
	<li>ffmpeg</li>
	<li>OpenCV</li>
  
 </ul>
<h4>Демо</h4>
<p>Демо доступно только для локального развертывания на машине</p>

СРЕДА ЗАПУСКА
------------
1) использование утилиты производится на Windows;
2) требуется установленный Python 3.8.9;

Возможно дальнейшее использование на Linux

УСТАНОВКА
------------
### Установка пакетов для Python

Лучше если установка будет производиться в virtualenv

Выполните 
~~~
pip3 install vosk
pip3 install spacy
python -m spacy download ru_core_news_lg
~~~

### Установка и скачивание дополнительных пакетов

Необходимо установить ffmpeg и добавить исполняемые файлы в переменную окружения PATH

Для Vosk необходимо скачать русскую языковую модель по адресу https://alphacephei.com/vosk/models/vosk-model-ru-0.22.zip
Далее архив с моделью нужно распаковать рядом с файлом test.py чтобы получить такую структуру файлов

~~~
keywords.py
test.py
model/
...
~~~

### Способ использования
Скачайте репозиторий и модель

Установите зависимости и распакуйте модель по иструкции

Обрабатываемое видео разместите рядом с файлом test.py

Для обработки запустите следующую команду:
~~~
python test.py *ваше_имя_файла*.mp4
...
~~~

После обработки в папке создатся файл *ваше_имя_файла.mp4*.json
В нем будут распознанные полный текст, ключевые слова, названия регионов, организаций 
и имена людей в разделах: text, keywords, persons, locations, organizations


РАЗРАБОТЧИКИ

<h4>Грибов Евгений https://t.me/myxomor46 </h4>
<h4>Блох Денис https://t.me/magron3 </h4>

