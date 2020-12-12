def run() -> str:
    name: str = str(input('Your name: '))
    greeting: str = say_hello(name)

    return greeting


def say_hello(name: str) -> str:
    return 'Hello ' + name