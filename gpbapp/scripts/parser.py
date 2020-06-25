""" Parser """

# -*- coding: utf-8 -*-
import re
import unicodedata, unidecode
import string

class Parser():

    def __init__(self):
        """ Take a french sentence as parameters.
            Return a keyword.

            sentence              (str ): french sentence only.
            request_keywords      (str ): result of sentence_parsing. """

        self.sentence = None
        self.request_keyword = {
            "status" : "", # EMPTY, FOUND, NOT FOUND
            "greeting_form" : "",
            "sentence_type" : "",
            "keyword" : ""
        }

        self.result = ""

    def sentence_parsing(self, sentence=None):
        """ We check that the sentence received by GrandPapyBot is
        syntactically correct.

        In french, a question must have one of the following three form :

        1. Subject + verb + complement + question mark (?)
        2. Verb + subject + complement + question mark (?)
        3. "Est-ce que" + subject + verb + complement + question mark (?) """

        # 0. Initialization
        self.sentence = sentence
        self.request_keyword = {
            "status" : "",
            "greeting_form" : "",
            "sentence_type" : "",
            "keyword" : ""
        }

        status = ""
        sentence_type = ""
        keyword = ""
        greeting_form = ""

        # 1. We remove the spaces too
        self.sentence = " ".join(self.sentence.split())

        # 2. We retired accents
        self.sentence = unidecode.unidecode(self.sentence)

        if len(self.sentence) == 0:
            status = "EMPTY"
        else:

            # 1. We check if exist a greeting form
            if re.match(r"^(Salut|Bonjour|Coucou)[ a-zA-z]*[!,.]\s", self.sentence) is not None:
                greeting_form = "TRUE"
                self.sentence = re.sub(r"^(Salut|Bonjour|Coucou)[ a-zA-z]*[!,.]\s", "", self.sentence)
            else:
                greeting_form = "FALSE"

            # 2. We check if the sentence is a question
            if re.match(r"^(Je|Tu|Il|Nous|Vous|Ils) ?[ \-'a-zA-z]*\?$", self.sentence):
                sentence_type = "TYPE ONE"
            elif re.match(r"^(Est[ -]?ce que)\s{1}([jJ]e|[Tt]u|[Ii]l|[Nn]ous|[Vv]ous|[Ii]ls){1}\s{1}[a-zA-z]*\s{1}[ \-'a-zA-Z]*\?$", self.sentence):
                sentence_type = "TYPE TWO"
            elif re.match(r"^[a-zA-z]*[-\s]{1}([jJ]e|[Tt]u|[Ii]l|[Nn]ous|[Vv]ous|[Ii]ls){1}[ \-'a-zA-Z]*\s{1}\?$", self.sentence):
                sentence_type = "TYPE THREE"
            else:
                sentence_type = "NO SENTENCE"
                status = "NO SENTENCE"

            # 4. We execute the code
            if sentence_type != "NO SENTENCE":

                search_result = re.search(r"(((de\sla|du|de|d'|le|la|l'[^adresse]){1}[\s\-'a-zA-ZÉé]*\?$))", self.sentence)
                sentence_keywords = search_result.group(1)

                req_keyword = re.sub(r"^(de\sla\s|du\s|de\s|d'|la\s|le\s|l'|les\s)", "", sentence_keywords)
                req_keyword = re.sub(r"(\s\?)$", "", req_keyword)

                status = "FOUND"
                keyword = req_keyword

            else:

                status = "FOUND"
                keyword = self.sentence_parsing_rescue(sentence=sentence)

        self.request_keyword["status"] = status
        self.request_keyword["sentence_type"] = sentence_type
        self.request_keyword["greeting_form"] = greeting_form
        self.request_keyword["keyword"] = keyword

        return self.request_keyword

    def sentence_parsing_rescue(self, sentence=None):

        self.sentence = sentence

        # 2. Remove accent
        self.sentence = unidecode.unidecode(self.sentence)

        # 3. Remove punctuation
        self.result = ""
        for letter in self.sentence:
            # If char is not punctuation, add it to the result.
            if letter == "'" or letter == "-":
                self.result += " "
            elif letter not in string.punctuation:
                self.result += letter

        self.sentence = self.result

        # 4. Remove Majuscule
        self.sentence = self.sentence.lower()

        # 5. Remove the spaces too
        self.sentence = " ".join(self.sentence.split())

        # 6. Remove french stop words
        stop_words = ("salut", "connais", "grandpy", "adresse", "a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô")
        split_sentence = self.sentence.split()
        keywords_sentence = []

        for word in split_sentence:
            if word not in stop_words:
                keywords_sentence.append(word)

        self.sentence = ' '.join(keywords_sentence)

        return self.sentence
