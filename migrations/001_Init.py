"""Peewee migrations -- 001_Init.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['table_name']            # Return model in current state by name
    > Model = migrator.ModelClass                   # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.run(func, *args, **kwargs)           # Run python function with the given args
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.add_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)
    > migrator.add_constraint(model, name, sql)
    > migrator.drop_index(model, *col_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.drop_constraints(model, *constraints)

"""

from contextlib import suppress

import peewee as pw
from peewee_migrate import Migrator


with suppress(ImportError):
    import playhouse.postgres_ext as pw_pext


def migrate(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your migrations here."""
    
    @migrator.create_model
    class BaseModel(pw.Model):
        id = pw.AutoField()

        class Meta:
            table_name = "basemodel"

    @migrator.create_model
    class TgUser(pw.Model):
        id = pw.BigIntegerField(primary_key=True)
        name = pw.CharField(max_length=255, null=True)
        is_admin = pw.BooleanField(default=False)
        last_activity = pw.DateTimeField(null=True)
        created_at = pw.DateTimeField(default=False, null=True)

        class Meta:
            table_name = "tguser"

    @migrator.create_model
    class Title(pw.Model):
        id = pw.AutoField()
        name = pw.CharField(max_length=255, null=True)
        is_default = pw.BooleanField(default=False)
        place = pw.IntegerField(null=True)
        tap_count = pw.IntegerField(default=0)

        class Meta:
            table_name = "title"

    @migrator.create_model
    class Photo(pw.Model):
        id = pw.AutoField()
        photo_id = pw.CharField(max_length=255, null=True)

        class Meta:
            table_name = "photo"

    @migrator.create_model
    class Person(pw.Model):
        id = pw.AutoField()
        name = pw.CharField(max_length=255, null=True)
        place = pw.IntegerField(null=True)

        class Meta:
            table_name = "person"

    @migrator.create_model
    class Event(pw.Model):
        id = pw.AutoField()
        user = pw.ForeignKeyField(column_name='user_id', field='id', model=migrator.orm['tguser'], null=True)
        title = pw.ForeignKeyField(column_name='title_id', field='id', model=migrator.orm['title'], null=True)
        is_default = pw.BooleanField(default=False)
        text = pw.TextField(null=True)
        photo = pw.ForeignKeyField(column_name='photo_id', field='id', model=migrator.orm['photo'], null=True)
        person = pw.ForeignKeyField(column_name='person_id', field='id', model=migrator.orm['person'], null=True)
        button_text = pw.CharField(max_length=255, null=True)
        button_link = pw.CharField(max_length=255, null=True)
        date = pw.DateTimeField(null=True)
        message_date = pw.DateTimeField(null=True)

        class Meta:
            table_name = "event"


def rollback(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your rollback migrations here."""
    
    migrator.remove_model('event')

    migrator.remove_model('person')

    migrator.remove_model('photo')

    migrator.remove_model('title')

    migrator.remove_model('tguser')

    migrator.remove_model('basemodel')
