from django.db import models
from django.contrib.auth import get_user_model


class Author(models.Model):
    """Модель автора."""

    user = models.OneToOneField(get_user_model(), models.CASCADE)
    raiting = models.IntegerField()

    def __str__(self):
        return f"Автор - {self.user.username}"

    def update_rating(self):
        post_raiting = sum([x.raiting for x in self.posts.all()])
        comment_raiting = sum([x.raiting for x in self.user.comments.all()])

        post_comment_raiting = 0
        for post in self.posts.all():
            for comment in post.post_comments.all():
                post_comment_raiting += comment.raiting
        # post_comment_raiting = sum([x.raiting for x in [post.post_comments.all() for post in self.posts.all()]])


        calculate_raiting = (post_raiting * 3) + comment_raiting + post_comment_raiting
        self.raiting = calculate_raiting 
        self.save()


class Category(models.Model):
    """Модель категории."""
    
    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return f"Категория - {self.name}"


class PostCategory(models.Model):
    """Модель категории поста."""
    category = models.ForeignKey(Category, models.CASCADE)
    post = models.ForeignKey('Post', models.CASCADE)


class Post(models.Model):
    """Модель пост."""
    
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    text = models.TextField()
    type = models.CharField(max_length=20, choices=(
        ('news', 'Новость'),
        ('article', 'Статья'),
    )) 
    raiting = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through=PostCategory)
    author = models.ForeignKey(Author, models.CASCADE, related_name='posts') 
   
    def like(self):
        self.raiting += 1
        self.save()

    def dislike(self):
        self.raiting -= 1
        self.save()

    @property
    def preview(self):
        return self.text[:124] + '...'


class Comment(models.Model):
    """Модель комментария."""

    post = models.ForeignKey(Post, models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(get_user_model(), models.CASCADE, related_name='comments')
    text = models.TextField()
    raiting = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
   
    def like(self):
        self.raiting += 1
        self.save()

    def dislike(self):
        self.raiting -= 1
        self.save()