import factory
from snippets import models


class SnippetFactory(factory.Factory):
    class Meta:
        model = models.Snippet

    title = factory.Faker("sentence")
    code = factory.Faker("text")
    linenos = factory.Faker("boolean")
    language = factory.Faker("text")
    style = factory.Faker("text")
