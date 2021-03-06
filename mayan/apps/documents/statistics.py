from __future__ import absolute_import, unicode_literals

import datetime

import qsstats

from .models import Document, DocumentPage, DocumentVersion


def new_documents_per_month():
    qss = qsstats.QuerySetStats(Document.passthrough.all(), 'date_added')

    today = datetime.date.today()
    this_year = datetime.date(year=today.year, month=1, day=1)

    return {
        'series': {
            'Documents': map(lambda x: {x[0].month: x[1]}, qss.time_series(start=this_year, end=today, interval='months'))
        }
    }


def new_document_versions_per_month():
    qss = qsstats.QuerySetStats(DocumentVersion.objects.all(), 'document__date_added')

    today = datetime.date.today()
    this_year = datetime.date(year=today.year, month=1, day=1)

    return {
        'series': {
            'Versions': map(lambda x: {x[0].month: x[1]}, qss.time_series(start=this_year, end=today, interval='months'))
        }
    }


def new_document_pages_per_month():
    qss = qsstats.QuerySetStats(DocumentPage.objects.all(), 'document_version__document__date_added')

    today = datetime.date.today()
    this_year = datetime.date(year=today.year, month=1, day=1)

    return {
        'series': {
            'Pages': map(lambda x: {x[0].month: x[1]}, qss.time_series(start=this_year, end=today, interval='months'))
        }
    }


def total_document_per_month():
    qss = qsstats.QuerySetStats(Document.objects.all(), 'date_added')
    this_year = datetime.date.today().year

    result = []

    for month in range(1, datetime.date.today().month + 1):
        next_month = month + 1

        if next_month == 12:
            next_month = 1
            year = this_year + 1
        else:
            next_month = month + 1
            year = this_year

        result.append({month: qss.until(datetime.date(year, next_month, 1))})

    return {
        'series': {
            'Documents': result
        }
    }


def total_document_version_per_month():
    qss = qsstats.QuerySetStats(DocumentVersion.objects.all(), 'document__date_added')
    this_year = datetime.date.today().year

    result = []

    for month in range(1, datetime.date.today().month + 1):
        next_month = month + 1

        if next_month == 12:
            next_month = 1
            year = this_year + 1
        else:
            next_month = month + 1
            year = this_year

        result.append({month: qss.until(datetime.date(year, next_month, 1))})

    return {
        'series': {
            'Versions': result
        }
    }


def total_document_page_per_month():
    qss = qsstats.QuerySetStats(DocumentPage.objects.all(), 'document_version__document__date_added')
    this_year = datetime.date.today().year

    result = []

    for month in range(1, datetime.date.today().month + 1):
        next_month = month + 1

        if next_month == 12:
            next_month = 1
            year = this_year + 1
        else:
            next_month = month + 1
            year = this_year

        result.append({month: qss.until(datetime.date(year, next_month, 1))})

    return {
        'series': {
            'Pages': result
        }
    }
