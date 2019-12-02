import re
from abc import ABC


class ArticleExtractorI(ABC):
    def __init__(self):
        self._articles = []
        self._re_template = ''

    def extract(self, text, entity):
        article = ''
        pattern = self._re_template.format("")
        match = re.search("^" + pattern, entity, re.IGNORECASE)
        if match:
            article = match.group('article')
            return article

        pattern = self._re_template.format(re.escape(entity.split()[0]))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            article = match.group('article')
            return article

        return article


class DummyArticleExtractor(ArticleExtractorI):
    def extract(self, text, entity):
        return ''


class ItalianArticleExtractor(ArticleExtractorI):
    def __init__(self):
        super().__init__()
        self._articles = ['Il', 'Lo', 'La', 'I', 'Gli', 'Le', 'L']
        self._re_template = "(?P<article>" + "|".join(
            ["\\b" + article + "\\b" for article in self._articles]) + ")(\s?|\'){}"


class FrenchArticleExtractor(ArticleExtractorI):
    def __init__(self):
        super().__init__()
        self._articles = ['Le', 'La', 'L', 'Les']
        self._re_template = "(?P<article>" + "|".join(
            ["\\b" + article + "\\b" for article in self._articles]) + ")(\s?|\'){}"


class GermanArticleExtractor(ArticleExtractorI):
    def __init__(self):
        super().__init__()
        self._articles = ['Der', 'Die', 'Das', 'Ein', 'Eine']
        self._re_template = "(?P<article>" + "|".join(
            ["\\b" + article + "\\b" for article in self._articles]) + ")(\s){}"

    def extract(self, text, entity):
        text = text.split("\n")[0]
        return super().extract(text, entity)


class SpanishArticleExtractor(ArticleExtractorI):
    def __init__(self):
        super().__init__()
        self._articles = ['El', 'La', 'Los', 'Las']
        self._re_template = "(?P<article>" + "|".join(
            ["\\b" + article + "\\b" for article in self._articles]) + ")(\s){}"


class ArticleExtractorFactory(object):
    @staticmethod
    def make_extractor(lang):
        if lang == 'it':
            return ItalianArticleExtractor()

        if lang == 'de':
            return GermanArticleExtractor()

        if lang == 'es':
            return SpanishArticleExtractor()

        return DummyArticleExtractor()
