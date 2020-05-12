from mylib.sound.echo import echo_test

def render_test():
    result = None

    try:
        print("render")
        echo_test()
    except Exception as ex:
        pass

    return result

if __name__ == "__main__" :
    render_test()