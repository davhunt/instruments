import pandas as pd
import sys

if __name__ == "__main__":
    redcap_path = sys.argv[1]
    dd_path = sys.argv[2]

    datadict_df = pd.read_csv(dd_path)

    id_col_name = "record_id" # default
    for _, row in datadict_df.iterrows():
        prov = row["provenance"].split(" ")
        if "file:" in prov and "variable:" in prov:
            idx = prov.index("file:")
            filename = prov[idx+1].strip("\";,")
            if filename in redcap_path.lower() and "id:" in prov:
                idx = prov.index("id:")
                id_col_name = prov[idx+1].strip("\";,")
                break
    if id_col_name == "record_id":
        print(id_col_name)
        sys.exit(0)
    rc_df = pd.read_csv(redcap_path)
    for col, _ in rc_df.iteritems():
        found = False
        if col.startswith(id_col_name):
            id_col = col
            found = True
            break
    if not found:
        sys.exit("Error: Can't find column starting with " + id_col_name + " in redcap: " + redcap_path + ", exiting")
    else:
        print(id_col)
