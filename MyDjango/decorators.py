from django.shortcuts import redirect


def auto_session(fun):
    def inner(request, *args, **kwargs):
        if request.session.get("user") is None:
            return redirect(to="/")
        return fun(request, *args, **kwargs)
    return inner