from data.config import DATABASE, USER, PASSWORD, HOST, PORT

print(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
