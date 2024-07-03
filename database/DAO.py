from database.DB_connessione import DBConnect
from model.state import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from state s  """

        cursor.execute(query)

        for row in cursor:
            result.append(
                State(row["id"], row["Name"], row["Capital"], row["Lat"], row["Lng"], row["Area"], row["Population"],
                      row["Neighbors"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(n1,n2, anno,giorni):
        """ somma il numero di avvistamenti, purchè non siano
        passati più di x giorni da uno all'altro"""
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as p
                    from  sighting s ,sighting s2
                    where s.state = %s and s2.state = %s
                    and DATEDIFF(s.`datetime`,s2.`datetime`) < %s
                    and YEAR(s.`datetime`) = %s and s.`datetime` = s2.`datetime`"""
        cursor.execute(query,(n1,n2,giorni,anno))
        for row in cursor:
            result.append(row["p"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNeigh(idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT  *
                    from neighbor n 
                    where n.state1 > n.state2 
                    """
        cursor.execute(query)
        for row in cursor:
            result.append((idMap[row["state1"]],idMap[row["state2"]]))
        cursor.close()
        conn.close()
        return result