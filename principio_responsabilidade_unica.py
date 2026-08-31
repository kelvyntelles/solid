pedidos = []


itens = [
    {
        "nome": "Bola de futebol",
        "preco": 99,
        "quantidade": 5
    },
    {
        "nome": "Chuteira",
        "preco": 349,
        "quantidade": 1
    },
    {
        "nome": "Meiao",
        "preco": 29,
        "quantidade": 3
    },
    {
        "nome": "Short",
        "preco": 59,
        "quantidade": 3
    },
    {
        "nome": "Camisa",
        "preco": 89,
        "quantidade": 5
    },
]


class Pedido:
    def __init__(self, cliente: str, itens: list):
        self.cliente = cliente
        self.itens = itens

    def calcular_total(self) -> float:
        total = 0

        for item in self.itens:
            total += item["preco"] * item["quantidade"]

        return total


class PedidoRepository:
    def salvar(self, pedido: Pedido):
        pedidos.append(pedido)


class EmailService:
    def enviar_confirmacao(self, pedido: Pedido):
        print(f"Destinatario: {pedido.cliente}")
        print(
            f"Email: Enviando confirmação para "
            f"{pedido.cliente}"
        )


class NotaFiscalService:
    def gerar(self, pedido: Pedido):
        total = pedido.calcular_total()

        print(
            f"Nota fiscal do: {pedido.cliente} "
            f"- Valor: {total}"
        )


class PedidoService:
    def __init__(
        self,
        repositorio: PedidoRepository,
        email_service: EmailService,
        nota_fiscal_service: NotaFiscalService
    ):
        self.repositorio = repositorio
        self.email_service = email_service
        self.nota_fiscal_service = nota_fiscal_service

    def processar(self, pedido: Pedido):
        self.repositorio.salvar(pedido)

        self.email_service.enviar_confirmacao(pedido)

        self.nota_fiscal_service.gerar(pedido)

        print("Pedido enviado com sucesso!")


pedido = Pedido("Kelvyn", itens)

repositorio = PedidoRepository()
email_service = EmailService()
nota_fiscal_service = NotaFiscalService()

pedido_service = PedidoService(
    repositorio,
    email_service,
    nota_fiscal_service
)

pedido_service.processar(pedido)