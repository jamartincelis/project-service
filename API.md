# Project Service

Endpoints del microservicio de metas.

## Health check

```bash
curl --request GET \
  --url http://localhost:8000/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/health-check/
```

## Obtener las metas del usuario

```bash
curl --request GET \
  --url http://localhost:8000/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/
```

## Crear la metas del usuario

```bash
curl --request POST \
  --url http://localhost:8000/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/ \
  --header 'content-type: application/json' \
  --data '{"user": "0390a508-dba5-4344-b77f-93e1227d42f4","category": "eeb4ccdb-f90e-4b96-888c-d8937185d96c","goal_date": "2022-01-01","total": 5000,"from_account" : "ABCDEFGHI","to_account" : "ZYXWVUTSRQ","name": "Mi meta prueba"}'
```

respuesta 

```json
{
  "id": "514b33f9-6ea2-45bc-a695-7ace39c82c44",
  "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
  "status": "d7d30bcd-8417-47c9-b294-a4ca5bfd3506",
  "category": "eeb4ccdb-f90e-4b96-888c-d8937185d96c",
  "name": "Mi meta prueba",
  "goal_date": "2022-01-01",
  "deleted_at": null,
  "total": 5000,
  "progress": "0.00",
  "processing": "0.00",
  "pending": "0.00",
  "from_account": "ABCDEFGHI",
  "to_account": "ZYXWVUTSRQ",
  "updated_at": "2021-12-14T23:06:36.549681-06:00",
  "created_at": "2021-12-14T23:06:36.549726-06:00"
}
```

# Consultar detalle de la meta


```bash
curl --request GET \
  --url http://localhost:8000/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/3cb17971-e530-4070-b37f-c7b164699295/
```
respuesta 

```json
  {
  "id": "3cb17971-e530-4070-b37f-c7b164699295",
  "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
  "status": "d7d30bcd-8417-47c9-b294-a4ca5bfd3506",
  "category": "eeb4ccdb-f90e-4b96-888c-d8937185d96c",
  "name": "Mi meta",
  "goal_date": "2022-01-01",
  "deleted_at": null,
  "total": 10000,
  "progress": "0.00",
  "processing": "0.00",
  "pending": "0.00",
  "from_account": "ABCDEFGHI",
  "to_account": "ZYXWVUTSRQ",
  "updated_at": "2021-05-01T14:20:30-05:00",
  "created_at": "2021-05-01T14:20:30-05:00"
}
```

# Actualizar la meta

Forma 1

```bash
curl --request PATCH \
  --url http://localhost:8000/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/3cb17971-e530-4070-b37f-c7b164699295/ \
  --header 'content-type: application/json' \
  --data '{"total": 6000}'
```

respuesta

```json
  {
  "id": "3cb17971-e530-4070-b37f-c7b164699295",
  "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
  "status": "d7d30bcd-8417-47c9-b294-a4ca5bfd3506",
  "category": "eeb4ccdb-f90e-4b96-888c-d8937185d96c",
  "name": "Mi meta",
  "goal_date": "2022-01-01",
  "deleted_at": null,
  "total": 6000,
  "progress": "0.00",
  "processing": "0.00",
  "pending": "0.00",
  "from_account": "ABCDEFGHI",
  "to_account": "ZYXWVUTSRQ",
  "updated_at": "2021-05-01T14:20:30-05:00",
  "created_at": "2021-05-01T14:20:30-05:00"
}
```

Forma 2

```bash
curl --request PUT \
  --url http://localhost:8000/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/3cb17971-e530-4070-b37f-c7b164699295/ \
  --header 'content-type: application/json' \
  --data '{"user": "0390a508-dba5-4344-b77f-93e1227d42f4","category": "eeb4ccdb-f90e-4b96-888c-d8937185d96c","goal_date": "2022-02-01","total": 7000,"from_account" : "ZYXWVUTSRQ","to_account" : "ABCDEFGHI","name": "Mi meta prueba actualizando put"}'
```

respuesta 

```json
  {
  "id": "3cb17971-e530-4070-b37f-c7b164699295",
  "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
  "status": "d7d30bcd-8417-47c9-b294-a4ca5bfd3506",
  "category": "eeb4ccdb-f90e-4b96-888c-d8937185d96c",
  "name": "Mi meta prueba actualizando put",
  "goal_date": "2022-02-01",
  "deleted_at": null,
  "total": 7000,
  "progress": "0.00",
  "processing": "0.00",
  "pending": "0.00",
  "from_account": "ZYXWVUTSRQ",
  "to_account": "ABCDEFGHI",
  "updated_at": "2021-05-01T14:20:30-05:00",
  "created_at": "2021-05-01T14:20:30-05:00"
}
```