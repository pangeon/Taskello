from utils import path_finder as path
from utils import str_utils
from utils.db_manager import mysql_connector as db
from data import _variables as app
from data import _db_config as cfg_db

from controllers import profiles_controller as profile_man
from controllers import tasks_controller as task_man
from controllers import types_controller as type_man
from controllers import assigned_tasks_controller as ass_task_man
from controllers import all_data_controller as all_data_man

import itertools

def welcome():
    print("--- {}, ver {} ---\n".format(app.name, app.version))

conn = db.define_db(
    cfg_db.db_host, 
    cfg_db.db_name, 
    cfg_db.db_user, 
    cfg_db.db_pass
)

if __name__ == "__main__":
    prof = profile_man.get_profile_email(conn, "pangeon@tlen.pl")
    print(prof)
    # str = "'pangeon@tlen.pl'"
    # sql = "SELECT * FROM profiles WHERE email = " + str
    # result = db.sql_single_querry(conn, sql)
    # print(result)
    # l_prof = profile_man.login_profile(conn, val = (
    #     "pangeon@tlen.pl", "78ABC"
    # ))
    # print(l_prof)
    pass