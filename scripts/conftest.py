import pytest
import pandas as pd


@pytest.fixture
def id_col():
    ids =  [130079, 130080, 130081, 130082, 130083, 130084, 130085, 130086, 130087, 130088, 130089, 130090,
            130091, 130092, 130093, 130094, 130095, 130096, 130097, 130098, 130099, 130100, 130101, 130102, 130103,
            130104, 130105, 130106, 130107, 130108, 130109, 130110, 130111, 130112, 130113, 130114, 130115, 130116,
            130117, 130118]
    return ids


@pytest.fixture
def adexi_surv():
    simple_surv = {
        "adexi": {
            "sub1": {
                "questions": [1, 2, 5, 7, 8, 9, 11, 12, 13],
                "score_type": "sum"
            },
            "sub2": {
                "questions": [3, 4, 6, 10, 14], 
                "score_type": "sum"
            }
        }
    }
    return simple_surv


@pytest.fixture
def aq10_surv():
    cond_surv = {
        "aq10": {
            "sub1": {
                "questions": [1, 7, 8, 10],
                "criteria": [1, 2],
                "score_type": "count"
            }, 
            "sub2": {
                "questions": [2, 3, 4, 5, 6, 9],
                "criteria": [3, 4],
                "score_type": "count"
            },
            "total": {
                "questions": [],
                "products": ["sub1", "sub2"],
                "score_type": "sum"
            }
        }
    }
    return cond_surv


@pytest.fixture
def conditional_data_single(aq10_surv, id_col):
    solutions = {
        "aq10_scrd_sub1_s1_r1_e1": 
                        ["N/A",1,"N/A",1,"N/A",2,1,4,"N/A",1,"N/A",1,"N/A","N/A",3,"N/A","N/A",2,"N/A",2,"N/A",
                         "N/A",3,"N/A","N/A",1,"N/A",1,"N/A","N/A","N/A",2,1,0,"N/A","N/A",1,2,0,"N/A"],
        "aq10_scrd_sub2_s1_r1_e1": 
                    ["N/A",0,"N/A",3,"N/A",1,0,2,"N/A",4,"N/A",1,"N/A","N/A",2,"N/A","N/A",3,"N/A",1,"N/A","N/A",0,
                     "N/A","N/A",0,"N/A",4,"N/A","N/A","N/A",4,2,1,"N/A","N/A",2,1,3,"N/A"],
        "aq10_scrd_total_s1_r1_e1":
                    ["N/A",1,"N/A",4,"N/A",3,1,6,"N/A",5,"N/A",2,"N/A","N/A",5,"N/A","N/A",5,"N/A",3,"N/A","N/A",
                     3,"N/A","N/A",1,"N/A",5,"N/A","N/A","N/A",6,3,1,"N/A","N/A",3,3,3,"N/A"]
    }
    solution_df = pd.DataFrame(data=solutions, index=id_col)
    cond_dat = "test_data/cond_data.csv"
    return aq10_surv, cond_dat, solution_df


@pytest.fixture
def conditional_data_multiple(aq10_surv, conditional_data_single):
    _, _, solution_df = conditional_data_single
    solution_df["aq10_scrd_sub1_s1_r2_e1"] = ["N/A",1,"N/A","N/A","N/A",2,1,4,"N/A",1,"N/A",1,"N/A","N/A","N/A",
                                              "N/A","N/A",2,"N/A",2,"N/A","N/A",3,"N/A","N/A",1,"N/A",1,"N/A",
                                              "N/A","N/A",2,1,0,"N/A","N/A",1,2,0,"N/A"]
    solution_df["aq10_scrd_sub2_s1_r2_e1"] = ["N/A",0,"N/A",3,"N/A",1,"N/A","N/A","N/A",4,"N/A","N/A","N/A","N/A",2,
                                              "N/A","N/A",3,"N/A","N/A","N/A","N/A",0,"N/A","N/A",0,"N/A",4,"N/A",
                                              "N/A","N/A",4,2,1,"N/A","N/A",2,1,3,"N/A"]
    solution_df["aq10_scrd_total_s1_r2_e1"] = ["N/A",1,"N/A","N/A","N/A",3,"N/A","N/A","N/A",5,"N/A","N/A","N/A",
                                               "N/A","N/A","N/A","N/A",5,"N/A","N/A","N/A","N/A",3,"N/A","N/A",1,
                                               "N/A",5,"N/A","N/A","N/A",6,3,1,"N/A","N/A",3,3,3,"N/A"]
    simple_dat_mult = "test_data/cond_data_mult.csv"
    return aq10_surv, simple_dat_mult, solution_df


@pytest.fixture
def simple_data_single(adexi_surv, id_col):
    simple_dat = "test_data/simple_data.csv"
    solutions = {
        "adexi_scrd_sub1_s1_r1_e1": 
                        ["N/A", 22, "N/A", 23, "N/A", 18, 11, 26, "N/A", 22, "N/A", 18, "N/A", "N/A", 26, "N/A",
                        "N/A", 26, "N/A", 26, "N/A", "N/A", 9, "N/A", "N/A", 17, "N/A", 33, "N/A", "N/A", 
                        "N/A", 23, 21, 23, "N/A", "N/A", 22, 27, 35, "N/A"],
        "adexi_scrd_sub2_s1_r1_e1": 
                    ["N/A", 14, "N/A", 15, "N/A", 20, 10, 14, "N/A", 10, "N/A", 12, "N/A", "N/A", 20, "N/A", "N/A", 
                     17, "N/A", 16, "N/A", "N/A", 6, "N/A", "N/A", 11, "N/A", 14, "N/A", "N/A", "N/A", 19, 12,
                     9, "N/A", "N/A", 12, 15, 24, "N/A"]
    }
    solution_df = pd.DataFrame(data=solutions, index=id_col)
    return adexi_surv, simple_dat, solution_df


@pytest.fixture
def simple_data_multiple(adexi_surv, simple_data_single):
    _, _, solution_df = simple_data_single
    solution_df["adexi_b_scrd_sub1_s1_r2_e1"] = ["N/A","N/A","N/A",23,"N/A","N/A","N/A",26,"N/A","N/A","N/A",18,
                                                 "N/A","N/A",26,"N/A","N/A",26,"N/A",26,"N/A","N/A",9,"N/A","N/A",
                                                 17,"N/A",33,"N/A","N/A","N/A",23,21,23,"N/A","N/A",22,27,35,"N/A"]
    solution_df["adexi_b_scrd_sub2_s1_r2_e1"] = ["N/A","N/A","N/A",15,"N/A",20,10,"N/A","N/A","N/A","N/A",12,"N/A",
                                                 "N/A",20,"N/A","N/A",17,"N/A",16,"N/A","N/A",6,"N/A","N/A",11,"N/A",
                                                 14,"N/A","N/A","N/A",19,12,9,"N/A","N/A",12,15,24,"N/A"]
    simple_dat_mult = "test_data/simple_data_mult.csv"
    return adexi_surv, simple_dat_mult, solution_df


@pytest.fixture
def reverse_data_single(id_col):
    reverse_surv = {
        "ambi": {
            "sub1": {
                "questions": [9, 4, 6], 
                "rev_questions": [9, 4, 6],
                "max": 2,
                "score_type": "sum"
            },
            "sub2": {
                "questions": [12, 14, 15], 
                "rev_questions": [15],
                "max": 2,
                "score_type": "sum"
            },
            "total": {
                "questions": [],
                "products": ["sub1", "sub2"],
                "score_type": "sum"
            }
        }
    }
    solutions = {
        "adexi_b_scrd_sub1_s1_r1_e1": 
                        ["N/A", 22, "N/A", 23, "N/A", 18, 11, 26, "N/A", 22, "N/A", 18, "N/A", "N/A", 26, "N/A",
                        "N/A", 26, "N/A", 26, "N/A", "N/A", 9, "N/A", "N/A", 17, "N/A", 33, "N/A", "N/A", 
                        "N/A", 23, 21, 23, "N/A", "N/A", 22, 27, 35, "N/A"],
        "adexi_b_scrd_sub2_s1_r1_e1": 
                    ["N/A","N/A","N/A",15,"N/A",20,10,"N/A","N/A","N/A","N/A",12,"N/A","N/A",20,"N/A","N/A",17,
                     "N/A",16,"N/A","N/A",6,"N/A","N/A",11,"N/A",14,"N/A","N/A","N/A",19,12,9,"N/A","N/A",12,15,
                     24,"N/A"]
    }
    solution_df = pd.DataFrame(data=solutions, index=id_col)
    reverse_dat = "test_data/reverse_data.csv"
    return reverse_surv, reverse_dat, solution_df
