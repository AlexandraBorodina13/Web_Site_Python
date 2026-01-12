# Django CRUD Bookstore (Книжный магазин)

![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)
![Status](https://img.shields.io/badge/status-в%20разработке-yellow)

Веб-приложение книжного магазина с системой управления каталогом книг (CRUD), аутентификацией пользователей и пагинацией.

## **Цель проекта**

Разработка полнофункционального веб-приложения с backend на Django, демонстрирующего:
- Создание CRUD-операций (Create, Read, Update, Delete)
- Интеграцию с базой данных MySQL
- Реализацию системы аутентификации и авторизации
- Пагинацию данных
- Разделение ролей пользователей (администратор/обычный пользователь)

## **Архитектура проекта**

### **Стек технологий:**
- **Backend:** Django 4.x, Python 3.x
- **База данных:** MySQL
- **Frontend:** HTML, CSS, Bootstrap 5
- **Аутентификация:** Django Auth + кастомная модель User

### **Основные возможности:**
- **CRUD для книг** - добавление, редактирование, удаление, просмотр
- **Система пользователей** - регистрация, вход, выход  
- **Разделение ролей** - администратор vs обычный пользователь  
- **Пагинация** - постраничный вывод книг (3 на странице)  
- **Защита маршрутов** - декораторы для контроля доступа  
- **Админ-панель Django** - управление данными через /admin  
