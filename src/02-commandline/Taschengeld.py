'''
Created on 23.11.2011

@author: Werner
'''
class Bankkonto:
   """Einfache Bankkonto-Klasse"""

   def __init__(self,startbetrag):
      """Konstruktor: erzeugt Bankkonto"""
      self.kontostand = startbetrag

   def einzahlung(self, betrag):
      self.kontostand = self.kontostand + betrag

   def auszahlung(self, betrag):
      self.kontostand = self.kontostand - betrag

   def anzeigen(self):
      print (self.kontostand)


class Taschengeld(Bankkonto):
   """Taschengeld-Konto: man darf nicht ueberziehen . . ."""

   def __init__(self,startbetrag):
      """Konstruktor: erzeugt Taschengeldkonto"""
      # rufe Konstruktor aus Bankkonto-Klasse auf
      Bankkonto.__init__(self,startbetrag)

   def auszahlung(self, betrag):
      if ((self.kontostand - betrag) < 0.0):
         print ("ERROR!! DU darfst nicht ueberziehen! ERROR!!")
      else:
         self.kontostand = self.kontostand - betrag


# ausprobieren
konto1 = Taschengeld(100)
konto1.anzeigen()
konto1.einzahlung(200)
konto1.anzeigen()
konto1.auszahlung(525)
konto1.anzeigen()
konto1.auszahlung(125)
konto1.anzeigen()