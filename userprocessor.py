from utility import Utility
from sql import SQL

class UserProcessor:

    def process(self, url, filepath):
        try:
            data = Utility.request(url)
            if data:
                all_subscription = []
                for item in data:
                    #Remove or transform PII
                    item.pop('firstName', None)
                    item.pop('lastName', None)
                    item.pop('address', None)
                    item.pop('zipCode', None)
                    item['email'] = item['email'][item['email'].index('@') + 1:]


                    profile = item.pop('profile', None)
                    #flatten profile info
                    item['gender'] = profile['gender']
                    item['isSmoking'] = profile['isSmoking']
                    item['profession'] = profile['profession']
                    item['income'] = profile['income']

                    # get subscription to process separately
                    subscription = item.pop('subscription', None)
                    for element in subscription:
                        element['userid'] =  item['id']
                        all_subscription.append(element)


                self.save_user(data)
                self.save_subscriptions(all_subscription)

                #Save processed JSON for future use
                # Utility.save(data, filepath)
            return True
        except:
            print('Unable to save the users ')
        return False

    def save_user(self, data):
        if data:
            for record in data:
                params = (
                    record['createdAt'],
                    record['updatedAt'],
                    record['city'],
                    record['country'],
                    record['email'],
                    record['birthDate'],
                    record['gender'],
                    record['isSmoking'],
                    record['profession'],
                    record['income'],
                    record['id']
                )

                #Check existing item
                sql_string = "select id from users where id = %s limit 1;" % (record['id'])
                result = SQL.read_single(sql_string)
                if result:
                    # UPDATE
                    sql_string = """UPDATE users SET createdat=%s, updatedat=%s, city=%s, country=%s, email=%s, birthdate =%s ,gender=%s, issmoking=%s, profession=%s, income=%s WHERE id=%s"""
                    SQL.execute(sql_string, params)
                else:
                    #INSERT
                    sql_string = """INSERT INTO users(createdat, updatedat, city, country, email, birthdate, gender, issmoking, profession, income,id)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    SQL.execute(sql_string, params)
        pass

    def save_subscriptions(self, data):
        table_name = 'subscriptions'
        if data:
            columns = Utility.generate_columns(data)
            for record in data:
                # delete all subscriptions for a user
                sql_string = "delete from subscriptions where userid = %s" % (record['userid'])
                SQL.execute(sql_string, None)

            # insert all subscriptions all together
            values_str = Utility.generate_all_values(data)
            sql_string = "INSERT INTO %s (%s)\nVALUES %s" % (
                table_name,
                ', '.join(columns),
                values_str
            )
            SQL.execute(sql_string, None)
        pass







