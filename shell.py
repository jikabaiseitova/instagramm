from instagramm.models import *

### ORM ###
### методы Query Set
posts = Post.objects.all()

posts

posts_postman = Post.objects.filter(title='Postman')
str(posts_postman.query)


posts_filter = posts_postman.filter(body='body')
str(posts_filter.query)

posts_2 = posts_filter.filter(createdat='2023-01-01')

###  фильтрб (при передачи в filter) - это метод, аргументы, при передачи атрибутов точки не может быть и не исп ==
posts_2023 = Post.objects.filter(date_posted__year=2023)
posts_2023
str(posts_2023.query)


###filter - есть дополнит параметры поля
post_windows = Post.objects.filter(body__startswith='Windows').filter(date_posted__year=2022)
post_windows
str(post_windows.query)

###filter метод можно передавать через запятую
post_windows = Post.objects.filter(body__startswith='Windows', date_posted__year=2022)
post_windows
str(post_windows.query)


### данные не хранятся, это тоько запрос как ярлык
posts = Post.objects.filter(date_posted__year=2021)
posts
print(posts)
exit()

### get, filter ###

post = Post.objects.get(id=1)
posts = Post.objects.filter(date_posted__year=2021)
str(post.query)

post = Post.objects.filter(id=1)
str(post.query)



post = Post.objects.filter(date_updated__year=2023)
post

post = Post.objects.get(date_updated__year=2024)
post

###None###
post = Post.objects.filter(date_updated__year=2024).first
post
print(post)

###filter, exclude(filter) о чего нету, наоборот от фильтра###
post = Post.objects.filter(date_posted__year=2023)
str(post.query)

post = Post.objects.exclude(date_posted__year=2023)
str(post.query)
posts = Post.objects.exclude(date_posted__year=2023).filter(title__startswith='Linux').excclude(date_posted__year=2022)
posts
str(posts.query)


posts = Post.objects.all().order_by('id')
posts

###order by ASC, DESC(- вначале)
posts = Post.objects.all().order_by('-title')
posts
str(posts.query)

### список из словарей
posts = Post.objects.all().values()
posts
str(posts.query)

###можно выбрать то что нам надо
posts = Post.objects.all().values('title', 'body')
posts
str(posts.query)

### список из кортежей ### values_list, позиционная передача важна
posts = Post.objects.all().values_list('title', 'body')
posts
str(posts.query)
### избавиться от кортежа и получить списки
posts = Post.objects.all().values_list('title', flat=True)
posts
str(posts.query)

### none ### список пустой если надо показать
posts = Post.objects.all().none()
posts


comments = Comment.objects.all()
for comment in comments:
    print(comment.post.title)
str(comments.query)

### select_related, foreignkey (Inner join) тоб без подзапросов было
comments = Comment.objects.all().select_related('post')
str(comments.query)

comments = Comment.objects.all().select_related('post', 'user')
str(comments.query)

### user от коммента, от поста, достаем через два нижних подчеркиваний --
comments = Comment.objects.all().select_related('post', 'user', 'post__user')
str(comments.query)

### посмотрели срез списка query set (Limit, offset) отрицательные срезы не поддерживает
posts = Post.objects.all()[0:2]
posts[0:2]
str(posts[0:2].query)

posts = Post.objects.all()[0]

### последний посмотреть
posts = Post.objects.all().order_by('-id')[0]

posts = Post.objects.filter(id=250)[0]

### получить все по определенным столбцам
posts = Post.objects.all().only('title', 'body')
str(posts.query)



### Filter Lookup Type
###lte - меньше чем или равно
### lt - агические методы меньше чем, gt - больше чем
posts = Post.objects.filter(date_posted__lte='2022-12-31')
posts

posts = Post.objects.filter(date_posted__gt='2022-12-31')
posts

### exact - точечно, по умолчанию, его опускают
post = Post.objects.filter(id__exact=1)
post = Post.objects.filter(id=1)
post

### iexact - не обращает внимания на регистр
post = Post.objects.filter(title__exact='Post about Postman program')
post

post = Post.objects.filter(title__iexact='Post about postman program')
post

### contains - поиск по слову
posts = Post.objects.filter(title__contains='about')
posts

posts = Post.objects.filter(title__contains='program')

### поиск по слову и не обращать на регистр
posts = Post.objects.filter(title__icontains='program')

### се где есть о
posts = Post.objects.filter(title__icontains='o')

### in (list comprehenshion прочитать)
posts = Post.objects.filter(id__in=[3,4])


comments = Comment.objects.all()
comments
comments = Comment.objects.filter(post__title='Post about Postman program')
comments
str(comments.query)
comments = Comment.objects.filter(post__title__icontains='Postman')

### найти комменты поста юзера у которого адм
comments = Comment.objects.filter(post__user__username__startswith='adm')
comments

### передача and (именнованные аргументы)
posts = Post.objects.filter(date_posted__year=2022, title__icontains='postman')

### передача или (позиционный обект Q стал) через палку
from django.db.models import Q
posts = Post.objects.filter(Q(date_posted__year=2022) | Q(title__icontains='postman'))
posts = Post.objects.filter(Q(date_posted__year=2022) , Q(title__icontains='postman'))
posts = Post.objects.filter(Q(date_posted__year=2022) & Q(title__icontains='postman'))

### или, и
posts = Post.objects.filter((Q(date_posted__year=2022) | Q(title__icontains='postman')) & (Q(body__icontains='gaming')))
posts

exit()



