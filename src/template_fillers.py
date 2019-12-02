import re
from abc import ABC


class TemplateFillerI(ABC):
    def fill(self, template: str, entity: str, **kwargs):
        return template.replace("XXX", entity)


class ItalianTemplateFiller(TemplateFillerI):
    def __init__(self):
        self._reduction_rules = {'diil': 'del', 'dilo': 'dello', 'dila': 'della', 'dii': 'dei', 'digli': 'degli',
                                 'dile': 'delle', 'dil': 'dell\'',
                                 'ail': 'al', 'alo': 'allo', 'ala': 'alla', 'ai': 'ai', 'agli': 'agli', 'ale': 'alle',
                                 'dail': 'dal', 'dalo': 'dallo', 'dala': 'dalla', 'dai': 'dai', 'dagli': 'dagli',
                                 'dale': 'dalle',
                                 'inil': 'nel', 'inlo': 'nello', 'inla': 'nella', 'ini': 'nei', 'ingli': 'negli',
                                 'inle': 'nelle',
                                 'conil': 'col', 'conlo': 'cóllo', 'conla': 'cólla', 'coni': 'coi', 'congli': 'cogli',
                                 'conle': 'cólle',
                                 'suil': 'sul', 'sulo': 'sullo', 'sula': 'sulla', 'sui': 'sui', 'sugli': 'sugli',
                                 'sule': 'sulle',
                                 'peril': 'pel', 'perlo': 'pello', 'perla': 'pella', 'peri': 'pei', 'pergli': 'pegli',
                                 'perle': 'pelle'}

        self._template = "(?P<preposition>" + "|".join(["\\b" + preposition + "\\b"
                                                        for preposition in self._reduction_rules.keys()]) + ")"
        self._finder = re.compile(self._template, re.IGNORECASE)
        self._articles_gender = {'il': 'o', 'lo': 'o', 'i': 'i', 'gli': 'i', 'la': 'a', 'le': 'e'}

    def fill(self, template: str, entity: str, **kwargs):
        article = kwargs['article'].lower()
        article_in_entity = True if entity.lower().startswith(article) else False

        if article:
            if article_in_entity and re.search("(di|a|da|in|con|su|per)YYY", template):
                entity = re.sub("\\b" + article + "\\b", "", entity, 1, re.IGNORECASE)
                template = template.replace("YYY", article)
            elif article_in_entity:
                template = template.replace("YYY", "")
            else:
                template = template.replace("YYY", article)
            template = self._reduce(template)
        else:
            template = template.replace("YYY", "")

        gender = self._articles_gender.get(article, 'o')
        template = template.replace("GGG", gender)
        template = template.replace("XXX", entity)
        if '\' ' + entity in template:
            template = template.replace("\' ", "\'")
        template = re.sub("\s{2,}", " ", template)
        return template

    def _reduce(self, template):
        match = self._finder.search(template)
        if match:
            preposition = match.group('preposition').lower().strip()
            template = template.replace(preposition, self._reduction_rules[preposition])

        return template


class FrenchTemplateFiller(TemplateFillerI):
    def __init__(self):
        self._vowels = {'a', 'e', 'i', 'o', 'u', 'â', 'ê', 'î', 'ô', 'û', 'ë', 'ï', 'ü', 'y', 'ÿ', 'à', 'è', 'ù', 'é'}

    def fill(self, template: str, entity: str, **kwargs):
        if re.search("de\sXXX", template) and entity[0].lower() in self._vowels:
            template = re.sub("de\sXXX", "d'XXX", template)

        template = template.replace("XXX", entity)
        template = re.sub("\s{2,}", " ", template)
        return template.strip()


class GermanTemplateFiller(TemplateFillerI):
    def fill(self, template: str, entity: str, **kwargs):
        article = kwargs['article'].lower()

        article_in_entity = True if entity.lower().startswith(article) else False
        if article_in_entity:
            article = ""
        template = re.sub("YYY", article, template)
        template = template.replace("XXX", entity)
        template = re.sub("\s{2,}", " ", template)
        template = template.strip()
        template = template[0].upper() + template[1:]
        return template.strip()


class SpanishTemplateFiller(TemplateFillerI):
    def __init__(self):
        self._articles_gender = {'el': 'o', 'la': 'a', 'los': 'es', 'las': 'as'}

    def fill(self, template: str, entity: str, **kwargs):
        article = kwargs['article'].lower()
        article_in_entity = True if entity.lower().startswith(article) else False
        skip = False
        if article_in_entity and not re.search("(de)YYY", template):
            skip = True

        if article and not skip:
            if article == "el" and re.search("(de)YYY", template):
                template = template.replace("deYYY", 'del')
            else:
                template = template.replace("YYY", " " + article)
        else:
            template = template.replace("YYY", "")

        gender = self._articles_gender.get(article, 'o')
        template = template.replace("GGG", gender)
        template = template.replace("XXX", entity)
        template = re.sub("\s{2,}", " ", template)

        return template


class TemplateFillerFactory(object):
    @staticmethod
    def make_filler(lang):
        if lang == "en":
            return TemplateFillerI()
        if lang == "it":
            return ItalianTemplateFiller()
        if lang == "de":
            return GermanTemplateFiller()
        if lang == "es":
            return SpanishTemplateFiller()
        if lang == "fr":
            return FrenchTemplateFiller()

        return TemplateFillerI()
