from haystack import indexes
from forum.models import Gamereview


class ReviewIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='review_text.html')
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return Gamereview

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()