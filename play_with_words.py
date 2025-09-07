import random

# ✅ Word list with hints
words_with_hints = [
    # Birds 
    ("sparrow", "A small, chirpy bird found in cities and villages"),
    ("peacock", "India's national bird known for its colorful feathers"),
    ("eagle", "A powerful bird of prey with sharp vision"),
    ("parrot", "A colorful bird known for mimicking human speech"),
    ("owl", "A nocturnal bird with excellent night vision"),
    ("kingfisher", "A bird that dives into water to catch fish"),
    ("woodpecker", "A bird that pecks at tree trunks to find insects"),
    ("crane", "A tall bird often seen near wetlands"),
    ("flamingo", "A pink bird that stands on one leg"),
    ("penguin", "A flightless bird that swims in icy waters"),


    # Fruits
    ("apple", "A red or green fruit that keeps doctors away"),
    ("banana", "A long yellow fruit monkeys love"),
    ("mango", "A juicy tropical fruit, king of summer"),
    ("orange", "A citrus fruit rich in vitamin C"),
    ("grape", "Small round fruit, used to make wine"),
    ("papaya", "Orange-fleshed tropical fruit"),
    ("pineapple", "Spiky outside, sweet inside"),
    ("watermelon", "Large green fruit with red juicy flesh"),
    ("kiwi", "Brown fuzzy skin, green inside"),
    ("guava", "Tropical fruit with pink or white flesh"),
    ("pomegranate", "Red fruit full of juicy seeds"),
    ("lychee", "Small fruit with white flesh and red skin"),
    ("jackfruit", "Large fruit with yellow pods inside"),
    ("plum", "Small purple fruit with a pit"),
    ("cherry", "Tiny red fruit often on cakes"),
    ("pear", "Bell-shaped fruit, sweet and juicy"),
    ("coconut", "Hard shell, white flesh, tropical vibe"),
    ("fig", "Soft fruit with tiny seeds inside"),
    ("blueberry", "Small blue fruit, often in muffins"),
    ("strawberry", "Red fruit with seeds on the outside"),

    # Trees
    ("neem", "Medicinal tree with bitter leaves"),
    ("banyan", "Tree with aerial roots and wide canopy"),
    ("oak", "Strong hardwood tree, symbol of strength"),
    ("pine", "Evergreen tree with needle-like leaves"),
    ("teak", "Valuable timber tree"),
    ("mango tree", "Tree that bears sweet summer fruits"),
    ("coconut tree", "Tall tropical tree with large nuts"),
    ("palm", "Tropical tree often seen on beaches"),
    ("bamboo", "Fast-growing grass used in construction"),
    ("gulmohar", "Tree with bright red-orange flowers"),
    ("eucalyptus", "Aromatic tree used in oils"),
    ("sandalwood", "Tree known for fragrant wood"),
    ("peepal", "Sacred tree in Indian culture"),
    ("cherry tree", "Tree that blossoms with pink flowers"),
    ("apple tree", "Tree that gives crunchy fruits"),
    ("jacaranda", "Tree with purple blossoms"),
    ("deodar", "Himalayan cedar tree"),
    ("mahogany", "Tree with reddish-brown wood"),
    ("sal", "Tree used in furniture making"),
    ("rubber tree", "Source of natural latex"),

    # Animals
    ("lion", "King of the jungle"),
    ("tiger", "Striped big cat"),
    ("elephant", "Largest land animal with a trunk"),
    ("dog", "Loyal domestic pet"),
    ("cat", "Furry pet that purrs"),
    ("horse", "Used for riding and racing"),
    ("cow", "Gives milk"),
    ("buffalo", "Strong farm animal"),
    ("goat", "Climbs hills and gives milk"),
    ("sheep", "Wool-producing animal"),
    ("monkey", "Climbs trees and loves bananas"),
    ("deer", "Graceful animal with antlers"),
    ("fox", "Clever wild animal"),
    ("rabbit", "Small animal with long ears"),
    ("camel", "Desert animal with humps"),
    ("zebra", "Horse-like animal with black and white stripes"),
    ("bear", "Large furry animal, loves honey"),
    ("wolf", "Wild ancestor of dogs"),
    ("kangaroo", "Hops and carries babies in a pouch"),
    ("dolphin", "Intelligent sea mammal"),

    # Vegetables
    ("carrot", "Orange root vegetable"),
    ("potato", "Starchy vegetable used in fries"),
    ("tomato", "Red juicy vegetable (technically a fruit)"),
    ("onion", "Makes you cry while chopping"),
    ("garlic", "Pungent bulb used in cooking"),
    ("spinach", "Leafy green full of iron"),
    ("cabbage", "Round leafy vegetable"),
    ("cauliflower", "White flower-like vegetable"),
    ("broccoli", "Green tree-like vegetable"),
    ("beetroot", "Red root vegetable"),
    ("radish", "White crunchy root"),
    ("pumpkin", "Large orange vegetable"),
    ("cucumber", "Cool and refreshing"),
    ("brinjal", "Purple vegetable also called eggplant"),
    ("peas", "Small green balls in pods"),
    ("corn", "Yellow kernels on a cob"),
    ("ladyfinger", "Slim green vegetable also called okra"),
    ("turnip", "Round root vegetable"),
    ("chili", "Spicy vegetable used in curries"),
    ("ginger", "Spicy root used in tea and cooking"),

    # Objects
    ("chair", "You sit on it"),
    ("table", "Used for eating or working"),
    ("pencil", "Used for writing and drawing"),
    ("book", "Contains pages of knowledge"),
    ("clock", "Tells time"),
    ("phone", "Used to call and text"),
    ("fan", "Keeps you cool"),
    ("bulb", "Lights up a room"),
    ("mirror", "Reflects your image"),
    ("comb", "Used to style hair"),
    ("bottle", "Holds water or drinks"),
    ("bag", "Used to carry things"),
    ("umbrella", "Protects from rain"),
    ("shoes", "Worn on feet"),
    ("key", "Opens locks"),
    ("door", "Entry to a room"),
    ("window", "Lets in light and air"),
    ("towel", "Used to dry yourself"),
    ("soap", "Used for cleaning"),
    ("brush", "Used for painting or cleaning")
]

# ✅ Track available words to avoid repeats
available_words = words_with_hints.copy()
# Game state variables

lives_remaining = 5
guessed_letters = ''

def pick_a_word():
    global available_words
    if not available_words:
        print("All words have been used. Restarting the list.")
        available_words = words_with_hints.copy()
    word_hint = random.choice(available_words)
    available_words.remove(word_hint)
    return word_hint

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '-'
    print("Word:", display_word)

def get_guess(word):
    print_word_with_blanks(word)
    print("Lives Remaining:", lives_remaining)
    return input("Guess a letter or the whole word: ").lower()

def all_letters_guessed(word):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def whole_word_guess(guess, word):
    global lives_remaining
    if guess == word:
        return True
    else:
        lives_remaining -= 1
        return False

def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if guess in guessed_letters:
        print("You already guessed that letter.")
        return False
    guessed_letters += guess
    if guess not in word:
        lives_remaining -= 1
    return all_letters_guessed(word)

def process_guess(guess, word):
    if len(guess) > 1:
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)

def play():
    global guessed_letters, lives_remaining
    word, hint = pick_a_word()
    guessed_letters = ''
    lives_remaining = 5
    print("\n🔍 Hint:", hint)
    print("📏 The word has", len(word), "letters.")
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print("🎉 You win! Well done!")
            break
        if lives_remaining == 0:
            print("💀 You are Hung!")
            print("The word was:", word)
            break   
play()