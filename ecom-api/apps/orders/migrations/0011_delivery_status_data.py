from django.db import migrations
import os


def load_sql_file(filename):
    """Load sql script file."""
    file_path = os.path.join(os.path.dirname(__file__), filename)
    sql_statement = open(file_path).read()
    return sql_statement


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0010_deliverystatus"),  # Add your existing app migration here
    ]

    operations = [
        migrations.RunSQL(load_sql_file("0011_delivery_status_data.sql")),
    ]
