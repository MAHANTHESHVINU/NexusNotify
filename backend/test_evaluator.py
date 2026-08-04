from app.evaluation.evaluator import Evaluator

truth = [
    "PHISHING",
    "PROMOTION",
    "TRANSACTIONAL",
    "PHISHING",
]

prediction = [
    "PHISHING",
    "PROMOTION",
    "TRANSACTIONAL",
    "TRANSACTIONAL",
]

metrics = Evaluator().evaluate(
    truth,
    prediction,
)

print(metrics)