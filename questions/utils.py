def save_answer(form) -> None:
    if form.is_valid():
        form.save()
