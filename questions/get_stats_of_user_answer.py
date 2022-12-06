def get_stats_of_user_answer(user_answer_of_block_question) -> str:
    valid: int = 0
    invalid: int = 0
    for question in user_answer_of_block_question:
        for answer in question.cleaned_data["answers"]:
            if answer.is_valid_answer():
                valid += 1
            else:
                invalid += 1
    return f"Правильных ответов: {valid}, ошибок {invalid}"
