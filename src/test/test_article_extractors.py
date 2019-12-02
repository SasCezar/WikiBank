import unittest

from article_extractors import ItalianArticleExtractor, GermanArticleExtractor, SpanishArticleExtractor


class TestItalianArticleExtractor(unittest.TestCase):
    def test_none(self):
        extractor = ItalianArticleExtractor()

        text = """Barack Hussein Obama II (/bəˈrɑːk hʊˈseɪn oʊˈbɑːmə/, pronuncia[?·info]; Honolulu, 4 agosto 1961) è 
        un politico statunitense, 44º presidente degli Stati Uniti d'America dal 2009 al 2017, prima persona di 
        origini afroamericane a ricoprire tale carica. 

Figlio di un'antropologa originaria del Kansas e di un economista kenyota, Obama si è laureato in scienze politiche 
alla Columbia University (1983) e in giurisprudenza alla Harvard Law School (1991), dove è stato la prima persona di 
colore a dirigere la rivista Harvard Law Review. Prima di portare a termine gli studi in legge, ha prestato la sua 
opera come «community organizer» a Chicago; successivamente ha lavorato come avvocato nel campo della difesa dei 
diritti civili, insegnando inoltre diritto costituzionale presso la Law School dell'Università di Chicago dal 1992 al 
2004. 

Barack Obama è stato membro del Senato dell'Illinois per tre mandati, dal 1997 al 2004. Dopo essersi candidato senza 
successo alla Camera dei rappresentanti nel 2000, quattro anni più tardi concorse per il Senato federale, imponendosi 
a sorpresa nelle primarie del Partito Democratico del marzo 2004 su di un folto gruppo di contendenti. L'inopinata 
vittoria alle primarie contribuì ad accrescere la sua notorietà; in seguito, il suo discorso introduttivo («keynote 
address») pronunciato in occasione della convention democratica di luglio lo rese una delle figure più eminenti del 
suo partito. Obama fu quindi eletto al Senato degli Stati Uniti nel novembre 2004, con il più ampio margine nella 
storia dell'Illinois, e prestò servizio come senatore junior dal gennaio 2005 al novembre 2008. 

Il 10 febbraio 2007 annunciò ufficialmente la propria candidatura alle successive consultazioni presidenziali.[1] 
Alle elezioni primarie del Partito Democratico, dopo un'aspra contesa, sconfisse Hillary Clinton, senatrice in carica 
per lo Stato di New York e già first lady, favorita della vigilia; il 3 giugno 2008 Obama raggiunse il quorum 
necessario per la candidatura, divenendo così la prima persona di origini afroamericane a correre per la Casa Bianca 
in rappresentanza di uno dei due maggiori partiti. 

L'esponente del Partito Democratico vinse le elezioni presidenziali del 4 novembre 2008 contro John McCain, 
senatore repubblicano dell'Arizona, insediandosi formalmente alla presidenza il 20 gennaio successivo. Il 6 novembre 
2012 fu riconfermato per un secondo mandato, imponendosi sul candidato repubblicano Mitt Romney. 

Il settimanale statunitense TIME lo ha prescelto quale «persona dell'anno» nel 2008[2] e nel 2012;[3] nel 2009 è 
stato insignito del Premio Nobel per la pace «per i suoi sforzi straordinari volti a rafforzare la diplomazia 
internazionale e la cooperazione tra i popoli».[4] """

        article = extractor.extract(text, "Barack Obama")

        self.assertEqual("", article)

    def test_yes(self):
        extractor = ItalianArticleExtractor()

        text = """I Girasoli sono una serie di dipinti ad olio su tela realizzati tra il 1888 e il 1889 dal pittore 
        Vincent van Gogh. Tra i soggetti preferiti dal pittore, sono oggi tra le sue opere più riconoscibili e note 
        presso il grande pubblico. """
        article = extractor.extract(text, "Girasoli")

        self.assertEqual("I", article)

    def test_i(self):
        extractor = ItalianArticleExtractor()
        text = """I Foxboro Hot Tubs sono un gruppo garage rock statunitense."""
        entity = "Foxboro Hot Tubs"

        article = extractor.extract(text, entity)
        self.assertEqual("I", article)

    def test_in(self):
        extractor = ItalianArticleExtractor()

        text = """La bella e la bestia (Beauty and the Beast) è un film del 2017 diretto da Bill Condon.

Scritto da Evan Spiliotopoulos e Stephen Chbosky, il film è un remake in live action dell'omonimo film d'animazione 
del 1991, tratto dalla fiaba di Jeanne-Marie Leprince de Beaumont. Il film è interpretato da un cast corale che 
comprende Emma Watson, Dan Stevens, Luke Evans, Kevin Kline, Josh Gad, Ewan McGregor, Stanley Tucci, Ian McKellen ed 
Emma Thompson. 

È il primo film Disney in cui compare un personaggio omosessuale: si tratta di Le Tont, interpretato da Josh Gad.[1]"""
        article = extractor.extract(text, "La bella e la bestia")

        self.assertEqual("La", article)

    def test_bug(self):
        extractor = ItalianArticleExtractor()
        text = """La Online Encyclopedia of Mass Violence (OEMV) è un progetto enciclopedico istituito su iniziativa 
        dello storico e politologo francese Jacques Sémelin, direttore di ricerca presso il Centre National de la 
        Recherche Scientifique, coadiuvato da un'équipe di docenti universitari provenienti da vari paesi. È stata 
        creata con lo scopo di costituire una fonte affidabile di dati riguardo a massacri, genocidi e crimini contro 
        non combattenti perpetrati durante il XX secolo o in precedenza. """
        article = extractor.extract(text, "Online Encyclopedia of Mass Violence")

        self.assertEqual("La", article)

    def test_neg(self):
        extractor = ItalianArticleExtractor()
        text = """Four Seasons of Love è il quarto album della cantante statunitense Donna Summer, pubblicato l'11 
        ottobre 1976 dalle etichette Casablanca.Si tratta di un concept album ispirato alle quattro stagioni 
        dell'anno.Spring Affair - 8:29 - (Pete Bellotte - Giorgio Moroder - Donna Summer)Summer Fever - 8:06 - (Pete 
        Bellotte - Giorgio Moroder - Donna Summer)Autumn Changes - 5:28 - (Pete Bellotte - Giorgio Moroder - Donna 
        Summer)Winter Melody - 6:33 - (Pete Bellotte - Giorgio Moroder - Donna Summer)Spring Reprise - 3:51 - (Pete 
        Bellotte - Giorgio Moroder - Donna Summer) """

        article = extractor.extract(text, "Four Seasons of Love")

        self.assertEqual("", article)

    def test_neg_inside(self):
        extractor = ItalianArticleExtractor()
        text = """Leksand è una cittadina della Svezia centrale, capoluogo del comune omonimo, nella contea di 
        Dalarna; nel 2010 aveva una popolazione di 5.934 abitanti.Qui è nato il musicista The Tallest Man on Earth. """

        article = extractor.extract(text, "Leksand")

        self.assertEqual("", article)

    def test_apostrofo(self):
        extractor = ItalianArticleExtractor()
        text = """L'Astronomia è la scienza che si occupa dell'osservazione e della spiegazione degli eventi celesti. 
        Studia le origini e l'evoluzione, le proprietà fisiche, chimiche e temporali degli oggetti che formano 
        l'universo e che possono essere osservati sulla sfera celeste. 

È una delle scienze più antiche e molte civiltà arcaiche in tutto il mondo hanno studiato in modo più o meno 
sistematico il cielo e gli eventi astronomici: egizi e greci nell'area mediterranea, babilonesi, indiani e cinesi 
nell'oriente, fino ai maya e agli incas nelle Americhe. Questi antichi studi astronomici erano orientati verso lo 
studio delle posizioni degli astri (astrometria), la periodicità degli eventi e la cosmologia e quindi, 
in particolare per questo ultimo aspetto, l'astronomia antica è quasi sempre fortemente collegata con aspetti 
religiosi. Oggi, invece, la ricerca astronomica moderna è praticamente sinonimo di astrofisica. 

L'astronomia non va confusa con l'astrologia, una pseudoscienza che sostiene che i moti apparenti del Sole e dei 
pianeti nello zodiaco influenzino in qualche modo gli eventi umani, personali e collettivi. Anche se le due 
discipline hanno un'origine comune, esse sono totalmente differenti: gli astronomi hanno abbracciato il metodo 
scientifico sin dai tempi di Galileo, a differenza degli astrologi. 

L'astronomia è una delle poche scienze in cui il lavoro di ricerca del dilettante e dell'amatore (l'astrofilo) può 
giocare un ruolo rilevante, fornendo dati sulle stelle variabili o scoprendo comete, novae, supernovae, asteroidi o 
altri oggetti. """

        article = extractor.extract(text, "Astronomia")
        self.assertEqual("L", article)


class TestGermanArticleExtractor(unittest.TestCase):
    def test_article(self):
        text = "Die Hunde (Canidae) sind eine Familie innerhalb der Überfamilie der Hundeartigen (Canoidea). Zu den Hunden gehören beispielsweise die Füchse, verschiedene als „Schakal“ bezeichnete Arten, Kojoten und Wölfe, deren domestizierte Formen, die Haushunde, als Namensgeber für die Gruppe dienten."
        entity = "Hunde"
        extractor = GermanArticleExtractor()
        article = extractor.extract(text, entity)
        self.assertEqual(article.lower(), 'die')


class TestSpanishArticleExtractor(unittest.TestCase):
    def test_article(self):
        text = """Los diplúridos (Dipluridae) son una familia de arañas del suborden Mygalomorphae, única representante de la superfamilia de los dipluroideos (Dipluroidea).​ En inglés se conocen como funnel-web tarantulas, que puede traducirse como  araña tela de embudo.  Este grupo de arañas tienen dos pares de filotráqueas o pulmones laminares, y quelíceros (colmillos) que al moverse de arriba abajo les sirven para apuñalar a sus presas. Antes se incluía en esta familia a Atrax robustus, aunque ahora se clasifica en la familia Hexathelidae.Los miembros de esta familia suelen elaborar sus telarañas en forma de túneles o embudos. Algunos construyen madrigueras forradas de seda en vez de telarañas propiamente dichas (Diplura, Trechona, algunas especies de Linothele). Generalmente construyen sus refugios en grietas del suelo, en la corteza de los árboles, bajo los troncos o en camas de hojas.​Los diplúridos se encuentran en casi cualquier ecosistema tropical del planeta. La mayoría en América del Sur y Central. Muchos en la región Australiana. El género Indothele se  encuentra en India y Sri Lanka. Ischnothele es una género neotropical, pero una de sus especies reside en la India. Varios géneros son de origen Africano, con el  Thelechoris también presente en Madagascar. El género más común en Estados Unidos es Euagrus, que construye su red bajo las piedras de los cañones húmedos. Abunda en áreas como las  Montañas Chiricahua de Arizona.Leptothele y Phyxioschema suthepium son endémicos de Tailandia, y las especies de Phyxioschema se encuentran en Asia Central. Masteria está ampliamente distribuida, con especies originarias de lugares como América Central, Fiyi, las Filipinas, Queensland y Nueva Guinea.​No existen pruebas acerca de la toxicidad del veneno de los diplúridos, aunque lo sensato es evitar el contacto directo con los miembros de mayor tamaño (Diplura sp., Harmonicon sp., Linothele sp., y Trechona sp.).[cita requerida]El muy  venenoso  género Atrax se solía incluir en esta familia, pero actualmente pertenece a Hexathelidae.Raven, R. J.​ y Coyle, F. A.​ reconocen cuatro subfamilias:Subfamilia Diplurinae Simon, 1889Clostes Menge, 1869 † — fósil, Eoceno ámbar BálticoCretadiplura Selden, 2005 † — fósil, Cretácico InferiorDinodiplura Selden, 2005 † — fósil, Cretácico InferiorDiplura C. L. Koch, 1850 — Sudamérica, CubaHarmonicon F. O. P-Cambridge, 1896 — [Guiana Francesa]], BrasilLinothele Karsch, 1879 — SudaméricaTrechona C. L. Koch, 1850 — SudaméricaSubfamilia  Euagrinae Raven, 1979Allothele Tucker, 1920 — ÁfricaAustralothele Raven, 1984 — AustraliaCaledothele Raven, 1991 — AustraliaCarrai Raven, 1984 — Nueva Gales del Sur (Australia)Cethegus Thorell, 1881 — AustraliaEuagrus Ausserer, 1875 — del sur de Estados Unidos a Costa Rica, Sudáfrica, TaiwanMicrohexura Crosby & Bishop, 1925 — Estados UnidosNamirea Raven, 1984 — AustraliaPhyxioschema Simon, 1889 — Asia CentralStenygrocercus Simon, 1892 — Nueva CaledoniaSubfamilia  Ischnothelinae F. O. Pickard-Cambridge, 1897Andethele Coyle, 1995 — PerúIndothele Coyle, 1995 — IndiaIschnothele Ausserer, 1875 — de México a Argentina, Caribe, IndiaLathrothele Benoit, 1965 — ÁfricaThelechoris Karsch, 1881 — África, MadagascarSubfamilia  Masteriinae Simon, 1889Chilehexops Coyle, 1986 — Chile, ArgentinaMasteria L. Koch, 1873 — Caribe, América Central y el sur, Oceanía, AustraliaStriamea Raven, 1981 — Colombiaincertae sedisLeptothele Raven & Schwendinger, 1995 — TailandiaTroglodiplura Main, 1969 — Australia"""
        entity = "diplúridos"
        extractor = SpanishArticleExtractor()
        article = extractor.extract(text, entity)
        self.assertEqual(article.lower(), 'los')

    def test_article_2(self):
        text = """La Universidad de las Hamburguesas es el nombre que recibe el centro de formación de McDonald's en Oak Brook, Illinois. Tiene un tamaño de 12.000 metros cuadrados. Fue fundada el 24 de febrero de 1961 por su director general Fred Turner y por Ray Kroc, el mismo año que compró la cadena a los hermanos McDonald.​Hoy en día cuenta con 19 instructores que enseñan en 28 idiomas diferentes. Tiene 13 aulas, auditorio de 300 butacas, 12 aulas de interacción educativa y 3 laboratorios. Los estudiantes reciben aproximadamente 32 horas de entrenamiento en su primer mes y estudian ahí más de 7500 estudiantes cada año. Desde su creación más de 80.000 mánagers y dueños de restaurantes se han graduado.​A día de hoy cuenta con siete «universidades» en todo el mundo, donde se ha invertido mucho dinero. A pesar de que se bromee diciendo «el McDonald's» cuando se pregunta sobre las salidas de un título con poco futuro laboral, en Shanghái, la tasa de aceptación en esta universidad fue de 1 de cada 100 aspirantes (1%). Eso hace a la Universidad de las Hamburguesas siete veces más exclusiva que la Universidad de Harvard.​La filosofía de Ray Kroc: «si estamos yendo a alguna parte, debemos tener talento. Dedicaré mi dinero al talento.»,  a pesar de su muerte en 1984, sigue viva en su cadena de universidades, donde gracias a entre otras cosas a sus tutoriales, día tras día enseñan a nuevos talentos."""
        entity = "Universidad de las Hamburguesas"
        extractor = SpanishArticleExtractor()
        article = extractor.extract(text, entity)
        self.assertEqual(article.lower(), 'la')
