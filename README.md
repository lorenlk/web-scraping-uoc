# Práctica 1: Web scraping
## Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web del [Instituto Geográfico Nacional](http://www.ign.es/web/sis-area-sismicidad) y generar un dataset.

## Miembros del Equipo
La actividad ha sido realizada de manera individual por **Pere Mayoral Moreno**.

### Prerequisitos
Para ejecutar el script es necesario instalar la siguientes librerias:

```
pip install selenium
pip install lxml
pip install bs4
```
Tambien se deberá descargar el WebDriver de Chrome en el siguiente link [Chrome Webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) y descomprimirlo en C:/Windows

## Contenido
* [csv/dataset.csv](csv/dataset.csv) Contiene el dataset extraido de la web (en este caso entre las fechas 04/03/2017 y 01/02/2018)
* [doc/practica.pdf](doc/practica.pdf) Contiene las respuestas al enunciado de la práctica
* [src](src) Contiene el codigo fuente en Python
