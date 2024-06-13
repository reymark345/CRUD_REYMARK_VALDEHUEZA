from django.db import models

from datetime import datetime


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee'

class ValidatedGrants(models.Model):
    household_no = models.CharField(max_length=128, blank=True, null=True)
    set = models.CharField(max_length=128, blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    middle_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    extension_name = models.CharField(max_length=128, blank=True, null=True)
    province = models.CharField(max_length=128, blank=True, null=True)
    municipality = models.CharField(max_length=128, blank=True, null=True)
    barangay = models.CharField(max_length=128, blank=True, null=True)
    sex = models.CharField(max_length=128, blank=True, null=True)
    distribution_status = models.CharField(max_length=128, blank=True, null=True)
    date_of_card_release_actual = models.CharField(max_length=128, blank=True, null=True)
    who_released_cash_card = models.CharField(max_length=128, blank=True, null=True)
    where_the_cash_card_released = models.CharField(max_length=128, blank=True, null=True)
    date_of_card_released = models.CharField(max_length=128, blank=True, null=True)
    cash_card_number = models.CharField(max_length=128, blank=True, null=True)
    type_id = models.CharField(max_length=128, blank=True, null=True)
    id_number = models.CharField(max_length=128, blank=True, null=True)
    client_status = models.CharField(max_length=128, blank=True, null=True)
    income = models.CharField(max_length=128, blank=True, null=True)
    member_status = models.CharField(max_length=128, blank=True, null=True)
    duplicate_name = models.CharField(max_length=128, blank=True, null=True)
    verified_barangay = models.CharField(max_length=128, blank=True, null=True)
    physical_cc_presented = models.CharField(max_length=128, blank=True, null=True)
    overall_remarks = models.CharField(max_length=128, blank=True, null=True)
    eligible = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'validated_grants'


class GranteeList(models.Model):
    region = models.CharField(max_length=128, blank=True, null=True)
    province = models.CharField(max_length=128, blank=True, null=True)
    municipality = models.CharField(max_length=128, blank=True, null=True)
    barangay = models.CharField(max_length=128, blank=True, null=True)
    purok = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    hh_id = models.CharField(max_length=128, blank=True, null=True)
    entryid = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    middle_name = models.CharField(max_length=128, blank=True, null=True)
    extension_name = models.CharField(max_length=128, blank=True, null=True)
    birthday = models.CharField(max_length=128, blank=True, null=True)
    age = models.CharField(max_length=128, blank=True, null=True)
    client_status = models.CharField(max_length=128, blank=True, null=True)
    member_status = models.CharField(max_length=128, blank=True, null=True)
    registration_status = models.CharField(max_length=128, blank=True, null=True)
    sex = models.CharField(max_length=128, blank=True, null=True)
    relationship_to_hh_head = models.CharField(max_length=128, blank=True, null=True)
    ipaffiliation = models.CharField(max_length=128, blank=True, null=True)
    hh_set = models.CharField(max_length=128, blank=True, null=True)
    group = models.CharField(max_length=128, blank=True, null=True)
    mothers_maiden = models.CharField(max_length=128, blank=True, null=True)
    date_of_enumeration = models.CharField(max_length=128, blank=True, null=True)
    lbp_account_number = models.CharField(max_length=128, blank=True, null=True)
    mode_of_payment = models.CharField(max_length=128, blank=True, null=True)
    date_tagged_hhstatus = models.CharField(max_length=128, blank=True, null=True)
    tagged_by = models.CharField(max_length=128, blank=True, null=True)
    date_registered = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'grantee_list'
        

        





        
        

        
        


