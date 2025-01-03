# Constants
DAILY_FRUIT_PORTION_LIMIT = 2  # Maximum number of fruit portions per day

# Helper functions
def is_limited_fruit(food_name, category):
    return (category == 'Fruits' and 
            food_name not in ['Lemon', 'Lime'])  # These fruits are unlimited

# Define allowed foods by category with conversion information
ALLOWED_FOODS = {
    'Fruits': {
        'Lemon': {'portion': 'Unlimited', 'conversion': 'One medium lemon is approximately 58 grams'},
        'Lime': {'portion': 'Unlimited', 'conversion': 'One medium lime is approximately 67 grams'},
        'Banana': {
            'portion': '1/2 (max 2 portions of listed fruits per day)', 
            'conversion': 'Half a medium banana is approximately 60 grams',
            'max_per_meal': 60,  # grams (half banana)
            'max_per_day': 120   # grams (max 2 portions)
        },
        'Mixed Berries': {
            'portion': '1/2 cup (max 2 portions of listed fruits per day)',
            'conversion': 'Half a cup of mixed berries is approximately 75 grams',
            'max_per_meal': 75,  # grams (half cup)
            'max_per_day': 150   # grams (max 2 portions)
        },
        'Strawberries': {
            'portion': '1/2 cup (max 2 portions of listed fruits per day)',
            'conversion': 'Half a cup is approximately 75 grams, about 4 medium strawberries',
            'max_per_meal': 75,
            'max_per_day': 150
        },
        'Blueberries': {
            'portion': '1/2 cup (max 2 portions of listed fruits per day)',
            'conversion': 'Half a cup is approximately 74 grams, about 40 blueberries',
            'max_per_meal': 74,
            'max_per_day': 148
        },
        'Raspberries': {
            'portion': '1/2 cup (max 2 portions of listed fruits per day)',
            'conversion': 'Half a cup is approximately 62 grams, about 30 raspberries',
            'max_per_meal': 62,
            'max_per_day': 124
        },
        'Blackberries': {
            'portion': '1/2 cup (max 2 portions of listed fruits per day)',
            'conversion': 'Half a cup is approximately 72 grams, about 16 blackberries',
            'max_per_meal': 72,
            'max_per_day': 144
        },
        'Cherries': {
            'portion': '3 pieces (max 2 portions of listed fruits per day)',
            'conversion': '3 cherries is approximately 15 grams',
            'max_per_meal': 15,
            'max_per_day': 30
        },
        'Citrus': {
            'portion': '1 piece (max 2 portions of listed fruits per day)',
            'conversion': 'One medium orange is approximately 130 grams',
            'max_per_meal': 130,
            'max_per_day': 260
        },
        'Grapes': {
            'portion': '10 pieces (max 2 portions of listed fruits per day)',
            'conversion': '10 grapes is approximately 50 grams',
            'max_per_meal': 50,
            'max_per_day': 100
        },
        'Honeydew': {
            'portion': '1/4 cup (max 2 portions of listed fruits per day)',
            'conversion': 'Quarter cup of diced honeydew is approximately 40 grams',
            'max_per_meal': 40,
            'max_per_day': 80
        },
        'Pineapple': {
            'portion': '1/4 cup (max 2 portions of listed fruits per day)',
            'conversion': 'Quarter cup of diced pineapple is approximately 40 grams',
            'max_per_meal': 40,
            'max_per_day': 80
        },
        'Pomegranate': {
            'portion': '1/4 cup seeds (max 2 portions of listed fruits per day)',
            'conversion': 'Quarter cup of pomegranate seeds is approximately 35 grams',
            'max_per_meal': 35,
            'max_per_day': 70
        }
    },
    'Vegetables': {
        'Alfalfa sprouts': {'portion': 'Unlimited', 'conversion': '1 cup of sprouts is approximately 33 grams'},
        'Bamboo shoots': {'portion': 'Unlimited', 'conversion': '1 cup of shoots is approximately 120 grams'},
        'Bok choy': {'portion': 'Unlimited', 'conversion': '1 cup chopped is approximately 70 grams'},
        'Carrot': {'portion': 'Unlimited', 'conversion': '1 medium carrot is approximately 61 grams'},
        'Chives': {'portion': 'Unlimited', 'conversion': '1 tablespoon chopped is approximately 3 grams'},
        'Cucumber': {'portion': 'Unlimited', 'conversion': '1 cup sliced is approximately 120 grams'},
        'Eggplant': {'portion': 'Unlimited', 'conversion': '1 cup cubed is approximately 82 grams'},
        'Ginger': {'portion': 'Unlimited', 'conversion': '1 tablespoon minced is approximately 6 grams'},
        'Kale': {'portion': 'Unlimited', 'conversion': '1 cup chopped is approximately 67 grams'},
        'Lettuce': {'portion': 'Unlimited', 'conversion': '1 cup shredded is approximately 47 grams'},
        'Olives': {'portion': 'Unlimited', 'conversion': '10 medium olives is approximately 33 grams'},
        'Peppers': {'portion': 'Unlimited', 'conversion': '1 medium bell pepper is approximately 120 grams'},
        'Radicchio': {'portion': 'Unlimited', 'conversion': '1 cup shredded is approximately 40 grams'},
        'Radish': {'portion': 'Unlimited', 'conversion': '10 medium radishes is approximately 70 grams'},
        'Rocket': {'portion': 'Unlimited', 'conversion': '1 cup is approximately 20 grams'},
        'Spring onion': {'portion': 'Unlimited (green part only)', 'conversion': '1 spring onion (green part) is approximately 5 grams'},
        'Sunflower sprouts': {'portion': 'Unlimited', 'conversion': '1 cup is approximately 25 grams'},
        'Tomatoes': {
            'portion': '2 pieces',
            'conversion': '2 medium tomatoes is approximately 246 grams',
            'max_per_meal': 246,  # grams (2 tomatoes)
            'max_per_day': None   # No daily limit
        },
        'Asparagus': {
            'portion': '1 spear',
            'conversion': '1 medium spear is approximately 16 grams',
            'max_per_meal': 16,
            'max_per_day': None
        },
        'Artichoke hearts': {
            'portion': '1/8 cup',
            'conversion': '1/8 cup is approximately 20 grams',
            'max_per_meal': 20,
            'max_per_day': None
        },
        'Avocado': {
            'portion': '1/4 per day',
            'conversion': '1/4 avocado is approximately 50 grams',
            'max_per_meal': 50,   # grams (1/4 avocado)
            'max_per_day': 50     # grams (1/4 per day limit)
        },
        'Beetroot': {
            'portion': '2 slices',
            'conversion': '2 slices is approximately 30 grams',
            'max_per_meal': 30,
            'max_per_day': None
        },
        'Broccoli': {
            'portion': '1/2 cup',
            'conversion': '1/2 cup chopped is approximately 45 grams',
            'max_per_meal': 45,
            'max_per_day': None
        },
        'Brussels sprouts': {
            'portion': '2 pieces',
            'conversion': '2 medium sprouts is approximately 30 grams',
            'max_per_meal': 30,
            'max_per_day': None
        },
        'Cabbage': {
            'portion': '1/2 cup',
            'conversion': '1/2 cup shredded is approximately 35 grams',
            'max_per_meal': 35,
            'max_per_day': None
        },
        'Cabbage savoy': {
            'portion': '3/4 cup',
            'conversion': '3/4 cup shredded is approximately 50 grams',
            'max_per_meal': 50,
            'max_per_day': None
        },
        'Celery': {
            'portion': '1 stick',
            'conversion': '1 medium stick is approximately 40 grams',
            'max_per_meal': 40,
            'max_per_day': None
        },
        'Fennel bulb': {
            'portion': '1/2 cup',
            'conversion': '1/2 cup sliced is approximately 44 grams',
            'max_per_meal': 44,
            'max_per_day': None
        },
        'Green beans': {
            'portion': '10 beans',
            'conversion': '10 medium green beans is approximately 50 grams',
            'max_per_meal': 50,
            'max_per_day': None
        },
        'Peas': {
            'portion': '1/4 cup',
            'conversion': '1/4 cup is approximately 35 grams',
            'max_per_meal': 35,
            'max_per_day': None
        },
        'Pumpkin': {
            'portion': '1/4 cup',
            'conversion': '1/4 cup cubed is approximately 40 grams',
            'max_per_meal': 40,
            'max_per_day': None
        },
        'Snow peas': {
            'portion': '5 pods',
            'conversion': '5 pods is approximately 25 grams',
            'max_per_meal': 25,
            'max_per_day': None
        },
        'Spinach': {
            'portion': '15 leaves',
            'conversion': '15 medium leaves is approximately 30 grams',
            'max_per_meal': 30,
            'max_per_day': None
        },
        'Courgettes': {
            'portion': '3/4 cup',
            'conversion': '3/4 cup sliced is approximately 90 grams',
            'max_per_meal': 90,
            'max_per_day': None
        },
        'Leek': {
            'portion': '1/2 piece',
            'conversion': 'Half a medium leek is approximately 45 grams',
            'max_per_meal': 45,
            'max_per_day': None
        }
    },
    'Grains': {
        'White Rice': {
            'portion': '1/2 cup cooked',
            'conversion': 'Half a cup of cooked rice is approximately 30 grams of raw rice',
            'max_per_meal': 30,   # grams of raw rice
            'max_per_day': None
        },
        'Quinoa': {
            'portion': '1/2 cup cooked',
            'conversion': 'Half a cup of cooked quinoa is approximately 35 grams of raw quinoa',
            'max_per_meal': 35,   # grams of raw quinoa
            'max_per_day': None
        }
    },
    'Nuts': {
        'Almond flour': {
            'portion': '1/4 cup',
            'conversion': 'Quarter cup of almond flour is approximately 28 grams',
            'max_per_meal': 28,
            'max_per_day': 28
        },
        'Coconut flour': {
            'portion': '1/4 cup (flour/shredded)',
            'conversion': 'Quarter cup of shredded coconut is approximately 20 grams',
            'max_per_meal': 20,
            'max_per_day': 20
        },
        'Macadamias': {
            'portion': '20 nuts',
            'conversion': '20 macadamia nuts is approximately 28 grams',
            'max_per_meal': 28,
            'max_per_day': 28
        },
        'Pine nuts': {
            'portion': '1 tbsp',
            'conversion': '1 tablespoon of pine nuts is approximately 9 grams',
            'max_per_meal': 9,
            'max_per_day': 9
        },
        'Almonds': {
            'portion': '20 nuts',
            'conversion': '20 whole almonds is approximately 24 grams',
            'max_per_meal': 24,
            'max_per_day': 24
        },
        'Almond milk': {
            'portion': '1 cup',
            'conversion': '1 cup is approximately 240 ml',
            'max_per_meal': 240,
            'max_per_day': 240
        }
    },
    'Oils': {
        'Garlic infused oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 15 grams'
        },
        'Chili infused oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 15 grams'
        },
        'Flax oil': {
            'portion': 'Unlimited (low lignin)',
            'conversion': '1 tablespoon is approximately 14 grams'
        },
        'Grapeseed oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 14 grams'
        },
        'MCT oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 14 grams'
        },
        'Olive oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 13.5 grams'
        },
        'Polyunsaturated vegetable oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 14 grams'
        },
        'Pumpkin seed oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 14 grams'
        },
        'Sesame oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 13.6 grams'
        },
        'Sunflower oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 14 grams'
        },
        'Walnut oil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 14 grams'
        }
    },
    'Sweeteners': {
        'Raw honey': {
            'portion': '1 tbsp per day',
            'conversion': '1 tablespoon of honey is approximately 21 grams',
            'max_per_meal': 21,
            'max_per_day': 21
        },
        'Stevia': 'Unlimited',
        'Coconut sugar': {
            'portion': '1 tbsp per day',
            'conversion': '1 tablespoon of coconut sugar is approximately 12 grams',
            'max_per_meal': 12,
            'max_per_day': 12
        },
        'Monk fruit sweetener': 'Unlimited'
    },
    'Beverages': {
        'Coffee': {
            'portion': '1 cup per day',
            'conversion': '1 cup is approximately 240 ml',
            'max_per_meal': 240,
            'max_per_day': 240
        },
        'Herbal tea': {
            'portion': 'Unlimited',
            'conversion': '1 cup is approximately 240 ml',
            'max_per_meal': None,
            'max_per_day': None
        }
    },
    'Condiments': {
        'Turmeric': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon fresh is approximately 6 grams, 1 teaspoon dried is approximately 2 grams'
        },
        'Cinnamon': {
            'portion': 'Unlimited',
            'conversion': '1 teaspoon ground is approximately 2.6 grams'
        },
        'Salt': {
            'portion': 'Unlimited',
            'conversion': '1 teaspoon is approximately 6 grams'
        },
        'Pepper': {
            'portion': 'Unlimited',
            'conversion': '1 teaspoon ground is approximately 2.3 grams'
        },
        # Fresh herbs
        'Fresh Basil': {
            'portion': 'Unlimited',
            'conversion': '1 cup loosely packed is approximately 24 grams, 10 medium leaves is about 5 grams'
        },
        'Fresh Oregano': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon chopped is approximately 3 grams'
        },
        'Fresh Thyme': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon leaves is approximately 2 grams'
        },
        'Fresh Rosemary': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon chopped is approximately 4 grams'
        },
        'Fresh Sage': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon chopped is approximately 3 grams'
        },
        'Fresh Mint': {
            'portion': 'Unlimited',
            'conversion': '1 cup loosely packed is approximately 20 grams'
        },
        'Fresh Parsley': {
            'portion': 'Unlimited',
            'conversion': '1 cup chopped is approximately 60 grams'
        },
        'Fresh Cilantro': {
            'portion': 'Unlimited',
            'conversion': '1 cup loosely packed is approximately 16 grams'
        },
        'Fresh Dill': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon chopped is approximately 3 grams'
        },
        'Fresh Chives': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon chopped is approximately 3 grams'
        },
        'Fresh Tarragon': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon chopped is approximately 3 grams'
        },
        # Dried herbs
        'Dried Basil': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 5.4 grams'
        },
        'Dried Oregano': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 5.7 grams'
        },
        'Dried Thyme': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 5.3 grams'
        },
        'Dried Rosemary': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 4.8 grams'
        },
        'Dried Sage': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 5.0 grams'
        },
        'Dried Parsley': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 3.8 grams'
        },
        'Dried Dill': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon is approximately 4.2 grams'
        },
        'Italian Herbs': {
            'portion': 'Unlimited',
            'conversion': '1 tablespoon mixed dried herbs is approximately 5 grams'
        },
        'Vanilla': {
            'portion': 'Unlimited',
            'conversion': '1 teaspoon vanilla extract is approximately 4.2 grams, 1 vanilla bean is approximately 5 grams'
        },
        'Bicarbonate of soda': {
            'portion': 'Unlimited',
            'conversion': '1 teaspoon is approximately 4.8 grams'
        }
    },
    'Proteins': {
        'Lean fresh lamb': {
            'portion': 'Unlimited',
            'conversion': 'A typical serving (100 grams) is about the size of a deck of cards'
        },
        'Lean fresh beef': {
            'portion': 'Unlimited',
            'conversion': 'A typical serving (100 grams) is about the size of a deck of cards'
        },
        'Lean fresh chicken': {
            'portion': 'Unlimited',
            'conversion': 'A medium chicken breast is approximately 150-200 grams'
        },
        'Fresh fish': {
            'portion': 'Unlimited',
            'conversion': 'A typical serving (100 grams) is about the size of a checkbook'
        },
        'Prawns': {
            'portion': 'Unlimited',
            'conversion': '10 medium prawns is approximately 90-100 grams'
        },
        'Mussels': {
            'portion': 'Unlimited',
            'conversion': '10-12 mussels (without shell) is approximately 100 grams'
        },
        'Oysters': {
            'portion': 'Unlimited',
            'conversion': '6 medium oysters (meat only) is approximately 100 grams'
        },
        'Scallops': {
            'portion': 'Unlimited',
            'conversion': '6 medium scallops is approximately 90 grams'
        },
        'Crab': {
            'portion': 'Unlimited',
            'conversion': '100 grams of crab meat is approximately 1 cup of flaked meat'
        },
        'Lobster': {
            'portion': 'Unlimited',
            'conversion': '100 grams of lobster meat is approximately 3/4 cup of chopped meat'
        },
        'Clams': {
            'portion': 'Unlimited',
            'conversion': '10 small clams (meat only) is approximately 85 grams'
        },
        'Lean fresh pork': {
            'portion': 'Unlimited',
            'conversion': 'A typical serving (100 grams) is about the size of a deck of cards'
        },
        'Eggs': {
            'portion': 'Unlimited',
            'conversion': 'One large egg is approximately 50 grams'
        },
        'Collagen': {
            'portion': '10g',
            'conversion': '1 tablespoon of collagen powder is approximately 11 grams'
        }
    }
} 