from django.shortcuts import render

from django.http import HttpResponse


def list_singers():
    singers = [
        {
            'id': 1,
            'name': 'Twenty One Pilots',
            'genre': 'Hip-Hop, Rock, Pop',
            'lead_singer': 'Tyler Joseph',
            'slug': 'twenty-one-pilots'
        },
        {
            'id': 2,
            'name': 'Mitski',
            'genre': 'Indie Rock',
            'lead_singer': 'Mitsuki Miyawaki',
            'slug': 'mitski'
        },
        {
            'id': 3,
            'name': 'Mindless Self Indulgence',
            'genre': 'Industrial Rock, Punk Rock, Electropunk',
            'lead_singer': 'Jimmy Urine',
            'slug': 'mindless-self-indulgence'
        },
        {
            'id': 4,
            'name': 'Placebo',
            'genre': 'Alternative Rock',
            'lead_singer': 'Brian Molko',
            'slug': 'placebo'
        },
        {
            'id': 5,
            'name': 'Radiohead',
            'genre': 'Alternative Rock, Art Rock, Electronic',
            'lead_singer': 'Thom Yorke',
            'slug': 'radiohead'
        },
    ]
    return singers


def popular_singers(request):
    html_content = """
    <html>
    <body>
        <h1>My favourite artists</h1>
        <ul>
    """
    for singer in list_singers():
        singer_url = f"/singer/?id={singer['id']}"
        html_content += f"<li><a href='{singer_url}'><strong>{singer['name']}</strong></a>" \
                                 f" - {singer['genre']} (Lead singer: {singer['lead_singer']})</li>"

    html_content += """
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content, content_type='text/html; charset=utf-8')


def singer_card(request):

    singer_id = request.GET.get('id')
    singer_id = int(singer_id)
    singers = list_singers()
    singer = next((s for s in singers if s['id'] == singer_id), None)

    html_content = f"""
    <html>
    <body>
        <h1>{singer['name']}</h1>
        <p>Genre: {singer['genre']}</p>
        <p>Lead singer: {singer['lead_singer']}</p>
    </body>
    </html>
    """
    return HttpResponse(html_content, content_type='text/html; charset=utf-8')
