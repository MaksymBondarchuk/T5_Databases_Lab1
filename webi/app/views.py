from httplib import HTTPResponse
from django.http.response import HttpResponse
from django.shortcuts import render

from Get_Tables import get_users
from Get_Tables import get_bills
from Get_Tables import get_times
from Get_Tables import get_transactions

from Get_Tables import get_users_ids

from Search import search_bool
from Search import search_date
from Search import search_text_not_word
from Search import search_phrase
from Search import search_bill

from ChangeDB import remove_transaction
from ChangeDB import add_transaction
from ChangeDB import change_transaction

from Load_from_file import load_from_file

# Create your views here.





def show_users(request):
    return render(request, "Table.html", {"table": get_users()})


def show_bills(request):
    return render(request, "Table.html", {"table": get_bills()})


def show_transactions(request):
    return render(request, "Transactions_table.html", {"table": get_transactions()})


def show_times(request):
    return render(request, "Table.html", {"table": get_times()})


def show_bool_search(request):
    return render(request, "Table.html", {"table": search_bool(request.GET["bool"])})


def show_date_search(request):
    return render(request, "Table.html", {"table": search_date(request.GET["start"], request.GET["end"])})


def show_text_not_word_search(request):
    return render(request, "Table.html", {"table": search_text_not_word(request.GET["column"], request.GET["word"])})


def show_phrase_search(request):
    return render(request, "Table.html", {"table": search_phrase(request.GET["column"], request.GET["phrase"])})


def show_bill_search(request):
    return render(request, "Table.html", {"table": search_bill(request.GET["column"], request.GET["start"], request.GET["end"])})


def remove(request):
    return render(request, "info.html", remove_transaction(request.GET["id"]))


def add(request):
    return render(request, "info.html", add_transaction(request.GET["id"]))


def change(request):
    return render(request, "info.html", change_transaction(request.GET["id"], request.GET["field"], request.GET["new"]))


def tr_ids(request):
    return render(request, "Change.html", {"table_tr": get_users_ids()})


def view(request):
    return render(request, "View.html")


def search(request):
    return render(request, "Search.html")


def users(request):
    return render(request, "Search_users.html")


def bills(request):
    return render(request, "Search_bills.html")


def times(request):
    return render(request, "Search_times.html")

def load(request):
    return render(request, "Load.html")


def load_file(request):
     return render(request, "info.html", load_from_file(request.GET["file"], request.GET["table"]))