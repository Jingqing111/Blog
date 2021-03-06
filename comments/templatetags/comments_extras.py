from django import template
from ..forms import CommentForm

# 在 templatetags 目录下创建一个 comments_extras.py 文件，这个文件存放自定义的模板标签代码。
register = template.Library()


# 然后我们定义一个 inclusion_tag 类型的模板标签，用于渲染评论表单
@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }


@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }