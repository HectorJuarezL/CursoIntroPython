def main():
    try:
        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#    except PermissionError as err:
#        print("got a problem trying to read the file:", err)
#    except (BlockingIOError, TimeoutError):
#        print("Filesystem under heavy load, can't complete reading configuration file")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")


if __name__ == '__main__':
    main()