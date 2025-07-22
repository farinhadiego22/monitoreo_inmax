# Monitoreo Inmax

Este proyecto está diseñado para el monitoreo utilizando una arquitectura basada en Docker, lo que facilita su despliegue y portabilidad. Incluye una aplicación frontend construida con Vue 3 y Vite.

## Características principales

- Contenerización completa con Docker.
- Frontend moderno utilizando Vue 3 y Vite.
- Configuración simple y rápida para desarrollo y producción.

## Requisitos previos

- [Docker](https://www.docker.com/get-started) instalado en tu sistema.

## Instalación y ejecución

1. Clona este repositorio:
   ```bash
   git clone https://github.com/farinhadiego22/monitoreo_inmax.git
   cd monitoreo_inmax
   ```

2. Construye y levanta los contenedores con Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Accede al frontend desde tu navegador en [http://localhost:8080](http://localhost:8080) (ajusta el puerto si es necesario).

## Estructura del proyecto

- `frontend/`: Contiene la aplicación Vue 3 + Vite.
- Otros directorios y servicios pueden estar incluidos según la configuración del sistema de monitoreo.

## Personalización

Puedes modificar los archivos de configuración de Docker y del frontend para adaptarlo a tus necesidades específicas.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.

---

### Créditos

- [Vue 3 + Vite](https://vuejs.org/)
- Docker