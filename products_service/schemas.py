from pydantic import BaseModel

class SchemaProduct(BaseModel):
    title: str = "Продукт"
    price: float = 23.4
    
class SchemaGetProduct(SchemaProduct):
    id: int = 123

class SchemaProductGetArgs:
    def __init__(
        self,
        id: int
        ) -> None:
        self.id = id
    