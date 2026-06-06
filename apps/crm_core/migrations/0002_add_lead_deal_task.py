from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm_core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lead",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("account", models.ForeignKey(blank=True, null=True, on_delete=models.deletion.CASCADE, related_name='leads', to='crm_core.account')),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("status", models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Deal",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("account", models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='deals', to='crm_core.account')),
                ("title", models.CharField(max_length=255)),
                ("value", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("stage", models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("account", models.ForeignKey(blank=True, null=True, on_delete=models.deletion.CASCADE, related_name='tasks', to='crm_core.account')),
                ("subject", models.CharField(max_length=255)),
                ("due_date", models.DateField(blank=True, null=True)),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
    ]
