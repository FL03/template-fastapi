if __name__ == "__main__":
    from synapse.interface import run
    from synapse.telegram import bot

    import multiprocessing

    a = multiprocessing.Process(target=bot)
    b = multiprocessing.Process(target=run)
    a.start()
    b.start()
