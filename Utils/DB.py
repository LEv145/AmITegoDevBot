from contextlib import closing
import sqlite3


class Get:
    def __init__(self):
        pass

    def mute(self, member):
        conn = sqlite3.connect("./Data/DataBase/members_mutes.db")
        cursor = conn.cursor()

        if member:
            cursor.execute(f"SELECT * FROM mute WHERE member={member.id}")
            result = cursor.fetchone()
        else:
            cursor.execute(f"SELECT * FROM mute")
            result = cursor.fetchall()

        return result

    def warns(self, member):
        conn = sqlite3.connect("./Data/DataBase/members_warns.db")
        cursor = conn.cursor()

        result = None
        if member:
            cursor.execute(f"SELECT * FROM warns WHERE member={member.id} ORDER BY ID DESC")
            result = cursor.fetchall()

        return result

    def privateChannels(self, member):
        conn = sqlite3.connect("./Data/Cache/guild_channels.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM privates WHERE member={member.id}")
        result = cursor.fetchone()

        conn.close()
        return result

    def options(self, name):
        conn = sqlite3.connect("./Data/DataBase/guild_options.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {name}")
        result = cursor.fetchone()

        conn.close()
        return result


class Set:
    def __init__(self):
        pass

    def privateChannels(self, channel, member):
        conn = sqlite3.connect("./Data/Cache/guild_channels.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM privates WHERE member={member.id}")
        if cursor.fetchone():
            cursor.execute(f"UPDATE privates SET member={member.id}, channel={channel.id} WHERE member={member.id}")
        else:
            cursor.execute(f"INSERT INTO privates VALUES ({channel.id}, {member.id})")

        conn.commit()
        conn.close()

    def options(self, data):  # [{"name": "имя", "data": "инфа"}, {}, {}]
        conn = sqlite3.connect("./Data/DataBase/guild_options.db")
        cursor = conn.cursor()

        for i in data:
            name = i["name"]
            update = i["update"]
            insert = i["insert"]

            cursor.execute(f"SELECT * FROM {name}")

            if not cursor.fetchone():
                cursor.execute(f"INSERT INTO {name} VALUES ({insert})")
            else:
                cursor.execute(f"UPDATE {name} SET {update}")

        conn.commit()
        conn.close()

    def mute(self, member, time):
        conn = sqlite3.connect("./Data/DataBase/members_mutes.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM mute")
        if not cursor.fetchone():
            cursor.execute(f"INSERT INTO mute VALUES ({member.id}, 0)")
        else:
            cursor.execute(f"UPDATE mute SET time = {time} WHERE member='{member.id}'")

        conn.commit()
        conn.close()

    def warns(self, mode, member, moderator, *reason):
        conn = sqlite3.connect("./Data/DataBase/members_mutes.db")
        cursor = conn.cursor()

        if mode == "add":
            ids = 0
            for i in cursor.execute(f"SELECT * FROM warns WHERE member={member.id} ORDER BY ID DESC").fetchall():
                if not i["id"]:
                    ids = 1
                    break
                else:
                    ids = i["id"] + 1
                    break

            cursor.execute(f"INSERT INTO warns VALUES ({ids}, {member.id}, {moderator}, {reason[0]}")
            return ids

        if mode == "remove":
            cursor.execute(f"DELETE FROM warns WHERE ID = {moderator}")

        conn.commit()
        conn.close()




