(venv) sky@MBP-Aleksej News_Portal % python3 manage.py makemigrations
(venv) sky@MBP-Aleksej News_Portal % python3 manage.py migrate
(venv) sky@MBP-Aleksej News_Portal % python3 manage.py shell

>>> from main_app.models import *
>>> u1 = User.objects.create_user(username='Alex')
>>> u2 = User.objects.create_user(username='Alex2')
>>> Author.objects.create(authorUser=u1)
>>> Author.objects.create(authorUser=u2)

>>> Category.objects.create(name='Latest news')
>>> Category.objects.create(name='The most important news')
>>> Category.objects.create(name='Jango project news')
>>> Category.objects.create(name='Good news')

>>> author = Author.objects.get(id=1)
>>> Post.objects.create(author=author, categoryType='AR', title='VSS Unity совершил удачный полет', text='На сей раз все прошло в штатном режиме, и корабль был доставлен носителем компании Virgin на высоту почти 15 км.')
>>> Post.objects.create(author=author, categoryType='AR', title='Tianzhou-2 произвел стыковку', text='Китай успешно доставил на орбитальную станцию космический грузовик «Тяньчжоу-2»')
>>> author = Author.objects.get(id=2)
>>> Post.objects.create(author=author, categoryType='NW', title='АвтоВАЗу не даются детали', text='Компания приостановит конвейер из-за нехватки импортных комплектующих')

>>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
>>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))
>>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
>>> Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))

>>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='Super!')
>>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='Отлично полетел!')
>>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='Стыковка на ура!')
>>> Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='Может сами начнут делать комплектующие?')

>>> Post.objects.get(id = 1).like()
>>> Post.objects.get(id = 1).like()
>>> Post.objects.get(id = 1).like()
>>> Post.objects.get(id = 1).dislike()
>>> Post.objects.get(id = 2).like()
>>> Post.objects.get(id = 3).like()
>>> Post.objects.get(id = 3).dislike()
>>> Post.objects.get(id = 3).dislike()
>>> Comment.objects.get(id = 1).like()
>>> Comment.objects.get(id = 2).like()
>>> Comment.objects.get(id = 2).like()
>>> Comment.objects.get(id = 3).dislike()

>>> Author.objects.get(id=1).update_rating()
>>> Author.objects.get(id=2).update_rating()

>>> Author.objects.order_by('-ratingAuthor').values('authorUser__username', 'ratingAuthor')[0]
>>> Post.objects.filter(categoryType='AR').order_by('-rating').values('dateCreation', 'author__authorUser__username', 'rating', 'title')[0]
>>> Post.objects.filter(categoryType='AR').order_by('-rating')[0].preview()
>>> for i in Comment.objects.filter(commentPost = Post.objects.filter(categoryType='AR').order_by('-rating')[0]): f"{i.dateCreation} | {i.commentUser.username} | {i.rating} | {i.text}"
