# Generated by Django 2.2.24 on 2021-12-23 09:06

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0134_granthalloffame_granthalloffamegrantee'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrantPayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('name', models.CharField(help_text='Display Name for Payout', max_length=25)),
                ('contract_address', models.CharField(blank=True, help_text='Payout Contract from which funds would be claimed', max_length=255, null=True)),
                ('network', models.CharField(choices=[('mainnet', 'mainnet'), ('rinkeby', 'rinkeby')], default='mainnet', help_text='Network where contract is deployed', max_length=15)),
                ('payout_token', models.CharField(default='DAI', help_text='Currency in which funds would be paid', max_length=10)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('ready', 'ready'), ('expired', 'expired'), ('funding_withdrawn', 'funding_withdrawn')], default='pending', max_length=20)),
                ('funding_withdrawal_date', models.DateTimeField(blank=True, help_text='When was funding in Matching Contract withdrawn?', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='claim_tx',
            field=models.CharField(blank=True, help_text='The claim txid', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clrmatch',
            name='payout_tx',
            field=models.CharField(blank=True, help_text='The payout txid', max_length=255),
        ),
        migrations.AddField(
            model_name='clrmatch',
            name='grant_payout',
            field=models.ForeignKey(blank=True, help_text='Grant Payout', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clr_matches', to='grants.GrantPayout'),
        ),
        migrations.AddField(
            model_name='grantclr',
            name='grant_payout',
            field=models.ForeignKey(blank=True, help_text='Grant Payout', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grant_clrs', to='grants.GrantPayout'),
        ),
    ]
