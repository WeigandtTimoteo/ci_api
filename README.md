# Cabanillas Servicios Inmobiliarios - API Backend

API RESTful robusta y de alto rendimiento desarrollada para gestionar el catálogo de propiedades, la administración de contenidos multimedia y el sistema de filtrado avanzado de **Cabanillas Servicios Inmobiliarios** (Córdoba, Argentina).

## 🚀 Características Principales

- **RESTful Architecture:** Endpoints estructurados y optimizados para el consumo ágil desde clientes SPA (Single Page Applications) como React.
- **Sistema de Filtrado Relacional:** Soporte completo en backend para consultas dinámicas complejas por parámetros (`search`, `operation_type`, `age_status`, `rooms`, `min_price`, `max_price`).
- **Gestión Multimedia Multi-imagen:** Modelos estructurados para soportar múltiples fotografías en alta resolución por cada inmueble registrado.
- **Panel de Administración Custom:** Interfaz limpia en Django Admin para que los asesores inmobiliarios puedan cargar, modificar o dar de baja propiedades y fotos sin necesidad de tocar código.
- **CORS Configurado:** Políticas de intercambio de recursos de origen cruzado listas para producción, permitiendo la comunicación exclusiva con el dominio del frontend.

## 🛠️ Tecnologías Utilizadas

- **Python 3.11+**
- **Django Framework**
- **Django REST Framework (DRF)**
- **PostgreSQL** (Producción) / **SQLite** (Desarrollo)
- **Pillow** (Procesamiento y optimización de imágenes)

## 📋 Endpoints de la API

### Propiedades
- `GET /api/properties/` - Retorna el listado de propiedades (Soporta filtrado a través de Query Params).
- `GET /api/properties/<id>/` - Retorna el detalle técnico y la galería de imágenes completa de una propiedad específica.

**Parámetros de filtro aceptados en el listado:**
- `search`: Texto libre (Busca en títulos, ubicaciones o descripciones).
- `operation_type`: `SALE` (Venta) o `RENT` (Alquiler).
- `age_status`: `CONSTRUCTION` (En construcción), `NEW` (A estrenar) o `USED` (Usado).
- `rooms`: Cantidad exacta de ambientes.
- `min_price` / `max_price`: Rangos numéricos para el valor en USD.

## 📦 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/cabanillas-backend.git](https://github.com/tu-usuario/cabanillas-backend.git)
   cd cabanillas-backend