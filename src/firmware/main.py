import micropython


def main():
    micropython.alloc_emergency_exception_buf(100)
    # TODO: main code goes here


if __name__ == '__main__':
    main()
