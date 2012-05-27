#-*- encoding: utf-8 -*-


class QuePlaca:
    def __init__(self):
        pass

    def regexp_placa(self,placa):
        import re
        regexp = re.compile("\w{3}\-\d{4}")

        if regexp.match(str.upper(placa)):
            return True
        else:
            return False


    def quePlaca(self,placa):
        pass


    def ui(self):
        print "***********************"
        print "*                     *"
        print "*     quePlaca        *"
        print "*                     *"
        print "***********************"
        print
        print "Consulte Qualquer Placa"
        print "Ex: ABC-1234"

        placa = "abc-1234"
        while placa:
            print
            print "-> Deixe em Branco para Sair "
            placa = raw_input("-> ")

            if not self.quePlaca(placa):
                print "!! Placa Inválida !!"










