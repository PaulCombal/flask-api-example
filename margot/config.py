class TestConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:my-secret-pw@127.0.0.1:3306/testdb'
    testing = True
    debug = True