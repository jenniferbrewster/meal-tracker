"""
Nutritional values per 100g of food
Source: USDA FoodData Central (https://fdc.nal.usda.gov/)
"""

FOOD_NUTRIENTS = {
    'Vegetables': {
        'Spinach': {  # Raw spinach, USDA #11457
            'calories': 23,
            'protein': 2.86,
            'fat': 0.39,
            'carbs': 3.63,
            'fiber': 2.2
        },
        'Broccoli': {  # Raw broccoli, USDA #11090
            'calories': 34,
            'protein': 2.82,
            'fat': 0.37,
            'carbs': 6.64,
            'fiber': 2.6
        },
        'Leek': {  # Raw leek, USDA #11246
            'calories': 61,
            'protein': 1.5,
            'fat': 0.3,
            'carbs': 14.15,
            'fiber': 1.8
        },
        'Cucumber': {  # Raw cucumber with peel, USDA #11205
            'calories': 15,
            'protein': 0.65,
            'fat': 0.11,
            'carbs': 3.63,
            'fiber': 0.5
        },
        'Avocado': {  # Raw avocado, USDA #09037
            'calories': 160,
            'protein': 2,
            'fat': 14.66,
            'carbs': 8.53,
            'fiber': 6.7
        },
        'Carrot': {  # Raw carrot, USDA #11124
            'calories': 41,
            'protein': 0.93,
            'fat': 0.24,
            'carbs': 9.58,
            'fiber': 2.8
        },
        'Celery': {  # Raw celery, USDA #11143
            'calories': 16,
            'protein': 0.69,
            'fat': 0.17,
            'carbs': 2.97,
            'fiber': 1.6
        },
        'Green beans': {  # Raw green beans, USDA #11052
            'calories': 31,
            'protein': 1.83,
            'fat': 0.22,
            'carbs': 7.07,
            'fiber': 3.4
        },
        'Pumpkin': {  # Raw pumpkin, USDA #11422
            'calories': 26,
            'protein': 1,
            'fat': 0.1,
            'carbs': 6.5,
            'fiber': 0.5
        },
        'Radicchio': {  # Raw radicchio
            'calories': 23,
            'protein': 1.4,
            'fat': 0.2,
            'carbs': 4.5,
            'fiber': 2.0
        },
        'Rocket': {  # Raw rocket/arugula
            'calories': 25,
            'protein': 2.6,
            'fat': 0.7,
            'carbs': 3.7,
            'fiber': 1.6
        },
        'Spring onion': {  # Green part only
            'calories': 32,
            'protein': 1.8,
            'fat': 0.2,
            'carbs': 7.3,
            'fiber': 2.6
        },
        'Sunflower sprouts': {  # Raw
            'calories': 29,
            'protein': 2.5,
            'fat': 0.55,
            'carbs': 4.5,
            'fiber': 2.0
        },
        'Artichoke hearts': {  # Raw globe artichoke hearts
            'calories': 47,
            'protein': 3.3,
            'fat': 0.2,
            'carbs': 10.5,
            'fiber': 5.4
        },
        'Cabbage savoy': {  # Raw
            'calories': 27,
            'protein': 2.0,
            'fat': 0.2,
            'carbs': 6.0,
            'fiber': 3.0
        },
        'Ginger': {  # Fresh raw ginger
            'calories': 80,
            'protein': 1.8,
            'fat': 0.8,
            'carbs': 17.8,
            'fiber': 2.0
        }
    },
    'Fruits': {
        'Banana': {  # Raw banana, USDA #09040
            'calories': 89,
            'protein': 1.09,
            'fat': 0.33,
            'carbs': 22.84,
            'fiber': 2.6
        },
        'Strawberries': {  # Raw strawberries, USDA #09316
            'calories': 32,
            'protein': 0.67,
            'fat': 0.3,
            'carbs': 7.68,
            'fiber': 2.0
        },
        'Blueberries': {  # Raw blueberries, USDA #09050
            'calories': 57,
            'protein': 0.74,
            'fat': 0.33,
            'carbs': 14.49,
            'fiber': 2.4
        },
        'Raspberries': {  # Raw raspberries, USDA #09302
            'calories': 52,
            'protein': 1.2,
            'fat': 0.65,
            'carbs': 11.94,
            'fiber': 6.5
        },
        'Blackberries': {  # Raw blackberries, USDA #09042
            'calories': 43,
            'protein': 1.39,
            'fat': 0.49,
            'carbs': 9.61,
            'fiber': 5.3
        },
        'Cherries': {  # Raw sweet cherries, USDA #09070
            'calories': 63,
            'protein': 1.06,
            'fat': 0.2,
            'carbs': 16.01,
            'fiber': 2.1
        },
        'Citrus': {  # Raw orange, USDA #09200
            'calories': 47,
            'protein': 0.94,
            'fat': 0.12,
            'carbs': 11.75,
            'fiber': 2.4
        },
        'Grapes': {  # Raw grapes, USDA #09132
            'calories': 69,
            'protein': 0.72,
            'fat': 0.16,
            'carbs': 18.1,
            'fiber': 0.9
        },
        'Pineapple': {  # Raw pineapple, USDA #09266
            'calories': 50,
            'protein': 0.54,
            'fat': 0.12,
            'carbs': 13.12,
            'fiber': 1.4
        },
        'Lemon': {  # Raw lemon, USDA #09150
            'calories': 29,
            'protein': 1.1,
            'fat': 0.3,
            'carbs': 9.32,
            'fiber': 2.8
        },
        'Lime': {  # Raw lime, USDA #09159
            'calories': 30,
            'protein': 0.7,
            'fat': 0.2,
            'carbs': 10.54,
            'fiber': 2.8
        },
        'Honeydew': {  # Raw honeydew melon, USDA #09184
            'calories': 36,
            'protein': 0.54,
            'fat': 0.14,
            'carbs': 9.09,
            'fiber': 0.8
        },
        'Pomegranate': {  # Raw pomegranate seeds, USDA #09286
            'calories': 83,
            'protein': 1.67,
            'fat': 1.17,
            'carbs': 18.7,
            'fiber': 4.0
        }
    },
    'Proteins': {
        'Eggs': {  # Raw whole egg, USDA #01123
            'calories': 143,
            'protein': 12.56,
            'fat': 9.51,
            'carbs': 0.72,
            'fiber': 0
        },
        "Turkey": {
          "calories": 135,
          "protein": 30,
          "carbs": 0,
          "fat": 1.5
        },
        'Chicken Pieces with Skin': {  # Raw chicken pieces with skin
            'calories': 239,
            'protein': 27,
            'carbs': 0,
            'fat': 14
        },
        'Lean fresh chicken': {  # Chicken breast, raw, USDA #05062
            'calories': 120,
            'protein': 22.5,
            'fat': 2.62,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh fish': {  # Salmon, raw, USDA #15076
            'calories': 208,
            'protein': 20.42,
            'fat': 13.42,
            'carbs': 0,
            'fiber': 0
        },
        'Lean fresh lamb': {  # Raw lamb, USDA #17078
            'calories': 282,
            'protein': 16.56,
            'fat': 23.43,
            'carbs': 0,
            'fiber': 0
        },
        'Lean fresh beef': {  # Raw lean beef, USDA #23557
            'calories': 213,
            'protein': 22.03,
            'fat': 13.83,
            'carbs': 0,
            'fiber': 0
        },
        'Prawns': {  # Raw prawns, USDA #15152
            'calories': 99,
            'protein': 20.91,
            'fat': 1.73,
            'carbs': 0,
            'fiber': 0
        },
        'Mussels': {  # Raw blue mussels, USDA #15164
            'calories': 86,
            'protein': 11.9,
            'fat': 2.24,
            'carbs': 3.69,
            'fiber': 0
        },
        'Oysters': {  # Raw oysters, USDA #15171
            'calories': 69,
            'protein': 9.45,
            'fat': 2.47,
            'carbs': 3.91,
            'fiber': 0
        },
        'Scallops': {  # Raw scallops, USDA #15172
            'calories': 69,
            'protein': 12.06,
            'fat': 0.49,
            'carbs': 3.18,
            'fiber': 0
        },
        'Crab': {  # Raw crab meat, USDA #15139
            'calories': 87,
            'protein': 18.1,
            'fat': 1.08,
            'carbs': 0,
            'fiber': 0
        },
        'Lobster': {  # Raw lobster, USDA #15147
            'calories': 89,
            'protein': 18.8,
            'fat': 0.9,
            'carbs': 0.5,
            'fiber': 0
        },
        'Clams': {  # Raw clams, USDA #15157
            'calories': 86,
            'protein': 14.67,
            'fat': 0.96,
            'carbs': 3.57,
            'fiber': 0
        },
        'Lean fresh pork': {  # Raw lean pork loin, USDA #10020
            'calories': 143,
            'protein': 21.69,
            'fat': 5.41,
            'carbs': 0,
            'fiber': 0
        },
        'Collagen': {  # Hydrolyzed collagen powder, estimated
            'calories': 340,
            'protein': 85,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        }
    },
    'Nuts': {
        'Almonds': {  # Raw almonds, USDA #12061
            'calories': 579,
            'protein': 21.15,
            'fat': 49.93,
            'carbs': 21.55,
            'fiber': 12.5
        },
        'Almond flour': {  # Almond flour, USDA #93740
            'calories': 571,
            'protein': 21.4,
            'fat': 50.2,
            'carbs': 19.2,
            'fiber': 10.4
        },
        'Pine nuts': {  # Raw pine nuts, USDA #12147
            'calories': 673,
            'protein': 13.69,
            'fat': 68.37,
            'carbs': 13.08,
            'fiber': 3.7
        },
        'Macadamias': {  # Raw macadamia nuts, USDA #12131
            'calories': 718,
            'protein': 7.91,
            'fat': 75.77,
            'carbs': 13.82,
            'fiber': 8.6
        },
        'Coconut flour': {  # Coconut flour, USDA #93747
            'calories': 354,
            'protein': 17.5,
            'fat': 11.5,
            'carbs': 60.0,
            'fiber': 39.0
        },
        'Almond milk': {  # Calculated based on 4 almonds per 100g
            'calories': 28,  # (579 * 0.048)
            'protein': 1.02,  # (21.15 * 0.048)
            'fat': 2.40,  # (49.93 * 0.048)
            'carbs': 1.03,  # (21.55 * 0.048)
            'fiber': 0.60   # (12.5 * 0.048)
        }
    },
    'Grains': {
        'White Rice': {  # Raw white rice, USDA #20444
            'calories': 365,
            'protein': 7.13,
            'fat': 0.66,
            'carbs': 80,
            'fiber': 1.3
        },
        'Quinoa': {  # Raw quinoa, USDA #20035
            'calories': 368,
            'protein': 14.12,
            'fat': 6.07,
            'carbs': 64.16,
            'fiber': 7.0
        }
    },
    'Oils': {
        'Olive oil': {  # USDA #04053
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'MCT oil': {  # Estimated
            'calories': 860,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'Flax oil': {  # USDA #42231
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'Sesame oil': {  # USDA #04058
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'Sunflower oil': {  # USDA #04506
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'Walnut oil': {  # USDA #12155
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'Garlic infused oil': {  # Based on olive oil, USDA #04053
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'Chili infused oil': {  # Based on olive oil, USDA #04053
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'Grapeseed oil': {  # USDA #04517
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'Pumpkin seed oil': {  # Based on olive oil values
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        },
        'Polyunsaturated vegetable oil': {  # Based on olive oil values
            'calories': 884,
            'protein': 0,
            'fat': 100,
            'carbs': 0,
            'fiber': 0
        }
    },
    'Beverages': {
        'Coffee': {  # Brewed coffee, USDA #14209
            'calories': 1,
            'protein': 0.12,
            'fat': 0.02,
            'carbs': 0,
            'fiber': 0
        },
        'Herbal tea': {  # Brewed tea, USDA #14355
            'calories': 1,
            'protein': 0,
            'fat': 0,
            'carbs': 0.2,
            'fiber': 0
        }
    },
    'Sweeteners': {
        'Raw honey': {  # Raw honey, USDA #19296
            'calories': 304,
            'protein': 0.3,
            'fat': 0,
            'carbs': 82.4,
            'fiber': 0.2
        },
        'Coconut sugar': {  # Coconut palm sugar, estimated
            'calories': 375,
            'protein': 0,
            'fat': 0,
            'carbs': 100,
            'fiber': 0
        },
        'Stevia': {  # Zero calorie sweetener
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Monk fruit sweetener': {  # Zero calorie sweetener
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        }
    },
    'Condiments': {
        'Turmeric': {  # Negligible macros
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Cinnamon': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Salt': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Pepper': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Basil': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Oregano': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Thyme': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Rosemary': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Sage': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Mint': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Parsley': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Cilantro': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Dill': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Chives': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Fresh Tarragon': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Dried Basil': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Dried Oregano': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Dried Thyme': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Dried Rosemary': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Dried Sage': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Dried Parsley': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Dried Dill': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Italian Herbs': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Vanilla': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Bicarbonate of soda': {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbs': 0,
            'fiber': 0
        },
        'Mustard': {
           "calories": 3,
           "protein": 0.2,
           "carbs": 0.5,
           "fat": 0.2,   
           'fiber': 0.5
        },
        'Fennel Seeds': {
           "calories": 6,
           "protein": 0.3,
           "carbs": 1.4,
           "fat": 0.3,
           "fiber": 1.4
        },
        'Curry Leaves': {
           "calories": 23,
           "protein": 2.0,
           "carbs": 4.0,
           "fat": 0.5,
           "fiber": 0
        }
    }
}
