from django import forms
from .models import Post, Comment
from django.utils.text import slugify
from tinymce.widgets import TinyMCE



class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={"cols": 30, "rows": 20}))

    class Meta:
        model = Post
        fields = [
            "title",
            "image",
            "content",
            "author",
        ]

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields["author"].widget.attrs.update({"class": "form-control","style": "background-color:#f0f0f0" })
        self.fields["title"].widget.attrs.update({"class": "form-control","style": "background-color:#f0f0f0" })
        self.fields["image"].widget.attrs.update({"class": "form-control","style": "background-color:#f0f0f0" })
        self.fields["content"].widget.attrs.update({"class": "form-control","style": "background-color:#f0f0f0" })


    # slug alanını title alanı ile otomatik dolduruyoruz.
    def save(self, commit=True):
        instance = super(BlogPostForm, self).save(commit=False)
        if not instance.slug:
            instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
            "rating",
        ]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update({"class": "form-control"})
        self.fields["rating"].widget.attrs.update({"class": "form-control"})

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 5:
            raise forms.ValidationError('Rating must be between 0 and 5.')
        return rating
