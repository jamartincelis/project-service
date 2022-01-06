# Project Service

Endpoints del microservicio de metas.

## Health check

```bash
curl --request GET \
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/health-check/
```

## Obtener las metas del usuario

```bash
curl --request GET \
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/
```

## Crear la meta del usuario sin reglas

```bash
curl --request POST \
  --url http://127.0.0.1/project-service/user/b9e605ee-4cca-400e-99c5-ae24abca97d5/projects/ \
  --header 'content-type: application/json' \
  --header 'user-agent: vscode-restclient' \
  --data '{"user": "0390a508-dba5-4344-b77f-93e1227d42f4","category": "7c1521e9-6d06-4c6e-9aa5-db4414afe71f","goal_date": "2022-01-01","total": 5000,"from_account" : "333bb09d-26ab-4fe5-8051-6619dba1eff7","to_account" : "c80f5170-2926-4b45-af64-dfe13e24a222","name": "mi meta prueba","rules_list" : []}'
```

respuesta 

```json
{
  "id": "468d4f49-418d-449e-ae90-445588f13c71",
  "category": {
    "id": "7c1521e9-6d06-4c6e-9aa5-db4414afe71f",
    "name": "auto",
    "description": "Meta auto",
    "metadata": {
      "icon": "assets/img/category/saving.svg",
      "color": "#FF8300",
      "active": true,
      "short_name": "META_AUTO"
    },
    "catalog": "2b40a466-8f48-4c4a-a03f-9094b9dbe7b0"
  },
  "user": "b9e605ee-4cca-400e-99c5-ae24abca97d5",
  "status": "f2a34b3c-5eea-4bfd-a18e-06d675826486",
  "name": "mi meta prueba",
  "goal_date": "2022-01-01",
  "deleted_at": null,
  "total": "5000.00",
  "progress": "0.00",
  "processing": "0.00",
  "pending": "0.00",
  "from_account": "333bb09d-26ab-4fe5-8051-6619dba1eff7",
  "to_account": "c80f5170-2926-4b45-af64-dfe13e24a222",
  "updated_at": "2022-01-04T14:08:24.843936-06:00",
  "created_at": "2022-01-04T14:08:24.843952-06:00",
  "rules_list": []
}
```

## Crear la meta del usuario con reglas

```bash
curl --request POST \
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/3cb17971-e530-4070-b37f-c7b164699295/rules/ \
  --header 'content-type: application/json' \
  --header 'user-agent: vscode-restclient' \
  --data '{"rules_list" : [{"rule_type" : "01fdb81f-88ef-4f7a-bc0a-c9f66430f391","rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e","amount": 19100.00},{"rule_type" : "a3125075-ff44-4b8b-be29-6c73fd846872","rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e","amount": 51000.00}]}'
```

respuesta 

```json
{
  "id": "ed0f0467-35b3-40bf-b042-782df31aa495",
  "category": {
    "id": "7c1521e9-6d06-4c6e-9aa5-db4414afe71f",
    "name": "auto",
    "description": "Meta auto",
    "metadata": {
      "icon": "assets/img/category/saving.svg",
      "color": "#FF8300",
      "active": true,
      "short_name": "META_AUTO"
    },
    "catalog": "2b40a466-8f48-4c4a-a03f-9094b9dbe7b0"
  },
  "user": "b9e605ee-4cca-400e-99c5-ae24abca97d5",
  "status": "f2a34b3c-5eea-4bfd-a18e-06d675826486",
  "name": "mi meta prueba",
  "goal_date": "2022-01-01",
  "deleted_at": null,
  "total": "5000.00",
  "progress": "0.00",
  "processing": "0.00",
  "pending": "0.00",
  "from_account": "333bb09d-26ab-4fe5-8051-6619dba1eff7",
  "to_account": "c80f5170-2926-4b45-af64-dfe13e24a222",
  "updated_at": "2022-01-04T14:16:57.234998-06:00",
  "created_at": "2022-01-04T14:16:57.235014-06:00",
  "rules_list": [
    {
      "id": "b71b72a5-ff83-44e4-8461-7ee3343bc97f",
      "rule_type": {
        "id": "01fdb81f-88ef-4f7a-bc0a-c9f66430f391",
        "name": "Desafío 52 semanas",
        "description": "Ahorra según el desafío de las 52 semanas, aumentando un dólar al día",
        "metadata": {
          "icon": "https://via.placeholder.com/150",
          "limit": 1,
          "active": true,
          "default": false,
          "frequency_description": "${} cada semana"
        },
        "catalog": "47bd8165-2b84-4bc9-91d0-6126beee2b40"
      },
      "user": "b9e605ee-4cca-400e-99c5-ae24abca97d5",
      "status": "65729137-0844-4b28-85b5-2e81b73a948a",
      "amount": "19100.00",
      "frequency": 0,
      "day": 0,
      "onboarding": false,
      "created_at": "2022-01-04T14:16:57.255316-06:00",
      "updated_at": "2022-01-04T14:16:57.255332-06:00",
      "configuration": null,
      "project": "ed0f0467-35b3-40bf-b042-782df31aa495"
    },
    {
      "id": "3b430183-ebbe-46ab-8fd2-0696865d628f",
      "rule_type": {
        "id": "a3125075-ff44-4b8b-be29-6c73fd846872",
        "name": "Pasión Futbolera",
        "description": "Ahorra cada vez que tu equipo juegue, gane o anote un gol",
        "metadata": {
          "icon": "https://via.placeholder.com/150",
          "limit": 3,
          "active": true,
          "default": false,
          "frequency_description": "${} cada que {}"
        },
        "catalog": "47bd8165-2b84-4bc9-91d0-6126beee2b40"
      },
      "user": "b9e605ee-4cca-400e-99c5-ae24abca97d5",
      "status": "65729137-0844-4b28-85b5-2e81b73a948a",
      "amount": "51000.00",
      "frequency": 0,
      "day": 0,
      "onboarding": false,
      "created_at": "2022-01-04T14:16:57.255394-06:00",
      "updated_at": "2022-01-04T14:16:57.255402-06:00",
      "configuration": null,
      "project": "ed0f0467-35b3-40bf-b042-782df31aa495"
    }
  ]
}
```

# Consultar detalle de la meta


```bash
curl --request GET \
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/3cb17971-e530-4070-b37f-c7b164699295/
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
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/3cb17971-e530-4070-b37f-c7b164699295/ \
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
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/projects/3cb17971-e530-4070-b37f-c7b164699295/ \
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

## Obtener las reglas del usuario

```bash
curl --request GET \
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/project/3cb17971-e530-4070-b37f-c7b164699295/rules/
```

respuesta 

```json
[
  {
    "id": "600b65a1-02e1-499e-ba7c-fe5d741c425d",
    "rule_type": {
      "id": "a3125075-ff44-4b8b-be29-6c73fd846872",
      "name": "Pasión Futbolera",
      "description": "Ahorra cada vez que tu equipo juegue, gane o anote un gol",
      "metadata": {
        "icon": "https://via.placeholder.com/150",
        "limit": 3,
        "active": true,
        "default": false,
        "frequency_description": "${} cada que {}"
      },
      "catalog": "47bd8165-2b84-4bc9-91d0-6126beee2b40"
    },
    "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
    "project": "3cb17971-e530-4070-b37f-c7b164699295",
    "status": "65729137-0844-4b28-85b5-2e81b73a948a",
    "rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e",
    "amount": "4000.00",
    "frequency": 0,
    "day": 0,
    "onboarding": false,
    "created_at": "2021-12-30T20:40:37.255871-06:00",
    "updated_at": "2021-12-30T20:40:37.255891-06:00"
  },
  {
    "id": "9e4a6d9d-bd45-4940-a085-100e20e2742e",
    "rule_type": {
      "id": "01fdb81f-88ef-4f7a-bc0a-c9f66430f391",
      "name": "Desafío 52 semanas",
      "description": "Ahorra según el desafío de las 52 semanas, aumentando un dólar al día",
      "metadata": {
        "icon": "https://via.placeholder.com/150",
        "limit": 1,
        "active": true,
        "default": false,
        "frequency_description": "${} cada semana"
      },
      "catalog": "47bd8165-2b84-4bc9-91d0-6126beee2b40"
    },
    "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
    "project": "3cb17971-e530-4070-b37f-c7b164699295",
    "status": "65729137-0844-4b28-85b5-2e81b73a948a",
    "rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e",
    "amount": "4000.00",
    "frequency": 0,
    "day": 0,
    "onboarding": false,
    "created_at": "2021-12-30T22:08:47.324695-06:00",
    "updated_at": "2021-12-30T22:08:47.324726-06:00"
  }
]
```

## Crear las reglas del usuario

```bash
curl --request POST \
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/project/3cb17971-e530-4070-b37f-c7b164699295/rules/ \
  --header 'content-type: application/json' \
  --data '{"rule_type" : "a3125075-ff44-4b8b-be29-6c73fd846872","rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e","amount": 4000.00}'
```
respuesta 

```json
{
  "id": "9e4a6d9d-bd45-4940-a085-100e20e2742e",
  "rule_type": {
    "id": "01fdb81f-88ef-4f7a-bc0a-c9f66430f391",
    "name": "Desafío 52 semanas",
    "description": "Ahorra según el desafío de las 52 semanas, aumentando un dólar al día",
    "metadata": {
      "icon": "https://via.placeholder.com/150",
      "limit": 1,
      "active": true,
      "default": false,
      "frequency_description": "${} cada semana"
    },
    "catalog": "47bd8165-2b84-4bc9-91d0-6126beee2b40"
  },
  "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
  "project": "3cb17971-e530-4070-b37f-c7b164699295",
  "status": "65729137-0844-4b28-85b5-2e81b73a948a",
  "rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e",
  "amount": "4000.00",
  "frequency": 0,
  "day": 0,
  "onboarding": false,
  "created_at": "2021-12-30T22:08:47.324695-06:00",
  "updated_at": "2021-12-30T22:08:47.324726-06:00"
}
```

## Detalle de la regla

```bash
curl --request GET \
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/project/3cb17971-e530-4070-b37f-c7b164699295/rules/6e10b138-9899-43cf-8a62-d6119456aa82/
```
respuesta 

```json
{
  "id": "6e10b138-9899-43cf-8a62-d6119456aa82",
  "rule_type": {
    "id": "a3125075-ff44-4b8b-be29-6c73fd846872",
    "name": "Pasión Futbolera",
    "description": "Ahorra cada vez que tu equipo juegue, gane o anote un gol",
    "metadata": {
      "icon": "https://via.placeholder.com/150",
      "limit": 3,
      "active": true,
      "default": false,
      "frequency_description": "${} cada que {}"
    },
    "catalog": "47bd8165-2b84-4bc9-91d0-6126beee2b40"
  },
  "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
  "project": "3cb17971-e530-4070-b37f-c7b164699295",
  "status": "65729137-0844-4b28-85b5-2e81b73a948a",
  "rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e",
  "amount": "7000.00",
  "frequency": 0,
  "day": 0,
  "onboarding": true,
  "created_at": "2021-05-01T14:20:30-05:00",
  "updated_at": "2021-12-30T20:18:45.848324-06:00"
}
```

## Actualizar parcialmente la regla. Forma 1.

```bash
curl --request PATCH \
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/project/3cb17971-e530-4070-b37f-c7b164699295/rules/6e10b138-9899-43cf-8a62-d6119456aa82/ \
  --header 'content-type: application/json' \
  --data '{"amount": 6000.00}'
```
respuesta 

```json
{
  "id": "6e10b138-9899-43cf-8a62-d6119456aa82",
  "rule_type": {
    "id": "a3125075-ff44-4b8b-be29-6c73fd846872",
    "name": "Pasión Futbolera",
    "description": "Ahorra cada vez que tu equipo juegue, gane o anote un gol",
    "metadata": {
      "icon": "https://via.placeholder.com/150",
      "limit": 3,
      "active": true,
      "default": false,
      "frequency_description": "${} cada que {}"
    },
    "catalog": "47bd8165-2b84-4bc9-91d0-6126beee2b40"
  },
  "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
  "project": "3cb17971-e530-4070-b37f-c7b164699295",
  "status": "65729137-0844-4b28-85b5-2e81b73a948a",
  "rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e",
  "amount": "6000.00",
  "frequency": 0,
  "day": 0,
  "onboarding": true,
  "created_at": "2021-05-01T14:20:30-05:00",
  "updated_at": "2021-12-30T22:16:13.761477-06:00"
}
```

## Actualizar parcialmente la regla. Forma 2.

```bash
curl --request PUT \
  --url http://127.0.0.1/project-service/user/0390a508-dba5-4344-b77f-93e1227d42f4/project/3cb17971-e530-4070-b37f-c7b164699295/rules/6e10b138-9899-43cf-8a62-d6119456aa82/ \
  --header 'content-type: application/json' \
  --data '{"user": "0390a508-dba5-4344-b77f-93e1227d42f4","project": "3cb17971-e530-4070-b37f-c7b164699295","rule_type": "a3125075-ff44-4b8b-be29-6c73fd846872","rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e","amount": 7000.00,"onboarding": 1,"frequency": 0}'
```
respuesta 

```json
{
  "id": "6e10b138-9899-43cf-8a62-d6119456aa82",
  "rule_type": {
    "id": "a3125075-ff44-4b8b-be29-6c73fd846872",
    "name": "Pasión Futbolera",
    "description": "Ahorra cada vez que tu equipo juegue, gane o anote un gol",
    "metadata": {
      "icon": "https://via.placeholder.com/150",
      "limit": 3,
      "active": true,
      "default": false,
      "frequency_description": "${} cada que {}"
    },
    "catalog": "47bd8165-2b84-4bc9-91d0-6126beee2b40"
  },
  "user": "0390a508-dba5-4344-b77f-93e1227d42f4",
  "project": "3cb17971-e530-4070-b37f-c7b164699295",
  "status": "65729137-0844-4b28-85b5-2e81b73a948a",
  "rule_category": "a34b4b3f-fb71-4e0b-b82e-beb94b79932e",
  "amount": "7000.00",
  "frequency": 0,
  "day": 0,
  "onboarding": true,
  "created_at": "2021-05-01T14:20:30-05:00",
  "updated_at": "2021-12-30T22:17:41.743765-06:00"
}
```
