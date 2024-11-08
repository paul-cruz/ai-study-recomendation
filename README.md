# AI Study Recomendation

## Arquitecutra de la solución

![arquitectura](./images/Arquitectura_ai-study-recommendation.png)

## Clonar el repositorio

```bash
git clone https://github.com/paul-cruz/ai-study-recommendation.git
```

## Requirements for setting up GCP CI/CD pipeline📋

Para poder llevar a cabo la implementación y despliegue del proyecto se debera contar con lo siguiente:

- [Cuenta activa y configurada en Google Cloud Platform](https://console.cloud.google.com/) - La plataforma de nube dónde se aloja y consume servicios el proyecto.
- [node v22.11.0+](https://nodejs.org/) - JavaScript runtime
- [npm 10.9.0](https://www.npmjs.com/package/install) - Sistema de gestión de paquetes para Node.js
- [python 3.13.0](https://www.python.org/downloads/) - Interpretador de python

### Crear una service account que usará el pipeline

Para poder construir, publicar y hacer consultas a vertex AI, la cuenta de servicio necesita los siguientes permisos:

- roles/aiplatform.user
- roles/cloudbuild.builds.editor
- roles/run.developer

`Estos permisos no siguen la practica de menos privilegios, no se recomienda para producción, es solo para pruebas`

## Conectar Github y Google Cloud🛠️

Para conectar debes ir a la consola de [repositorios en Cloud Build](https://console.cloud.google.com/cloud-build/repositories/) y habiliar la API si no lo está.

Despúes seleccionar conectar repositorio:

![conectar repo](./images/connect_repo.png)

Y seguir las instrucciones y autenticaciones entre GitHub y GCP:

![configurar repo](./images/repo_config.png)

## Crear triggers 🛠️

Ir a la sección de [triggers](https://console.cloud.google.com/cloud-build/triggers) y configurarlos de la siguiente manera:

### Trigger de Front-End

Se tiene que configurar el trigger para que cualquier cambio hecho bajo la carpeta **ai-study-recommendation** se construyan y desplieguen con cloud build.

![configuración 1](./images/web_repo1.png)

![configuración 2](./images/web_repo2.png)

![configuración 3](./images/web_repo3.png)

### Trigger de Back-End

Se tiene que configurar el trigger para que cualquier cambio hecho bajo la carpeta **ai-study-recommendation-endpoint** se construyan y desplieguen con cloud build.

![configuración 1](./images/api_repo1.png)

![configuración 2](./images/api_repo2.png)

![configuración 3](./images/api_repo3.png)
