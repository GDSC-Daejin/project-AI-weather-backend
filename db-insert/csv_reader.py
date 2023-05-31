import csv
import glob
import multiprocessing
import os
from db import sql_command, get_database_connection


def mt_process(args):
    sql_command(
        args["name"],
        args["cg1"],
        args["cg2"],
        args["url"],
        args["src"],
        args["fit"],
        args["seasons"],
        args["thickness"],
        args["index"],
    )


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    file_pattern = "csv/*.csv"
    file_list = glob.glob(file_pattern)

    process = 10
    if get_database_connection():
        for file_path in file_list:
            with open(file_path, "r", encoding="UTF8") as f:
                rdr = csv.reader(f)
                next(rdr)
                with multiprocessing.Pool(processes=process) as pool:
                    for line in rdr:
                        Label = {}
                        Label["index"] = line[0]
                        Label["name"] = line[1]
                        Label["cg1"] = line[2]
                        Label["cg2"] = line[3]
                        Label["url"] = line[4]
                        Label["src"] = line[5]
                        Label["fit"] = line[6]
                        Label["seasons"] = line[7]
                        Label["thickness"] = line[8]
                        pool.apply_async(mt_process, (Label,))
                    pool.close()
                    pool.join()
            if os.path.isfile(file_path):
                os.remove(file_path)
