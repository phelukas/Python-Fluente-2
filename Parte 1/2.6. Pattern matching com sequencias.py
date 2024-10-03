# Definindo a exceção ComandoInvalido
class ComandoInvalido(Exception):
    """Exceção levantada quando um comando inválido é recebido."""

    def __init__(self, mensagem):
        super().__init__(f"Comando inválido: {mensagem}")


# Função que trata os diferentes tipos de comandos
def tratar_comando(self, mensagem):
    match mensagem:  # Correspondência de padrões com base no conteúdo de 'mensagem'
        case ["BIPADOR", frequencia, vezes]:  # Comando para o bipador
            self.bipar(vezes, frequencia)

        case ["PESCOÇO", angulo]:  # Comando para movimentar o pescoço
            self.rotacionar_pescoco(angulo)

        case [
            "LED",
            identificador,
            intensidade,
        ]:  # Comando para ajustar o brilho do LED
            self.leds[identificador].ajustar_brilho(identificador, intensidade)

        case [
            "LED",
            identificador,
            vermelho,
            verde,
            azul,
        ]:  # Comando para definir a cor RGB do LED
            self.leds[identificador].definir_cor(identificador, vermelho, verde, azul)

        case _:  # Se nenhum padrão corresponder, lança a exceção ComandoInvalido
            raise ComandoInvalido(mensagem)


metro_areas = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:  # (1)
            case [name, _, _, (lat, lon)] if lon <= 0:  # (2)
                print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")
