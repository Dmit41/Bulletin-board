from django_filters import FilterSet, CharFilter, ModelChoiceFilter

from .models import Post, Response


class PostFilter(FilterSet):
    text = CharFilter(
        field_name='text',
        lookup_expr='icontains',
        label='Текст содержит:'
    )

    post = ModelChoiceFilter(
        field_name='post',
        queryset=Post.objects.all(),
        label='Пост',
        empty_label='Все посты'
    )

    class Meta:
        model = Response
        fields = {
            'post', 'text'
        }