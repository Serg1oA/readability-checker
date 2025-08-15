# readability.py
import textstat

def calculate_readability(text):
    """
    Calculates various readability scores for the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing the readability scores.
    """
    try:
        flesch_reading_ease = textstat.flesch_reading_ease(text)
        flesch_kincaid_grade = textstat.flesch_kincaid_grade(text)
        smog_index = textstat.smog_index(text)
        coleman_liau_index = textstat.coleman_liau_index(text)
        automated_readability_index = textstat.automated_readability_index(text)
        dale_chall_readability_score = textstat.dale_chall_readability_score(text)
        difficult_words = textstat.difficult_words(text)
        linsear_write_formula = textstat.linsear_write_formula(text)
        gunning_fog = textstat.gunning_fog(text)
        text_standard = textstat.text_standard(text)

        return {
            'Text Standard': text_standard,
            'Difficult Words': difficult_words,
            'Flesch Reading Ease': flesch_reading_ease,
            'Flesch Kincaid Grade': flesch_kincaid_grade,
            'SMOG Index': smog_index,
            'Coleman-Liau Index': coleman_liau_index,
            'Automated Readability Index': automated_readability_index,
            'Dale-Chall Readability Score': dale_chall_readability_score,
            'Linsear Write Formula': linsear_write_formula,
            'Gunning Fog': gunning_fog
        }
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    text = """The Australian platypus is an odd animal and is quite different from the other animals in the world.
    Its snout is like a duck’s bill, it has webbed feet and a beaver’s tail."""
    scores = calculate_readability(text)
    for key, value in scores.items():
        print(f"{key}: {value}")