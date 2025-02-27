import re

regexp = re.compile('[+\-*=\s^/]|[0-9]+')


class CaptchaSolver:
    def __init__(self):
        pass

    def is_ariphmetic(self, text):
        math_chars = regexp.findall(text)
        return len(math_chars) >= 5 and "=" in text

    def solve_math(self, text):
        phrase, answer, eval_answer = self._extract_math_phrase(text)
        # True - OK. False - Cancel
        click_action = self._extract_action(text)
        if eval_answer == answer:
            return click_action
        else:
            return not click_action

    def solve_logic(self, text):
        return self._extract_action(text)

    def _extract_math_phrase(self, text):
        equals_index = text.index("=")
        left = []
        right = []
        for i in reversed(range(1, equals_index)):
            char = text[i]
            result = regexp.match(char)
            if result is not None:
                left.append(char)
            else:
                break

        for i in range(equals_index + 1, len(text)):
            char = text[i]
            result = regexp.match(char)
            if result is not None:
                right.append(char)
            else:
                break

        left_part = "".join(reversed(left)).strip()
        right_part = "".join(right).strip()
        eval_result = str(eval(left_part))
        print(
            f"Solver: Left part > {left_part}, right part > {right_part}, eval > {eval_result}, result > {eval_result == right_part}")
        return left_part, right_part, eval_result

    def _extract_action(self, text):
        words = text.lower().split()
        click_index = words.index("click")

        action = "".join(words[click_index + 1:click_index + 2])
        print("Solver: dialog click action > %s" % action)
        return len(action) <= 4
