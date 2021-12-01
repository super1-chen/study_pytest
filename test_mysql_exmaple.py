import datetime

import pytest
from pytest import FixtureRequest
from pytest_mysql import factories
from pytest_mysql.config import get_config
from peewee import MySQLDatabase

from models import User

mysql_in_docker = factories.mysql_noproc()
mysql = factories.mysql("mysql_in_docker")

def peewee_mysql(fixture_name, *models):
    @pytest.fixture
    def inner_fixture(mysql, request: FixtureRequest):
        config = get_config(request)
        test_db =  MySQLDatabase(**{
                "host": config["host"],
                "port": int(config["port"]),
                "user": config["user"],
                "passwd": config["passwd"],
                "database": config["dbname"]
            }
        )
        test_db.bind(models, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(models)
        yield test_db
        test_db.drop_tables(models)
        test_db.close()
    return inner_fixture

user_fixture = peewee_mysql("user_fixture", User)

def test_mysql_peewee(user_fixture):
    user = User()
    user.username = "chenchao"
    user.password = "chenchao"
    user.email = "tccc123@163.com"
    user.join_date = datetime.datetime(2021, 11, 11, 00, 11, 11)
    user.save()
    
    new_user = User.get_by_id(User.id == user.id)
    assert new_user.id == 1
    assert new_user.email == "tccc123@163.com"

def test_mysql_docker(mysql):
    """Run test."""
    cur = mysql.cursor()
    cur.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);")
    cur.execute("show databases;")
    mysql.commit()
    cur.close()
