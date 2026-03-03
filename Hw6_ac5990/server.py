from flask import Flask, render_template, request, jsonify

#new instance
app = Flask(__name__)

##-------------------DATASET------------------------------------------
data = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "cover": "https://m.media-amazon.com/images/I/81kg51XRc1L._AC_UF1000,1000_QL80_.jpg",
        "year": 2018,
        "summary": (
            "Clear argues that focusing on systems over goals and making tiny changes "
            "(like doing two push-ups a day) leads to remarkable results over time, using "
            "a framework based on the 'Four Laws of Behavior Change': Make it Obvious, "
            "Attractive, Easy, and Satisfying. The book provides practical strategies, "
            "drawing from psychology and neuroscience, to help readers master their daily "
            "routines and transform their lives."
        ),
        "author": ["James Clear"],
        "awards": ["2018 Goodreads Choice Award Semifinalist for Best Nonfiction"],
        "sales": 20_000_000,
        "score": 4.0,
        "category": ["personal growth", "habit building", "productivity"],
        "subcategory": ["habit formation", "behavior change", "self-improvement", "productivity performance"],
        "similar_book_ids": [4, 5],
    },
    {
        "id": 2,
        "title": "The 7 Habits of Highly Effective People",
        "cover": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScvG5V45V-ycac_VpPlDtLl6bbiaOC4OkR6Q&s",
        "year": 1989,
        "summary": (
            "Covey presents a principle-centered approach to personal and professional "
            "effectiveness, outlining seven habits that move individuals from dependence "
            "to independence to interdependence. Drawing on timeless character ethics, the "
            "book teaches readers to be proactive, prioritize what matters most, seek mutual "
            "benefit, and continually renew themselves across physical, mental, emotional, "
            "and spiritual dimensions."
        ),
        "author": ["Stephen R. Covey"],
        "awards": ["Named #1 Most Influential Business Book of the 20th Century by Forbes"],
        "sales": 40_000_000,
        "score": 4.5,
        "category": ["personal growth", "productivity", "leadership"],
        "subcategory": ["effectiveness", "character development", "time management", "interpersonal skills"],
        "similar_book_ids": [3, 6],
    },
    {
        "id": 3,
        "title": "How to Win Friends and Influence People",
        "cover": "https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781982171452/how-to-win-friends-and-influence-people-9781982171452_hr.jpg",
        "year": 1936,
        "summary": (
            "Carnegie outlines timeless principles for building meaningful relationships and "
            "influencing others through genuine appreciation, active listening, and empathy "
            "rather than manipulation. The book offers practical techniques for handling "
            "people, winning them to your way of thinking, and becoming a more effective "
            "communicator in both personal and professional settings."
        ),
        "author": ["Dale Carnegie"],
        "awards": ["One of Time Magazine's 100 Most Influential Books"],
        "sales": 30_000_000,
        "score": 4.0,
        "category": ["personal growth", "communication", "relationships"],
        "subcategory": ["social skills", "persuasion", "networking", "empathy"],
        "similar_book_ids": [2, 7],
    },
    {
        "id": 4,
        "title": "Think and Grow Rich",
        "cover": "https://m.media-amazon.com/images/I/71UypkUjStL._AC_UF1000,1000_QL80_.jpg",
        "year": 1937,
        "summary": (
            "Hill distills lessons from interviews with over 500 successful individuals "
            "including Carnegie and Edison into 13 principles for achieving wealth and "
            "success, centered around the power of desire, faith, and a definite plan. "
            "The book emphasizes the role of mindset, persistence, and the subconscious "
            "mind in turning thoughts into tangible achievement."
        ),
        "author": ["Napoleon Hill"],
        "awards": ["One of the Best-Selling Books of All Time"],
        "sales": 100_000_000,
        "score": 4.0,
        "category": ["personal growth", "wealth", "mindset"],
        "subcategory": ["success principles", "motivation", "goal setting", "financial mindset"],
        "similar_book_ids": [1, 5],
    },
    {
        "id": 5,
        "title": "The Power of Now",
        "cover": "https://upload.wikimedia.org/wikipedia/en/6/66/TPON_Cover_LG.jpg",
        "year": 1997,
        "summary": (
            "Tolle guides readers toward spiritual enlightenment by teaching them to detach "
            "from the incessant chatter of the mind and live fully in the present moment. "
            "The book blends Eastern philosophy and Western psychology to show how ego-driven "
            "thinking causes suffering, and how embracing the 'Now' leads to inner peace, "
            "clarity, and genuine transformation."
        ),
        "author": ["Eckhart Tolle"],
        "awards": ["New York Times Bestseller", "Recommended by Oprah Winfrey"],
        "sales": 3_000_000,
        "score": 4.0,
        "category": ["mindfulness", "spirituality", "personal growth"],
        "subcategory": ["present moment awareness", "meditation", "ego dissolution", "mental clarity"],
        "similar_book_ids": [1, 8],
    },
    {
        "id": 6,
        "title": "Deep Work",
        "cover": "https://m.media-amazon.com/images/I/71QKQ9mwV7L._AC_UF1000,1000_QL80_.jpg",
        "year": 2016,
        "summary": (
            "Newport argues that the ability to focus without distraction on cognitively "
            "demanding tasks — what he calls 'deep work' — is becoming increasingly rare "
            "and increasingly valuable in our economy. He provides rules and strategies for "
            "cultivating this skill, including scheduling deep work blocks, embracing boredom, "
            "quitting social media, and draining the shallows of your professional life."
        ),
        "author": ["Cal Newport"],
        "awards": ["Wall Street Journal Bestseller"],
        "sales": 1_000_000,
        "score": 4.5,
        "category": ["productivity", "focus", "professional development"],
        "subcategory": ["concentration", "distraction management", "deliberate practice", "time management"],
        "similar_book_ids": [1, 2],
    },
    {
        "id": 7,
        "title": "Man's Search for Meaning",
        "cover": "https://m.media-amazon.com/images/I/81UhnGT7BvL._AC_UF1000,1000_QL80_.jpg",
        "year": 1946,
        "summary": (
            "Psychiatrist and Holocaust survivor Viktor Frankl recounts his experiences in "
            "Nazi concentration camps and introduces logotherapy, a form of psychotherapy "
            "based on the idea that the primary human drive is the search for meaning. The "
            "book argues that even in the most dehumanizing conditions, individuals can "
            "choose their attitude and find purpose, making it one of the most profound "
            "works on resilience and the human spirit."
        ),
        "author": ["Viktor E. Frankl"],
        "awards": ["One of the Ten Most Influential Books in the United States (Library of Congress)"],
        "sales": 16_000_000,
        "score": 5.0,
        "category": ["mindset", "resilience", "personal growth"],
        "subcategory": ["meaning making", "existentialism", "psychological resilience", "mental health"],
        "similar_book_ids": [3, 5],
    },
    {
        "id": 8,
        "title": "Mindset: The New Psychology of Success",
        "cover": "https://m.media-amazon.com/images/I/71h937MExWL._AC_UF1000,1000_QL80_.jpg",
        "year": 2006,
        "summary": (
            "Stanford psychologist Carol Dweck introduces the concept of 'fixed' versus "
            "'growth' mindsets, showing through decades of research how our beliefs about "
            "our own abilities shape our success in school, work, sports, and relationships. "
            "The book teaches readers how to cultivate a growth mindset that embraces "
            "challenges, persists through setbacks, and sees effort as the path to mastery."
        ),
        "author": ["Carol S. Dweck"],
        "awards": ["Goodreads Choice Award Nominee"],
        "sales": 2_000_000,
        "score": 4.5,
        "category": ["mindset", "personal growth", "psychology"],
        "subcategory": ["growth mindset", "learning", "resilience", "self-belief"],
        "similar_book_ids": [7, 1],
    },
    {
        "id": 9,
        "title": "The Subtle Art of Not Giving a F*ck",
        "cover": "https://m.media-amazon.com/images/I/71QKQ9mwV7L._AC_UF1000,1000_QL80_.jpg",
        "year": 2016,
        "summary": (
            "Manson takes a counterintuitive approach to self-help, arguing that the key "
            "to a good life is not pursuing more positivity but rather getting better at "
            "handling adversity by choosing what truly matters to you. Drawing on philosophy, "
            "psychology, and his own life experiences, he challenges readers to stop chasing "
            "happiness and instead embrace struggle, uncertainty, and personal responsibility."
        ),
        "author": ["Mark Manson"],
        "awards": ["2016 Goodreads Choice Award Nominee for Self Help"],
        "sales": 12_000_000,
        "score": 4.0,
        "category": ["personal growth", "mindset", "philosophy"],
        "subcategory": ["values", "responsibility", "emotional resilience", "life philosophy"],
        "similar_book_ids": [7, 5],
    },
    {
        "id": 10,
        "title": "Can't Hurt Me",
        "cover": "https://m.media-amazon.com/images/I/81pIGKnME8L._AC_UF1000,1000_QL80_.jpg",
        "year": 2018,
        "summary": (
            "Former Navy SEAL David Goggins shares his journey from a traumatic childhood "
            "and obesity to becoming one of the world's top endurance athletes, revealing "
            "how mastering the mind is the key to overcoming any obstacle. Through his "
            "'accountability mirror,' the '40% rule,' and other mental tools, he challenges "
            "readers to push far beyond their perceived limits and unlock their true potential."
        ),
        "author": ["David Goggins"],
        "awards": ["New York Times Bestseller", "Audible Audiobook of the Year 2018"],
        "sales": 4_000_000,
        "score": 4.5,
        "category": ["mindset", "resilience", "personal growth"],
        "subcategory": ["mental toughness", "discipline", "overcoming adversity", "motivation"],
        "similar_book_ids": [7, 8],
    },
]


@app.route('/')
def homepage():
    return render_template('index.html', data=data)

@app.route('/view/<id>')
def details(id):
    return render_template('detail.html', data=data, id=id)

@app.route('/search', methods=['POST'])
def search_action():
    if request.method == 'POST':
        query = request.form.get('query').lower()
        results = [b for b in data if query in b['title'].lower()]
        return render_template('search.html', results=results, query=query)


if __name__ == '__main__':
    app.run(debug=True)

