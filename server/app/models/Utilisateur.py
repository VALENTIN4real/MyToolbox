from ..database.db import get_db


class Utilisateur:
    def __init__(self, id, nom, has_tr, valeur_tr, part_salariale_tr, part_patronale_tr):
        self.id = id
        self.nom = nom
        self.has_tr = has_tr
        self.valeur_tr = valeur_tr
        self.part_salariale_tr = part_salariale_tr
        self.part_patronale_tr = part_patronale_tr

    @staticmethod
    def get_user_by_id():
        db = get_db()
        user = db.execute(
            'SELECT * FROM utilisateur WHERE id = ?', id
        ).fetchone()
        return user

    @staticmethod
    def get_users():
        db = get_db()
        users = db.execute(
            'SELECT * FROM utilisateur'
        ).fetchall()
        return users