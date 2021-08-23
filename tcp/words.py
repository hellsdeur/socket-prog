dic = {
    "Alimento (Comida / Bebida)": ["Água", "Bolo", "Chocolate", "Dendê", "Espinafre", "Feijão", "Goiaba", "Hobza",
                                   "Iogurte", "Jícama", "Kolache", "Leite", "Mandioca", "Nachos", "Orégano", "Pudim",
                                   "Quiabo", "Rúcula", "Suco", "Torresmo", "Uvaia", "Vieira", "Waffle", "Xerém",
                                   "Yakisoba", "Zefati"],

    "Fruta (Fruto)": ["Abacaxi", "Banana", "Caju", "Damasco", "Embaúba", "Figo", "Gravatá", "Heisteria", "Ingá",
                      "Jatobá", "Kabosu", "Limão", "Maçã", "Nêspera", "Oxicoco", "Pera", "Quiuí", "Romã", "Sapoti",
                      "Tamarindo", "Uva", "Veludo", "Wampi", "Xixá", "Yuzu", "Zitrone"],

    "Animal (Bicho)": ["Anta", "Boto", "Cavalo", "Dromedário", "Elefante", "Furão", "Girafa", "Hiena", "Impala",
                       "Jumento", "Kudu", "Leão", "Morcego", "Naja", "Ovelha", "Pato", "Quero-Quero", "Rinoceronte",
                       "Sapo", "Tamanduá", "Urutau", "Veado", "Wombat", "Xaréu", "Yak", "Zebra"],

    "Ave (Pássaro)": ["Andorinha", "Bandeirinha", "Codorna", "Diuca", "Ema", "Flamingo", "Garrincha", "Harpia",
                      "Inhambu", "Jacu", "Lagarteiro", "Macuco", "Narceja", "Ógea", "Perdiz", "Quelea", "Rolinha",
                      "Sabiá", "Tuiuiú", "Urubu", "Vissiá", "Xexéu", "Zaragateiro"],

    "Mamífero": ["Alce", "Baleia", "Cabra", "Doninha", "Esquilo", "Foca", "Gambá", "Hipopótamo", "Iaque", "Jaguar",
                 "Kudu", "Lobo", "Macaco", "Nutria", "Onça", "Paca", "Quati", "Rato", "Sagüi", "Tatu", "Urso", "Vaca",
                 "Zorrilho"],

    "Artista": ["Angélica", "Bottelho", "Cazuza", "Donatello", "Eliana", "Fídias", "Glória Maria", "Hilda Hilst",
                "Irene Vilar", "John Graz", "Keith Haring", "Lísipo", "Maria Graham", "Novalis", "Otto Dix",
                "Paulo Freire", "Qi Baishi", "Rui Barbosa", "Silvio Santos", "Tunga", "Ugo Foscolo", "Voltaire",
                "William Kentridge", "Xie Zhiliu", "Yves Klein", "Ziraldo"],

    "Grupo Musical (Banda)": ["ABBA", "Blitz", "Chicago", "Detonautas", "Eagles", "Fresno", "Genesis", "Hibria", "Ira!",
                              "Journey", "Kiss", "Leela", "Metallica", "Natiruts", "Oasis", "Pollo", "Queen", "Restart",
                              "Scorpions", "Titãs", "U2", "Viper", "Warhorse", "Xandria", "Yes", "Zero"],

    "Cantores do Brasil": ["Anitta", "Armandinho ", "Bruna Karla", "Byafra ", "Cassiane", "Chorão ", "Damares",
                           "Daniel ", "Ed Motta", "Elba Ramalho ", "Fafá de Belém", "Fagner ", "Gal Costa",
                           "Gilberto Gil ", "Heloisa Rosa", "Hugo Pena ", "Ivan Lins", "Ivete Sangalo ", "João Bosco",
                           "Joelma ", "Kamau", "Kelly Key ", "Leonardo", "Luka ", "Michel Teló", "Miúcha ", "Negra Li",
                           "Netinho ", "Olívia Hime", "Ovelha ", "Peninha", "Pitty ", "Quelynah ", "Rita Lee",
                           "Roberto Carlos ", "Sérgio Reis", "Simony ", "Tânia Mara", "Tom Jobim ", "Ualas Baptista",
                           "Ursula Corona ", "Vanusa", "Vinny ", "Waldick Soriano", "Wanessa Camargo ", "Xanddy",
                           "Xuxa ", "Ylana Queiroga", "Yudi Tamashiro ", "Zé Ramalho", "Zizi Possi"],

    "C.E.P. (Cidade, Estado, País)": ["Agudos", "Amazonas", "Angola ", "Braúna", "Bahia", "Butão ", "Canela",
                                      "Colorado", "Colômbia ", "Dionísio", "Delaware", "Dinamarca ", "Encanto",
                                      "Espírito Santo", "Equador ", "Fartura", "Flórida", "França ", "Goiabeira",
                                      "Goiás", "Gana ", "Harda", "Havaí", "Haiti ", "Iconha", "Indiana", "Itália ",
                                      "Jangada", "Jalisco", "Jordânia ", "Kohima", "Karnataka", "Kenya ", "Limoeiro",
                                      "Lara", "Laos ", "Manga", "Minnesota", "México ", "Natal", "Nevada", "Noruega ",
                                      "Ouvidor", "Oregon", "Omã ", "Palhoça", "Paraíba", "Peru ", "Queluz",
                                      "Quintana Roo", "Quirguistão ", "Registro", "Rondônia", "Ruanda ", "Saboeiro",
                                      "Sergipe", "Síria ", "Tamboril", "Tocantins", "Tonga ", "Umbuzeiro", "Utah",
                                      "Uruguai ", "Vassouras", "Virgínia", "Venezuela ", "Warangal", "Wisconsin ",
                                      "Xalapa ", "Yuma", "Yucatán ", "Zabelê", "Zamfara", "Zâmbia"],

    "País (Território)": ["Argentina", "Brasil", "Chile", "Dominica", "Espanha", "Finlândia", "Grécia", "Hungria",
                          "Índia", "Japão", "Kiribati", "Lesoto", "Marrocos", "Nigéria", "Omã", "Portugal", "Quênia",
                          "Rússia", "Suíça", "Tunísia", "Uganda", "Vietnã", "Zimbábue"],

    "Cidade do Brasil": ["Alegre", "Bandeira", "Cantá", "Divino", "Esperança", "Feliz", "Gentil", "Harmonia", "Ipê",
                         "Jatobá", "Kaloré", "Limoeiro", "Macieira", "Natal", "Ouro", "Pescador", "Quebrangulo",
                         "Romaria", "Saúde", "Tefé", "Una", "Valente", "Wanderley", "Xaxim", "Zacarias"],

    "Cidade dos Estados Unidos": ["Adona", "Boston", "Chicago", "Dallas", "Eureka", "Filadélfia", "Goodyear",
                                  "Honolulu", "Indianápolis", "Jackson", "Killen", "Lincoln", "Miami", "Nome",
                                  "Orlando", "Plano", "Quimby", "Reno", "Salem", "Tampa", "Urbana", "Vivian",
                                  "Williams", "Xenia", "Yuma", "Zebulon"],

    "Idioma (Língua / Dialeto)": ["Alemão", "Búlgaro", "Chinês", "Dinamarquês", "Espanhol", "Finlandês", "Grego",
                                  "Holandês", "Inglês", "Japonês", "Kirundi", "Latim", "Mandarim", "Norueguês",
                                  "Occitano", "Português", "Quirguiz", "Russo", "Sérvio", "Turco", "Ucraniano",
                                  "Vietnamita", "Wallisiano", "Xona", "Yue", "Zulu"],

    "Moeda (Dinheiro)": ["Ariary", "Bolivar", "Coroa", "Dólar", "Euro", "Franco", "Guarani", "Hryvnia", "Iene", "J??",
                         "Kuna", "Loti", "Metical", "Ngultrum", "Ouguiya", "Peso", "Quetzal", "Real", "Som", "Taka",
                         "Uguia", "Vatu", "Won", "Xelim", "Yen", "Zloty"],

    "Cor (Tonalidade)": ["Azul", "Branco", "Cinza", "Dourado", "Escarlate", "Ferrugem", "Grená", "Herbal", "Índigo",
                         "Jasmim", "Kiwi", "Laranja", "Marrom", "Neve", "Ocre", "Preto", "Quartzo", "Rosa", "Salmão",
                         "Turquesa", "Urucum", "Vermelho", "Xanadu", "Zaffre"],

    "Esporte (Desporto)": ["Atletismo", "Basquetebol", "Corrida", "Decatlo", "Esgrima", "Futebol", "Ginástica",
                           "Hipismo", "Iatismo", "Judô", "Karate", "Luta", "Maratona", "Natação", "Orientação",
                           "Patinação", "Queimada", "Rugby", "Surfe", "Tênis", "Ultimate Frisbee", "Voleibol",
                           "Wakeboard", "Xadrez"],

    "Time (Clube de Futebol)": ["Arsenal", "Barcelona", "Chelsea", "Dínamo", "Estudiante", "Fiorentina", "Genoa",
                                "Huracán", "Internazionale", "Juventus", "Kashima Antlers", "Lazio", "Milan",
                                "Nacional", "Once Caldas", "Porto", "Querétaro", "Real Madrid", "Sevilla", "Tijuana",
                                "Universitario", "Verona", "Watford", "Xerez", "Yokohama", "Zamora"],

    "Time do Brasil": ["Atlético", "Botafogo", "Cruzeiro", "Democrata", "Estanciano", "Flamengo", "Grêmio", "Horizonte",
                       "Internacional", "Juventude", "Kapital", "Luverdense", "Mixto", "Náutico", "Operário",
                       "Palmeiras", "Quissamã", "Remo", "São Paulo", "Tupi", "Uberaba", "Vasco da Gama",
                       "Wenceslauense", "Xanxerense", "Ypiranga", "Zumbi"],

    "Marca": ["Amafil", "Bombril", "Cral", "Danone", "Eletrolux", "Ferrari", "Gillette", "Havaianas", "Isopor", "Joma",
              "Kappa", "Lycra", "Miojo", "Nintendo", "Orient", "Polo", "Q-Boa", "Racco", "Samsung", "Toddy", "Unilever",
              "Viagra", "Wilson", "Xadrez", "Ypê", "Zoomp"],

    "Marca de Automóvel": ["Audi", "BMW", "Chevrolet", "Dodge", "Engesa", "FIAT", "Gurgel", "Honda", "Iveco", "Jeep",
                           "Kia", "Lamborghini", "Mitsubishi", "Nissan", "Oldsmobile", "Porsche", "Qvale", "Renault",
                           "Scania", "Tata", "UMM", "Valtra", "Wanderer", "X??", "Yamaha", "Zastava"],

    "Marca de Cachaça": ["Atitude", "Boazinha", "Cabaré", "Damió", "Evidência", "Feliciana", "Granfina", "Havana",
                         "Isaura", "Juízo", "Katira", "Luana", "Mulata", "Nobre", "Opinião", "Pitú", "Quaty",
                         "Relíquia", "Seleta", "Triunfo", "Urucuiana", "Vaidosa", "Werneck", "Xanadu", "Ypióca",
                         "Zanoni"],

    "Marca de Café": ["Alvorada", "Brasileiro", "Cristal", "Dragão", "Evolutto", "Favorito", "Garoto", "Haiti", "Itaú",
                      "Jandaia", "Kimimo", "Lydia", "Melitta", "Nordestino", "Orfeu", "Pilão", "Quentinho", "Rancheiro",
                      "Sorriso", "Tropical", "Unaí", "Vascafé", "Wenzel", "Xororo", "Zen"],

    "Marca de Refrigerante": ["Artemis", "Baré", "Coca-Cola", "Del Rey", "E??", "Fanta", "Guaranita", "H2OH!", "It!",
                              "Jesus", "Kuat", "Leda", "Mineiro", "Nativa", "Orangina", "Pepsi", "Qualitá", "Roller",
                              "Sprite", "Taí", "Uai", "Vannucci", "Wewi", "Xamego", "Yas", "Zap"],

    "Nome de Pessoa": ["Alex", "Ana ", "Beatriz", "Bruno ", "Carla", "Carlos ", "Dara", "Diego ", "Elias", "Eva ",
                       "Fátima", "Francisco ", "Gabriel", "Geralda ", "Helena", "Henrique ", "Inácio", "Iracema ",
                       "Joana", "José ", "Karen", "kleiton ", "Laura", "Luciano ", "Marcos", "Maria ", "Nara",
                       "Nilton ", "Odair", "Olívia ", "Paulo", "Priscila ", "Queiroz", "Quênia ", "Rafael", "Regina ",
                       "Sandra", "Sílvio ", "Thaís", "Thiago ", "Ubiratan", "Úrsula ", "Vagner", "Vitória ",
                       "Wanderlei", "Wanessa ", "Xavier", "Xênia ", "Yago", "Yara ", "Zacarias", "Zaíra"],

    "Sobrenome": ["Alves", "Barbosa", "Costa", "Dias", "Esteves", "Ferreira", "Gonçalves", "Herrera", "Ibanez",
                  "Juarez", "Klein", "Lopes", "Martins", "Nogueira", "Oliveira", "Pereira", "Quadros", "Ramos", "Silva",
                  "Teixeira", "Ulhoa", "Vieira", "Wahnon", "Ximenes", "Yacoub", "Zurita"],

    "Objeto (Concreto)": ["Abajur", "Boneca", "Caneta", "Diário", "Escada", "Faca", "Gaita", "Harpa", "Isqueiro",
                          "Jarra", "Kunai", "Lanterna", "Martelo", "Navalha", "Óculos", "Pente", "Quadro", "Régua",
                          "Sanfona", "Tesoura", "Urinol", "Vassoura", "Webcam", "Xícara", "Yoyo (Ioiô)", "Zabumba"],

    "Partes do Corpo Humano": ["Audição", "Braço", "Cabeça", "Dedo", "Estômago", "Face", "Garganta", "Hormônio",
                               "Intestino", "Joelho", "Lábios", "Mão", "Nariz", "Osso", "Pele", "Quadril", "Rim",
                               "Suor", "Tronco", "Unha", "Veia", "X??", "Zigomático"],

    "Personagem": ["Ariel", "Boitatá", "Cinderella", "Don Juan", "Emília", "Fausto", "Gavroche", "Hércules", "Isabel",
                   "Jigsaw", "Kakashi", "Lobisomem", "Madeline", "Neck", "Orik", "Pinóquio", "Quasimodo", "Rapunzel",
                   "She-Ra", "Tarzan", "Ururau", "Vickie", "Wolverine", "Xuxu", "Yoda", "Zé Colméia"],

    "Profissão (Ocupação)": ["Arquiteto", "Bombeiro", "Caminhoneiro", "Detetive", "Engenheiro", "Ferreiro", "Gerente",
                             "Historiador", "Ilustrador", "Jardineiro", "Karateca", "Lenhador", "Mecânico",
                             "Neurocirurgião", "Ombudsman", "Professor", "Químico", "Relojoeiro", "Sapateiro",
                             "Tapeceiro", "Urologista", "Vaqueiro", "Ywyrájá", "Xaropeiro"],

    "Especialidade (Área do Conhecimento)": ["Administração", "Botânica", "Ciências", "Desenho", "Enfermagem", "Física",
                                             "Geografia", "História", "Irrigação", "Jornalismo", "Letras", "Medicina",
                                             "Nutrição", "Odontologia", "Psicologia", "Química", "Radiologia",
                                             "Sociologia", "Teatro", "Urbanismo", "Virologia", "Xenobiologia",
                                             "Zoologia"],

    "Desenho Animado": ["Astro Boy", "Ben 10", "CatDog", "Doug", "Evangelion", "Futurama", "Garfield", "He-Man",
                        "Inspetor Bugiganga", "Johnny Bravo", "Kid vs. Kat", "Luluzinha", "Marsupilami", "Naruto",
                        "One Piece", "Pica-Pau", "Quarteto Fantástico", "Riquinho", "Scooby-Doo", "Tom e Jerry",
                        "Ultra Maniac", "Vandread", "Will e Dewitt", "X-Men", "Yu-Gi-Oh!", "Zé Colméia"],

    "Filme": ["Amélia", "Bruno", "Camilla", "Desejo", "Elektra", "Felicidade", "Gilda", "Hulk", "Infiel", "Jezebel",
              "Kedma", "Lilith", "Malícia", "Nosferatu", "Osama", "Pânico", "Quicksilver", "Robôs", "Sabrina",
              "Tentação", "Ultimate X", "Vírus", "Walesa", "Xanadu", "Zelig"],

    "Filme do Brasil": ["Acquária", "Besouro", "Carandiru", "Desenrola", "Estranhos", "Fulaninha", "Gabriela", "Hoje",
                        "Iracema", "Jenipapo", "Kenoma", "Lamarca", "Motel", "Nina", "Olga", "Podecrer!", "Quilombo",
                        "Redentor", "Senhora", "Tiradentes", "Urutau", "Verônica", "Wilsinho Galiléia", "Xingu",
                        "Yndio do Brasil", "Zé do Periquito"],

    "Verbo": ["Amar", "Beber", "Cantar", "Dançar", "Educar", "Falar", "Gostar", "Herdar", "Ingerir", "Jogar", "Lavar",
              "Morar", "Negar", "Olhar", "Pensar", "Quebrar", "Rir", "Ser", "Ter", "Usar", "Ver", "Warrantar",
              "Xavecar", "Zelar"],

    "Elemento Químico": ["Alumínio", "Berílio", "Carbono", "Dúbnio", "Estanho", "Fósforo", "Germânio", "Hélio", "Índio",
                         "Potássio", "Lutécio", "Mercúrio", "Níquel", "Oxigênio", "Polônio", "Q??", "Rádio", "Silício",
                         "Túlio", "Urânio", "Vanádio", "Tungstênio", "Xenônio", "Ítrio", "Zinco"],

    "Fobia (Medo)": ["Afobia", "Biofobia", "Criofobia", "Dorafobia", "Eritofobia", "Fotofobia", "Gatofobia",
                     "Heliofobia", "Iofobia", "Japanofobia", "Katsaridafobia", "Logofobia", "Mitofobia", "Neofobia",
                     "Octofobia", "Pirofobia", "Quilofobia", "Ritifobia", "Sitiofobia", "Toxifobia", "Urofobia",
                     "Verbofobia", "Xilofobia", "Zoofobia"],

    "Mineral": ["Ametista", "Blenda", "Cobre", "Distena", "Euxenita", "Fenacite", "Grafite", "Hialita", "Ilmenita",
                "Jade", "Kobellita", "Lazurita", "Niobite", "Opala", "Prata", "Quartzo", "Rubi", "Sal", "Talco",
                "Ultramarina", "Vivianite", "Willemite", "Xisto", "Yttria (Óxido de ítrio)", "Zoisite"]

}
