from django.shortcuts import render, redirect
from django.http import JsonResponse

# Define the questions
questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Paris", "London", "Berlin", "Madrid"]
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ["Mars", "Venus", "Earth", "Jupiter"]
    },
    {
        'question': "Who wrote 'Hamlet'?",
        'options': ["William Shakespeare", "Charles Dickens", "J.K. Rowling", "Mark Twain"]
    },
    {
        'question': "What is the square root of 64?",
        'options': ["6", "7", "8", "9"]
    },
    {
        'question': "Which is the largest ocean on Earth?",
        'options': ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"]
    }
]

def test_view(request):
    # Get current question index from session or default to 0
    current_question = request.session.get('current_question', 0)
    question = questions[current_question]

    # Get the total number of questions
    total_questions = len(questions)

    # Render the test page with the current question and options
    return render(request, 'test_app/test.html', {
        'question': question,
        'current_question': current_question,
        'total_questions': total_questions,
    })

def next_question(request):
    # Save the selected answer to the session
    selected_option = request.POST.get('answer')
    current_question = int(request.POST.get('current_question', 0))

    # Save the answer in the session (if selected)
    if selected_option:
        answers = request.session.get('answers', {})
        answers[current_question] = selected_option
        request.session['answers'] = answers

    # Move to the next question
    current_question += 1
    if current_question >= len(questions):
        # All questions are done, send finished flag
        return JsonResponse({'next_question': False})
    else:
        # Render the next question
        return JsonResponse({'next_question': True})

def prev_question(request):
    # Get the current question index from the session
    current_question = request.session.get('current_question', 0)

    # If we're not at the first question, go back
    if current_question > 0:
        current_question -= 1

    # Save the updated index in session and render the question
    request.session['current_question'] = current_question
    question = questions[current_question]
    total_questions = len(questions)

    return render(request, 'test_app/test.html', {
        'question': question,
        'current_question': current_question,
        'total_questions': total_questions,
    })

def completion_view(request):
    return render(request, 'test_app/completion.html', {'message': "You completed the test"})

def home_view(request):
    return render(request, 'test_app/home.html')
