import re
import unittest

from tokenizers import SpacyTokenizer, KannadaTokenizer


class TestSpacyTokenizer(unittest.TestCase):

    def test_tokenizer_en(self):
        tokenizer = SpacyTokenizer('en')
        text = """Oecomys is a genus of rodent within the tribe Oryzomyini of family Cricetidae. It contains about 17 species, which live in trees and are distributed across forested parts of South America, extending into Panama and Trinidad.\n\nCarleton"""
        tokens, break_levels, _ = tokenizer.tokenize(text)
        gt_tokens = ["Oecomys", "is", "a", "genus", "of", "rodent", "within", "the", "tribe", "Oryzomyini", "of",
                     "family", "Cricetidae", ".", "It", "contains", "about", "17", "species", ",", "which", "live",
                     "in", "trees", "and", "are", "distributed", "across", "forested", "parts", "of", "South",
                     "America", ",", "extending", "into", "Panama", "and", "Trinidad", ".", "Carleton"]
        self.assertListEqual(tokens, gt_tokens)
        gt_breaks = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     0, 1, 1, 1, 1, 1, 0, 4]
        self.assertListEqual(break_levels, gt_breaks)

    def test_tokenizer_it(self):
        text = """Finale Emilia (Al Finàl in dialetto finalese, Al Finèl in dialetto modenese) è un comune italiano di 15 573 abitanti della provincia di Modena, in Emilia-Romagna, di cui costituisce il più orientale comune della provincia, e fa parte dell'Unione Comuni Modenesi Area Nord. Dista dal capoluogo circa 42 chilometri a nord-est.

Finale gode di un tipico clima temperato continentale della pianura padana e delle medie latitudini. Come nel resto della pianura circostante, gli inverni sono moderatamente rigidi, poco piovosi e con giornate di nebbia; le estati sono calde ed afose nei mesi di luglio e agosto, con temperature che possono salire oltre i 35º e con precipitazioni a carattere temporalesco; le primavere e gli autunni sono generalmente piovosi.

Classificazione climatica: zona E
Classificazione sismica: zona 3.

Finale deriva da locus finalis, che significa luogo di confine. Posto attualmente al confine tra le province di Modena e di Ferrara, il nome è in relazione con la sua posizione che anche anticamente era posta al confine del Ducato di Modena e lo Stato pontificio. Fino al 1863 si chiamava Finale di Modena, poi con la sua inclusione nel Regno d'Italia fu definitivamente chiamato Finale Emilia.

Il territorio finalese costituisce da sempre una zona di confine con una storia che si perde nella notte dei tempi: i primi insediamenti urbani di cui si hanno testimonianze risalgono all'Età del Bronzo. L'aspetto strategico che riveste il territorio finalese era già ben noto ai tempi dei Romani che vi si insediarono fra il II e il IV secolo fondando forse quella Forum Alieni menzionata da Tacito nelle sue Historiae.
Il primo documento ufficiale in cui si fa esplicita menzione a Finale risale al 1009, in particolare il documento cita il castello finalese menzionato come oggetto di scambio fra il vescovo di Modena Varino e l'abate di Nonantola Rodolfo.
Risale, comunque, al 1213 la nascita ufficiale dell'abitato finalese cioè quando gli abitanti di Ponteduce, durante la guerra fra Salinguerra Torelli e il marchese Aldobrandino d'Este, si unirono ai militari di stanza al Castrum finalis, determinando in seguito, l'ampliamento dell'abitato e la fondazione del Comune di Finale, che trovò espressione concreta nell'innalzamento della Torre del Popolo di Modena o Torre dell'Orologio.
Dalla fine del XIII secolo le sorti di Finale si legano indissolubilmente a quelle di Modena che in questo periodo passa sotto il dominio degli Estensi.
Alla fine del XV secolo cominciò a svilupparsi il nucleo civile ed economico del paese includendo piccole fabbriche artigianali dedite principalmente alla lavorazione della lana, del cuoio e del vetro.
Nella prima metà del XVI secolo il duca Ercole II d'Este, su richiesta degli stessi finalesi, fece abbattere le mura cittadine in modo da dare maggiore spazio alle locali attività industriali.
Nel 1598 il duca Cesare d'Este, costretto a cedere Ferrara al Papa, si rifugiò a Finale, che, grazie all'ospitalità dimostrata ricevette il titolo di Finale Fedelissimo.
Il XVIII secolo fu funestato da guerre e distruzione e nella zona si avvicendarono le truppe di diverse fazioni fino a quelle francesi di Napoleone.
Il periodo fu particolarmente duro per Finale e per le zone circostanti, ciononostante la vitalità economica e commerciale del paese non venne mai meno, particolarmente intensa fu l'attività bancaria gestita dalla comunità ebraica locale: una delle più radicate ed importanti della zona del modenese.
Ad ulteriore riconoscimento dell'importanza economica e culturale raggiunta, il 30 gennaio 1779 il duca Francesco III concesse a Finale il titolo di Città.
Nel 1805 Finale fu inclusa nel Regno d'Italia costituito da Napoleone. Successivamente il Congresso di Vienna restituì Finale al dominio degli Estensi che lo mantennero fino all'incorporazione di Finale nel Regno d'Italia.
Nel 1886 vi avviene la fondazione della prima cooperativa in provincia di Modena e fra le prime in Italia denominata "Associazione degli operai braccianti e scariolanti di Finale Emilia". Finale Emilia era storicamente considerata un'importante "città d'acqua" per la navigabilità del fiume Panaro, chiamata dagli Este la piccola Venezia, e quando alla fine del XIX secolo il fiume Panaro cambiò il suo corso, l'agricoltura divenne il cardine dell'economia della cittadina e dei suoi dintorni, fino alla seconda metà del XX secolo, quando con la costruzione del polo industriale sorsero numerose industrie.

Sul finire della Seconda guerra mondiale, nella notte tra il 22 e il 23 aprile 1945, la V Armata statunitense e la VIII Armata inglese, dopo violenti scontri conclusero l'accerchiamento delle truppe tedesche poste a difesa di Bologna. Il congiungimento delle due armate sul Fiume Panaro nei pressi di Finale verso Bondeno, comportò la perdita di oltre 40 000 uomini dell'Asse e il collasso della Wehrmacht in Italia. Questa azione è stata considerata, l'ultima operazione bellica di rilievo nella campagna d'Italia da parte del generale Harold Alexander (comandante in capo delle truppe alleate nella penisola). Nel corso dei combattimenti i Nazisti minarono un gran numero di abitazioni di Finale Emilia, distruggendo quanto non era stato ancora colpito dai precedenti bombardamenti alleati. Molti finalesi tentarono disperatamente di impedire questa azione, i combattimenti strada per strada furono particolarmente feroci. La superiorità numerica dei Nazisti ebbe ragione del valore dei locali, ma gli Alleati guadagnarono forse quel tempo prezioso per accerchiare e sconfiggere il nemico.
Nel 2012 il patrimonio artistico di Finale Emilia è stato gravemente danneggiato dal terremoto che ha colpito tutta la Bassa modenese. Le scosse hanno causato il crollo della Torre dei Modenesi in piazza Baccarini, di buona parte della Rocca Estense, del Palazzo Veneziani e della parte superiore del Duomo. La maggioranza dei danni si è avuta con la scossa del 20 maggio, mentre quelle successive hanno causato danni minori; Finale Emilia fu proprio epicentro della scossa principale del 20 maggio, di magnitudo 5.9.

La città godeva di una propria nobiltà civica, con tanto di libro d'oro della nobiltà, composta da quelle famiglie che per vari motivi avevano contribuito alla storia della città. La Consulta araldica del Regno d'Italia riconobbe la nobiltà civica di Finale Emilia e di contesto entrarono a far parte dell'Elenco Ufficiale della Nobiltà Italiana le seguenti famiglie col titolo di Nobile di Finale:

Di particolare rilievo è il Castello delle Rocche (detto anche "Rocca Estense") il cui corpo quadrilatero è munito di torri, sulle quali spiccano le aquile estensi e del mastio. Come altri monumenti è rimasto gravemente danneggiata dal terremoto del 20 maggio 2012.

La Torre dei Modenesi, o come la chiamavano gli abitanti Torre dell'Orologio, fu costruita nel 1213 (e già simbolo della città), avrebbe compiuto 800 anni nel 2013. Diventò il simbolo del terremoto che dopo varie scosse la fece crollare quasi completamente il 20 maggio 2012.

Altri quattro grandi edifici caratterizzano Finale: il Palazzo Comunale, con l'orologio e la statua di San Zenone, la chiesa di San Bartolomeo, il Teatro Sociale e il cimitero ebraico, con la tomba di Donato Donati del XVII secolo.

Abitanti censiti

Gli stranieri residenti nel comune sono 2.085, ovvero il 13,3% della popolazione. Di seguito sono riportati i gruppi più consistenti:

Marocco, 960
Romania, 246
Cina, 167
Nigeria, 93
Moldavia, 92
Albania, 90
Ucraina, 86
Tunisia, 53
Polonia, 53
Pakistan, 40

Oltre alla lingua italiana, a Finale Emilia è utilizzato il locale dialetto finalese, appartenente al gruppo ferrarese della lingua emiliano-romagnola.

Finale Emilia rispecchia le tradizioni emiliane in molti piatti preparati nella cittadina; tipicamente di Finale sono l'anicione, un distillato a base di anice, e soprattutto la sfogliata, talvolta conosciuta come "torta degli ebrei" o "tibuia". Sulla sua preparazione, a base di farina, strutto e formaggio grana ancor oggi si mantiene un certo riserbo, come vuole la tradizione. Nei secoli scorsi infatti, questa ricetta era conosciuta solo dagli ebrei residenti in zona, e da loro era segretamente custodita; tuttavia, nel 1861, un ebreo divenuto cattolico di nome Mandolino Rimini, decise di rivelarla ai cristiani per vendicarsi del disprezzo che gli ebrei avevano maturato nei suoi confronti, dopo la sua conversione.

Finale Emilia è gemellata con:

 Grézieu-la-Varenne
 Villa Sant'Angelo
 Formigine"""
        tokenizer = SpacyTokenizer('it')
        tokens, break_levels, _ = tokenizer.tokenize(text)
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        self.assertEqual(len(tokens), len(break_levels))
        self.assertEqual(text.replace("\n ", "\n"), rebuilt)

    def test_tokenizer_it_2(self):
        tokenizer = SpacyTokenizer('it')
        table = str.maketrans({"\t": "\\t", "\r": "\\r", "\f": "\\f", "\b": "\\b"})
        text = """L'Universo è comunemente definito come il complesso di tutto lo spazio e di ciò che contiene, il che comprende tutta la materia e l'energia, i pianeti, le stelle, le galassie e il contenuto dello spazio intergalattico.L'osservazione scientifica dell'Universo, la cui parte osservabile ha un diametro di circa 92 miliardi di anni luce, suggerisce che l'Universo sia stato governato dalle stesse leggi e costanti fisiche per la maggior parte della sua storia e in tutta la sua estensione osservabile, e permette delle inferenze sulle sue fasi iniziali. La teoria del Big Bang è il più accreditato modello cosmologico che descrive la nascita dell'Universo; si calcola che il Big Bang sia avvenuto circa 13,798 ± 0,037 miliardi di anni fa.La massima distanza che è teoricamente possibile osservare è contenuta nell'universo osservabile. Osservazioni di supernovae hanno dimostrato che l'Universo, almeno nella regione contenente l'universo osservabile, sembra espandersi a un ritmo crescente, e una serie di modelli sono sorti per prevederne il destino finale. I fisici rimangono incerti su che cosa abbia preceduto il Big Bang; molti si rifiutano di speculare, dubitando che si potranno mai trovare informazioni relative allo stato originario. Alcuni propongono modelli di universo ciclico, altri descrivono uno stato iniziale senza confini, da cui è emerso e si è espanso lo spaziotempo al momento del Big Bang.Esistono anche speculazioni teoriche sul multiverso, nelle quali cosmologi e fisici ipotizzano che il nostro universo sia solo uno tra i molti che possono esistere.

Il termine universo deriva dal latino universus (tutto, intero) parola composta da unus (uno) e versus (volto, avvolto. Part. pass. di vertere). La parola latina fu usata spesso da Cicerone e tardi autori latini con il senso posseduto oggi in italiano.La contrazione poetica Unvorsum, da cui deriva universus, fu usata per la prima volta da Tito Lucrezio Caro nel Libro IV (capoverso 262) del suo De rerum natura ("Sulla natura delle cose"). Secondo una particolare interpretazione, essa significherebbe "tutto ciò che ruota come uno" o "tutto ciò che viene ruotato da uno". In questo senso, essa può essere considerata come una traduzione da un'antica parola greca per l'universo, περιφορά (periforá, "circumambulazione", parola originariamente usata per descrivere il percorso del cibo, che veniva servito lungo la cerchia dei commensali). περιφορά si riferiva a uno dei primi modelli greci dell'universo, quello delle sfere celesti, che secondo Aristotele erano messe in moto, per l'appunto, da un unico "essere", il cosiddetto "Primo Mobile" o "Primo Motore".
Un altro termine per "universo" nell'Antica Grecia era τὸ πᾶν (tò pán, si veda Il Tutto, Pan). Termini correlati erano materia (τὸ ὅλον, tò hólon) e luogo (τὸ κενόν, tò kenón).Altri sinonimi per universo tra i filosofi dell'antica Grecia includevano κόσμος (cosmo) e φύσις (significante Natura, e da cui deriva la parola "fisica"). Si ritrovano gli stessi sinonimi tra gli autori latini (totum, mundus, natura) e infine nel linguaggio moderno, ad esempio nelle parole tedesche Das All, Weltall, e Natur, oltre che, naturalmente, in italiano.

La più ampia definizione di universo la si ritrova nel De divisione naturae del filosofo e teologo medioevale Giovanni Scoto Eriugena, che lo definì semplicemente come il tutto: tutto ciò che è creato e tutto ciò che non è creato.

Più comunemente, l'universo è definito come tutto ciò che esiste fisicamente. Secondo le nostre attuali conoscenze, esso consiste allora di tre elementi fondamentali: spaziotempo, energia (che comprende quantità di moto e materia) e leggi fisiche.

È possibile concepire spaziotempi disconnessi, esistenti ma incapaci di interagire l'uno con l'altro. Una metafora facilmente visualizzabile di ciò è un gruppo di bolle di sapone separate. Gli osservatori vivono all'interno di una "bolla" e non possono interagire con quelli in altre bolle di sapone, nemmeno in linea di principio. Secondo una terminologia comune, ciascuna "bolla" di spaziotempo è un universo, mentre il nostro particolare spaziotempo è indicato come "l'Universo", così come indichiamo la nostra luna come la "Luna". L'insieme degli spaziotempi è chiamato multiverso. In linea di principio, gli altri universi disconnessi dal nostro possono avere differenti dimensionalità e topologie spazio-temporali, forme differenti di materia ed energia, diverse leggi e costanti fisiche, ma queste sono speculazioni.

Secondo una definizione ancora più restrittiva, l'universo è tutto ciò che nello spazio-tempo connesso può interagire con noi e viceversa.
Secondo la teoria della Relatività generale, alcune regioni dello spazio non interagiranno mai con noi in tutta la durata dell'universo: l'espansione dello spazio causa l'allontanamento di queste regioni da noi a una velocità maggiore di quella della luce. Quelle regioni remote sono considerate esistenti e parte della realtà tanto quanto noi, ma non saremo mai in grado di interagire con loro. La regione spaziale nella quale possiamo influire e dalla quale essere influenzati è denotata come universo osservabile. Strettamente parlando, l'universo osservabile dipende dalla posizione dell'osservatore. Viaggiando, un osservatore può entrare in contatto con una regione di spazio-tempo più grande, e dunque il suo universo osservabile sarà più grande. Tuttavia nemmeno il più rapido dei viaggiatori potrebbe interagire con tutto lo spazio. In genere, per universo osservabile si intende l'universo osservabile dalla Via Lattea.

Nel corso della storia registrata, diverse cosmologie e cosmogonie sono state proposte per spiegare le osservazioni sull'universo. I primi modelli quantitativi, geocentrici, sono stati sviluppati dai filosofi dell'Antica Grecia. Nel corso dei secoli, osservazioni più precise e teorie migliori sulla gravità hanno portato prima al modello eliocentrico di Niccolò Copernico, poi al modello del sistema solare di Isaac Newton. Ulteriori miglioramenti nel campo dell'astronomia hanno portato a comprendere come il Sistema Solare sia incorporato in una galassia composta da miliardi di stelle, la Via Lattea, e che esistono n miliardi di galassie più o meno simili. Studi sulla loro distribuzione e sulla loro riga spettrale hanno portato alla cosmologia moderna. Le scoperte dello spostamento verso il rosso e della radiazione cosmica di fondo hanno rivelato come l'universo si stia espandendo e che forse ha avuto un inizio.

Secondo il modello scientifico prevalente dell'universo, il modello del Big Bang, l'universo si è espanso da una fase estremamente calda e densa chiamata epoca di Planck, in cui era concentrata tutta la materia e l'energia dell'universo osservabile. Dall'epoca di Planck, l'universo si è espanso fino alla sua forma attuale, forse con un breve periodo (meno di 10-32 secondi) di inflazione cosmica.
Diverse misurazioni sperimentali indipendenti supportano questa teoria di espansione metrica dello spazio e, più in generale, la teoria del Big Bang. Osservazioni recenti indicano come questa espansione stia accelerando a causa dell'energia oscura, e come la maggior parte della materia nell'universo potrebbe essere in una forma non rilevabile dagli strumenti attuali, e quindi non conteggiata nei modelli dell'universo, ostacolando le nostre previsioni sul destino ultimo dell'universo. Questa forma di materia è stata denominata materia oscura.Il 21 marzo 2013 la guida dei team europei di ricerca riguardanti la sonda Planck ha pubblicato la più recente mappa della radiazione cosmica di fondo del cielo. La mappa suggerisce che l'universo sia un po' più vecchio di quanto si credesse. Secondo la mappa, sottili fluttuazioni di temperatura sono state impresse sul cielo profondo quando il cosmo aveva circa 370.000 anni. Tali fluttuazioni riflettono increspature sorte già nei primi 10−30 secondi. A quanto pare, queste increspature hanno dato luogo alla presente vasta struttura di superammassi di galassie e materia oscura. Secondo il team di Planck, l'universo ha circa 13,798 ± 0,037 miliardi anni di età, ed è costituito per il 4,9% di materia ordinaria, per il 26,8% di materia oscura e per il 68,3% da energia oscura. Inoltre, la costante di Hubble è stata misurata in 67,80 ± 0,77 (km/s)/Mpc.Le interpretazioni precedenti delle osservazioni astronomiche avevano indicato come l'età dell'universo fosse di 13,772 ± 0,059 miliardi di anni, (mentre il disaccoppiamento della luce e della materia, si veda CMBR, avvenne 380.000 anni dopo il Big Bang), e che il diametro dell'universo osservabile è di minimo 93 miliardi di anni luce. Secondo la relatività generale, lo spazio può espandersi con velocità maggiore di quella della luce, ma possiamo vederne solo una piccola porzione a causa delle limitazioni imposte dalla velocità della luce stessa. Dato che non è possibile effettuare osservazioni oltrepassando i limiti imposti dalla velocità della luce (e, in generale, di ogni radiazione elettromagnetica), non è possibile stabilire se le dimensioni dell'universo siano finite o infinite.

La regione dell'Universo visibile dalla Terra (l'universo osservabile) è una sfera con un raggio di circa 46 miliardi di anni luce. Per confronto, il diametro di una Galassia tipica è di 30.000 anni luce, e la distanza tipica tra due galassie vicine è invece di 3 milioni di anni-luce. Ad esempio, la Via Lattea ha un diametro di circa 100.000 anni luce, e la galassia più vicina a noi, Andromeda, si trova approssimativamente a 2,5 milioni di anni luce da noi.Ci sono probabilmente più di 100 miliardi (1011) di galassie nell'universo osservabile, seppure l'analisi dei dati dei progetti "Hubble Deep Field" e "Hubble Ultra Deep Field" abbia portato a teorizzarne un numero compreso tra i 300 e i 500 miliardi. Le galassie tipiche vanno dalle galassie nane con un minimo di dieci milioni (107) di stelle fino alle galassie giganti con mille miliardi (1012) di stelle, le quali orbitano tutte attorno al centro di massa della loro galassia. Uno studio del 2010 stima il numero di stelle dell'universo osservabile in 300.000 trilioni (3×1023), mentre uno studio del 2016 ipotizza che il numero totale di galassie nell'universo osservabile, comprese quelle troppo piccole per essere rilevate dagli attuali telescopi, sia di 2000 miliardi (2x1012).

La materia osservabile è distribuita in maniera omogenea (uniformemente) in tutto l'universo, in media su distanze di più di 300 milioni di anni luce. Tuttavia, su piccole scale di lunghezza, la materia si dispone in "grumi", raggruppandosi gerarchicamente: una gran quantità di atomi è presente nelle stelle, la maggior parte delle stelle si raggruppa in galassie, la maggior parte delle galassie in ammassi, superammassi di galassie e, infine, si hanno strutture a larga scala come la Grande muraglia. La materia osservabile dell'Universo è inoltre diffusa isotropicamente, il che significa che ogni regione del cielo ha all'incirca lo stesso contenuto.L'universo è inoltre immerso in una radiazione a microonde altamente isotropica, che corrisponde ad un equilibrio termico con spettro di corpo nero di circa 2,725 Kelvin. L'ipotesi secondo cui l'Universo sia omogeneo e isotropo su grandi scale è nota come principio cosmologico, che è supportato da osservazioni astronomiche.
L'attuale densità globale dell'universo è molto bassa, circa 9,9 × 10−30 grammi per centimetro cubo. Questa massa-energia sembra essere formata per il 68,3% da energia oscura, il 26,8% da materia oscura fredda e il 4,9% da materia ordinaria. La densità in atomi è dell'ordine di un singolo atomo di idrogeno per ogni quattro metri cubi di volume.Le proprietà dell'energia oscura e della materia oscura sono in gran parte sconosciute. La materia oscura interagisce con il campo gravitazionale come la materia ordinaria, e quindi rallenta l'espansione dell'universo; al contrario, l'energia oscura accelera la sua espansione.
La stima più precisa dell'età dell'universo è di 13,798 ± 0,037 miliardi di anni, calcolata sulla base delle osservazioni della radiazione cosmica di fondo condotte con la sonda PLANCK. Stime indipendenti (sulla base di misurazioni come la datazione radioattiva) convergono anch'esse su 13-15 miliardi di anni.
L'universo non è stato lo stesso in ogni momento della sua storia; ad esempio, le popolazioni relative dei quasar e delle galassie sono cambiate e lo spazio stesso si è espanso. Questa espansione spiega come sulla Terra si possa osservare la luce proveniente da una galassia lontana 30 miliardi di anni luce, anche se la luce ha viaggiato per 13 miliardi di anni: lo spazio si è ampliato. Questa espansione è coerente con l'osservazione che la luce proveniente da galassie lontane ha subito lo spostamento verso il rosso: la lunghezza d'onda dei fotoni emessi è stata "stirata" e dunque aumentata, con un conseguente abbassamento della loro frequenza, durante il loro viaggio. Sulla base di studi di supernovae di tipo Ia, corroborati anche da altri dati, il tasso di questa espansione spaziale è in accelerazione.
Le frazioni relative di diversi elementi chimici - in particolare degli atomi più leggeri, come idrogeno, deuterio e elio - sembrano identiche in tutto l'universo e in tutta la sua storia osservabile.L'universo sembra avere molta più materia che antimateria, un'asimmetria forse correlata alle osservazioni in merito alla violazione di CP. L'universo sembra non avere nessuna carica elettrica netta, e quindi la gravità sembra essere l'interazione dominante su scale di lunghezza cosmologica. L'universo sembra non avere né un momento né un momento angolare netti. L'assenza di carica e quantità di moto nette sarebbe conseguenza di accettate leggi fisiche (la Legge di Gauss e la non-divergenza dello pseudotensore stress-energia-momento rispettivamente), se l'universo fosse finito.

L'universo sembra avere un continuum spazio-temporale liscio costituito da tre dimensioni spaziali e da una temporale. In media, le osservazioni sullo spazio tridimensionale suggeriscono che esso sia piatto, cioè abbia curvatura vicina a zero; ciò implica che la geometria euclidea è sperimentalmente vera con elevata precisione per la maggior parte dell'Universo. Lo spaziotempo sembra anche avere una topologia semplicemente connessa, almeno sulla scala di lunghezza dell'universo osservabile. Tuttavia le osservazioni attuali non possono escludere la possibilità che l'universo abbia più dimensioni, e che il suo spazio-tempo possa avere una topologia globale molteplicemente connessa, in analogia con le topologie del cilindro o del toro.L'universo sembra comportarsi in modo tale da seguire regolarmente un insieme di leggi e costanti fisiche. Secondo l'attuale Modello standard della fisica, tutta la materia è composta da tre generazioni di leptoni e quark, che sono entrambi fermioni. Queste particelle elementari interagiscono attraverso almeno tre interazioni fondamentali: l'interazione elettrodebole che comprende l'elettromagnetismo e la forza nucleare debole, la forza nucleare forte descritta dalla cromodinamica quantistica e la gravità, che, al momento, è descritta al meglio dalla relatività generale. Le prime due interazioni possono essere descritte da teorie quantistiche rinormalizzate, e sono mediate da bosoni di gauge ciascuno dei quali corrisponde a un particolare tipo di simmetria di gauge.
Una teoria quantistica dei campi rinormalizzata della relatività generale non è ancora stata raggiunta, anche se le varie forme di teoria delle stringhe sembrano promettenti. Si ritiene che la teoria della relatività speciale valga in tutto l'universo, a condizione che le scale di lunghezza spaziali e temporali siano sufficientemente brevi, altrimenti deve essere applicata la più generale teoria della relatività generale. Non esiste una spiegazione per i valori particolari che le costanti della fisica sembrano avere nel nostro universo, come ad esempio quello per la costante di Planck h o per la costante di gravitazione universale G. Sono state identificate diverse leggi di conservazione, come la conservazione della carica, del momento, del momento angolare e dell'energia; in molti casi, queste leggi di conservazione possono essere correlate a simmetrie o a identità matematiche.

Sembra che molte delle proprietà dell'Universo abbiano valori speciali, nel senso che un universo con proprietà solo leggermente differenti non sarebbe in grado di sostenere la vita intelligente. Non tutti gli scienziati concordano sul fatto che l'Universo sia effettivamente "finemente regolato" (un fine-tuned Universe in inglese).
In particolare, non si sa in quali condizioni la vita intelligente si potrebbe formare e quali possano essere le forme che essa richiede. Un'osservazione rilevante in questa discussione è che per un osservatore che esista, e quindi in grado di osservare una regolazione fine, l'Universo deve essere in grado di sostenere la vita intelligente. Pertanto, la probabilità condizionata di osservare un universo messo a punto per sostenere la vita intelligente è sempre 1. Questa osservazione è nota come principio antropico ed è particolarmente importante se la creazione dell'Universo è probabilistica o se esistono universi multipli con proprietà variabili (vedi La teoria del Multiverso).

Storicamente diverse cosmologie e cosmogonie si sono basate su narrazioni degli eventi fra antiche divinità. Le prime teorie di un universo impersonale governato da leggi fisiche risalgono agli antichi greci e indiani. Nei secoli, nuove invenzioni di strumenti per l'osservazione e scoperte nel campo dei moti dei corpi e della gravitazione portarono ad una sempre più accurata descrizione dell'universo. L'era moderna della cosmologia ebbe inizio nel 1915 con la teoria della relatività generale di Einstein, che rese possibile fare ipotesi quantitative sull'origine, l'evoluzione e la conclusione dell'intero universo. La più moderna ed accettata teoria sulla cosmologia si basa sulla relatività generale e, più nello specifico, sull'ipotesi del Big Bang.

Molte culture hanno storie che descrivono l'origine del mondo, le quali possono essere raggruppate sommariamente in tipologie comuni. Una di queste è la nascita del mondo da un uovo cosmico; esempi di storie relative a questa tipologia sono il poema epico finlandese Kalevala, la storia cinese di Pangu e l'indiano Brahmanda Purana. La Creazione può venire provocata da una singola entità, la quale emana o produce qualcosa da essa stessa, come nel caso del Buddhismo tibetano (Adi-Buddha) o di Gaia, del mito azteco di Coatlicue, della divinità egiziana Atum o della Genesi ebraico-cristiana. In altri tipi di storie, il mondo viene creato dall'unione di una divinità maschile e di una femminile, come nella narrazione mitologica Māori di Rangi e Papa. In altre storie ancora, l'universo è creato dalla lavorazione di "materiale" preesistente, come nella narrazione epica babilonese Enûma Eliš, in quella norrena del gigante Ymir e nella storia di Izanagi e Izanami della mitologia giapponese; altre volte l'universo ha origine da principi fondamentali: si vedano ad esempio Brahman e Prakṛti, o lo yin e lo yang del Tao.

Dal VI secolo prima di Cristo, i Presocratici svilupparono il primo modello filosofico conosciuto dell'universo. Gli antichi filosofi greci notarono che l'apparenza poteva ingannare e che doveva essere compresa per delineare la realtà dietro l'apparenza stessa. In particolare, notarono l'abilità delle cose di mutare forma (come il ghiaccio, in acqua e poi in vapore) e diversi filosofi proposero che tutti gli apparentemente differenti materiali del mondo fossero forme diverse di un singolo materiale primordiale, chiamato Archè. Il primo a pensare ciò fu Talete, il quale affermò che questo materiale era l'acqua. Uno studente di Talete, Anassimandro, propose che ogni cosa provenisse dall'illimitato Ápeiron. Anassimene di Mileto, invece, propose l'aria come Arché, a causa delle sue qualità percepite attrattive e repulsive che le permetteva di condensarsi e dissociarsi in forme differenti.
Anassagora propose il principio dell'intelletto cosmico mentre Eraclito affermò che l'Arché fosse il fuoco (e parlò anche di Logos). Empedocle propose quattro elementi: terra, acqua, aria e fuoco, dando così vita ad una credenza molto popolare. Come Pitagora, Platone credeva che tutte le cose erano composte da numeri, trasformando gli elementi di Empedocle in "solidi". Leucippo, Democrito, e altri filosofi successivi - tra cui Epicuro -, proposero che l'universo fosse composto da elementi invisibili, gli atomi, i quali si muovono all'interno del vuoto. Aristotele invece non credeva che fosse possibile in quanto l'aria, come l'acqua, generava una resistenza al moto. L'aria infatti si precipita a riempire un vuoto e, facendo ciò, il suo moto è indefinitivamente veloce e privo di resistenze.
Anche se Eraclito parla di cambiamenti eterni, Parmenide, suo quasi contemporaneo, dà un radicale suggerimento, affermando che tutti i cambiamenti sono un'illusione e che la vera realtà è eternamente immutata e di una natura singola. Parmenide chiama questa realtà "Essere". La teoria di Parmenide sembrò implausibile a molti Greci ma un suo studente, Zenone di Elea sostenne questa teoria con diversi e famosi paradossi, i Paradossi di Zenone. Aristotele rispose a questi paradossi sviluppando la nozione di una potenziale infinità numerabile, un esempio della quale è il concetto di continuo infinitamente divisibile. Diversamente dall'eterno e immutabile ciclo del tempo, egli credeva che il mondo fosse delimitato da sfere celesti.
Il filosofo indiano Kanada, fondatore della scuola Vaiśeṣika, sviluppò una teoria di atomismo e propose la luce e il calore come varietà della stessa sostanza. Nel V secolo d.C., il filosofo buddhista Dignaga affermò che l'atomo è un punto adimensionale fatto di energia. Negò quindi l'esistenza di una sostanza materiale e affermò che il movimento consisteva in flash momentanei di un flusso di energia.La teoria del finitismo temporale si ispirò alla dottrina della Creazione tipica delle tre religioni abramitiche: giudaismo, cristianesimo e islamismo. Il filosofo cristiano Giovanni Filopono presentò un'argomentazione filosofica contro la nozione greca di un infinito passato ed un infinito futuro. L'argomentazione contro il passato fu creata dal filosofo islamico al-Kindi, dal filosofo ebraico Saadya Gaon e dal teologo islamico Al-Ghazali. Facendosi prestare la "fisica" e la "metafisica" aristoteliche, idearono due argomentazioni logiche contro l'infinitezza del passato, la prima delle quali "argomenta dell'impossibilità dell'esistenza di un infinito attuale", che afferma:
"Un infinito attuale non può esistere."
"Un infinito regresso temporale di eventi è un infinito attuale."

  
    
      
        ⇒
      
    
    {\displaystyle \Rightarrow }
   "Un infinito regresso temporale di eventi non può esistere."La seconda argomentazione "argomenta dell'impossibilità di completare un infinito attuale con un'adduzione successiva":
"Un infinito attuale non può essere completato da una successiva aggiunta."
"Le serie temporali dei passati esempi è stata completata da aggiunte successive."

  
    
      
        ⇒
      
    
    {\displaystyle \Rightarrow }
   "Le serie temporali dei passati eventi non può essere un infinito attuale."Entrambe le argomentazioni furono adottate dai filosofi e teologi cristiani e la seconda argomentazione, in particolare, divenne molto famosa dopo che essa fu adottata da Immanuel Kant nelle sue famose tesi sulla prima antinomia sul tempo.

Dei primi modelli astronomici dell'universo furono proposti dagli astronomi babilonesi che vedevano l'universo come un disco piatto posato su un oceano; tale idea fu la premessa per le mappe di Anassimandro ed Ecateo di Mileto.
In seguito, i filosofi greci, osservando i moti dei corpi celesti, si concentrarono su modelli di universo sviluppati molto più profondamente su prove empiriche. Il primo modello coerente fu proposto da Eudosso di Cnido. Secondo l'interpretazione fisica di Aristotele del modello, delle sfere celesti ruotano eternamente con moto uniforme attorno ad una Terra immobile, mentre gli elementi classici sono contenuti interamente nella sfera terrestre. Questo modello fu rifinito da Callippo di Cizico e dopo che le sfere concentriche furono abbandonate, fu portato al quasi perfetto accordo con le osservazioni astronomiche da Claudio Tolomeo. Il successo di questo modello è largamente dovuto alla matematica: ogni funzione (come la posizione di un pianeta) può essere decomposta in una serie di funzioni circolari (serie di Fourier). Altri filosofi greci, come il pitagorico Filolao affermarono che al centro dell'universo vi era un "fuoco centrale" attorno cui la Terra, il Sole, la Luna e gli altri pianeti rivoluzionano in un moto uniforme circolare. L'astronomo greco Aristarco di Samo fu il primo a proporre un modello eliocentrico. Anche se il testo originale è stato perso, un riferimento in un testo di Archimede descrive la teoria eliocentrica di Aristarco. Archimede scrive:

Aristarco quindi credeva che le stelle fossero molto distanti e attribuiva a questa lontananza il fatto che non si riuscisse a misurare alcun moto stellare di parallasse, il quale è un movimento apparente delle stelle determinato dal movimento della Terra attorno al Sole. Le stelle sono infatti molto più distanti rispetto a quanto si potesse immaginare nei tempi antichi e la loro parallasse è così piccola che poté essere misurata solo nel XVIII secolo. Il modello geocentrico, invece, forniva una valida spiegazione della non osservabilità del fenomeno della parallasse stellare. Il rifiuto della concezione eliocentrica fu apparentemente abbastanza forte, come il seguente passaggio di Plutarco suggerisce:

L'unico astronomo conosciuto dell'antichità che abbia supportato il modello eliocentrico di Aristarco fu Seleuco di Seleucia, un astronomo greco che visse un secolo dopo Aristarco stesso. Secondo Plutarco, Seleuco fu il primo a dare prova della correttezza del sistema eliocentrico attraverso il ragionamento ma non si ha conoscenza di quali argomentazioni abbia usato. Tali argomenti a favore della teoria eliocentrica furono probabilmente legati al fenomeno delle maree. Secondo Strabone, Seleuco fu il primo ad affermare che le maree sono dovute all'attrazione della Luna e che la loro altezza dipende dalla posizione della Luna rispetto al Sole. In alternativa, avrebbe potuto provare la teoria eliocentrica determinando la costante di un modello geometrico della teoria eliocentrica e sviluppando metodi per determinare le posizioni planetarie usando questo modello, come ciò che avrebbe fatto in seguito Corpernico nel XVI secolo. Durante il Medioevo, il modello eliocentrico poteva essere proposto solo dall'astronomo indiano Aryabhata e dai persiani Abu Ma'shar al-Balkhi e Al-Sijzi.

Il modello aristotelico fu accettato nel mondo occidentale per circa due millenni, finché Copernico non ravvivò la teoria di Aristarco che i dati astronomici potevano essere spiegati più plausibilmente se la Terra ruotava attorno al proprio asse e se il Sole fosse posizionato al centro dell'universo.

Come fa notare Copernico stesso, l'idea che la Terra ruoti era molto antica, databile almeno fin da Filolao (circa 450 a.C.), Eraclide Pontico (circa 350 a.C.) ed Ecfanto di Siracusa. Circa un secolo prima di Copernico, uno studioso cristiano, Nicola Cusano, aveva anch'esso proposto che la Terra ruotasse attorno al proprio asse nel suo stesso testo, La Dotta Ignoranza (1440). Anche Aryabhata (476 - 550), Brahmagupta (598 - 668), Abu Ma'shar al-Balkhi e Al-Sijzi avevano presunto che la Terra ruotasse attorno al proprio asse. La prima prova empirica della rotazione della Terra, ottenuta osservando le comete, fu data da Nasir al-Din al-Tusi (1201 - 1274) e da Ali Qushji (1403 - 1474).

Questa cosmologia era accettata da Isaac Newton, Christiaan Huygens e altri scienziati. Edmund Halley (1720) e Jean-Philippe Loys de Chéseaux (1744) notarono, indipendentemente, che il presupposto di uno spazio infinito e saturo, uniforme con le stelle, avrebbe portato alla conclusione che il cielo notturno avrebbe dovuto essere luminoso come quello durante il dì; questa analisi divenne nota, nel XIX secolo come il Paradosso di Olbers. Newton credeva che uno spazio infinito uniformemente saturo con la materia avrebbe causato infinite forze ed infinita stabilità che avrebbe portato la materia a condensarsi verso l'interno a causa della sua stessa gravità. Questa instabilità fu chiarita nel 1902 dal criterio dell'instabilità di Jeans. Una soluzione a questo paradosso è l'universo di Charlier, in cui la materia è organizzata gerarchicamente (sistemi di corpi orbitanti che sono loro stessi in orbita in sistemi più grandi, ad infinitum) in un frattale come ad esempio quello in cui l'universo ha una densità complessiva trascurabile; un modello cosmologico simile fu proposto precedentemente, nel 1761, da Johann Heinrich Lambert. Un avanzamento astronomico significativo del XVIII secolo si ebbe con le nebulose, su cui discussero anche Thomas Wright e Immanuel Kant.La cosmologia fisica dell'era moderna cominciò nel 1917, quando Albert Einstein per primo applicò la sua teoria generale della relatività per modellare strutture e dinamiche dell'universo.

Delle quattro interazioni fondamentali, l'interazione gravitazionale è la dominante su scala cosmologica dove infatti le altre tre forze sono trascurabili. Dato che tutta la materia e l'energia gravitano, gli effetti della gravità stessa sono cumulativi; al contrario, gli effetti di cariche positive e negative tendono ad annullarsi l'una con l'altra, rendendo l'elettromagnetismo relativamente insignificante su scala cosmologica. Le rimanenti due interazioni, la forza nucleare debole e forte si riducono molto rapidamente con l'aumentare della distanza cosicché i loro effetti sono confinati principalmente su scala subatomica.

Una volta stabilita la predominanza della gravitazione nelle strutture cosmiche, per avere modelli accurati del passato e del futuro dell'universo bisogna avere una teoria anch'essa accurata della gravitazione dei corpi. La miglior teoria in merito è la teoria della relatività generale di Albert Einstein, la quale finora ha superato con successo ogni test sperimentale eseguito. Le previsioni cosmologiche effettuate con essa appaiono, con l'osservazione astronomica, corrette, così non vi sono ragioni per adottare una teoria differente.
La relatività generale richiede dieci equazioni differenziali parziali non lineari per la metrica spaziotemporale (Equazioni di campo) che, applicate al "sistema Universo", devono essere risolte con la distribuzione della massa - energia e della quantità di moto su tutto l'universo. Dato che queste non sono note in dettaglio, i modelli cosmologici si sono finora basati sul principio cosmologico, che afferma che l'universo è omogeneo e isotropo; ovvero che le galassie siano distribuite uniformemente su tutto l'universo, con la stessa densità media. Presumendo una polvere uniforme per tutto l'universo, le equazioni di campo di Einstein si riducono alle più semplici Equazioni di Friedmann e si può quindi prevedere facilmente il futuro dell'universo e conoscere anche con buona precisione il suo passato, sempre su scala cosmologica.
Le equazioni di campo di Einstein includono una costante cosmologica (Λ), che corrisponde ad una densità di energia dello spazio vuoto. In base al suo segno, la costante può ridurre (Λ negativo) o accelerare (Λ positivo) l'espansione dell'universo. Anche se molti scienziati, incluso Einstein, hanno sostenuto che Λ fosse uguale a zero, recenti osservazioni astronomiche di una supernova di tipo Ia hanno fatto individuare una buona quantità di energia oscura, la quale funziona da catalizzatrice per l'espansione dell'universo. Studi preliminari suggeriscono che l'energia oscura corrisponde ad un Λ positivo, anche se teorie alternative non si possono ancora escludere. Il fisico russo Jakov Borisovič Zel'dovič ha suggerito che Λ sia una misura di energia di punto zero associata con particelle virtuali della teoria quantistica dei campi, una diffusa energia del vuoto che esiste ovunque, anche nello spazio vuoto. Prova di questa energia di punto zero sarebbe osservabile nell'effetto Casimir.

Le distanze fra le galassie aumentano con il passare del tempo (legge di Hubble). L'animazione a fianco illustra un universo chiuso di Friedman con costante cosmologica Λ uguale a zero.
Le equazioni di campo di Einstein legano la geometria ed in particolare la curvatura dello spaziotempo alla presenza di materia o energia. La curvatura dello spaziotempo è un parametro che può essere positivo, negativo o nullo. Semplificando lo spaziotempo (che è a quattro dimensioni) in una superficie bidimensionale (che è a due dimensioni) per ovvia comodità di rappresentazione, la curvatura si manifesta, su una superficie bidimensionale, nella somma degli angoli interni di un triangolo. In uno spazio piatto, ovvero "a curvatura nulla" (spazio euclideo, spaziotempo di Minkowski), la somma degli angoli interni di un triangolo è esattamente uguale a 180 gradi. In uno spazio a curvatura positiva o negativa invece la somma degli angoli interni di un triangolo è rispettivamente maggiore o minore di 180 gradi (la differenza da questo ultimo valore è chiamato angolo di deficit). Una curvatura non nulla dello spaziotempo implica che questo debba essere studiato con le regole di una geometria non euclidea opportuna.
Le geometrie non euclidee devono essere quindi considerate nelle soluzioni generali dell'equazione di campo di Einstein.
In esse, il teorema di Pitagora per il calcolo delle distanze vale solamente su lunghezze infinitesime e deve essere "sostituito" con un più generale tensore metrico gμν, che può variare da luogo a luogo. Presumendo il principio cosmologico, secondo cui l'universo è omogeneo e isotropo, la densità di materia in ogni punto nello spazio è uguale ad ogni altro e quindi possono essere ricercate soluzioni simmetriche in cui il tensore metrico sarà costante ovunque nello spazio tridimensionale. Ciò porta a considerare un possibile tensore metrico chiamato Metrica di Friedmann - Lemaître - Robertson - Walker:

  
    
      
        d
        
          s
          
            2
          
        
        =
        −
        
          c
          
            2
          
        
        d
        
          t
          
            2
          
        
        +
        R
        (
        t
        
          )
          
            2
          
        
        
          (
          
            
              
                
                  d
                  
                    r
                    
                      2
                    
                  
                
                
                  1
                  −
                  k
                  
                    r
                    
                      2
                    
                  
                
              
            
            +
            
              r
              
                2
              
            
            d
            
              θ
              
                2
              
            
            +
            
              r
              
                2
              
            
            
              sin
              
                2
              
            
            ⁡
            θ
            
            d
            
              ϕ
              
                2
              
            
          
          )
        
      
    
    {\displaystyle ds^{2}=-c^{2}dt^{2}+R(t)^{2}\left({\frac {dr^{2}}{1-kr^{2}}}+r^{2}d\theta ^{2}+r^{2}\sin ^{2}\theta \,d\phi ^{2}\right)}
  dove (r, θ, φ) corrispondono ad un sistema di coordinate sferico. Questa metrica ha solo due parametri indeterminati: una scala di lunghezza complessiva R che può variare con il tempo (che infatti compare come R(t), dove t indica il tempo) e un indice di curvatura k che può assumere solo i valori 0, 1 o -1, corrispondenti al piano della geometria euclidea o a spazi di curvatura positiva o negativa. Tramite questi due parametri, la metrica influenza la storia dell'universo, la quale verrà quindi dedotta calcolando R in funzione del tempo, assegnati i valori di k e della costante cosmologica Λ, che è un parametro delle equazioni di campo di Einstein. L'equazione che descrive come varia R nel tempo ( R(t) ) quando si assume il principio cosmologico, è più propriamente conosciuta come equazione di Friedmann, che è una forma particolare dell'Equazione di campo di Einstein.Le soluzioni per R(t) dipendono da  k e da Λ, ma alcune caratteristiche qualitative di tali soluzioni sono generali. Prima e più importante, la lunghezza della scala R dell'Universo può rimanere costante solo se l'Universo è perfettamente isotropo, con curvatura positiva (k = 1), e con un preciso valore di densità uguale dappertutto; quest'osservazione venne fatta per la prima volta da Einstein. Anche questo equilibrio è tuttavia instabile, e d'altra parte l'Universo è noto per essere disomogeneo sulle scale più piccole; pertanto, in accordo con la relatività generale,  R deve cambiare. Quando R cambia, tutte le distanze spaziali nell'Universo cambiano in tandem: si registra un aumento globale o una contrazione dello spazio stesso. Questo spiega l'osservazione iniziale che le galassie si stanno allontanando tra di loro: lo spazio tra di loro si sta "stirando". Lo stiramento dello spazio spiega anche l'apparente paradosso per cui due galassie possono essere separate da 40 miliardi di anni luce anche se hanno iniziato la loro storia nello stesso punto 13 798 000 000 di anni fa e non si sono mai mosse più velocemente della luce.
La seconda caratteristica è che tutte le soluzioni suggeriscono la presenza nel passato di una singolarità gravitazionale: quando R va a 0, la materia e l'energia presenti nell'Universo divengono infinitamente dense. Può sembrare che questa conclusione sia dubbia, in quanto si basa su ipotesi discutibili di perfetta omogeneità e isotropia (principio cosmologico) e sull'idea che solo l'interazione gravitazionale sia significativa. Tuttavia, i Teoremi sulla singolarità di Penrose-Hawking indicano che una singolarità dovrebbe esistere anche sotto condizioni molto più generali. Pertanto, in base alle equazioni di campo di Einstein,  R è cresciuto rapidamente da uno stato di densità e calore inimmaginabili, esistente immediatamente dopo la singolarità. Questa è l'essenza del modello del Big Bang. Un comune errore che si fa pensando al Big Bang è che il modello preveda che la materia e l'energia siano esplose da un singolo punto nello spazio e nel tempo; in realtà, lo spazio stesso è stato creato nel Big Bang, intriso di una quantità fissa di energia e di materia distribuite inizialmente in modo uniforme; con l'espansione dello spazio (vale a dire, con l'aumento di  R (t)), la densità di materia e di energia diminuisce.

La terza caratteristica è che l'indice di curvatura k determina il segno della curvatura spaziale media dello spaziotempo su scale di lunghezza superiore al miliardo di anni luce. Se k = 1, la curvatura è positiva e l'Universo ha un volume finito. Questo tipo di Universo è spesso visualizzato come una sfera tridimensionale S3 incorporata in uno spazio quadridimensionale. Se  k è invece pari a zero o negativo, l'Universo può, in base alla sua topologia complessiva, avere un volume infinito. Può sembrare contro-intuitivo il fatto che un universo infinito e infinitamente denso possa essere stato creato in un solo istante con il Big Bang, quando R = 0, tuttavia ciò è ricavabile matematicamente ponendo k diverso da 1. Analogamente, un piano infinito ha curvatura nulla ma area infinita, un cilindro infinito è finito in una direzione, mentre un toro è finito in entrambe le direzioni. Un Universo toroidale potrebbe comportarsi come un universo con condizioni al contorno periodiche: un viaggiatore che attraversi un "confine" dello spazio riapparirebbe in un altro punto dello stesso Universo.

Il destino ultimo dell'Universo è attualmente sconosciuto, in quanto dipende strettamente dall'indice di curvatura k e dalla costante cosmologica Λ, entrambi ancora non noti sperimentalmente con sufficiente precisione. Se l'Universo è abbastanza denso, k è uguale a 1, la sua curvatura media sarebbe positiva e l'Universo finirebbe per collassare in un Big Crunch, per poi eventualmente dar vita ad un nuovo Universo in un Big Bounce. Se invece l'Universo non è sufficientemente denso, k è uguale a 0 o a -1, l'Universo si espanderebbe all'infinito (Big Freeze), raffreddandosi fino a diventare inospitale per tutte le forme di vita, le stelle si spegnerebbero e la materia finirebbe in buchi neri (secondo alcuni, come Lee Smolin, ogni buco nero potrebbe generare a sua volta un nuovo universo). Come osservato in precedenza, dati recenti suggeriscono che la velocità di espansione dell'Universo non è in calo come originariamente previsto, ma in aumento. Se la velocità di espansione continuasse ad aumentare indefinitamente, l'Universo si espanderebbe in modo tale da "fare a brandelli" tutta la materia: (Big Rip). Sulla base delle recenti osservazioni, l'Universo sembra avere una densità vicina al valore critico che separa il collasso (Big Crunch) dall'espansione eterna (Big Freeze); per comprendere quindi l'effettivo destino dell'universo sono necessarie osservazioni astronomiche più precise.

Il modello prevalente del Big Bang tiene conto di molte delle osservazioni sperimentali sopra descritte, come ad esempio la correlazione tra distanza e redshift delle galassie, il rapporto universale tra il numero di atomi di idrogeno e quello di atomi di elio, e la presenza dell'isotropica radiazione cosmica di fondo. Come notato sopra, il redshift deriva dall'espansione metrica dello spazio: con l'espansione dello spazio, la lunghezza d'onda di un fotone viaggiante attraverso lo spazio aumenta in maniera analoga, e il fotone diminuisce la sua energia. Più a lungo un fotone ha viaggiato, più è grande l'espansione che ha subito; di conseguenza, i fotoni delle galassie più distanti sono i più spostati verso le lunghezze d'onda più basse; si dice, con un anglicismo, che sono "red-shiftati", ovvero "spostati verso il rosso". Determinare la correlazione tra distanza e spostamento verso il rosso è un importante problema sperimentale di cosmologia fisica.

Le altre due osservazioni sperimentali possono essere spiegate combinando l'espansione globale dello spazio con la fisica nucleare e la fisica atomica. Con l'espansione dell'Universo, la densità di energia della radiazione elettromagnetica diminuisce più velocemente rispetto a quella della materia, in quanto l'energia di un fotone diminuisce con la sua lunghezza d'onda. Quindi, anche se la densità di energia dell'Universo è ora dominata dalla materia, un tempo era dominata dalla radiazione; poeticamente parlando, tutto era luce. Durante l'espansione dell'universo, la sua densità di energia è diminuita ed è diventato più freddo; in tal modo, le particelle elementari della materia si sono potute associare stabilmente in combinazioni sempre più grandi. Pertanto, nella prima parte dell'epoca dominata dalla materia, si sono formati protoni e neutroni stabili, che si sono poi associati in nuclei atomici. In questa fase, la materia dell'Universo era principalmente un caldo, denso plasma di elettroni negativi, neutrini neutri e nuclei positivi. Le reazioni nucleari tra i nuclei hanno portato alle abbondanze presenti dei nuclei più leggeri, in particolare dell'idrogeno, del deuterio e dell'elio. Elettroni e nuclei si sono infine combinati per formare atomi stabili, che sono trasparenti alla maggior parte delle lunghezze d'onda della radiazione; a questo punto, la radiazione si disaccoppiò quindi dalla materia, formando l'onnipresente, isotropico sfondo di radiazione a microonde osservato oggi.
Altre osservazioni non hanno ancora una risposta definitiva dalla fisica conosciuta. Secondo la teoria prevalente, un leggero squilibrio della materia sull'antimateria era presente alla creazione dell'Universo, o si sviluppò poco dopo, probabilmente a causa della violazione di CP osservata dai fisici delle particelle. Anche se materia e antimateria si sono in gran parte annientate l'una con l'altra, producendo fotoni, una piccola quantità di materia è così sopravvissuta, dando l'attuale Universo dominato dalla materia. Molte evidenze sperimentali suggeriscono che una rapida inflazione cosmica dell'Universo avvenne molto presto nella sua storia (circa 10−35 secondi dopo la sua creazione). Recenti osservazioni suggeriscono anche che la costante cosmologica (Λ) non è pari a zero e che il contenuto netto di massa-energia dell'Universo sia dominato da una energia oscura e da una materia oscura che non sono state ancora caratterizzate scientificamente. Esse differiscono nei loro effetti gravitazionali. La materia oscura gravita come la materia ordinaria, e rallenta quindi l'espansione dell'Universo; al contrario, l'energia oscura serve per accelerare l'espansione dell'Universo.

Alcune teorie speculative hanno proposto che questo Universo non sia che uno di un insieme di universi sconnessi, collettivamente indicati come multiverso, sfidando o migliorando definizioni più limitate dell'Universo. Le teorie scientifiche sul multiverso si distinguono da concetti come piani alternativi di coscienza e realtà simulata. L'idea di un universo più grande non è nuova; ad esempio, il vescovo Étienne Tempier di Parigi ha stabilito nel 1277 che Dio potesse creare tanti universi quanti ne ritenesse opportuni, una questione che è stata oggetto di accesi dibattiti tra i teologi francesi.Max Tegmark ha sviluppato uno schema di classificazione in quattro parti per i diversi tipi di multiversi che gli scienziati hanno suggerito in diversi ambiti di problemi. Un esempio di tali tipi è il modello di Universo primordiale a inflazione caotica.Un altro è l'interpretazione a molti mondi della meccanica quantistica. I mondi paralleli sarebbero generati in maniera simile alla sovrapposizione quantistica e alla decoerenza, con tutti gli stati della funzione d'onda in corso di realizzazione in mondi separati. In effetti, il multiverso si evolve come una funzione d'onda universale.
La categoria meno controversa di multiverso nello schema di Tegmark è il I Livello, che descrive eventi spazio-temporali remoti rispetto a noi ma ancora "nel nostro Universo". Se lo spazio è infinito, o sufficientemente ampio e uniforme, potrebbe contenere copie identiche della storia della Terra e del suo intero volume di Hubble. Tegmark ha calcolato la distanza a cui si troverebbe il nostro più vicino cosiddetto Doppelgänger, e tale distanza sarebbe pari a circa 1010115 metri.
In linea di principio, sarebbe impossibile verificare scientificamente l'esistenza di un volume di Hubble identico al nostro. Tuttavia, dovrebbe seguire come conseguenza abbastanza semplice da osservazioni scientifiche e teorie altrimenti non correlate. Tegmark suggerisce che l'analisi statistica effettuata sfruttando il principio antropico offre la possibilità di testare le teorie del multiverso in alcuni casi.

Un'importante domanda della cosmologia per ora senza risposta è quella della forma dell'universo, ovvero di quale sia la combinazione di curvatura e topologia che lo domina. Intuitivamente, ci si chiede quanto le relazioni tra i suoi punti rispecchino le regole della geometria euclidea o piuttosto quelle di altre geometrie, e, per quanto riguarda la topologia, ci si può chiedere ad esempio se l'universo è fatto di un solo "blocco", oppure se invece presenta "strappi" di qualche genere.
La forma o geometria dell'Universo include sia la geometria locale dell'Universo osservabile sia la geometria globale, che possiamo essere o non essere in grado di misurare. Formalmente, lo scienziato indaga quale 3-varietà corrisponde alla sezione spaziale in coordinate comoventi dello spaziotempo quadridimensionale dell'Universo. I cosmologi normalmente lavorano con una data fetta di spazio-tempo di tipo spazio chiamata coordinata comovente. In termini osservativi, la sezione dello spazio-tempo che si può osservare è il cono di luce passato (i punti all'interno dell'orizzonte cosmologico, dato un certo tempo per raggiungere l'osservatore). Se l'universo osservabile è più piccolo dell'intero Universo (in alcuni modelli è di molti ordini di grandezza inferiore), non si può determinare la struttura globale mediante l'osservazione: ci si deve limitare a una piccola regione.
Tra i modelli di Friedmann–Lemaître–Robertson–Walker (FLRW), la forma di universo attualmente più popolare tra quelle trovate per contenere i dati osservativi, tra i cosmologi, è il modello piatto infinito, mentre altri modelli FLRW includono lo spazio di Poincaré dodecaedrico e il Corno di Picard. I dati che si adattano a questi modelli FLRW di spazio includono in particolare le mappe della radiazione cosmica di fondo della sonda Wilkinson Microwave Anisotropy Probe (WMAP). La NASA ha pubblicato i primi dati del WMAP relativi alle radiazioni cosmiche di fondo nel febbraio 2003. Nel 2009 è stato lanciato l'osservatorio Planck per osservare il fondo a microonde a una più alta risoluzione di WMAP, possibilmente fornendo maggiori informazioni sulla forma dell'Universo. I dati sono stati poi pubblicati a marzo del 2013 - si veda il paragrafo Storia della sua osservazione.
""".strip().translate(table).strip()
        # text = re.sub("{\\\displaystyle[^\n]*}\n", "", text)
        text = re.sub("(\n|\s){2,}", "\n\n", text)
        text = re.sub("\n{3,}", "\n\n", text)
        tokens, break_levels, _ = tokenizer.tokenize(text)
        print(tokens)
        self.maxDiff = None
        print(break_levels)
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        print(len(text))
        print(len(rebuilt))
        # k = [i for i in range(len(rebuilt)) if text[i] != rebuilt[i]][0]
        # print(repr(text[k-5:]))
        # print(repr(rebuilt[len(text):]))
        self.assertEqual(len(tokens), len(break_levels))
        self.assertEqual(text, rebuilt)

    def test_toke_3(self):
        text = """"Un infinito attuale non può esistere."
"Un infinito regresso temporale di eventi è un infinito attuale.\""""
        tokenizer = SpacyTokenizer('it')
        tokens, break_levels, _ = tokenizer.tokenize(text)
        print(tokens)
        print(break_levels)
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        self.assertEqual(len(tokens), len(break_levels))
        self.assertEqual(text, rebuilt)

    def test_toke_4(self):
        text = """Nielles-lès-Bléquin è un comune francese di 907 abitanti situato nel dipartimento del Passo di Calais nella regione dell'Alta Francia.

Abitanti censiti"""
        tokenizer = SpacyTokenizer('it')
        tokens, break_levels, _ = tokenizer.tokenize(text)
        print(tokens)
        print(break_levels)
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        self.assertEqual(len(tokens), len(break_levels))
        self.assertEqual(text, rebuilt)

    def test_toke_5(self):
        text = """Brignano Gera d'Adda (Brignà in dialetto bergamasco, e semplicemente Brignano fino al 1863) è un comune italiano di 6 009 abitanti della provincia di Bergamo, in Lombardia.
Situato nella pianura bergamasca, nel lembo di terra denominato Gera d'Adda, dista circa 18 chilometri a sud dal capoluogo orobico.

Le origini del comune risalgono I secolo a.C. quando nella zona si verificarono numerosi insediamenti romani, come testimoniato dai numerosi ritrovamenti archeologici dell'epoca.
Il primo documento che attesta l'esistenza del borgo risale invece all'847.

La storia di Brignano si intreccia con quella dei Visconti fin dal 1186, data in cui Federico Barbarossa ne concede loro il territorio in feudo.
Dopo essere passata, nel 1272, ai Torriani rientra nel possesso dei Visconti nel 1310.
Sagramoro I, figlio illegittimo di Bernabò Visconti, è il capostipite della linea dinastica dei Visconti di Brignano.
La dominazione viscontea venne sancita in modo definitivo dalla costruzione del fosso bergamasco, che delimitava i territori di Brignano a nord e ad est, dividendolo dalle terre poste sotto la repubblica di Venezia ed includendolo definitivamente sotto l'influenza milanese.
L'ultima discendente dei Visconti di Brignano, Antonietta Visconti Sauli, chiude questa linea dinastica con la propria morte nel 1892.
Alcuni autori hanno riconosciuto in Francesco Bernardino Visconti l'Innominato di Alessandro Manzoni.

==

Di particolare interesse nel comune è il palazzo visconteo che nella parte conosciuta come Palazzo Vecchio ospita la sede dell'amministrazione comunale, mentre il Palazzo Nuovo ha subito una serie di passaggi di proprietà presso privati.
I palazzi sono ampiamente affrescati, tra gli autori ricordiamo i Fratelli Galliari ed il Magnasco.
Dalle facciate esterne del palazzo vecchio, si nota la tipica architettura di fine 500 e inizio 600.

All'interno, un porticato con pilastri a pianta quadrata.

All'interno delle sale a pian terreno (che attualmente ospitano gli uffici comunali) si possono ammirare affreschi sui soffitti).

Uno scalone a tre rampe, dalle pareti interamente affrescate, porta al piano nobile. La parete adiacente al primo pianerottolo riporta la rappresentazione di un guerriero, che rimanda all'idea della stirpe vittoriosa dei Visconti; sulla parete sud è manifestata la lotta tra Ercole (riconoscibile dalla pelle del leone che lo ricopre parzialmente) e il gigante Anteo. A bilanciare le scene, stanno tre statue dipinte di soggetti femminili, che rappresentano la Nobiltà, l'Intelligenza e la Generosità.

Lo scalone conduce all'ingresso della Sala del Trono, probabilmente in origine destinata a ricevimenti o eventi ufficiali. Sulle pareti sono riconoscibili le rappresentazioni di otto dei dodici signori di Milano.

Proseguendo la visita, si giunge nell'attigua Sala dell'Innominato, l'ambiente di maggiori dimensioni.
Palazzo Nuovo è un complesso, confinante con Palazzo Vecchio, che risale ai secoli XVI-XVIII. Adiacente all'edificio, si sviluppa un grande parco.
Il Palazzo Visconti viene ancora oggi chiamato impropriamente il "castello". Questo fa supporre che un tempo vi fosse una fortificazione difensiva all'interno dell'area dell'odierno Palazzo Vecchio. Durante i lavori di restauro sono state portate alla luce tracce di strutture fortificate nella zona che collega il Palazzo Vecchio al Palazzo Nuovo.
Nel XV secolo la struttura diviene prettamente residenziale, con la serie di interventi che culmineranno poi nel XVII secolo nella completa trasformazione del Castello in Palazzo.

Sul territorio brignanese sono presenti quattro chiese di notevole pregio artistico e storico.

==
La Chiesa dell'Assunta, la parrocchiale, è stata costruita tra il 1783 e il 1788.
Si tratta di un'opera neoclassica a croce latina e a navata unica. All'interno si trovano un altare dei Fantoni e un'Ultima Cena attribuita al Morazzoni.
Le pareti e la volta sono ornate con affreschi di Romeo Rivetta, 1914-1918.
L'Altare è molto imponente: largo 6,5m e alto 3m, rivestito di Bardiglio celeste e decorato da cornici bianche. Al centro dell'altare, il tabernacolo, con una porta in lamina a sbalzo che rappresenta la cena di Emmaus.

Dietro l'altare, in posizione un po' nascosta, è collocato il Coro.

==
La Chiesa di Sant'Andrea è un edificio ecclesiale romanico risalente al X-XI secolo. Si tratta di un edificio a navata unica divisa i quattro campate.

Vi si accede attraverso un portico quattrocentesco.
Sono ancora leggibili alcuni affreschi che ornano le pareti interne e l'abside. Nel sottarco absidale sono ancora percepibili otto sante raffigurate a mezzo busto inserite in nicchie.
Nell'abside è rappresentato il Creatore tra simbolo evangelico e Dottori della Chiesa.

==
La Chiesa di San Rocco XVI secolo e presenta al suo intero degli affreschi di particolare bellezza tra i quali si distingue, nell'abside, una Madonna e il Bambino tra i santi Sebastiano e Rocco, del 1576.

==

Il Santuario della Madonna dei Campi si trova nelle immediate vicinanze del centro cittadino, nella campagna tra i comuni di Brignano Gera d'Adda, Castel Rozzone e Treviglio.
Si tratta di una chiesa seicentesca a navata unica il cui elemento più importante è un altare policromo del 1725-1727 attribuito ai Fantoni, ed una statua marmorea, di attribuzione non ben definita, rappresentante la Vergine che tiene per mano il bambino e schiaccia sotto i piedi un animale mostruoso, simbolo del demonio.
La statua, posta in una nicchia dell'altare maggiore, venne incoronata durante una celebrazione dell'anno 1949.
All'esterno un portico a tre arcate, con archi a tutto sesto. Sotto il portico, accanto al portone, si aprono due basse finestre con inginocchiatoio in pietra.
Il campanile, alto 22 metri, conteneva 5 campane, che furono requisite per scopi bellici nel 1942. Le attuali campane nel 1949.

1 760 nel 1751
2 319 nel 1805
3 000 dopo annessione di Castel Rozzone nel 1809
2 431 nel 1816
2 634 nel 1853
2 958 nel 1859Abitanti censiti

""".strip()
        table = str.maketrans({"\t": "\\t", "\r": "\\r", "\f": "\\f", "\b": "\\b"})
        text.translate(table).strip()
        text = re.sub("(\n|\s){2,}", "\n\n", text)
        text = re.sub("\n{3,}", "\n\n", text)
        tokenizer = SpacyTokenizer('it')
        tokens, break_levels, _ = tokenizer.tokenize(text)
        print(tokens)
        print(break_levels)
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        self.assertEqual(len(tokens), len(break_levels))
        self.assertEqual(text, rebuilt)

    def test_toke_6(self):
        text = """In matematica, per algebra su un campo K, o

K-algebra, si intende uno spazio vettoriale A sopra K munito di una operazione binaria "compatibile" con le altre leggi di composizione chiamata solitamente "moltiplicazione" degli elementi di A.
Una generalizzazione diretta riguarda la possibilità di servirsi, invece che di un campo di base, di un qualsiasi anello commutativo.

Consideriamo un campo K, uno spazio vettoriale

A

{\displaystyle A}

su K e una operazione binaria su tale spazio

∗

:

A

×

A

→

A

{\displaystyle *:A\times A\to A}

Supponiamo inoltre che l'operazione * sia bilineare, cioè tale che:

(

x

+

y

)

∗

z

=

x

∗

z

+

y

∗

z

{\displaystyle (x+y)*z=x*z+y*z}

x

∗

(

y

+

z

)

=

x

∗

y

+

x

∗

z

{\displaystyle x*(y+z)=x*y+x*z}

(

a

x

)

∗

y

=

a

(

x

∗

y

)

{\displaystyle (ax)*y=a(x*y)}

x

∗

(

b

y

)

=

b

(

x

∗

y

)

{\displaystyle x*(by)=b(x*y)}

con a e b scalari arbitrari in K e con x, y e z vettori arbitrari in A.
Lo spazio A arricchito con questa operazione si dice algebra sul campo K e K si chiama campo di base dell'algebra A. In genere l'operazione binaria viene chiamata "moltiplicazione" dell'algebra e l'oggetto fornito da una espressione come x y viene chiamato prodotto di x e y. Tuttavia l'operazione binaria in molte specie particolari di algebre su campo viene indicata con nomi e notazioni specifiche.
Strutture simili alle algebre su campo, ma un po' più generali si possono definire ricorrendo, invece che ad un campo, ad un anello commutativo K: abbiamo bisogno di un modulo A su K e un'operazione di moltiplicazione bilineare che soddisfa le stesse identità sopra riportate; allora A è una K-algebra, e K è anello base di A.
Due algebre sullo stesso campo K, A e B, si dicono isomorfe se e solo se esiste una applicazione biiettiva lineare rispetto a K

f : A → B tale che f(x* y) = f(x) * f(y) per x e y elementi arbitrari di A. Per molte considerazioni generali due algebre su campo isomorfe sono essenzialmente la stessa entità; esse differiscono nei modi usati per chiamare e per denotare i loro elementi.

Per le algebre su un campo, la moltiplicazione bilineare da A × A a A è completamente determinata dalla moltiplicazione degli elementi della base di A. Viceversa, una volta che la base per A è stata scelta, il prodotto degli elementi della base può essere scelto arbitrariamente, e quindi esteso in un unico modo a un operatore bilineare su A, cioè tale che la moltiplicazione risultante soddisfi le leggi dell'algebra.
Quindi, dato il campo K, ogni algebra può essere specificata a meno di isomorfismi assegnando la sua dimensione (per esempio n), e specificando n³ coefficienti di struttura ci,j,k, che sono scalari.
Questi coefficienti di struttura determinano la moltiplicazione in A tramite la seguente regola:

e

i

e

j

=

∑

k

=

1

n

c

i

,

j

,

k

e

k

{\displaystyle \mathbf {e} _{i}\mathbf {e} _{j}=\sum _{k=1}^{n}c_{i,j,k}\mathbf {e} _{k}}

dove e1,...,en formano una base di A. L'unico requisito per i coefficienti di struttura è che, se la dimensione n è infinita, allora questa somma deve sempre convergere (nel senso più appropriato per la situazione).
Si noti comunque che molti differenti insiemi di coefficienti di struttura possono dare origine ad algebre isomorfe.
Quando l'algebra può essere dotata di una metrica, allora i coefficienti di struttura sono scritti con indici superiori e inferiori, così da distinguere le loro proprietà nelle trasformazioni di coordinate. Così, in fisica matematica, i coefficienti di struttura sono spesso indicati con ci,jk, e la loro regola di definizione è scritta usando la notazione di Einstein come:

eiej = ci,jkek.Se si applica questo ai vettori scritti nella normale notazione a indici, la formula diventa:

(x y)k = ci,jkxiyj.Se K è solo un anello commutativo e non un campo, allora lo stesso procedimento funziona se A è un modulo libero su K. Se non lo è, allora la moltiplicazione è ancora completamente determinata dalla sua azione su un insieme generatore di A; comunque, le costanti di struttura non possono essere specificate arbitrariamente in questo caso, e conoscere solo le costanti di struttura non individua l'algebra a meno di isomorfismi.

Si dice algebra commutativa un'algebra la cui moltiplicazione è commutativa. Si dice algebra associativa un'algebra la cui moltiplicazione è associativa. La maggior parte delle specie di algebra su campo più familiari godono delle due suddette proprietà.

Algebre associative:
Algebra dell'insieme delle parti con le operazioni di differenza simmetrica e intersezione, sul campo delle classi di resto modulo 2

Z

2

{\displaystyle Z_{2}}

.
Algebra di tutte le matrici n × n sopra un campo (o anello commutativo) K avente come moltiplicazione la usuale moltiplicazione di matrici.
Algebra di gruppo, dove come base dello spazio vettoriale si assume un gruppo qualsiasi e come moltiplicazione dell'algebra si assume l'estensione bilineare della moltiplicazione del gruppo. Essa è commutativa se e solo se è tale il gruppo.
Algebra commutativa K[x] di tutti i polinomi sopra il campo K,
Algebre di funzioni: ad esempio, l'algebra sul campo R costituita dalle funzioni continue a valori reali aventi come dominio l'intervallo [0,1] o l'algebra sul campo dei numeri complessi di tutte le funzioni olomorfe definite su qualche insieme aperto fissato del piano complesso. Anche queste sono algebre commutative.
Algebre d'incidenza costruite su qualche insieme parzialmente ordinato localmente finito.
Algebre degli operatori lineari agenti, ad esempio, su uno spazio di Hilbert, per la quale come moltiplicazione della struttura si assume la composizione degli operatori.Tutte queste algebre sono dotate anche di una topologia; molte di esse sono definite sopra uno spazio di Banach e queste strutture sono dette algebre di Banach. Se inoltre è data anche una involuzione, otteniamo le C*-algebre. Queste algebre sono studiate nell'analisi funzionale.
I generi più noti di algebre non associative sono quelle che si avvicinano alle associative, cioè quelle nelle quali le differenze tra i diversi modi di comporre mediante la moltiplicazione dati elementi sono vincolate da semplici espressioni. Passiamoli in rassegna.

Algebre di Lie, per le quali si chiede valgano la x*x = 0 e l'identità di Jacobi (x*y)*z + (y*z)*x + (z*x)*y = 0. Con queste algebre il prodotto è chiamato parentesi di Lie e tradizionalmente viene scritto [x,y] invece di x*y. Esempi di queste algebre sono:
Spazio euclideo sul campo dei numeri reali R³ con la moltiplicazione data dal prodotto vettore.
Algebre di campi vettoriali su varietà differenziabili (se K è R o il campo C) oppure una varietà algebrica (per K qualsiasi);
Da ogni algebra associativa si deriva un'algebra di Lie adottando il commutatore per il ruolo di parentesi di Lie. Infatti ogni algebra di Lie si può costruire in questo modo oppure è la sottoalgebra di un'algebra di Lie costruita con i commutatori.Algebre di Jordan, per le quali si chiede valgano la (x*y)*x² = x*(y*x²) e la commutatività x*y = y*x.
Ogni algebra associativa sopra un campo avente caratteristica diversa da 2 dà origine ad un'algebra di Jordan definendo una nuova moltiplicazione x$y := (1/2)(x*y + y*x). Contrariamente al caso delle algebre di Lie, non tutte le algebre di Jordan si possono costruire in questo modo. Quelle che lo possono sono chiamate speciali.Algebre alternative, per le quali si richiede sia (x*x)*y = x*(x*y) e (y*x)*x = y*(x*x). Gli esempi più importanti sono dati dall'algebra degli ottonioni (algebra sui reali) e generalizzazioni degli ottonioni su altri campi. Osserviamo esplicitamente che tutte le algebre associative sono alternative. A meno di isomorfismi le sole algebre alternative finito-dimensionali sui reali sono l'algebra dei reali, l'algebra dei complessi, l'algebra dei quaternioni e l'algebra degli ottonioni.Algebre associative sulle potenze, per le quali si richiede che sia xm*xn = xm+n, per m ed n interi positivi qualsiasi. (Qui si definiscono le potenze xn ricorsivamente come

x*(xn-1).) Esempi di queste algebre sono forniti da tutte le algebre associative, da tutte le algebre alternative e dall'algebra dei sedenioni.

Algebra di divisione, struttura nella quale esistono gli inversi moltiplicativi, ovvero nella quale si può effettuare la divisione. Le algebre di divisione finito-dimensionali sul campo dei numeri reali possono essere classificate pulitamente.Algebra quadratica, struttura per la quale si chiede che valga la regola xx = re + sx, dove r ed s sono elementi del campo di base ed e un elemento invertibile dell'algebra. A questa classe di strutture appartengono tutte le algebre alternative finito-dimensionali e l'algebra delle matrici reali di aspetto 2 × 2. A meno di isomorfismi, le sole altre algebre quadratiche sui reali senza divisori dello zero sono fornite dai numeri reali, dai numeri complessi, dai quaternioni e dagli ottonioni.La successione delle algebre di Cayley-Dickson sul campo dei reali, che inizia con le seguenti:
C, algebra bidimensionale dei complessi (algebra commutativa e associativa);
algebra dei quaternioni H (algebra associativa);
algebra degli ottonioni (algebra alternativa);
algebra dei sedenioni (algebra associativa sulle potenze, come tutte le altre della successione).Le algebre di Poisson svolgono un ruolo nella quantizzazione geometrica. Ciascuna di esse è uno spazio vettoriale arricchito con due moltiplicazioni che conducono a una struttura di algebra commutativa e una di algebra di Lie.""".strip()
        table = str.maketrans({"\t": "\\t", "\r": "\\r", "\f": "\\f", "\b": "\\b"})
        text = text.translate(table).strip()
        text = re.sub("(\n|\s){2,}", "\n\n", text)
        text = re.sub("\n{3,}", "\n\n", text)
        tokenizer = SpacyTokenizer('it')
        tokens, break_levels, _ = tokenizer.tokenize(text)
        print(tokens)
        print(break_levels)
        print(len(tokens))
        print(len(break_levels))
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        # k = [i for i in range(len(rebuilt)) if text[i] != rebuilt[i]][0]
        # print(repr(text[k-4:]))
        # print(repr(rebuilt[k-4:]))
        # print(repr(rebuilt[len(text):]))
        self.assertEqual(len(tokens), len(break_levels))
        self.maxDiff = None
        self.assertEqual(text, rebuilt)

    def test_toke_7(self):
        text = "Hello\n.\nmario"
        tokenizer = SpacyTokenizer('it')
        tokens, break_levels, _ = tokenizer.tokenize(text)
        print(tokens)
        print(break_levels)
        print(len(tokens))
        print(len(break_levels))
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        # k = [i for i in range(len(rebuilt)) if text[i] != rebuilt[i]][0]
        # print(repr(text[k - 4:]))
        # print(repr(rebuilt[k - 4:]))
        self.assertEqual(len(tokens), len(break_levels))
        self.maxDiff = None
        self.assertEqual(text, rebuilt)

    def test_toke_8(self):
        text = """Il Budapest String Quartet era un quartetto d\'archi operativo dal 1917 al 1967. Originariamente era costituito da tre ungheresi e un olandese; alla fine, il quartetto era composto da quattro russi. Un certo numero di registrazioni furono fatte per la HMV/Victor fino al 1938; dal 1940 al 1967 ha registrato per la Columbia Records. Inoltre, molte delle esibizioni dal vivo del Quartetto sono state registrate presso la Biblioteca del Congresso e in altre sedi.\n\n1° Violino:\n\nEmil Hauser (1893–1978) (dal 1917 al 1932)\nJosef Roisman (Joe) (1900–1974) (dal 1932 al 1967)2° Violino:\n\nAlfred Indig (1892–?) (dal 1917 al 1920)\nImre Pogany (1893–1975) (dal 1920 al 1927)\nJosef Roisman (Joe) (1900–1974) (dal 1927 al 1932)\nAlexander Schneider (Sasha) (1908–1993) (dal 1932 al 1944 e dal 1955 al 1967)\nEdgar Ortenberg (1900–1996) (dal 1944 al 1949)\nJac Gorodetzky (1913–1955) (dal 1949 al 1955)Viola:\n\nIstván Ipolyi (1886–1955) (dal 1917 al 1936)\nBoris Kroyt (1897–1969) (dal 1936 al 1967)Violoncello:\n\nHarry Son (nato Henri Mozes Son) (1880–1942) (dal 1917 al 1930)\nMischa Schneider (1904–1985) (dal 1930 al 1967)\n\nIl Budapest String Quartet fu costituito nel 1917 da quattro amici, tutti membri di orchestre d\'opera che avevano cessato l\'operatività a causa della prima guerra mondiale. I membri erano tutti protetti di Jenő Hubay (violino), allievo ungherese di József Joachim e David Popper (violoncello), un boemo. Hubay e Popper contribuirono a rendere Budapest un importante centro per l\'educazione musicale, che attraeva studenti famosi come Josef Szigeti. Hubay e Popper avevano sostenuto Sándor Végh e Feri Roth nella formazione di quartetti, e facevano parte essi stessi di un primo Budapest Quartet, il nuovo quartetto prese il nome in parte in onore di questo. Il recital di debutto del nuovo Budapest String Quartet (in ungherese: Budapesti Vonósnégyes), ebbe luogo nel dicembre 1917 a Kolozsvár, allora in Ungheria, ora chiamato Cluj-Napoca, nell\'attuale Romania.Il quartetto nasce con certe regole:\n\nTutte le controversie, musicali o lavorative, dovevano essere risolti da un voto. In caso di parità, nessun cambiamento.\nI musicisti non sono autorizzati a prendere altri impegni al di fuori del quartetto.\nI giocatori vengono pagati in modo egualitario. Nessuna preferenza è ammessa per il leader (primo violino).\nLe mogli e le fidanzate non sono ammesse alle prove o alle discussioni.Nessun quartetto precedente aveva tentato di sopravvivere interamente con il ricavato dei suoi concerti. Fu una decisione coraggiosa per l\'epoca. Molto più tardi, nel luglio 1930, i membri attuali aggiunsero un\'altra regola per risolvere i voti pari. Un suonatore, estratto a sorte, avrebbe avuto un voto decisivo. Le sue iniziali sarebbero state scritte sulla musica e avrebbe sempre il voto in più per quel pezzo. Se veniva sostituito, il suo successore avrebbe preso i suoi diritti di voto.I membri originali erano Emil Hauser, 24 anni, di Budapest; Alfred Indig, 25 anni, dall\'Ungheria; István Ipolyi, 31 anni, da Újvidék in Ungheria; e Harry Son da Rotterdam, Paesi Bassi.Nel 1920 si dimise Indig nella speranza di un avanzamento; fu sostituito da Imre Pogany. Pogany veniva da Budapest e aveva studiato sotto Hubay e Zoltán Kodály. Dopo le dimissioni, Indig divenne solista con l\'Orchestra reale del Concertgebouw di Amsterdam. Nel 1931 divenne primo violino della Filarmonica di Berlino. Quando i nazisti salirono al potere, Indig fuggì a Parigi dove diresse un quartetto per un po\'. Indig visse ad Amsterdam fino al 1951 e da allora in poi ritornò a Parigi. La data e luogo della sua morte rimangono sconosciute.\n\nNel 1921 o 1922, a causa di disordini a Budapest, il quartetto si trasferisce a Berlino, dove sviluppò un vasto repertorio. Il quartetto, tuttavia, ricevete recensioni contrastanti. Nel 1925 suonarono a Londra dove firmarono un contratto discografico con la Voce del Padrone, per effettuare registrazioni nello Studio B della Voce del Padrone a Hayes e nella Queen\'s Small Hall.Nel maggio del 1927, senza dirlo agli altri, Pogany viaggiò a Cincinnati per vedere il suo amico Fritz Reiner per un posto di lavoro nell\'orchestra sinfonica del luogo. Gli fu offerto il Secondo Violino Principale, ma rifiutò. Gli altri membri del quartetto erano furiosi, perché se avesse lasciato, sarebbe stato molto difficile trovare e provare un sostituto in tempo per la nuova stagione. In conseguenza di ciò Pogany si dimise. Emigrò in America ed entrò nella Cincinnati Symphony Orchestra, insegnando anche presso il Conservatorio di Musica locale. Nel 1929 entrò a far parte della New York Philharmonic Orchestra diretta da Arturo Toscanini in qualità di secondo violino principale. Vi rimase fino al suo pensionamento nel 1958.\n\nL\'uomo consigliato per sostituire Pogany era Josef Roisman (Joe). Roisman nacque il 25 luglio 1900 a Odessa. Iniziò il violino all\'età di sei anni con Pyotr Stolyarsky, che è stato anche il primo maestro di David Oistrakh e Nathan Milstein. Dopo la tragica morte prematura del padre di Josef, una ricca donna di Odessa rese possibile per Josef, la sorella e la madre il trasferimento a Berlino, in modo che Josef potesse studiare con Alexander Fiedemann. Là Josef fece amicizia con Boris Kroyt, un altro originario di Odessa, che studiava con Fiedemann. Allo scoppio della prima guerra mondiale la famiglia ritornò a Odessa dove Josef continuò i suoi studi con Naoum Blinder, un altro musicista di Odessa, che era appena tornato da Inghilterra.Dopo la rivoluzione russa, Roisman fu cooptato per suonare nelle fattorie nelle fabbriche. Riuscì a fuggire nel 1923 mentre lavorava nei pressi della Polonia. Si spostò a Praga, poi a Berlino. A Berlino Roisman si incontrò con Kroyt, che trovò lavoro per lui in un\'orchestra di un cinema. Fu durante questo periodo che venne l\'offerta del quartetto. Roisman era a proprio agio e sicuro nell\'orchestra, ma il suo primo amore era la musica da camera. Alla fine la moglie Polo lo convinse ad assumersi il rischio finanziario ed affrontare il sacrificio.Immediatamente cominciò a pentirsene. Hauser e figlio erano costantemente in discussione e sollecitavano il suo voto. Inoltre, Roisman aveva i suoi problemi, in particolare, Hauser e Ipolyi, non riuscivano a suonare lo "Spiccato" (una forma particolare di Staccato, in tedesco Springbogen), in modo che il quartetto era costretto a non usarlo. Il resto del quartetto aveva dovuto diventare esperto nell\'usare un\'altra tecnica (in tedesco Spitzen) per aggirare l\'incapacità di Hauser e Ipolyi di eseguire lo spiccato. Per Roisman fu un duro lavoro recuperare. Dovette trascorrere molte ore a fare pratica e non era soddisfatto del risultato. In Germania, il quartetto era chiamato das Spitzenquartett (non un complimento), perché aveva sostituito lo "Springbogen" con lo "Spitzen" .Infine nel 1930-1931 Son non sopportava più le litigate e diede le dimissioni. Emigrò in Palestina e suonò in concerti lì e all\'estero. Poco prima della seconda guerra mondiale prese la sfortunata decisione di tornare a Rotterdam. Dopo che i tedeschi invasero i Paesi Bassi, lui e sua moglie Marianne furono arrestati ad Amsterdam ed è morto nel 1942 nel campo di concentramento di Auschwitz-Monowitz.\n\nIl nuovo violoncellista fu originariamente chiamato Mojzesz Sznejder, poi reso in tedesco come \'Mischa Schneider\'. Nato nel 1904 a Vilna, Russia (ora Vilnius, Lituania), Schneider aveva avuto una educazione difficile. La famiglia aveva pochi soldi e suo padre era un tiranno. Mischa spesso si trovò a difendere suo fratello minore Sasha contro il padre. Nel 1920, all\'età di 16 anni, Mischa lasciò la casa per studiare a Lipsia sotto Julius Klengel, insegnante del suo maestro. Fra i suoi compagni c\'erano Emanuel Feuermann, Gregor Piatigorsky e Benar Heifetz. Dopo la laurea si trasferì a Francoforte, dove ha insegnato presso il Conservatorio Hoch. Si accorse che soffriva di paura del palcoscenico, quando si suona da soli, un problema che non esiste quando si suona in un quartetto. Si unì al Quartetto Prisca, ma si dimise dopo un po\' a causa di uno scontro di personalità con due degli altri membri. Il Quartetto Prisca aveva spesso suonato a Colonia e lì ebbe modo di conoscere i Reifenbergs, la cui figlia Eva aveva sposato Emanuel Feuermann. Fu Frau Reifenberg che introdusse Schneider nel Budapest Quartet.\n\nIn gennaio e febbraio 1931 il quartetto fece la sua prima tournée negli Stati Uniti. Le recensioni erano abbastanza buone, ma finanziariamente il tour era poco gratificante. Le discussioni sullo Spitzen e su altre questioni continuarono e le relazioni divennero difficili. Poi, nel 1932, Hauser volle suonare in alcuni concerti con Alice Ehlers. Il quartetto rifiutò di permettere questa deviazione dalle regole; ci fu un litigio e Hauser si dimise. Emigrò a Gerusalemme, formò un quartetto e fondò il Conservatorio di Musica Palestina. Hauser aiutò il violinista Bronisław Huberman a soccorrere molti ebrei provenienti dall\'Austria, Cecoslovacchia e Germania ed fu determinante nella fondazione della Palestine Symphony Orchestra. Nel 1940 si trasferì negli Stati Uniti, insegnando prima al Bard College nello Stato di New York del nord e in seguito alla Juilliard School of Music. Hauser tornò in Israele nel 1960, dove morì nel 1978 all\'età di 84 anni.\n\nAvendo perso Hauser, il quartetto aveva bisogno di un nuovo leader. L\'introduzione di una persona sconosciuta come leader è un passo rischioso per un quartetto. A causa delle relazioni che si stabiliscono e il \'livello di comodità\', un passaggio dal secondo violino al primo è più sicuro. Per questo motivo, Roisman si convinse ad effettuare il passaggio dal secondo al primo.Il nuovo secondo era il fratello minore di Mischa Schneider Alexander (Sasha), nato Abram Sznejder. A 13 anni Abram era quasi morto di tetano dopo un taglio al ginocchio in un incidente. Il tetano distorse le sue articolazioni e il recupero fu lungo e doloroso. Sasha lasciò Vilna nel 1924 e raggiunse il fratello a Francoforte, garantendosi una borsa di studio per violino con Adolf Rebner, il preside, insegnante di violino al Conservatorio Hoch. Nel 1927, Alexander divenne il leader (primo violino) di un\'orchestra di Saarbrücken. Nel 1929 fu nominato capo della Norddeutscher Rundfunk Orchestra di Amburgo. Nel 1932, perse il lavoro a seguito della campagna nazista contro gli ebrei in atto. Era giunto il momento di lasciare la Germania e il posto vacante di Budapest era arrivato proprio al momento giusto.Dopo l\'arrivo di Sasha il livello delle prestazioni del Quartetto migliorò subito e il gruppo cominciò ad attirare un pubblico più ampio. Ne seguì una tournée di successo negli Stati Uniti, Indie orientali olandesi, Australia e Nuova Zelanda e in cambio del loro trasferimento in Australia, l\'Australian Broadcasting Corporation garantì al quartetto sei mesi di lavoro all\'anno. Eppure le relazioni personali all\'interno del Quartetto erano cattive. Sasha fu messo spesso in minoranza; odiava questo, ma Ipolyi era solitamente in grado di calmarlo. Ipolyi stesso aveva problemi mentali. Mischa aveva divorziato dalla moglie e si era risposato. Il gruppo non guadagnava ancora abbastanza.Nel 1934 gli ebrei erano stati espulsi da tutte le orchestre tedesche, ma il Quartetto, come visitatore \'Ungherese\', era stato risparmiato. Tuttavia una sera ricevettero minacce da un gruppo nazista. Durante la notte cambiarono sede da Berlino a Parigi e non tornarono mai più in Germania. Fecero una tournée in Europa e Stati Uniti, ma vivendo sempre in alberghi a basso costo e mangiando in posti a buon mercato.\n\nIpolyi divenne un membro isolato del quartetto, l\'unico ungherese fra tre russi. Era anche l\'unico musicista Spitzen rimasto, vecchio nello stile ed anche sull\'orlo di una crisi di nervi. Nel 1936 gli altri lo convinsero a dimettersi. Si stabilì in Norvegia e durante l\'occupazione tedesca fu arrestato, ma fu poi liberato grazie all\'intervento del conte Bernadotte, capo della Croce Rossa Internazionale. Fuggì in Svezia, ma tornò in Norvegia dopo la guerra. Ipolyi divenne cittadino norvegese, formò un quartetto a Bergen e divenne professore. Mischa Schneider fece in modo che Ipolyi ricevesse le royalties dovutegli e morì nel 1955.\n\nEra urgente trovare un nuovo violista per sostituire Ipolyi. L\'Australian Broadcast Corporation aveva ingaggiato il Quartetto per una tournée di venti settimane con inizio a maggio 1937, con quattro spettacoli alla settimana e l\'opzione di altri dieci settimane in Nuova Zelanda. Nonostante gli impegni regolari in Europa e in America, avevano bisogno di soldi. Roisman aveva quasi assunto Edgar Ortenberg, che aveva conosciuto quando erano entrambi bambini a Odessa e poi di nuovo a Berlino nel 1926, ma la moglie di Ortenberg voleva che aderisse come violinista. Roisman in seguito cercò di trovare a Berlino il suo amico di gioventù Boris Kroyt. Fino a quando i nazisti non divennero onnipotenti, Kroyt aveva vissuto bene, ma i nazisti impedirono di lavorare a tutti gli ebrei, se non in gruppi ebraici. Aveva una moglie e figli da mantenere ed erano tutti in pericolo. L\'offerta di Budapest arrivò nel momento ideale. Era un musicista così naturale che poteva allontanarsi senza fare molta pratica. Si presero del tempo per abituarsi gli uni agli altri, ma alla fine raggiunsero un livello tecnico molto alto.Nel mese di novembre 1936, raggiunsero New York e i critici rimasero impressionati come mai prima, confrontandoli con Toscanini e Schnabel. I concerti erano molto frequentati. Nella primavera del 1937 si recarono in Australia, Nuova Zelanda e nelle Indie orientali olandesi con risultati altrettanto buoni. Quando venne il momento di tornare in Europa, presero in considerazione di stabilirsi in Australia e fecero una votazione su questo argomento. La guerra civile spagnola aveva chiuso molti luoghi in Italia e in Spagna. Gli Schneiders votarono per andarci, mentre gli altri due votarono per proseguire. Secondo il regolamento un pareggio significa "nessun cambiamento", così proseguirono. Dopo aver suonato in Francia e Gran Bretagna, raggiunsero di nuovo New York nel marzo 1938.Tutti i concerti degli Stati Uniti venivano contrattati da Annie Friedberg da New York. Questo continuò per tutto il loro periodo negli Stati Uniti, cominciando con un piccolo compenso, per finire con ottimi ritorni economici sia per loro che per lei.Avevano fatto cinque tournée negli Stati Uniti senza alcuna difficoltà, ma questa volta vennero respinti. I loro passaporti Nansen non erano abbastanza buoni, a quanto pare. Furono portati via ignominiosamente alla Ellis Island su una chiatta di carbone. Ci vollero frenetiche trattative, muovendo qualche filo, da parte della Friedberg che coinvolse il sindaco La Guardia, per farli uscire appena in tempo per il loro primo concerto. Non erano nelle migliori condizioni per un concerto e pensarono che non era troppo buono. Invece ottenunnero una recensione entusiastica da The New York Times. Fu questo, alla fine, che aprì loro la porta del successo vero e proprio negli Stati Uniti. Improvvisamente tutti i critici lodavano il loro come mai prima d\'ora e il pubblico e prenotazioni dilagarono. Considerando quello che era appena accaduto in Europa, la rottura era avvenuta appena in tempo.\nIl 25 aprile 1938 registrarono il Quintetto per clarinetto di Mozart con Benny Goodman per l\'etichetta Victor. Questa registrazione vendette bene anche se Goodman si pentì di non aver fatto prima uno spettacolo dal vivo. Lui e il quartetto fecero solo tre concerti insieme: ottobre e novembre 1938 e agosto 1941. Ogni volta i critici sentirono che il risultato era accurato, ma mancava la sensazione di ispirazione che si aspettavano.Nel 1939 ancora una volta ebbero buoni risultati a Parigi, Amsterdam, Bruxelles, in Norvegia e Gran Bretagna, ma non in Spagna e in Italia, dove le persone erano più interessate alle questioni politiche. Dagli Stati Uniti ricevettero una richiesta di suonare cinque strumenti ad arco Stradivari, che richiedevano un uso regolare, alla Biblioteca del Congresso di Washington. Questi strumenti erano stati acquistati e donati da Gertrude Clarke Whittall, che ebbe un\'influenza continuativa. La sala da concerto sul terreno della Biblioteca era stata appena costruita (nel 1925), con i soldi donati da Elizabeth Sprague Coolidge, un importante benefattore della musica da camera e di diversi festival musicali. In quel periodo sentirono che essa avrebbe potuto tenerli lontani dai rapporti esistenti in Europa.\n\nIn estate tornarono di nuovo a trascorrere tre mesi negli Stati Uniti presso il Mills College a Oakland in California, un posto dove potevano rilassarsi. Il Pro Arte Quartet normalmente faceva così, ma quest\'anno avevano preferito stare in Belgio. Non tornarono mai più e il quartetto Budapest andò a Mills per i successivi quindici anni. Quel primo anno a Mills appresero che in Europa era iniziata la seconda guerra mondiale e i loro contratti europei erano ormai annullati. L\'offerta della Biblioteca del Congresso ora sembrava più attraente e accettarono. I loro concerti presso la biblioteca continuarono per molti anni e crearono un rapporto importante per loro.Fino dal 1925 avevano fatto registrazioni per His Master\'s Voice, prima alla Beethoven Saal di Berlino, poi all\'Abbey Road Studio di Londra e dal 1938 a Camden, nel New Jersey per la RCA Victor, la controllata statunitense di HMV. Il contratto HMV era valido fino al giugno 1940. Non pagava bene e la RCA aveva una buona scorta di registrazioni non ancora pubblicate. La RCA non desiderava fare altre registrazioni nel 1939. Il quartetto trovò difficoltà a convincere la RCA a dare loro la quantità di lavoro che volevano o per pagarli così come loro nuova reputazione avrebbe potuto giustificare. Inoltre RCA non abeva fretta di prolungare il contratto esistente. Il quartetto ritenne che con la loro crescente reputazione negli Stati Uniti avrebbero potuto fare meglio con la Columbia Recording Company. Alla Columbia furono felici di firmare un accordo e fare tante più registrazioni quante il quartetto voleva, tanto più che non avevano nulla di loro registrato. L\'operazione fu fatta e mantenuta segreta il più a lungo possibile. Quando finalmente lo vennero a sapere la RCA scrisse: "Siamo stupefatti... decisamente vicino a una violazione della fiducia". Essi avrebbero dovuto capire che non avevano il diritto di essere gli unici negoziatori in un affare. Nel corso di 35 anni il quartetto ha registrato 89 pezzi, alcuni dei quali più volte. Per molti anni fu il principale fornitore di musica classica della Columbia, una perdita assoluta per la RCA.\n\nAll\'inizio ci furono difficoltà. In primo luogo l\'American Federation of Musicians, proteggendo i posti di lavoro americani, chiese che qualcuno pagasse due membri come "appoggi" durante le registrazioni. Il quartetto e la Columbia discussero su chi di essi dovesse pagare. Dopo che questo fi risolto l\'AFM trascinò la Columbia in una disputa che durò fino al febbraio del 1945. Inoltre, dopo che la guerra era stata dichiarata, il governo degli Stati Uniti razionò il materiale per fare i dischi. Anche così, tra il 1941 e il 1946, il quartetto guadagnò $ 60.000 dalla Columbia in diritti d\'autore. Ricavarono anche $ 16.000 dalla HMV.\n\nSasha sentiva di poterlo fare e aveva bisogno di lavorare al di fuori del quartetto. Come secondo violino non ottenne le stesse imprese sfidanti che aveva sostenuto come leader. Dopo averci pensato un sacco, finalmente prese una decisione e lo disse agli altri, il 26 novembre 1943. Aveva ancora solo trentacinque anni, avendone trascorsi undici nel quartetto e aveva bisogno di espandere la sua gamma di esperienze. Il 1º gennaio 1944 il quartetto scelse il nuovo secondo violino. Era Edgar Ortenberg, l\'uomo che per poco non era stato il loro violista.Come Joe e Boris, Edgar era cresciuto a Odessa. Fino alla rivoluzione russa suo padre era stato il direttore di una banca. In seguito furono molto a corto di denaro. Nel 1921 vinse la medaglia d\'oro al Conservatorio di Odessa e fu immediatamente assunto per insegnare lì. Nel 1924 si trasferì a Berlino per migliorare, proprio come avevano fatto Joe, gli Schneider e Boris. Dopo aver raggiunto Berlino ottenne subito una borsa di studio presso la Hochschule für Musik. Cambiò il suo nome da Eleazer a Edgar. Creò un quartetto e andò tournée in Europa fino al 1933, quando i nazisti li saccheggiarono e si trasferì rapidamente a Parigi. Là il Conservatorio russo formò un quartetto ed ebbero un certo successo in Europa. Quando ci fu la minaccia della guerra si arruolò nell\'esercito francese. Nel mese di aprile 1940 lasciò a causa di una malattia. Lui e sua moglie lasciarono Parigi poco prima che arrivassero i tedeschi. Andarono in Portogallo e riuscirono a prendere l\'ultima nave spagnola per andare negli Stati Uniti. Dopo aver lottato a New York per qualche tempo, ricevette una seconda offerta dal Budapest Quartet nel dicembre del 1943 e questa volta accettò.Edgar in generale fu considerato un ottimo sostituto per Sasha. Tuttavia alcuni critici e tutti i musicisti avevano la sensazione che avrebbe dovuto suonare con più forza. D\'altra parte, egli sentiva che il loro suono era un po\' ruvido. Volle anche passare più tempo a provare dal momento che aveva bisogno di abituarsi ai loro metodi e abituarsi al loro vasto repertorio. Gli altri, in particolare Boris, non erano così desiderosi di provare. Ci vollero due anni ad Edgar per sentirsi pienamente a casa. Tuttavia gli altri sentivano che Edgar avrebbe dovuto fare pratica privatamente e stava diventando chiaramente nervoso. Di nuovo i critici sentirono che il quartetto era meraviglioso, ma non tanto buono come prima. Ortenberg era esausto dai continui viaggi. Verso la fine del 1948 gli altri gli dissero che volevano un diverso secondo violino. Non appena fu reso noto, Ortenberg fu invaso da altre offerte. Ortenberg fece il suo ultimo spettacolo con il quartetto il 10 marzo 1949 presso la Cornell University. Si unì alla Settlement Music School di Filadelfia e vi rimase fino al pensionamento nel 1984. Ha insegnato anche presso la Temple University dal 1953 al 1978.\n\nIl nuovo secondo violino era Jac Gorodetzky. Nacque a Odessa, ma la famiglia si trasferì a Londra quando aveva solo un anno, per evitare un pogrom. Si trasferirono negli Stati Uniti prima della guerra, stabilendosi a Filadelfia. Era benvisto come uno studente e si assicurò buone posizioni in orchestre e quartetti. Tuttavia il suo modo di suonare, come Ortenberg, era un po\' troppo sommesso. Fu benvisto alle audizioni del Budapest ed aveva circa 35 anni.Nel 1950 il quartetto andò in Europa per la prima volta dopo la guerra. Convennero di non andare in Germania, soprattutto perché Schneider aveva perso la madre e la sorella ad Auschwitz. Questa tournée, unita alla continua richiesta negli Stati Uniti provocò un pesante stress a Gorodetzky. Sviluppò una paura da palcoscenico, richiedendo a volte impegnative prove extra di opere che avevano già suonato.Poi, nel settembre 1952 suonarono in Giappone. Furono il primo quartetto ad arrivare lì dopo la guerra. L\'intera stagione fu venduta in due ore. C\'erano 3000 persone presenti al primo concerto. C\'era del personale pronto a provvedere ad ogni loro necessità ed c\'erano auto per portarli dappertutto. Una notte sentirono il bisogno di fare qualche esercizio a Okayama. Stavano camminando su una strada stretta, quando Joe cadde in un fosso di nove piedi e si ruppe il polso sinistro. Lo misero all\'Ospedale militare degli Stati Uniti a Tokyo. Al ritorno negli Stati Uniti fu detto loro che il polso era stato aggiustato malamente e doveva essere rotto e ingessato nuovamente. I Concerti diventarono trii e quartetti per pianoforte. Dopo mesi di duro lavoro Joe riprese i suoi doveri a Portland, Oregon il 12 gennaio 1953.Nel 1954 fecero un\'altra tournée giapponese con ancora maggiore successo, ma Jac era sempre più a disagio. Nel mese di febbraio disse agli altri che voleva andarsene. Speravano che parlasse così perché era fuori di sé. Nessuno si rese conto di quanto stesse male. Infine nel mese di novembre 1955 si uccise in un piccolo hotel di Washington. Gli altri musicisti si sentivano terribilmente. Suonarono concerti di beneficenza per la sua famiglia presso la Settlement Music School. Più tardi Mischa lasciò loro la maggior parte della sua musica e alla sua morte Joe lasciò loro la maggior parte del suo denaro.\n\nJoe rifiutò di accettare un altro nuovo secondo violino, ma fortunatamente riuscirono a convincere Sasha a tornare. Contro la loro regola precedente gli permisero di passare un po\' di tempo a lavorare in modo indipendente perché avevano bisogno di lui e non avevano voglia di prendere così tanti impegni come prima. Non appena tornò tutti si sentirono più felici per molti anni e la critica era esagerata nel lodarli.Nei dieci anni in cui era stato lontano Sasha era stato molto occupato. Aveva rifiutato offerte di guidare la Pro Arte e i Quartetti Paganini. Fece una tournée con Ralph Kirkpatrick. Suonò le suite per violoncello solo di Bach. Suonò i trii. Studiò con Pablo Casals a Prades e convinse Casals ad iniziare i festival di Prades, Porto Rico, Israele e Marlboro nel Vermont. Diede vita ad un quartetto per registrare tutti gli 83 quartetti di Haydn per la società Haydn, anche se terminarono i soldi prima che fosse finito. Convinse la signora Coolidge a finanziare la fornitura di concerti all\'aperto gratuiti a Greenwich Village. Aveva suonato con il Budapest quando Ortenberg o Gorodetzky non stavano bene.\n\nMentre si avvicinava il 1960 il quartetto fu molto felice. È stato il quartetto più popolare e famoso, con 55 album registrati pubblicati dalla Columbia e due milioni di copie vendute, suonando in molti luoghi famosi e festival. Tuttavia nel 1960 Joe iniziò ad avere periodi di scarsa intonazione apparentemente a causa di un attacco di cuore delicato alla fine del 1960. Solo allora disse agli altri che, già nel 1939 gli era stato detto che la sua pressione sanguigna era alta. Di tanto in tanto aveva avuto problemi di intonazione, ma nel 1960 peggiorò.Nel marzo 1962 hanno suonato il loro ultimo concerto nella Biblioteca del Congresso. C\'erano stati un certo numero di problemi, tra questi l\'intonazione di Joe era stato il peggiore. I critici ed il pubblico si erano lamentati e la signora Coolidge si era lamentata. Furono sostituiti dal giovane Quartetto Juilliard. Poi, in autunno erano in Europa, quando all\'improvviso Joe ha subito un\'ernia del disco. Ripresero a suonare nei primi mesi del 1963 e tornarono in Australia dopo ventisei anni di lontananza. L\'energia di Joe era in declino e ridussero di anno in anno il numero concerti.\n\nNel 1955 Sasha aveva aderito alla Marlboro Music School and Festival del Marlboro College nel Vermont meridionale. Era una scuola, un festival di musica e un ritiro estivo. Era un ciclone. Spinse i giovani musicisti a aumentare il loro talento. Con il tempo portò gli altri musicisti del Budapest e resero il posto un terreno fecondo per una generazione di musicisti da camera. La scuola era stata fondata nel 1950 dal violinista Adolf Busch e dal flautista Marcel Moyse e le loro famiglie. Busch morì prima che Sasha arrivasse, ma il suo figliastro Rudolf Serkin era ancora molto attivo e i due divennero amici fedeli. Sasha trascorse le successive venti estati lì.Nel 1962 Sasha convinse Mischa a venire anch\'egli e l\'anno successivo ci andò l\'intero quartetto. Ci andarono molti musicisti esperti. Molti musicisti più giovani di talento vennero e raggiunsero standard elevati. Gli studenti trovavano Sasha molto deciso e il suo modo era un po\' duro con quelli che erano nervosi o che non cercavano di raggiungere gli standard più alti. Per i migliori però lui era perfetto. Mischa e Boris erano più gemtili. Erano molto disposti a provare le nuove idee dei loro studenti e ogni aspetto era ispirato dall\'entusiasmo dell\'altro.Sasha convinse Michael Tree, Arnold Steinhardt, John Dalley e David Soyer a formare un quartetto - una sfida formidabile per qualsiasi musicista e Boris suggerì il nome Guarneri. Passarono un sacco di tempo insieme a Marlboro ed il Guarneri Quartet può essere considerato come l\'erede musicale del Budapest Quartet. Sasha ha dato il quartetto un consiglio, "Ogni volta che suonate un trio d\'archi e quartetti per pianoforte, fatevi una regola che suoni il secondo violino e non il primo .... Se suonate solo il secondo violino, diventerete un po\' ammuffiti per altre cose". Disse che, dopo aver lasciato il Budapest, ci mide tre anni per tornare in buone condizioni di interpretazione. L\'Emerson String Quartet ha una visione simile e lo risolve alternando le sedie tra i due violini.\nNegli anni successivi il Budapest suonò un minor numero di concerti e si videro l\'un l\'altro solo per i concerti. Il pubblico riempiva le sale ed erano molto ammirati, ma non facevano pratica molto spesso, né singolarmente né insieme. Ci furono errori in alcuni particolari, ma l\'effetto generale era ancora buono. Sasha sentiva di voler condividere quello che stava ancora imparando, ma Joe voleva rimanere com\'era.\n\nNel gennaio 1965 il gruppo trascorse dodici giorni registrando il quartetto "American" di Dvořák e il Quartetto di Smetana "From My Life". Joe ebbe grossi problemi di intonazione e Mischa problemi con la schiena. Una registrazione di Dvořák fu assemblato insieme da più riprese e pubblicato, ma i giocatori rifiutarono di accettare un simile giunzione dello Smetana. Poi Mischa e Boris e il Guarneri eseguirono e registrarono "Souvenir de Florence" di Tchaikovsky, con successo. Improvvisamente Mischa dovette sottoporsi a un intervento chirurgico alla schiena, che lo aveva tormentato fin dal 1930. L\'operazione non riuscì e anche un secondo tentativo fallì. Misha non ha mai suonato di nuovo, ma ha insegnato molto, tra l\'altro per 25 estati al Marlboro Music Festival. Mischa morì il 3 ottobre 1985 a Buffalo, New York.Nel 1977 Sasha improvvisamente lasciò Marlboro. Non spiegò mai il perché ma lui e Serkin rimasero amici. Nel 1969 Boris morì di cancro. Nel 1974 Joe ha avuto un attacco cardiaco ed è morto. Nel 1993 Sasha ebbe un\'insufficienza cardiaca ed morì dopo aver suonato quasi fino alla fine.Il Budapest String Quartet ha avuto un enorme influenza sulla musica da camera negli Stati Uniti e a livello internazionale. Quando iniziarono alla fine del 1930 fu difficile ottenere un grande pubblico. I concerti a Washington e New York, le trasmissioni radiofoniche e le numerose registrazioni gradualmente aumentarono il numero degli spettatori, li ha resi famosi e ricchi ed ha stabilito un alto standard che influì su molti musicisti successivi.Jascha Heifetz una volta fu citato per questa frase: "Un russo è un anarchico. Due russi sono una partita a scacchi. Tre russi sono una rivoluzione. Quattro russi sono il Budapest String Quartet".\n\nLe seguenti liste iniziano dal 1932; questo è l\'anno in cui Josef Roisman divenne il leader del quartetto come 1° Violino, in sostituzione di Emil Hauser e Alexander Schneider si unì al quartetto come 2° violino. Così, con l\'eccezione di István Ipolyi, che rimase fino al 1936, il quartetto aveva quasi completato la sua trasformazione al suo relativamente stabile cast di quattro russi e raggiunse la sua reputazione di lunga durata.\nSebbene la maggior parte delle voci nei seguenti elenchi siano prese sia da LP e CD reali e dalle loro note di copertina o stampa affidabile, o fonti online, le liste sono completate da una discografia preparata dalla Sony Classical, a quanto pare per il loro uso personale interno, per identificare i numeri nel magazzino. Tuttavia questa discografia Sony contiene una serie di errori nell\'identificazione delle date di registrazione, l\'organico e in alcuni casi anche composizioni e compositori. Tutte le informazioni di questa discografia Sony, come illustrato di seguito, che non è stato possibile verificare e confrontare da un\'altra fonte, sono precedute da un asterisco [*] come forse discutibile.\nLe parentesi quadre indicano le iniziali del violista, o del secondo violino; ad esempio, [Va = II] indica István Ipolyi come violista. Diverse date di registrazione sono o non specificate o sconosciute. Tutte le registrazioni precedenti sono state pubblicate come incisione su gommalacca 78 giri, molte in seguito ristampate come dischi in vinile e, successivamente, in formato CD. La prima pubblicazione delle ultime registrazioni fu direttamente in formato LP. Tutte le registrazioni sono monofoniche se non specificate come stereo.\n\n1° Violino: Josef Roisman; 2° Violino: Alexander Schneider; Viola: István Ipolyi o Boris Kroyt; Violoncello: Mischa Schneider\n\nBartók: Quartetto n. 2 in La minore, Op. 17 (Reg. 25/4/1936 [*Va=II]; *LP riedizione Odyssey Y4-34643).\nBeethoven: Quartetto n. 2 in Sol maggiore, Op. 18 n. 2 (Reg. 1/6/1938 [*Va=BK]; *LP riedizione Odyssey Y3-35240).\nBeethoven: Quartetto n. 3 in Re maggiore, Op. 18 n. 3 (Reg. 30/4/1935 [*Va=II]; *LP riedizione Odyssey Y3-35240).\nBeethoven: Quartetto n. 8 in Mi minore, Op. 59 \'Rasumovsky\' n. 2 (Reg. 24/4/1935 [Va=II]; *LP riedizione Odyssey Y4-34643, CD riedizione *Sony SBK-47665, *Portrait SBK-46545, Biddulph 80222).\nBeethoven: Quartetto n. 13 in Si bemolle maggiore, Op. 130 (Reg. 10/8/1933 & 4/4/1934 (or 4/5?/1934) [Va=II]; *LP riedizione Odyssey Y4-34643, CD riedizione Biddulph 80222).\nBrahms: Quartetto n. 2 in La minore, Op. 51 n. 2 (Reg. 30/4-1/5/1935 [Va=II]; CD riedizione Biddulph LAB-120/1).\nBrahms: Quartetto n. 3 in Si bemolle maggiore Op. 67 (Reg. 15,17,18/11/1933 (or same dates in 1932?) [Va=II]; *LP riedizione Odyssey Y4-34643, CD riedizione *Portrait MPK-45553, Biddulph LAB-120/1).\nBrahms: Quintetto d\'archi n. 1 in Fa maggiore, Op. 88, con Alfred Hobday (Reg. 8/2/1937 [Va=BK]; CD riedizione Biddulph LAB-120/1).\nBrahms: Quintetto d\'archi n. 2 in Sol maggiore, Op. 111, con Hans Mahlke (Reg. 15,17,18/11/1932 [Va=II]; CD riedizione Biddulph LAB-120/1).\nBrahms: String Sextet in Sol maggiore, Op. 36, con Alfred Hobday & Anthony Pini (Reg. 8/2/1937 [Va=BK]; CD riedizione Biddulph LAB-120/1).\nMendelssohn: Quartetto n. 1 in Mi bem. magg, Op. 12 (Reg. 29/4/1935 [Va=II]; *LP riedizione Odyssey Y4-34643).\nMozart: Quartetto n. 19 in Do maggiore, K 465 \'Dissonance\' (Reg. 14/11/1932 [Va=II]; *LP riedizione Odyssey Y3-33324, *Odyssey Y3-35240, CD riedizione EMI CDH-63697).\nMozart: Quartetto n. 20 in Re maggiore, K 499 \'Hoffmeister\' (Reg. 5/4/1934 [Va=II]; *LP riedizione Odyssey Y4-34643, CD riedizione EMI CDH-63697).\nMozart: Quartetto n. 23 in Fa maggiore, K 590 (Reg. 29/4/1935 [*Va=II]; *LP riedizione Odyssey Y3-35240).\nMozart: Quintetto di clarinetti in La maggiore, K 581 con Benny Goodman (Reg. 25/4/1938 [Va=BK]; CD riedizione EMI CDH-63697; Naxos Hist 8.111238).\nSchubert: Quartettsatz in Do minore, D 703 (DB 2221) (Reg. 4/4/1934 [*Va=II]; *LP riedizione Odyssey Y4-34643)\nSibelius: Quartetto in Re minore, Op. 56 Voces Intimae (Reg. 8/8/1933 [Va=II] Sibelius Society Volume 3).\nWolf: Italian Serenade in Sol maggiore (1887) (Reg. 18/11/1932 [*Va=II]; *LP riedizione Odyssey Y4-34643).\n\n1° Violino: Josef Roisman; 2° Violino: Alexander Schneider, Edgar Ortenberg, o Jac Gorodetzky; Viola: Boris Kroyt; Violoncello: Mischa Schneider\n\nBeethoven: Quartetto n. 1 in Fa maggiore, Op. 18 n. 1:reg. 9/9/1940 [2V=AS]; CD riedizione Sony MH2K-62870.\nreg. 5-9/5/1952 [2V=JG]; CD riedizione CBS MP2K-52531, United Archives NUA01.\nstereo reg. 1958 [2V=AS]; LP Col M3S-606; CD riedizione Sony 88697776782.Beethoven: Quartetto n. 2 in Sol maggiore, Op. 18 n. 2:reg. 1938: vedi HMV/Victor, sotto.\nreg. 5-9/5/1952 [2V=JG]; CD riedizione CBS MP2K-52531, United Archives NUA01.\nstereo reg. 1958 [2V=AS]; LP Col M3S-606; CD riedizione Sony 88697776782.Beethoven: Quartetto n. 3 in Re maggiore, Op. 18 n. 3:reg. 1935: vedi HMV/Victor, sotto.\nreg. 29/11/1951 [2V=JG]; CD riedizione CBS MP2K-52531, United Archives NUA01.\nstereo reg. 1958 [2V=AS]; LP Col M3S-606; CD riedizione Sony 88697776782.Beethoven: Quartetto n. 4 in Do minore, Op. 18 n. 4:reg. 9-10/1/1941 [2V=AS]; CD riedizione Sony MH2K-62870.\nreg. 2/12/1951 [2V=JG]; CD riedizione CBS MP2K-52531, United Archives NUA01.\nstereo reg. 1958 [2V=AS]; LP Col M3S-606; CD riedizione Sony 88697776782.Beethoven: Quartetto n. 5 in La maggiore, Op. 18 n. 5:(Minuet only): reg. 15/9/1941 [2V=AS]; CD riedizione Sony MH2K-62873.\nreg. 2/5/1951 [2V=JG]; CD riedizione CBS MP2K-52531, United Archives NUA01.\n(stereo reg. 1958 [2V=AS]; LP Col M3S-606); CD riedizione Sony 88697776782.Beethoven: Quartetto n. 6 in Si bemolle maggiore, Op. 18 n. 6reg. 2/4/1945 [2V=EO]; CD riedizione Sony MH2K-62870.\nreg. 26/11/1951 [2V=JG]; CD riedizione CBS MP2K-52531, United Archives NUA01.\nstereo reg. 1958 [2V=AS]; LP Col M3S-606; CD riedizione Sony 88697776782.Beethoven: Quartetto n. 7 in Fa maggiore, Op. 59 \'Rasumovsky\' n. 1:reg. 1930s: vedi HMV/Victor, sotto.\nreg. 5-9/5/52 [2V=JG]; *LP riedizione Odyssey Y3-33316; CD riedizione United Archives NUA01.\nstereo reg. 17-19/11/1959 [2V=AS]; CD riedizione Sony SBK-46545, Sony 88697776782.Beethoven: Quartetto n. 8 in Mi minore, Op. 59 \'Rasumovsky\' n. 2:reg. 1935: vedi HMV/Victor, sotto.\nreg. ?/5/1951 [2V=JG]; *LP riedizione Odyssey Y3-33316; CD riedizione United Archives NUA01.\nstereo reg. 17-19/11/1959 [2V=AS]; CD riedizione Sony SBK-46545, Sony 88697776782.Beethoven: Quartetto n. 9 in Do maggiore, Op. 59 \'Rasumovsky\' n. 3:reg. 15/9/1941 [2V=AS]; CD riedizione Sony MH2K-62870, *Sony SBK-47665.\nreg. 28/11/1951 [2V=JG]; *LP riedizione Odyssey Y3-33316; CD riedizione *Sony MPK-45551, United Archives NUA01.\nstereo reg. 16/5/1960 [2V=AS]; CD riedizione Sony SBK-47665, Sony 88697776782.Beethoven: Quartetto n. 10 in Mi bem. maggiore, Op. 74 \'Harp\':*reg. betw 1940-44 [*2V=AS]; CD riedizione *Sony SBK-47665.\nreg. ?/5/1951 [2V=JG]; *LP riedizione Odyssey Y3-33316, *Odyssey Y3-35240; CD riedizione *Sony MPK-45551, United Archives NUA01.\nstereo reg. 17/5/1960 [2V=AS]; CD riedizione Sony SBK-47665, CBS MPK-45551, Sony 88697776782.Beethoven: Quartetto n. 11 in Fa minore, Op. 95 \'Serioso\':reg. 5/12/1941 [2V=AS]; CD riedizione Sony MH2K-62870.\nreg. 2/12/1951 [2V=JG]; *LP riedizione Odyssey Y3-33316; CD riedizione United Archives NUA01.\nstereo reg. 1960 [2V=AS]; CD riedizione Sony SBK-46545, CBS MPK-45551, Sony 88697776782.Beethoven: Quartetto n. 12 in Mi bemolle maggiore, Op. 127:reg. 26/2/1942 [2V=AS]; CD riedizione Sony MH2K-62873.\nreg. 5-9/5/1952 [2V=JG]; CD riedizione United Archives NUA01.\nstereo reg. 1961 [2V=AS]; LP Col M5S-677; CD riedizione Sony 88697776782.Beethoven: Quartetto n. 13 in Si bem. magg., Op. 130:reg. 1933-34: vedi HMV/Victor, sotto.\nreg. 3/5/1951 [2V=JG]; CD riedizione United Archives NUA01.\nstereo reg. 1961 [2V=AS]; LP Col M5S-677; CD riedizione Sony 88697776782.Beethoven: Quartetto n. 14 in Do diesis minore, Op. 131:reg. 9/9 & 21/10/1940 [2V=AS]; CD riedizione Sony MH2K-62873.\nreg. 4-6/12/1951 [2V=JG]; CD riedizione United Archives NUA01.\nstereo reg. 1961 [2V=AS]; LP Col M5S-677; CD riedizione Sony 88697776782.Beethoven: Quartetto n. 15 in La minore, Op. 132:reg. 13-14/4/1942 [2V=AS]; CD riedizione Sony MH2K-62873.\nreg. 26-28/5/1952 [2V=JG]; CD riedizione United Archives NUA01.\nstereo reg. 1961 [2V=AS]; LP Col M5S-677; CD riedizione Sony 88697776782.Beethoven: Quartetto n. 16 in Fa maggiore, Op. 135:reg. 9-10/9/1940 [2V=AS]; CD riedizione Sony MH2K-62873.\nreg. 27/11/1951 [2V=JG]; CD riedizione United Archives NUA01.\nstereo reg. 1960 [2V=AS]; LP Col M5S-677; CD riedizione Sony 88697776782.Beethoven: Grosse Fuge in Si bemolle maggiore, Op. 133:reg. 1920s con different personnel\nreg. 7/5/1951 [2V=JG]; CD riedizione United Archives NUA01.\nstereo reg. 2/5/1961 [2V=AS]; CD riedizione Sony SBK-47665, CBS MPK-45551, Sony 88697776782.Beethoven: Quintetto d\'archi in Do maggiore, Op. 29, con Milton Katims: reg. 23/4/1945 [2V=EO]; CD riedizione Sony MH2K-62870.\nBeethoven: Quintetto in Mi bemolle maggiore for piano and winds, Op. 16 (version for piano and string trio), con Mieczysław Horszowski: LP Col MS-6473.\nBrahms: Quartetto n. 1 in Do minore, Op. 51 n. 1: stereo reg. 1963 [2V=AS]; CD riedizione CBS MPK-45686.\nBrahms: Quartetto n. 2 in La minore, Op. 51 n. 2: LP Col M2S-734.\nBrahms: Quartetto n. 3 in Si bemolle maggiore, Op. 67: stereo reg. 1963 [2V=AS]; CD riedizione CBS MPK-45553.\nBrahms: Piano Quartetto n. 2 in La maggiore, Op. 26, con Clifford Curzon: reg. 1952 [2V=JG]; LP Col ML-4630; CD riedizione Naxos Hist 8.110306.\nBrahms: Piano Quintetto in Fa minore, Op. 34:con Clifford Curzon: reg. 1950 [2V=JG]; LP Col ML-4336; CD riedizione Naxos Hist 8.110307.\ncon Rudolf Serkin: stereo reg. 1963 [2V=AS]; CD riedizione CBS MPK-45686.Brahms: Clarinet Quintetto in Si minore, Op. 115, con David Oppenheim: stereo reg. 1959 [2V=AS]; CD riedizione CBS MPK-45553.\nDebussy: Quartetto in Sol minore, Op. 10: CD riedizione CBS MPK-44843.\nDvořák: Quartetto n. 12 in Fa maggiore, Op. 96 \'American\': stereo reg. 1965 [2V=AS]; LP Col M-32792.\nDvořák: Quintetto d\'archi n. 3 in Mi bemolle maggiore, Op. 97, con Walter Trampler: LP Col M-32792.\nDvořák: Piano Quintetto in La maggiore, Op. 81, con Clifford Curzon: reg. 1953 [2V=JG]; LP Col ML-4825; CD riedizione Naxos Hist 8.110307.\nHaydn: Quartetto in Sol maggiore, Op. 76 n. 1: reg. 1954 [2V=JG]; CD riedizione United Archives UAR-003.\nHaydn: Quartetto in Re minore, Op. 76 n. 2 \'Quinten\': reg. 1954 [2V=JG]; CD riedizione United Archives UAR-003.\nHaydn: Quartetto in Do maggiore, Op. 76 n. 3 \'Emperor\': reg. 1954 [2V=JG]; CD riedizione United Archives UAR-003.\nHaydn: Quartetto in Si bemolle maggiore, Op. 76 n. 4 \'Sunrise\': reg. 1954 [2V=JG]; CD riedizione United Archives UAR-003.\nHaydn: Quartetto in Re maggiore, Op. 76 n. 5: reg. 1954 [2V=JG]; CD riedizione United Archives UAR-003.\nHaydn: Quartetto in Mi bemolle maggiore, Op. 76 n. 6: reg. 1954 [2V=JG]; CD riedizione United Archives UAR-003.\nMozart: Quartetto n. 14 in Sol maggiore, K 387: reg. 1953 [2V=JG]; CD riedizione Sony SM2K-47219.\nMozart: Quartetto n. 15 in Re minore, K 421: reg. 1953 [2V=JG]; CD riedizione Sony SM2K-47219.\nMozart: Quartetto n. 16 in E bemolle maggiore, K 428: reg. 1950 [2V=JG]; CD riedizione Sony SM2K-47219.\nMozart: Quartetto n. 17 in Si bemolle maggiore, K 458 \'Hunting\': reg. 1953 [2V=JG]; CD riedizione Sony SM2K-47219.\nMozart: Quartetto n. 18 in La maggiore, K 464: reg. 1953 [2V=JG]; CD riedizione Sony SM2K-47219.\nMozart: Quartetto n. 19 in Do maggiore, K 465 \'Dissonant\': reg. 1953 [2V=JG]; CD riedizione Sony SM2K-47219.\nMozart: Quintetto d\'archi n. 1 in Si bemolle maggiore, K 174:con Walter Trampler: reg. 1956 [2V=AS]; CD riedizione Sony SM3K-46527.\ncon Walter Trampler: stereo reg. 1965-1966 [2V=AS]; LP Col D3S-747; CD riedizione Sony CSCR 8346.Mozart: Quintetto d\'archi n. 2 in Do minore, K 406:con Milton Katims: reg. 1946 [2V=EO]; CD riedizione Sony SM3K-46527.\ncon Walter Trampler: stereo reg. 1965-1966 [2V=AS]; LP Col D3S-747; CD riedizione Sony CSCR 8346.Mozart: Quintetto d\'archi n. 3 in Do maggiore, K 515:con Milton Katims: reg. 1945 [2V=EO]; CD riedizione Sony SM3K-46527.\ncon Walter Trampler: stereo reg. 1965-1966 [2V=AS]; LP Col D3S-747; CD riedizione Sony CSCR 8346.Mozart: Quintetto d\'archi n. 4 in Sol minore, K 516:con Milton Katims: reg. 1941 [2V=AS]; CD riedizione Sony SM3K-46527.\ncon Walter Trampler: stereo reg. 1965-1966 [2V=AS]; LP Col D3S-747; CD riedizione Sony CSCR 8346.Mozart: Quintetto d\'archi n. 5 in Re maggiore, K 593:con Milton Katims: reg. 1946 [2V=EO]; CD riedizione Sony SM3K-46527.\ncon Walter Trampler: stereo reg. 1965-1966 [2V=AS]; LP Col D3S-747; CD riedizione Sony CSCR 8346.Mozart: Quintetto d\'archi n. 6 in Mi bemolle maggiore, K 614:con Milton Katims: reg. 1949 [2V=JG]; CD riedizione Sony SM3K-46527.\ncon Walter Trampler: stereo reg. 1965-1966 [2V=AS]; LP Col D3S-747; CD riedizione Sony CSCR 8346.Mozart: Piano Quartetto in Sol minore, K 478:con George Szell: reg. 1946 [2V=EO]; CD riedizione CBS MPK-47685, Naxos Hist 8.111238.\ncon Mieczysław Horszowski: stereo reg. 1963 [2V=AS]; CD riedizione Sony SM3K-46527.Mozart: Piano Quartetto in Mi bemolle maggiore, K 493:con George Szell: reg. 1946 [2V=EO]; CD riedizione CBS MPK-47685, Naxos Hist 8.111238.\ncon Mieczysław Horszowski: stereo reg. 1963 [2V=AS]; LP Col MS-6683.Mozart: Clarinet Quintetto in La maggiore, K 581 \'Stadler\', con David Oppenheim: stereo reg. 1959 [2V=AS]; CD riedizione Sony SM3K-46527.\nMozart: Serenade in Sol maggiore, K 525 \'Eine kleine Nachtmusik\' [Quintetto d\'archi version, con Julius Levine, double bass]: stereo reg. 1959 [2V=AS]; CD riedizione Sony SM3K-46527.\nRavel: Quartetto in Fa maggiore (1902–03): CD riedizione CBS MPK-44843.\nSchubert: Quartetto in La minore, D 804 \'Rosamunde\': reg. 1953 [2V=JG]; CD riedizione CBS MPK-45696.\nSchubert: Quartetto in Re minore, D 810 \'Death and the Maiden\': reg. 1953 [2V=JG]; CD riedizione CBS MPK-45696.\nSchubert: Quartetto in Sol maggiore, D 887: reg. 1953 [2V=JG]; LP riedizione Odyssey Y3-33320.\nSchubert: Quintetto d\'archi in Do maggiore, D 956, con Benar Heifetz, cello: reg. 16/9/1941 [2V=AS]; CD riedizione United Archives UPC 3760138170262.\nSchubert: Piano Quintetto in La maggiore, D 667 \'The Trout\':con Mieczysław Horszowski e Julius Levine: CD riedizione Sony SBK-46343.\ncon Mieczysław Horszowski e Georges E. Moleux: reg. 8/5/1950; LP Philips SBR 6220; CD riedizione United Archives UPC 3760138170262.Schumann: Piano Quintetto in Mi bemolle maggiore, Op. 44:con Clifford Curzon: reg. 1951 [2V=JG]; LP Col ML-4426; CD riedizione Naxos Hist 8.110306.\ncon Rudolf Serkin: stereo reg. 1963 [2V=AS]; CD riedizione CBS MYK-37256.\n\n1° Violino: Josef Roisman; 2° Violino: Alexander Schneider o Edgar Ortenberg; Viola: Boris Kroyt; Violoncello: Mischa Schneider\n\nBeethoven: Quartetto n. 1 in Fa maggiore, Op. 18, n. 1 (reg. vivo marzo 23, 1944 [2V=EO] at Library of Congress; CD riedizione Bridge 9342 A/B).\nBeethoven: Quartetto n. 2 in Sol maggiore, Op. 18, n. 2 (reg. vivo aprile 13, 1944 [2V=EO] alla Library of Congress; CD riedizione Bridge 9342 A/B).\nBeethoven: Quartetto n. 3 in Re maggiore, Op. 18, n. 3 (reg. vivo marzo 9, 1944 [2V=EO] alla Library of Congress; CD riedizione Bridge 9342 A/B).\nBeethoven: Quartetto n. 4 in Do minore, Op. 18, n. 4 (reg. vivo marzo 30, 1962 [2V=AS] alla Library of Congress; CD riedizione Bridge 9342 A/B).\nBeethoven: Quartetto n. 5 in La maggiore, Op. 18, n. 5 (reg. vivo novembre 1, 1943 [2V=AS] alla Library of Congress; CD riedizione Bridge 9342 A/B).\nBeethoven: Quartetto n. 6 in Si bem. magg., Op. 18, n. 6 (reg. vivo novembre 11, 1960 [2V=AS] alla Library of Congress; CD riedizione Bridge 9342 A/B).\nBeethoven: Quartetto n. 7 in Fa maggiore, Op. 59, n. 1 (reg. vivo ottobre 26, 1941 [2V=AS] alla Library of Congress; CD riedizione Bridge 9099 A/C).\nBeethoven: Quartetto n. 8 in Mi minore, Op. 59, n. 2 (reg. vivo aprile 1, 1960 [2V=AS] alla Library of Congress; CD riedizione Bridge 9099 A/C).\nBeethoven: Quartetto n. 9 in Do maggiore, Op. 59, n. 3 (reg. vivo marzo 6-7, 1946 [2V=EO] alla Library of Congress; CD riedizione Bridge 9099 A/C).\nBeethoven: Quartetto n. 10 in Mi bem. magg., Op. 74 (reg. vivo settembre 7, 1941 [2V=AS] alla Library of Congress; CD riedizione Bridge 9099 A/C).\nBeethoven: Quartetto n. 11 in Fa minore, Op. 95 (reg. vivo marzo 3, 1940 [2V=AS] alla Library of Congress; CD riedizione Bridge 9099 A/C).\nBeethoven: Quartetto n. 12 in Mi bem. magg., Op. 127 (reg. vivo marzo 15, 1941 [2V=AS] alla Library of Congress; CD riedizione Bridge 9072 A/C).\nBeethoven: Quartetto n. 13 in Si bem. magg., Op. 130 (reg. vivo aprile 7, 1960 [2V=AS] alla Library of Congress; CD riedizione Bridge 9072 A/C).\nBeethoven: Quartetto n. 14 in C sharp minor, Op. 131 (reg. vivo maggio 7, 1943 [2V=AS] alla Library of Congress; CD riedizione Bridge 9072 A/C).\nBeethoven: Quartetto n. 15 in La minore, Op. 132 (reg. vivo dicembre 20, 1945 [2V=EO] alla Library of Congress; CD riedizione Bridge 9072 A/C).\nBeethoven: Quartetto n. 16 in Fa maggiore, Op. 135 (reg. vivo marzo 16, 1943 [2V=AS] alla Library of Congress; CD riedizione Bridge 9072 A/C).\nBeethoven: Grosse Fuge in Si bem. magg., Op. 133 (reg. vivo aprile 7, 1960 [2V=AS] alla Library of Congress; CD riedizione Bridge 9072 A/C).\nBeethoven: Piano Trio n. 9 in Sol maggiore, Op. 121a \'Kakadu Variations\', con George Szell (reg. vivo maggio 16, 1946 alla Library of Congress; CD riedizione Intaglio INCD 7191).\nDvořák: Piano Quintetto in La maggiore, Op. 81, con Artur Balsam (reg. vivo 1959 [2V=AS] a New York; CD riedizione Documents LV 931/32).\nMozart: Quartetto n. 16 in Mi bem. magg., K 428 (reg. vivo 1959 [2V=AS] a New York; CD riedizione Documents LV 931/32).\nSchubert: Quartetto in Re minore, D 810 \'Death and the Maiden\' (reg. vivo 1959 [2V=AS] a New York; CD riedizione Documents LV 931/32).\nSchubert: Piano Quintet in La maggiore, D 667 \'The Trout\', con George Szell (reg. vivo maggio 16, 1946 alla Library of Congress; CD riedizione Intaglio INCD 7191).'"""
        table = str.maketrans({"\t": "\\t", "\r": "\\r", "\f": "\\f", "\b": "\\b"})
        text = text.translate(table).strip()
        text = re.sub("(\n|\s){2,}", "\n\n", text)
        text = re.sub("\n{3,}", "\n\n", text)
        tokenizer = SpacyTokenizer('it')
        tokens, break_levels, _ = tokenizer.tokenize(text)
        print(tokens)
        print(break_levels)
        print(len(tokens))
        print(len(break_levels))
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        k = [i for i in range(len(text)) if text[i] != rebuilt[i]][0]
        print(repr(text[k - 10:]))
        print(repr(rebuilt[k - 10:]))
        # print(repr(rebuilt[len(text):]))
        # self.assertEqual(len(tokens), len(break_levels))
        self.maxDiff = None
        self.assertEqual(text, rebuilt)

    def test_toke_9(self):
        text = """. ?/5/1951 [2V=JG];"""
        table = str.maketrans({"\t": "\\t", "\r": "\\r", "\f": "\\f", "\b": "\\b"})
        text = text.translate(table).strip()
        text = re.sub("(\n|\s){2,}", "\n\n", text)
        text = re.sub("\n{3,}", "\n\n", text)
        tokenizer = SpacyTokenizer('it')
        tokens, break_levels, _ = tokenizer.tokenize(text)
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        self.assertEqual(text, rebuilt)


SEP_MAPPING = {
    0: '',
    1: ' ',
    2: '\n',
    3: ' ',
    4: '\n\n'
}


def rebuild_sentence(start, end, tokens, breaks):
    sentence = ""
    for separator, token in zip(breaks[start:end], tokens[start:end]):
        sentence += SEP_MAPPING[separator] + token

    return sentence.strip()


class TestKannadaTokenizer(unittest.TestCase):

    def test_kannada(self):
        tokenizer = KannadaTokenizer()
        text = "ರಾಜ್ಯೋತ್ಸವ ಪ್ರಶಸ್ತಿ\nಕರ್ನಾಟಕ ರಾಜ್ಯ ಪ್ರಶಸ್ತಿಗಳು.\n\nರ್ನಾಟಕ ರಾಜ್ಯ ಪ್ರಶಸ್ತಿಗಳು"
        tokens, break_levels, _ = tokenizer.tokenize(text)
        rebuilt = rebuild_sentence(0, len(tokens), tokens, break_levels)
        self.assertEqual(rebuilt, text)
        self.assertEqual(len(tokens), len(break_levels))
