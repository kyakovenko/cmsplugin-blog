from django.conf.urls import url, patterns

from cmsplugin_blog.feeds import EntriesFeed, TaggedEntriesFeed, AuthorEntriesFeed
from cmsplugin_blog.models import Entry
from cmsplugin_blog.views import (EntryDateDetailView, EntryArchiveIndexView, BlogYearArchiveView,
                                  BlogMonthArchiveView, BlogDayArchiveView, BlogAuthorArchiveView,
                                  BlogTaggedArchiveView)


blog_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
    'allow_empty': True,
    'paginate_by': 15,
}

blog_detail = EntryDateDetailView.as_view(
    queryset=Entry.objects.all(),
    date_field='pub_date',
    month_format='%m',
    slug_field='entrytitle__slug',
)

urlpatterns = patterns('',
    url(r'^$', EntryArchiveIndexView.as_view(),
        blog_info_dict,
        name='blog_archive_index'),
    url(r'^(?P<year>\d{4})/$',
        BlogYearArchiveView.as_view(),
        name='blog_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        BlogMonthArchiveView.as_view(),
        name='blog_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        BlogDayArchiveView.as_view(),
        name='blog_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        blog_detail,
        name='blog_detail'),
    url(r'^tagged/(?P<tag>[^/]*)/$',
        BlogTaggedArchiveView.as_view(),
        name='blog_archive_tagged'),
    url(r'^author/(?P<author>[^/]*)/$',
        BlogAuthorArchiveView.as_view(),
        name='blog_archive_author'),
    url(r'^rss/any/tagged/(?P<tag>[^/]*)/$',
        TaggedEntriesFeed(), {'any_language': True},
        name='blog_rss_any_tagged'),
    url(r'^rss/tagged/(?P<tag>[^/]*)/$',
        TaggedEntriesFeed(),
        name='blog_rss_tagged'),
    url(r'^rss/any/author/(?P<author>[^/]*)/$',
        AuthorEntriesFeed(),
        {'any_language': True},
        name='blog_rss_any_author'),
    url(r'^rss/author/(?P<author>[^/]*)/$',
        AuthorEntriesFeed(),
        name='blog_rss_author'),
    url(r'^rss/any/$',
        EntriesFeed(),
        {'any_language': True},
        name='blog_rss_any'),
    url(r'^rss/$',
        EntriesFeed(),
        name='blog_rss'),
)
