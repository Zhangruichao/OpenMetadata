# generated by datamodel-codegen:
#   filename:  schema/type/jdbcConnection.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class DriverClass(BaseModel):
    __root__: str = Field(..., description='Type used for JDBC driver class.')


class ConnectionUrl(BaseModel):
    __root__: str = Field(
        ...,
        description='Type used for JDBC connection URL of format `url_scheme://<username>:<password>@<host>:<port>/<db_name>`.',
    )


class JdbcInfo(BaseModel):
    driverClass: DriverClass
    connectionUrl: ConnectionUrl


class JdbcConnection(BaseModel):
    driverClass: DriverClass = Field(..., description='JDBC driver class.')
    connectionUrl: ConnectionUrl = Field(..., description='JDBC connection URL.')
    userName: str = Field(..., description='Login user name.')
    password: str = Field(..., description='Login password.')