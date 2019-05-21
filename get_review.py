def get_review(_n):
    import mysql.connector

    conn = mysql.connector.connect(host='202.31.147.28', db='menu', charset='utf8', user='root', password='0000')
    cur = conn.cursor()

    cur.execute("SELECT * FROM review")
    review = cur.fetchall()
    result = []
    for i in review:
        if _n == 3:
            pass
        else:
            result.append(i[_n])
    print(result)

    cur.close()
    conn.close()
    
    return result


if __name__ == '__main__':
    get_review(3)
