// db = db.getSiblingDB("mongo-database")
db.createUser(
    {
        user: "db_user",
        pwd: "12345",
        roles: [
            {
                role: "readWrite",
                db: "mydatabase"
            }
        ]
    }
)