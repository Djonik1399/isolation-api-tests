from pydantic import BaseModel, IPvAnyAddress, HttpUrl

class HTTPClientTestConfig(BaseModel):
    url: HttpUrl
    timeout: float = 120.0

class HTTPServerTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress
