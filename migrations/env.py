import os

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

section = config.config_ini_section
config.set_section_option(
    section, "POSTGRES_USER", os.environ.get("POSTGRES_USER")
)
config.set_section_option(
    section, "POSTGRES_PASSWORD", os.environ.get("POSTGRES_PASSWORD")
)
config.set_section_option(
    section, "POSTGRES_HOSTNAME", os.environ.get("POSTGRES_HOSTNAME")
)
config.set_section_option(
    section, "APPLICATION_DB", os.environ.get("APPLICATION_DB")
)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None
from rentomatic.repository.postgres_objects import Base

target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.