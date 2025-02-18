import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,  precision_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

processed_data = r"../data/processed/KDD.csv"
raw_data = r"../data/raw/KDD+.txt"
columns = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
    'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
    'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login',
    'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
    'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
    'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
    'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'attack', 'level'
]

if not os.path.exists(processed_data):
    processed_dir = os.path.dirname(processed_data)
    print(processed_dir)
    os.makedirs(processed_dir)
    try:
        data = pd.read_csv(raw_data, names=columns)
        data.to_csv(processed_data, index=False)
        print("Data Saved!")
    except Exception as e:
        print(f"Exception occurred {e}")
else:
    pass

# TODO: Read Network data

network_data = pd.read_csv(processed_data)
print(network_data.head())






