from django.conf.urls import patterns, include, url
# from django.contrib import admin

urlpatterns = patterns('',

    # Examples:
    url(r'^$', 'app.views.home', name='home'),

    url(r'^users', 'app.views.show_users'),
    url(r'^bills', 'app.views.show_bills'),
    url(r'^times', 'app.views.show_times'),
    url(r'^transactions', 'app.views.show_transactions'),

    # Searches
    url(r'^usrs_search', 'app.views.users'),
    url(r'^blls_search', 'app.views.bills'),
    url(r'^tmes_search', 'app.views.times'),

    url(r'^bool', 'app.views.show_bool_search'),
    url(r'^date', 'app.views.show_date_search'),
    url(r'^not_word', 'app.views.show_text_not_word_search'),
    url(r'^phrase', 'app.views.show_phrase_search'),
    url(r'^bill', 'app.views.show_bill_search'),

    # Changes
    url(r'^remove', 'app.views.remove'),
    url(r'^add', 'app.views.add'),
    url(r'^change', 'app.views.change'),

    # Start links
    url(r'^view', 'app.views.view'),
    url(r'^search', 'app.views.search'),
    url(r'^chng', 'app.views.tr_ids'),

    url(r'^load', 'app.views.load'),
    url(r'^file_load', 'app.views.load_file'),

    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
