import unittest

from template_fillers import ItalianTemplateFiller


class TestItalianTemplateFiller(unittest.TestCase):
    def test_gli(self):
        filler = ItalianTemplateFiller()

        template = filler.fill("Chi è il presidente diYYY XXX?", "Stati Uniti", article="Gli")
        self.assertEqual("Chi è il presidente degli Stati Uniti?", template)

    def test_l(self):
        filler = ItalianTemplateFiller()

        template = filler.fill("Chi è il presidente diYYY XXX?", "America", article="L")
        self.assertEqual("Chi è il presidente dell'America?", template)

    def test_la_in(self):
        filler = ItalianTemplateFiller()

        template = filler.fill("Chi è l'autore diYYY XXX?", "La bella e la bestia", article="La")
        self.assertEqual("Chi è l'autore della bella e la bestia?", template)

    def test_gender(self):
        filler = ItalianTemplateFiller()

        template = filler.fill("Quando è statGGG lanciatGGG YYY XXX?", "Falcon 9 v1.0", article="Il")
        self.assertEqual("Quando è stato lanciato il Falcon 9 v1.0?", template)

    def test_in_capital(self):
        filler = ItalianTemplateFiller()
        template = filler.fill("Quando è uscitGGG YYY XXX?", "La conversazione", article="La")
        self.assertEqual("Quando è uscita La conversazione?", template)
