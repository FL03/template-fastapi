FROM jo3mccain/pypoetry:latest

ENV PORT=8080

ADD . /project
WORKDIR /project

COPY . .
RUN poetry install

EXPOSE ${PORT}/tcp

CMD ["poetry", "run", "python", "-m", "app"]
