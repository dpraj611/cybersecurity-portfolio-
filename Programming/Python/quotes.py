import random

# Define lists of quotes for each category
motivational_quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Everything you’ve ever wanted is on the other side of fear. - George Addair",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t wait for opportunity. Create it.",
    "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
    "The key to success is to focus on goals, not obstacles.",
    "Dream bigger. Do bigger.",
    "No one is to blame for your future situation but yourself.",
    "Your goals don’t care how you feel.",
    "Doubt kills more dreams than failure ever will.",
    "If it doesn’t challenge you, it won’t change you.",
    "The man who has confidence in himself gains the confidence of others.",
    "What’s meant to be will always find a way.",
    "Believe in yourself and you will be unstoppable.",
    "Don’t trade your authenticity for approval.",
    "Sometimes the best way to be happy is to learn to let go.",
    "It’s never too late for a new beginning in your life.",
    "Don’t wait for the perfect moment. Take the moment and make it perfect.",
    "Start where you are. Use what you have. Do what you can.",
    "I will not lose, for even in defeat, there’s a valuable lesson learned.",
    "It’s not whether you get knocked down, it’s whether you get up. - Vince Lombardi",
    "Failure is the condiment that gives success its flavor. - Truman Capote",
    "Our greatest glory is not in never falling, but in rising every time we fall. - Confucius",
    "What seems to us as bitter trials are often blessings in disguise. - Oscar Wilde",
    "Your passion is waiting for your courage to catch up.",
    "Success is what happens after you have survived your disappointments.",
    "Your only limit is your mind."
]

sad_quotes = [
    "Tears come from the heart and not from the brain. - Leonardo da Vinci",
    "It's hard to forget someone who gave you so much to remember.",
    "Sometimes, the hardest part isn't letting go but learning to start over.",
    "The pain of parting is nothing to the joy of meeting again. - Charles Dickens",
    "It is better to have loved and lost than never to have loved at all. - Alfred Lord Tennyson",
    "Behind every sweet smile, there is a bitter sadness that no one can ever see and feel.",
    "Sadness flies away on the wings of time. - Jean de La Fontaine",
    "The greatest pain that comes from love is loving someone you can never have.",
    "When you're feeling down, remember that even the darkest night will end and the sun will rise.",
    "Every heart has a pain. Only the way of expression is different.",
    "The sorrow we feel when we lose a loved one is the price we pay to have had them in our lives.",
    "When you are feeling low, look at the sky and remember that every storm eventually ends.",
    "Sometimes, you have to let go to see if there was anything worth holding on to.",
    "It's okay to be sad. Sometimes, it helps to cry it out.",
    "The only thing more exhausting than being depressed is pretending that you're not.",
    "Sadness is a natural part of life, but remember, it's just a passing phase.",
    "It's okay to feel sad, just don't let it define you.",
    "The darkest hour has only sixty minutes. - Morris Mandel",
    "Embrace the sadness; it's a part of the healing process.",
    "People cry not because they are weak. It's because they have been strong for too long.",
    "Sometimes the wrong choices bring us to the right places.",
    "You can’t always be strong. Sometimes you just need to be alone and let your tears out.",
    "Sadness is but a wall between two gardens. - Khalil Gibran",
    "You cannot protect yourself from sadness without protecting yourself from happiness. - Jonathan Safran Foer",
    "Heavy hearts, like heavy clouds in the sky, are best relieved by the letting of a little water. - Christopher Morley",
    "It’s always darkest before the dawn.",
    "We must understand that sadness is an ocean, and sometimes we drown, while other days we are forced to swim.",
    "Sadness is a part of life, but so is joy.",
    "It’s okay to be sad, but it’s not okay to give up.",
    "Crying is how your heart speaks, when your lips can’t explain the pain you feel.",
    "Some days are just bad days, that’s all.",
    "The soul would have no rainbow had the eyes no tears.",
    "Tears are words the heart can't express.",
    "Sometimes you have to know that not every fight is worth fighting.",
    "The way sadness works is one of the strange riddles of the world.",
    "The walls we build around us to keep sadness out also keep out the joy. - Jim Rohn",
    "Even the strongest feelings expire when ignored and taken for granted.",
    "Sometimes we need to be sad to remind ourselves how much we truly love life.",
    "Sadness gives depth. Happiness gives height.",
    "Sometimes you just need to be alone, not to be lonely, but to enjoy your free time being yourself.",
    "Pain is inevitable. Suffering is optional.",
    "Some of us think holding on makes us strong, but sometimes it is letting go.",
    "Sadness is an emotion we must experience to understand happiness.",
    "Healing doesn’t mean the damage never existed. It means the damage no longer controls your life.",
    "Pain is temporary, but quitting lasts forever.",
    "Allow yourself to feel, even if it hurts. It’s the first step to healing."
]

happy_quotes = [
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "The best way to cheer yourself up is to try to cheer somebody else up. - Mark Twain",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Happiness depends upon ourselves. - Aristotle",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Happiness is not by chance, but by choice. - Jim Rohn",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a direction, not a place. - Sydney J. Harris",
    "If you want to be happy, be. - Leo Tolstoy",
    "Happiness is a journey, not a destination. - Ben Sweetland",
    "The more you praise and celebrate your life, the more there is in life to celebrate. - Oprah Winfrey",
    "Happiness is not a goal...it's a by-product of a life well-lived. - Eleanor Roosevelt",
    "Happiness is the highest good. - Aristotle",
    "Joy is not in things; it is in us. - Richard Wagner",
    "A smile is the best makeup any girl can wear. - Marilyn Monroe",
    "Happiness is the best revenge. - Unknown",
    "There is only one happiness in this life, to love and be loved. - George Sand",
    "Happiness is like a butterfly. The more you chase it, the more it will elude you. - Henry David Thoreau",
    "Happiness is a choice, not a result. Nothing will make you happy until you choose to be happy. - Ralph Marston",
    "Be happy for this moment. This moment is your life.",
    "Happiness is a state of mind. It's just according to the way you look at things. - Walt Disney",
    "Smile, and the world smiles with you.",
    "True happiness arises, in the first place, from the enjoyment of one’s self. - Joseph Addison",
    "The happiest people don’t have the best of everything, they just make the best of everything.",
    "You do not find a happy life. You make it.",
    "Happiness is not a destination. It is a way of life.",
    "Happiness is the secret to all beauty. There is no beauty without happiness. - Christian Dior",
    "Happiness is not a matter of intensity but of balance, order, rhythm, and harmony. - Thomas Merton",
    "Happiness comes in waves. It’ll find you again.",
    "To be happy, one must be forgiving and loving.",
    "A happy soul is the best shield for a cruel world.",
    "Doing what you like is freedom. Liking what you do is happiness.",
    "Some cause happiness wherever they go; others whenever they go. - Oscar Wilde",
    "Happiness is contagious, spread it around.",
    "Happiness looks good on you!",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Nothing can dim the light that shines from within. - Maya Angelou",
    "Think of all the beauty still left around you and be happy. - Anne Frank",
    "Happiness is an inside job. Don’t assign anyone else that much power over your life.",
    "Let your smile change the world, but don’t let the world change your smile.",
    "Be crazy, be stupid, be silly, be weird. Be whatever, because life is too short to be anything but happy.",
    "You deserve to be happy. Don’t let anyone tell you otherwise.",
    "Happiness is a habit—cultivate it.",
    "Happiness starts with you—not with your relationships, not with your job, not with your money, but with you."
]

def get_random_quote(category):
    """Return a random quote from the specified category."""
    if category == 1:
        return random.choice(motivational_quotes)
    elif category == 2:
        return random.choice(sad_quotes)
    elif category == 3:
        return random.choice(happy_quotes)
    else:
        return "Oops! Looks like you picked the wrong category. Try 1 for motivational, 2 for sad, or 3 for happy."

def main():
    print("Welcome to the Quote Generator Extravaganza!")
    print("Choose your mood:")
    print("1 - Motivational (Because we all need a push!)")
    print("2 - Sad (For those rainy days and gloomy vibes.)")
    print("3 - Happy (For when you just want to smile!)")
    
    try:
        user_choice = int(input("Pick a number to get your quote (1, 2, or 3): "))
        quote = get_random_quote(user_choice)
        print("\nHere's your quote of the moment:")
        print(quote)
    except ValueError:
        print("Oops! That’s not a number. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
