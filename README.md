# fullthrottlelabs

• Custom management command to populate the database with dummy data <br />
• REST API to view the model data. <br />

## About

1. Created custom management comand for populating the database with dummy data.

### Custom management command created

```shell
python manage.py help	
```

#### Output

```shell
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

...

[main]
    custom_management_command

...
```

### Populating data into database

```shell
python manage.py custom_management_command 2
```

#### Output

```shell
Members are created successfully!
```

2. REST Api View- Utilized ListApiView from djangorestframework to display the data in REST API/ Json format.

• API VIEW- [Click Here](http://fullthrottle.pythonanywhere.com/?format=api).<br />
• JSON FORMAT- [Click Here](http://fullthrottle.pythonanywhere.com/?format=json)<br />

