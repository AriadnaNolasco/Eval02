Enlace del video: https://youtube.com/shorts/ZeXTbcy1WcM?feature=share
# Documentación de la API de Gestión de Finanzas Personales

Esta documentación describe los endpoints disponibles en la API para gestionar finanzas personales.

## 1. Cuentas (`/api/cuentas/`)

### 1.1 Listar Cuentas

* **URL:** `/api/cuentas/`
* **Método HTTP:** `GET`
* **Parámetros:** Ninguno
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    [
        {
            "id": 1,
            "nombre": "Cuenta Corriente",
            "saldo": "1500.50",
            "moneda": "PEN",
            "fecha_creacion": "2023-10-26T10:00:00Z"
        },
        {
            "id": 2,
            "nombre": "Tarjeta de Crédito",
            "saldo": "-250.75",
            "moneda": "PEN",
            "fecha_creacion": "2023-11-15T14:30:00Z"
        }
    ]
    ```
* **Códigos de Estado Posibles:**
    * `200 OK`: Lista de cuentas obtenida exitosamente.
    * `401 Unauthorized`: No autenticado.

### 1.2 Crear Cuenta

* **URL:** `/api/cuentas/`
* **Método HTTP:** `POST`
* **Parámetros Requeridos (JSON en el cuerpo de la petición):**
    ```json
    {
        "nombre": "Nueva Cuenta de Ahorros",
        "saldo": "5000.00",
        "moneda": "USD"
    }
    ```
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    {
        "id": 3,
        "nombre": "Nueva Cuenta de Ahorros",
        "saldo": "5000.00",
        "moneda": "USD",
        "fecha_creacion": "2023-12-01T09:15:00Z"
    }
    ```
* **Códigos de Estado Posibles:**
    * `201 Created`: Cuenta creada exitosamente.
    * `400 Bad Request`: Los datos proporcionados no son válidos.
    * `401 Unauthorized`: No autenticado.

### 1.3 Obtener Cuenta Específica

* **URL:** `/api/cuentas/{id}/` (reemplaza `{id}` con el ID de la cuenta)
* **Método HTTP:** `GET`
* **Parámetros:**
    * `id` (requerido): ID entero de la cuenta a obtener.
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    {
        "id": 1,
        "nombre": "Cuenta Corriente",
        "saldo": "1500.50",
        "moneda": "PEN",
        "fecha_creacion": "2023-10-26T10:00:00Z"
    }
    ```
* **Códigos de Estado Posibles:**
    * `200 OK`: Cuenta obtenida exitosamente.
    * `401 Unauthorized`: No autenticado.
    * `404 Not Found`: No se encontró la cuenta con el ID especificado.

### 1.4 Actualizar Cuenta

* **URL:** `/api/cuentas/{id}/` (reemplaza `{id}` con el ID de la cuenta)
* **Método HTTP:** `PUT`
* **Parámetros Requeridos (JSON en el cuerpo de la petición):**
    ```json
    {
        "nombre": "Cuenta Corriente Principal",
        "saldo": "1600.00",
        "moneda": "PEN"
        // Puedes incluir solo los campos que deseas actualizar
    }
    ```
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    {
        "id": 1,
        "nombre": "Cuenta Corriente Principal",
        "saldo": "1600.00",
        "moneda": "PEN",
        "fecha_creacion": "2023-10-26T10:00:00Z"
    }
    ```
* **Códigos de Estado Posibles:**
    * `200 OK`: Cuenta actualizada exitosamente.
    * `400 Bad Request`: Los datos proporcionados no son válidos.
    * `401 Unauthorized`: No autenticado.
    * `404 Not Found`: No se encontró la cuenta con el ID especificado.

### 1.5 Eliminar Cuenta

* **URL:** `/api/cuentas/{id}/` (reemplaza `{id}` con el ID de la cuenta)
* **Método HTTP:** `DELETE`
* **Parámetros:**
    * `id` (requerido): ID entero de la cuenta a eliminar.
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta:** `204 No Content` (si la eliminación fue exitosa)
* **Códigos de Estado Posibles:**
    * `204 No Content`: Cuenta eliminada exitosamente.
    * `401 Unauthorized`: No autenticado.
    * `404 Not Found`: No se encontró la cuenta con el ID especificado.

## 2. Categorías (`/api/categorias/`)

### 2.1 Listar Categorías

* **URL:** `/api/categorias/`
* **Método HTTP:** `GET`
* **Parámetros:** Ninguno
* **Autenticación:** Opcional (puede ser pública o requerir autenticación según la configuración)
* **Formato de Respuesta (JSON):**
    ```json
    [
        {
            "id": 1,
            "nombre": "Comida",
            "descripcion": "Gastos relacionados con alimentos"
        },
        {
            "id": 2,
            "nombre": "Transporte",
            "descripcion": "Gastos de movilidad"
        }
    ]
    ```
* **Códigos de Estado Posibles:**
    * `200 OK`: Lista de categorías obtenida exitosamente.
    * `401 Unauthorized`: No autenticado (si la autenticación es requerida).

### 2.2 Crear Categoría

* **URL:** `/api/categorias/`
* **Método HTTP:** `POST`
* **Parámetros Requeridos (JSON en el cuerpo de la petición):**
    ```json
    {
        "nombre": "Entretenimiento",
        "descripcion": "Gastos en ocio y diversión"
    }
    ```
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    {
        "id": 3,
        "nombre": "Entretenimiento",
        "descripcion": "Gastos en ocio y diversión"
    }
    ```
* **Códigos de Estado Posibles:**
    * `201 Created`: Categoría creada exitosamente.
    * `400 Bad Request`: Los datos proporcionados no son válidos.
    * `401 Unauthorized`: No autenticado.

### 2.3 Obtener Categoría Específica

* **URL:** `/api/categorias/{id}/` (reemplaza `{id}` con el ID de la categoría)
* **Método HTTP:** `GET`
* **Parámetros:**
    * `id` (requerido): ID entero de la categoría a obtener.
* **Autenticación:** Opcional (puede ser pública o requerir autenticación según la configuración)
* **Formato de Respuesta (JSON):**
    ```json
    {
        "id": 1,
        "nombre": "Comida",
        "descripcion": "Gastos relacionados con alimentos"
    }
    ```
* **Códigos de Estado Posibles:**
    * `200 OK`: Categoría obtenida exitosamente.
    * `401 Unauthorized`: No autenticado (si la autenticación es requerida).
    * `404 Not Found`: No se encontró la categoría con el ID especificado.

### 2.4 Actualizar Categoría

* **URL:** `/api/categorias/{id}/` (reemplaza `{id}` con el ID de la categoría)
* **Método HTTP:** `PUT`
* **Parámetros Requeridos (JSON en el cuerpo de la petición):**
    ```json
    {
        "nombre": "Alimentos y Bebidas",
        "descripcion": "Gastos en comida y bebidas"
        // Puedes incluir solo los campos que deseas actualizar
    }
    ```
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    {
        "id": 1,
        "nombre": "Alimentos y Bebidas",
        "descripcion": "Gastos en comida y bebidas"
    }
    ```
* **Códigos de Estado Posibles:**
    * `200 OK`: Categoría actualizada exitosamente.
    * `400 Bad Request`: Los datos proporcionados no son válidos.
    * `401 Unauthorized`: No autenticado.
    * `404 Not Found`: No se encontró la categoría con el ID especificado.

### 2.5 Eliminar Categoría

* **URL:** `/api/categorias/{id}/` (reemplaza `{id}` con el ID de la categoría)
* **Método HTTP:** `DELETE`
* **Parámetros:**
    * `id` (requerido): ID entero de la categoría a eliminar.
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta:** `204 No Content` (si la eliminación fue exitosa)
* **Códigos de Estado Posibles:**
    * `204 No Content`: Categoría eliminada exitosamente.
    * `401 Unauthorized`: No autenticado.
    * `404 Not Found`: No se encontró la categoría con el ID especificado.

## 3. Transacciones (`/api/transacciones/`)

### 3.1 Listar Transacciones

* **URL:** `/api/transacciones/`
* **Método HTTP:** `GET`
* **Parámetros:** Ninguno
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    [
        {
            "id": 1,
            "tipo": "G",
            "monto": "55.20",
            "fecha": "2023-11-20",
            "categoria": 1, // ID de la categoría
            "cuenta": 1,    // ID de la cuenta
            "descripcion": "Almuerzo"
        },
        {
            "id": 2,
            "tipo": "I",
            "monto": "1200.00",
            "fecha": "2023-11-25",
            "categoria": 5, // ID de la categoría (ej: Ingresos)
            "cuenta": 1,    // ID de la cuenta
            "descripcion": "Pago de salario"
        }
    ]
    ```
* **Códigos de Estado Posibles:**
    * `200 OK`: Lista de transacciones obtenida exitosamente.
    * `401 Unauthorized`: No autenticado.

### 3.2 Crear Transacción

* **URL:** `/api/transacciones/`
* **Método HTTP:** `POST`
* **Parámetros Requeridos (JSON en el cuerpo de la petición):**
    ```json
    {
        "tipo": "G", // 'I' para Ingreso, 'G' para Gasto
        "monto": "25.99",
        "fecha": "2023-12-02",
        "categoria": 2, // ID de la categoría
        "cuenta": 1,    // ID de la cuenta
        "descripcion": "Pasaje de bus"
    }
    ```
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    {
        "id": 3,
        "tipo": "G",
        "monto": "25.99",
        "fecha": "2023-12-02",
        "categoria": 2,
        "cuenta": 1,
        "descripcion": "Pasaje de bus"
    }
    ```
* **Códigos de Estado Posibles:**
    * `201 Created`: Transacción creada exitosamente.
    * `400 Bad Request`: Los datos proporcionados no son válidos.
    * `401 Unauthorized`: No autenticado.

### 3.3 Obtener Transacción Específica

* **URL:** `/api/transacciones/{id}/` (reemplaza `{id}` con el ID de la transacción)
* **Método HTTP:** `GET`
* **Parámetros:**
    * `id` (requerido): ID entero de la transacción a obtener.
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    {
        "id": 1,
        "tipo": "G",
        "monto": "55.20",
        "fecha": "2023-11-20",
        "categoria": 1,
        "cuenta": 1,
        "descripcion": "Almuerzo"
    }
    ```
* **Códigos de Estado Posibles:**
    * `200 OK`: Transacción obtenida exitosamente.
    * `401 Unauthorized`: No autenticado.
    * `404 Not Found`: No se encontró la transacción con el ID especificado.

### 3.4 Actualizar Transacción

* **URL:** `/api/transacciones/{id}/` (reemplaza `{id}` con el ID de la transacción)
* **Método HTTP:** `PUT`
* **Parámetros Requeridos (JSON en el cuerpo de la petición):**
    ```json
    {
        "monto": "60.00",
        "descripcion": "Almuerzo con colegas"
        // Puedes incluir solo los campos que deseas actualizar
    }
    ```
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    {
        "id": 1,
        "tipo": "G",
        "monto": "60.00",
        "fecha": "2023-11-20",
        "categoria": 1,
        "cuenta": 1,
        "descripcion": "Almuerzo con colegas"
    }
    ```
* **Códigos de Estado Posibles:**
    * `200 OK`: Transacción actualizada exitosamente.
    * `400 Bad Request`: Los datos proporcionados no son válidos.
    * `401 Unauthorized`: No autenticado.
    * `404 Not Found`: No se encontró la transacción con el ID especificado.

### 3.5 Eliminar Transacción

* **URL:** `/api/transacciones/{id}/` (reemplaza `{id}` con el ID de la transacción)
* **Método HTTP:** `DELETE`
* **Parámetros:**
    * `id` (requerido): ID entero de la transacción a eliminar.
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta:** `204 No Content` (si la eliminación fue exitosa)
* **Códigos de Estado Posibles:**
    * `204 No Content`: Transacción eliminada exitosamente.
    * `401 Unauthorized`: No autenticado.
    * `404 Not Found`: No se encontró la transacción con el ID especificado.

## 4. Presupuestos (`/api/presupuestos/`)

### 4.1 Listar Presupuestos

* **URL:** `/api/presupuestos/`
* **Método HTTP:** `GET`
* **Parámetros:** Ninguno
* **Autenticación:** Requerida (Token Authentication)
* **Formato de Respuesta (JSON):**
    ```json
    [
        {
            "id": 1,
            "categoria": 1, // ID de la categoría
            "monto_presupuestado": "300.00",
            "periodo_inicio":
