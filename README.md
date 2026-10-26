# Sistema de gestión para un shopping

Proyecto integrador de la materia **Algoritmos y Estructuras de Datos** (Ingeniería en Sistemas de Información, UTN Rosario, 2023). El sistema se desarrolló a lo largo del año en tres entregas, cada una sumando contenidos nuevos de la materia. Es una aplicación de consola escrita en Python.

## Qué hace

El sistema simula la administración de un shopping con tres tipos de usuario:

| Usuario | Qué puede hacer |
|---|---|
| **Administrador** | Gestionar locales (crear, modificar, eliminar, ver el mapa), crear cuentas de dueños de locales, aprobar o rechazar descuentos y ver reportes de uso. |
| **Dueño de local** | Crear descuentos para sus locales y ver el reporte de uso. |
| **Cliente** | Registrarse, buscar descuentos vigentes y solicitarlos. |

## Las tres entregas

| Carpeta | Contenidos de la materia | Autoría |
|---|---|---|
| [`tp1`](tp1) | Menús, estructuras de control, validación de entradas y funciones. | Individual |
| [`tp2`](tp2) | Arreglos, búsqueda dicotómica, ordenamiento y mapa de locales en una matriz. | Individual |
| [`tp3`](tp3) | Registros y archivos (persistencia con `pickle`), registros de longitud fija, reportes con rango de fechas. | Grupal |

**TP3, trabajo en equipo:** Tomás Andino, Micaela Consiglio, Marian Soria y Luciano Villavicencio. Mi aporte principal fue el diagrama Chapin del sistema completo.

Cada entrega tuvo asociado un diagrama Chapin con el diseño del algoritmo, que es parte del trabajo original de la cursada.

## Cómo ejecutarlo

Requiere Python 3. Desde la carpeta de cada entrega:

```bash
python main.py
```

Usuario administrador inicial (el que pedía la consigna): `admin@shopping.com` / `12345`.
En el TP3, los archivos de datos (`.dat`) se crean solos la primera vez que se ejecuta.

## Notas

- Es un proyecto académico: las claves se guardan sin cifrar porque así lo pedía la consigna.
- **TP1 y TP2 tienen correcciones posteriores a la entrega**, hechas para esta publicación: se quitó un borrador que había quedado pegado al final del TP1 y no dejaba ejecutarlo; en el TP2 se corrigió la búsqueda dicotómica de nombres de locales (no detectaba nombres repetidos), el límite de 50 locales y el comando de limpiar pantalla, que ahora funciona también fuera de Windows.
- **El TP3 se publica tal como fue entregado.** Limitaciones conocidas: las fechas se comparan como texto (DD/MM/AAAA), por lo que algunas comparaciones entre meses y años distintos pueden dar resultados incorrectos; el reporte de descuentos no filtra los usos por su fecha; y algunas entradas numéricas no controlan errores de tipeo.
- La gestión de novedades solo está diagramada en Chapin, como pedía la consigna.
