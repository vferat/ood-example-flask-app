from app import MyApp

application = MyApp

if __name__ == '__main__':
    import sys
    print(sys.executable)
    application.run()
