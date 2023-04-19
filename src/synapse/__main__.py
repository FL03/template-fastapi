if __name__ == "__main__":
    from synapse.interface import run

    import multiprocessing

    app = multiprocessing.Process(target=run)
    app.start()
