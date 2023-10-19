from faker import Faker
fake = Faker("id_ID")

def generate_data(records):
    queries = []
    for i in range (0, records + 1):
        title = fake.catch_phrase()
        desc = fake.sentence(nb_words=10)
        # email = fake.email()
        # query = f"INSERT INTO customer (name, email) VALUES ('{name}', '{email}');"
        query = f"INSERT INTO article (title, description) VALUES ('{title}','{desc}');" 
        queries.append(query)
    
    with open ("dummy.txt", "w") as file:
        file.write("\n".join(queries))

if __name__ == "__main__":
    num_records = 20
    generate_data(num_records)
    print("Pembuatan Data telah selesai!")

