УСТАНОВКА

- Установить Python и добавить его в PATH (в установщике есть соответствующая галочка)
- Распокавать этот архив в любом удобном месте

НАЧАЛО РАБОТЫ !!!!Обязательно соединение с интернетом!!!!

professions.csv - текстовый документ, который можно редактировать в любом текстовом редакторе, например, блокноте. 
Каждая строка в нем - специальность врача, которая имеется в системе вида id:Имя, при этом id обязательно должно соответствовать системному идентификатору специальности, а имя написано с учетом требований яндекса. 
В фид попадут только те врачи, спепциальности которых прописаны в этом файле.
Чтобы добавить специальность, узнайте id нужной специальности и добавьте новую строку в формате id:Имя (по аналогии с уже имеющимися)

<<двойной клик>> process.cmd - запускает процесс создания фида:
- обновляются файлы программы
- запускается скрипт, генерирующий фид
- обновляется LOG.log (журнал о том как прошел процесс) и yml/doctors.yml (выходные данные)
- фид отправляется в удаленное хранилище, где его видит Яндекс Вебмастер