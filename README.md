# Energy Service

This repository is used for the talk "Django Ninja for API Development: Lessons from Energy Market" together with 
[Anastasiia Potekhina](https://github.com/merry-mouse) at PyCon Sweden 2024

In this talk, we will dive into how Django Ninja has transformed the way we develop APIs for the energy industry, focusing on practical insights and real-world examples. Working with Swedish energy companies, we face the challenge of building fast, scalable, and reliable solutions for complex systems. Django Ninja has been a great framework for building robust APIs due to its simplicity, flexibility, and performance.

This service uses:

- Python 3.11.9
- [Django-ninja](https://django-ninja.dev/)
- [Rye](https://rye.astral.sh/)
- [Pre-commit](https://pre-commit.com/)
- Makefile

## How to run

### Instal the dependencies

This service use Rye, if you use it:

```shell
rye sync
```

If you don't:

```shell
pip install -r requirements.lock
```

### Load and run
It will run the docker-compose:
```shell
make compose
```

You need to access the database and create the database. After it you can load the data:
```shell
make loaddata
```

You can check the talk slides [here](https://github.com/beatrizuezu/energy-service/blob/main/pycon_2024_slides.pdf)
