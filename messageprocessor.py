from utility import Utility
from sql import SQL

class MessageProcessor:

    def process(self, url, filepath):
        try:
            data = Utility.request(url)
            if data:
                for item in data:
                    # Remove or transform PII
                    item.pop('message', None)

                self.save_messages(data)

                # Save processed JSON for future use
                # Utility.save(data, filepath)
            return True
        except:
            print('Unable to save the messages')
        return False

    def save_messages(self, data):
        table_name = 'messages'
        columns = Utility.generate_columns(data)

        if data:
            # insert all messages
            values_str = Utility.generate_all_values(data)
            sql_string = "INSERT INTO %s (%s)\nVALUES %s" % (
                table_name,
                ', '.join(columns),
                values_str
            )
            SQL.execute(sql_string, None)
        pass
