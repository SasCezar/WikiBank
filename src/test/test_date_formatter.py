import unittest

from date_formatter import DateFormatter, RomanLanguageDateFormatter, EnglishDateFormatter


class TestFormatterMethods(unittest.TestCase):
    def test_millennium(self):
        formatter = EnglishDateFormatter()
        precision = 6

        date = "+0000020000-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "21st millennium")

        date = "-00000002000-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "3rd millennium BC")

    def test_century(self):
        formatter = EnglishDateFormatter()
        precision = 7

        date = "+00000001900-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "20th century")

        date = "-00000001900-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "20th century BC")

    def test_year(self):
        formatter = EnglishDateFormatter()
        precision = 9

        date = "+00000001920-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "1920")
        date = "-00000001920-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "1920 BC")

    def test_month(self):
        formatter = EnglishDateFormatter()
        precision = 10

        date = "+00000001920-01-00T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "January 1920")

        date = "-000000020-01-00T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "January 20 BC")

    def test_day(self):
        formatter = EnglishDateFormatter()
        precision = 11

        date = "+00000001920-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "1 January 1920")

        date = "-000000020-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "1 January 20 BC")

    def test_month_french(self):
        formatter = DateFormatter(lang='fr', out_locale='fr-FR')
        precision = 10

        date = "+00000001920-01-02T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "janvier 1920")
        date = "-000000020-01-10T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "janvier 20 J.-C")

    def test_month_italian(self):
        formatter = RomanLanguageDateFormatter(lang='it', out_locale='it-IT')
        precision = 10

        date = "+00000001920-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "gennaio 1920")

        date = "-000000020-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "gennaio 20 a.C.")

    def test_day_french(self):
        formatter = RomanLanguageDateFormatter(lang='fr', out_locale='fr-FR')
        precision = 11

        date = "+00000001920-01-02T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "2 janvier 1920")

        date = "-000000020-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "1er janvier 20 J.-C")

    def test_day_italian(self):

        formatter = RomanLanguageDateFormatter(lang='it', out_locale='it-IT')
        precision = 11

        date = "+00000001920-01-02T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "2 gennaio 1920")

        date = "-000000020-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "1° gennaio 20 a.C.")

    def test_month_german(self):
        formatter = DateFormatter(lang='de', out_locale='de-DE')
        precision = 10

        date = "+00000001920-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "Januar 1920")

        date = "-000000020-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "Januar 20 v. Chr.")

    def test_millenium_german(self):
        formatter = DateFormatter(lang='de', out_locale='de-DE')
        precision = 6

        date = "+000002000-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "3. Jahrtausend")

        date = "-00000001000-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "2. Jahrtausend v. Chr.")

    def test_century_german(self):
        formatter = DateFormatter(lang='de', out_locale='de-DE')
        precision = 7

        date = "+00000200-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "3. Jahrhundert")

        date = "-0000000100-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "2. Jahrhundert v. Chr.")


class TestRomanFormatterMethods(unittest.TestCase):
    def test_millennium(self):
        formatter = RomanLanguageDateFormatter()
        precision = 6

        date = "+0000020000-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "XXI millennium")

        date = "-00000002000-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "III millennium BC")

    def test_day_spanish(self):
        formatter = DateFormatter(lang="es", out_locale='es-ES')
        precision = 11

        date = "+00000001920-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "1 de enero de 1920")

        date = "-000000020-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "1 de enero de 20 a. C.")

    def test_century(self):
        formatter = RomanLanguageDateFormatter()
        precision = 7

        date = "+00000001900-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "XX century")

        date = "-00000001900-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "XX century BC")

    def test_millenium_italian(self):
        formatter = RomanLanguageDateFormatter(lang="it", out_locale='it-IT')
        precision = 6

        date = "+0000020000-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "XXI millennio")

        date = "-00000002000-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "III millennio a.C.")

    def test_century_french(self):
        formatter = RomanLanguageDateFormatter(lang="fr", out_locale='fr-FR')
        precision = 7

        date = "+00000001900-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "XXe siècle")

        date = "-0000000800-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "IXe siècle J.-C")

    def test_century_spanish(self):
        formatter = RomanLanguageDateFormatter(lang="es", out_locale='es-ES')
        precision = 7

        date = "+00000001900-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "siglo XX")

        date = "-0000000801-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)
        self.assertEquals(formatted, "siglo IX a. C.")

class TestKannadaDateFormatter(unittest):
    def test_century(self):
        formatter = KannadaDateFormatter(lang="fr", out_locale='fr-FR')
        precision = 7

        date = "+00000001900-01-01T00:00:00Z"
        formatted = formatter.format(date, precision)

if __name__ == '__main__':
    unittest.main()
