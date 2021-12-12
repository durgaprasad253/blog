from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView
from . models import Post,Comment
from . forms import CommentsForm
from django.views import View
# 
class StartPageView(ListView):
    template_name="blog/index.html"
    model=Post
    ordering=["-date"]
    context_object_name="posts"
    def get_queryset(self):
        queryset= super().get_queryset()
        latest_post=queryset[:3]
        return latest_post

    

class AllPostsView(ListView):
    template_name="blog/all-posts.html"
    model=Post
    context_object_name="all_posts"
    ordering=["date"]

class PostDetailView(View):
    def get(self,request,slug):
        identified_post=Post.objects.get(slug=slug)
        form=CommentsForm()
        return render(request,"blog/post-details.html",{
            "post":identified_post,
            "tags":identified_post.tag.all(),
            "form":form,
            "comments":identified_post.comments.all().order_by("-id")
        })

    def post(self,request,slug):
        form=CommentsForm(request.POST)
        identified_post=Post.objects.get(slug=slug)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=identified_post
            comment.save()

            return HttpResponseRedirect("/posts/"+slug)
        return render(request,"blog/post-details.html",{
            "post":identified_post,
            "tags":identified_post.tag.all(),
            "form":form,
            "comments":identified_post.comments.all().order_by("-id")
        })
    # template_name="blog/post-details.html"
    # model=Post
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     identified_object=self.object
    #     context["tags"] = identified_object.tag.all()
    #     context["form"]=CommentsForm()
    #     return context
    

# def post_details(request,slug):
#     identified_post=get_object_or_404(Post,slug=slug)
#     return render(request,"blog/post-details.html",{
#         "post":identified_post,
#         "tags":identified_post.tag.all()
#     })