class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass
    PRIMARIO = "primario"
    SECUNDARIO = "secundario"
    UNIVERSITARIO = "universitario"
    JUBILADO = "jubilado"
    PRECIO_TICKET = 70
    DESACTIVADO = "desactivado"
    ACTIVADO = "activado"
    DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}
class Sube:
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario:
            descuento = DESCUENTOS[self.grupo_beneficiario]
            return PRECIO_TICKET * (1 - descuento / 100)
        return PRECIO_TICKET
    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("Usuario desactivado")
            precio_ticket = self.obtener_precio_ticket()
        if self.saldo < precio_ticket:
            raise NoHaySaldoException("No hay saldo suficiente")
            self.saldo -= precio_ticket
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in [ACTIVADO, DESACTIVADO]:
            raise EstadoNoExistenteException("Estado no existente")
            self.estado = nuevo_estado