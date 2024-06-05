from model.fake import adjetivos, substantivos, medida, marca, fornecedores, categorias
import random


class GerateProduct:

    def create_nome_product(self) -> str:
        adj = random.choice(adjetivos)
        subst = random.choice(substantivos)
        num = random.randint(100, 999)
        return f"{adj} {subst} {num}"


    def create_product_entry_json(self) -> dict:
        return { "product_id": f"Product {random.randint(0, 1_000_000)}",
                    "name": self.create_nome_product(),
                    "categoria": random.choice(categorias),
                    "marca": random.choice(marca),
                    "filial": random.randint(1, 5),
                    "fornecedor": random.choice(fornecedores),
                    "preço": float(str(random.randint(0, 99))+"."+str(random.randint(0,99))),
                    "unit": random.choice(medida),}
    

