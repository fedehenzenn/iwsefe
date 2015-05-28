from haystack import indexes
from forum.models import Gamereview


class ReviewIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='review_text.html')
    titulo = indexes.CharField(model_attr='title')
    fecha = indexes.DateTimeField(model_attr='date')

    def get_model(self):
        return Gamereview

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()