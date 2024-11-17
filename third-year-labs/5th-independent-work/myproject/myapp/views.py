from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to myapp!")


def about_me(request):
    html_content = """
    <html>
    <head><title>About Me</title></head>
    <body>
        <h1>About Me</h1>
        <table border="1">
            <tr>
                <th>Attribute</th>
                <th>Details</th>
            </tr>
            <tr>
                <td>Name</td>
                <td>Yuliia Riabko</td>
            </tr>
            <tr>
                <td>Role</td>
                <td>Software Developer</td>
            </tr>
            <tr>
                <td>University</td>
                <td>State University of Information and Communication Technologies</td>
            </tr>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html_content)
