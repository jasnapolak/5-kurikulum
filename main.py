from sqla_wrapper import SQLAlchemy

db = SQLAlchemy("sqlite:///localhost.sqlite")


print("it works")


class Message(db.Model):                            # We don't have to specifically say that the ID needs
    __tablename__ = "messages"                      # to be auto-incremented and unique
    id = db.Column(db.Integer, primary_key=True)    # SQLAlchemy do this for us automatically
    text = db.Column(db.String)
    username = db.Column(db.String)

db.create_all()

message = Message(text="Hello world! :)")
db.add(message)
db.commit()
# Because the .add() method will just add the object into the SQL transaction, but it will not commit it yet.
# You could add many objects in the same SQL transactions.
# With .commit() we complete the transaction and our object is now in the database.

messages = db.query(Message).all()

for row in messages:
    print(row.text)

# You can also filter the query per some field, like id:
messages = db.query(Message).filter(Message.id == 2).all()

# Or only get the first item from the database:
message_first = db.query(Message).first()
print(message_first.text)


