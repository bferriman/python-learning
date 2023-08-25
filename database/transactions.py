import psycopg2
from config import config


def add_part(part_name, vendor_list):
    # statement for inserting a new row into the parts table
    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"
    # statement for inserting a new row into the vendor_parts table
    assign_vendor = "INSERT INTO vendor_parts(vendor_id,part_id) VALUES(%s,%s)"

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # A new transaction is created by psycopg as soon as a SQL statement is
        # executed. All following statements will be part of same transaction
        # until you call commit()/rollback() or a statement fails - which will
        # abort the entire transaction.

        # insert a new part - begin transaction
        cur.execute(insert_part, (part_name,))
        # get the part id
        part_id = cur.fetchone()[0]
        # assign parts provided by vendors
        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))

        # commit changes - close transaction
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Screen', (5, 6))
    add_part('Antenna', (6, 7))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))


# Using 'with' can be a good way to manage transactions. Your
# transaction will commit automatically as long as no
# exception occurs within the 'with' block. A failing 'with'
# block ends the cursor, but not the connection, so the same
# connection can be used for subsequent transactions. vvv

# conn = psycopg2.connect(dsn)

# # transaction 1
# with conn:
#     with conn.cursor() as cur:
#         cur.execute(sql)

# # transaction 2
# with conn:
#     with conn.cursor() as cur:
#         cur.execute(sql)

# conn.close()