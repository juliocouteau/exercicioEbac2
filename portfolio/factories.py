import factory
from faker import Factory as FakerFactory
from django.contrib.auth.models import User
from django.utils.timezone import now
from portfolio.models import Post  # Alterado de blog para portfolio

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0
    content = factory.LazyAttribute(lambda x: faker.text())