from app import MyApp

application = MyApp

if __name__ == '__main__':
    import sys
    raise Exception(sys.executable)
    application.run()
