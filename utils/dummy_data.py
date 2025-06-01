from typing import Dict, List, Any

STATES_DATA = {
    "Himachal Pradesh": {
        "banner_image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=1200",
        "overview": {
            "capital": "Shimla",
            "best_time": "March to June",
            "known_for": ["Adventure Sports", "Hill Stations", "Buddhist Monasteries", "Apple Orchards"],
            "languages": ["Hindi", "Pahari", "Kangri"],
            "climate": "Pleasant summers and cold winters",
            "geography": "Mountainous terrain with elevations ranging from 350m to 7000m"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 15700000, "foreign": 250000, "total": 15950000, "growth": 8.5},
                {"year": 2021, "domestic": 14500000, "foreign": 200000, "total": 14700000, "growth": 15.2},
                {"year": 2020, "domestic": 12500000, "foreign": 150000, "total": 12650000, "growth": -32.5}
            ]
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Chamba Rumal", "description": "Traditional embroidered handkerchief"},
                {"name": "Kangra Paintings", "description": "Miniature paintings depicting Rajput lifestyle"},
                {"name": "Wood Carving", "description": "Intricate designs on local deodar wood"}
            ],
            "festivals": [
                {"name": "Kullu Dussehra", "month": "October", "description": "Week-long festival celebrating victory of good over evil"},
                {"name": "Losar Festival", "month": "February", "description": "Tibetan New Year celebrations"},
                {"name": "Mandi Shivratri", "month": "March", "description": "Week-long international fair"}
            ],
            "cuisines": [
                {"name": "Dham", "description": "Traditional feast served on leaf plates"},
                {"name": "Siddu", "description": "Stuffed bread made from wheat flour"},
                {"name": "Madra", "description": "Chickpeas cooked in yogurt gravy"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Shimla",
                    "description": "Former summer capital of British India",
                    "attractions": ["The Ridge", "Mall Road", "Jakhu Temple"],
                    "best_time": "March to June"
                },
                {
                    "name": "Manali",
                    "description": "Popular hill station known for adventure sports",
                    "attractions": ["Rohtang Pass", "Hadimba Temple", "Old Manali"],
                    "best_time": "October to June"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Chitkul",
                    "description": "Last inhabited village near Indo-Tibet border",
                    "attractions": ["Chitkul Temple", "Mountain Views", "Local Culture"],
                    "best_time": "May to October"
                },
                {
                    "name": "Tirthan Valley",
                    "description": "Offbeat destination for nature lovers",
                    "attractions": ["Trout Fishing", "Great Himalayan National Park", "Local Homestays"],
                    "best_time": "March to June"
                }
            ]
        }
    },
    "Rajasthan": {
        "banner_image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=1200",
        "overview": {
            "capital": "Jaipur",
            "best_time": "October to March",
            "known_for": ["Royal Palaces", "Desert Safari", "Folk Music", "Heritage Hotels"],
            "languages": ["Hindi", "Rajasthani", "Marwari"],
            "climate": "Hot and arid",
            "geography": "Mostly desert and arid regions with Aravalli range"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 18200000, "foreign": 450000, "total": 18650000, "growth": 12.3},
                {"year": 2021, "domestic": 16100000, "foreign": 350000, "total": 16450000, "growth": 18.5},
                {"year": 2020, "domestic": 13500000, "foreign": 250000, "total": 13750000, "growth": -28.9}
            ]
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Kathputli", "description": "Traditional puppet dance"},
                {"name": "Phad Painting", "description": "Scroll paintings depicting folk tales"},
                {"name": "Ghoomar", "description": "Traditional folk dance"}
            ],
            "festivals": [
                {"name": "Desert Festival", "month": "February", "description": "Celebration of desert culture in Jaisalmer"},
                {"name": "Pushkar Fair", "month": "November", "description": "Famous camel and livestock fair"},
                {"name": "Teej", "month": "August", "description": "Festival celebrating the monsoon"}
            ],
            "cuisines": [
                {"name": "Dal Baati Churma", "description": "Traditional Rajasthani dish"},
                {"name": "Laal Maas", "description": "Spicy meat curry"},
                {"name": "Ker Sangri", "description": "Desert beans and berries dish"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Jaipur",
                    "description": "The Pink City known for its architectural beauty",
                    "attractions": ["Hawa Mahal", "Amber Fort", "City Palace"],
                    "best_time": "October to March"
                },
                {
                    "name": "Udaipur",
                    "description": "City of Lakes and Palaces",
                    "attractions": ["Lake Pichola", "City Palace", "Fateh Sagar Lake"],
                    "best_time": "September to March"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Bundi",
                    "description": "Ancient town known for step wells and palaces",
                    "attractions": ["Taragarh Fort", "Raniji ki Baori", "Chitrashala"],
                    "best_time": "October to March"
                },
                {
                    "name": "Osian",
                    "description": "Ancient temple town in Thar Desert",
                    "attractions": ["Sachiya Mata Temple", "Desert Camping", "Temple Architecture"],
                    "best_time": "November to February"
                }
            ]
        }
    },
    "Kerala": {
        "banner_image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=1200",
        "overview": {
            "capital": "Thiruvananthapuram",
            "best_time": "October to March",
            "known_for": ["Backwaters", "Ayurveda", "Tea Gardens", "Beach Resorts"],
            "languages": ["Malayalam", "English"],
            "climate": "Tropical with moderate temperatures",
            "geography": "Coastal plains, highlands, and backwaters"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 16500000, "foreign": 550000, "total": 17050000, "growth": 14.2},
                {"year": 2021, "domestic": 14200000, "foreign": 400000, "total": 14600000, "growth": 16.8},
                {"year": 2020, "domestic": 12000000, "foreign": 300000, "total": 12300000, "growth": -25.6}
            ]
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Kathakali", "description": "Classical dance-drama with elaborate costumes"},
                {"name": "Mohiniyattam", "description": "Classical dance form of Kerala"},
                {"name": "Kalaripayattu", "description": "Ancient martial art form"}
            ],
            "festivals": [
                {"name": "Onam", "month": "August-September", "description": "Harvest festival with boat races"},
                {"name": "Thrissur Pooram", "month": "April-May", "description": "Famous temple festival"},
                {"name": "Vishu", "month": "April", "description": "Malayalam New Year"}
            ],
            "cuisines": [
                {"name": "Appam with Stew", "description": "Lacy rice hoppers with coconut stew"},
                {"name": "Kerala Fish Curry", "description": "Spicy fish curry with coconut"},
                {"name": "Puttu and Kadala", "description": "Steamed rice cake with black chickpeas"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Alleppey",
                    "description": "Venice of the East, famous for houseboats",
                    "attractions": ["Backwaters", "Alappuzha Beach", "Houseboats"],
                    "best_time": "November to February"
                },
                {
                    "name": "Munnar",
                    "description": "Hill station known for tea plantations",
                    "attractions": ["Tea Gardens", "Eravikulam National Park", "Top Station"],
                    "best_time": "September to March"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Wayanad",
                    "description": "Green paradise with wildlife sanctuaries",
                    "attractions": ["Edakkal Caves", "Banasura Dam", "Chembra Peak"],
                    "best_time": "October to May"
                },
                {
                    "name": "Vagamon",
                    "description": "Untouched hill station with meadows",
                    "attractions": ["Pine Forest", "Meadows", "Paragliding"],
                    "best_time": "September to May"
                }
            ]
        }
    },
    "Goa": {
        "banner_image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=1200",
        "overview": {
            "capital": "Panaji",
            "best_time": "November to February",
            "known_for": ["Beaches", "Portuguese Architecture", "Nightlife", "Water Sports"],
            "languages": ["Konkani", "Marathi", "English"],
            "climate": "Tropical with warm temperatures",
            "geography": "Coastal region with beaches and Western Ghats"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 7200000, "foreign": 900000, "total": 8100000, "growth": 18.5},
                {"year": 2021, "domestic": 6000000, "foreign": 700000, "total": 6700000, "growth": 22.3},
                {"year": 2020, "domestic": 4800000, "foreign": 500000, "total": 5300000, "growth": -31.2}
            ]
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Dekhni", "description": "Traditional Goan dance form"},
                {"name": "Zagor", "description": "Folk drama performance"},
                {"name": "Mando", "description": "Goan classical music"}
            ],
            "festivals": [
                {"name": "Carnival", "month": "February", "description": "Four-day festival of colors and music"},
                {"name": "Sao Joao", "month": "June", "description": "Feast of St. John the Baptist"},
                {"name": "Bonderam", "month": "August", "description": "Flag festival of Divar Island"}
            ],
            "cuisines": [
                {"name": "Fish Curry Rice", "description": "Traditional Goan curry with local fish"},
                {"name": "Vindaloo", "description": "Spicy curry with Portuguese influence"},
                {"name": "Bebinca", "description": "Traditional layered dessert"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Calangute",
                    "description": "Queen of Beaches in Goa",
                    "attractions": ["Calangute Beach", "Water Sports", "Shopping"],
                    "best_time": "November to February"
                },
                {
                    "name": "Old Goa",
                    "description": "UNESCO World Heritage site",
                    "attractions": ["Basilica of Bom Jesus", "Se Cathedral", "Church of St. Francis of Assisi"],
                    "best_time": "October to March"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Divar Island",
                    "description": "Peaceful island with Portuguese heritage",
                    "attractions": ["Old Portuguese Houses", "Church of Our Lady of Piety", "Village Life"],
                    "best_time": "November to February"
                },
                {
                    "name": "Cola Beach",
                    "description": "Hidden beach with lagoon",
                    "attractions": ["Lagoon", "Private Beach", "Dolphin Watching"],
                    "best_time": "October to March"
                }
            ]
        }
    },
    "Gujarat": {
        "banner_image": "https://www.bing.com/th/id/OIP.jrLNaH_hV0-5TcbXz2BH1gHaE7?w=254&h=211&c=8&rs=1&qlt=90&o=6&cb=thwsc1&dpr=2&pid=3.1&rm=2",
        "overview": {
            "capital": "Gandhinagar",
            "best_time": "October to March",
            "known_for": ["Rann of Kutch", "Industrial Hub", "Gandhi Heritage", "Wildlife"],
            "languages": ["Gujarati", "Hindi", "English"],
            "climate": "Hot and dry with mild winters",
            "geography": "Diverse landscape with desert, hills, and coastline"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 19500000, "foreign": 350000, "total": 19850000, "growth": 15.8},
                {"year": 2021, "domestic": 16800000, "foreign": 250000, "total": 17050000, "growth": 20.1},
                {"year": 2020, "domestic": 13900000, "foreign": 150000, "total": 14050000, "growth": -28.5}
            ],
            "monthly_distribution": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "visitors": [250000, 280000, 220000, 150000, 100000, 80000, 90000, 120000, 180000, 260000, 300000, 270000],
                "occupancy_rate": [85, 90, 75, 60, 45, 35, 40, 50, 65, 80, 95, 88]
            },
            "impact_metrics": {
                "revenue_cr": 12500,
                "revenue_growth": 18.5,
                "employment": 250000,
                "employment_growth": 12.3,
                "hotels": 1800,
                "hotels_growth": 8.5,
                "avg_stay": 4.2,
                "stay_duration_change": 0.5
            }
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Garba", "description": "Traditional dance form performed during Navratri"},
                {"name": "Bandhani", "description": "Traditional tie-dye textile art"},
                {"name": "Patola", "description": "Double ikat woven saree from Patan"}
            ],
            "festivals": [
                {"name": "Navratri", "month": "September-October", "description": "Nine nights of dance and celebration"},
                {"name": "Rann Utsav", "month": "November-February", "description": "Desert festival in White Rann"},
                {"name": "Uttarayan", "month": "January", "description": "International kite festival"}
            ],
            "cuisines": [
                {"name": "Dhokla", "description": "Steamed fermented rice and chickpea flour cake"},
                {"name": "Thepla", "description": "Flatbread made with fenugreek leaves"},
                {"name": "Undhiyu", "description": "Mixed vegetable dish"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Rann of Kutch",
                    "description": "World's largest salt desert",
                    "attractions": ["White Desert", "Handicraft Villages", "Cultural Shows"],
                    "best_time": "November to February"
                },
                {
                    "name": "Gir National Park",
                    "description": "Only home of Asiatic Lions",
                    "attractions": ["Lion Safari", "Bird Watching", "Tribal Villages"],
                    "best_time": "December to March"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Champaner-Pavagadh",
                    "description": "UNESCO World Heritage Site",
                    "attractions": ["Archaeological Park", "Jami Masjid", "Ancient Temples"],
                    "best_time": "November to February"
                },
                {
                    "name": "Dholavira",
                    "description": "Ancient Harappan City",
                    "attractions": ["Archaeological Site", "Museum", "Great Rann"],
                    "best_time": "October to March"
                }
            ]
        }
    },
    "Karnataka": {
        "banner_image": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=1200",
        "overview": {
            "capital": "Bengaluru",
            "best_time": "October to February",
            "known_for": ["Tech Hub", "Ancient Temples", "Coffee Plantations", "National Parks"],
            "languages": ["Kannada", "English", "Hindi"],
            "climate": "Moderate throughout the year",
            "geography": "Deccan plateau with Western Ghats and coastal plains"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 21500000, "foreign": 450000, "total": 21950000, "growth": 16.2},
                {"year": 2021, "domestic": 18400000, "foreign": 350000, "total": 18750000, "growth": 19.8},
                {"year": 2020, "domestic": 15200000, "foreign": 250000, "total": 15450000, "growth": -26.8}
            ],
            "monthly_distribution": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "visitors": [280000, 260000, 230000, 180000, 150000, 140000, 160000, 190000, 220000, 270000, 290000, 280000],
                "occupancy_rate": [88, 85, 75, 65, 55, 50, 60, 70, 80, 90, 92, 88]
            },
            "impact_metrics": {
                "revenue_cr": 15800,
                "revenue_growth": 21.5,
                "employment": 320000,
                "employment_growth": 15.3,
                "hotels": 2200,
                "hotels_growth": 10.5,
                "avg_stay": 4.8,
                "stay_duration_change": 0.8
            }
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Yakshagana", "description": "Traditional dance-drama"},
                {"name": "Bidriware", "description": "Metal handicraft with silver inlay"},
                {"name": "Mysore Painting", "description": "Traditional painting style with gold foil"}
            ],
            "festivals": [
                {"name": "Dasara", "month": "September-October", "description": "Royal celebration in Mysore"},
                {"name": "Hampi Utsav", "month": "November", "description": "Cultural festival in ruins"},
                {"name": "Pattadakal Dance Festival", "month": "January", "description": "Classical dance festival"}
            ],
            "cuisines": [
                {"name": "Mysore Masala Dosa", "description": "Crispy crepe with spicy potato filling"},
                {"name": "Bisi Bele Bath", "description": "Spicy rice dish with lentils"},
                {"name": "Coorg Pandi Curry", "description": "Traditional pork curry"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Hampi",
                    "description": "UNESCO World Heritage Site with ancient ruins",
                    "attractions": ["Virupaksha Temple", "Stone Chariot", "Hippie Island"],
                    "best_time": "October to March"
                },
                {
                    "name": "Coorg",
                    "description": "Scotland of India",
                    "attractions": ["Coffee Plantations", "Abbey Falls", "Raja's Seat"],
                    "best_time": "October to March"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Badami",
                    "description": "Ancient cave temples",
                    "attractions": ["Cave Temples", "Agastya Lake", "Archaeological Museum"],
                    "best_time": "November to February"
                },
                {
                    "name": "Kudremukh",
                    "description": "Hidden mountain paradise",
                    "attractions": ["Trek Routes", "National Park", "Waterfalls"],
                    "best_time": "October to May"
                }
            ]
        }
    },
    "Tamil Nadu": {
        "banner_image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=1200",
        "overview": {
            "capital": "Chennai",
            "best_time": "October to March",
            "known_for": ["Ancient Temples", "Classical Music", "Beaches", "Hill Stations"],
            "languages": ["Tamil", "English"],
            "climate": "Hot and humid with moderate winters",
            "geography": "Coastal plains and Western Ghats"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 22500000, "foreign": 550000, "total": 23050000, "growth": 17.5},
                {"year": 2021, "domestic": 19100000, "foreign": 400000, "total": 19500000, "growth": 21.2},
                {"year": 2020, "domestic": 15700000, "foreign": 300000, "total": 16000000, "growth": -25.8}
            ],
            "monthly_distribution": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "visitors": [290000, 270000, 240000, 190000, 160000, 150000, 170000, 200000, 230000, 280000, 300000, 290000],
                "occupancy_rate": [90, 88, 78, 68, 58, 52, 62, 72, 82, 92, 95, 90]
            },
            "impact_metrics": {
                "revenue_cr": 18500,
                "revenue_growth": 22.5,
                "employment": 380000,
                "employment_growth": 16.8,
                "hotels": 2500,
                "hotels_growth": 11.2,
                "avg_stay": 5.2,
                "stay_duration_change": 0.9
            }
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Bharatanatyam", "description": "Classical dance form"},
                {"name": "Tanjore Painting", "description": "Classical painting with gold foil"},
                {"name": "Carnatic Music", "description": "Classical music tradition"}
            ],
            "festivals": [
                {"name": "Pongal", "month": "January", "description": "Harvest festival"},
                {"name": "Madurai Chithirai", "month": "April-May", "description": "Temple festival"},
                {"name": "Dance Festival", "month": "December-January", "description": "Classical dance at Mamallapuram"}
            ],
            "cuisines": [
                {"name": "Chettinad Cuisine", "description": "Spicy traditional cuisine"},
                {"name": "Madurai Idli", "description": "Soft steamed rice cakes"},
                {"name": "Filter Coffee", "description": "Traditional South Indian coffee"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Mamallapuram",
                    "description": "UNESCO Heritage site with shore temple",
                    "attractions": ["Shore Temple", "Five Rathas", "Krishna's Butterball"],
                    "best_time": "November to February"
                },
                {
                    "name": "Ooty",
                    "description": "Queen of Hill Stations",
                    "attractions": ["Botanical Gardens", "Nilgiri Mountain Railway", "Ooty Lake"],
                    "best_time": "October to June"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Tranquebar",
                    "description": "Danish colonial town",
                    "attractions": ["Fort Dansborg", "New Jerusalem Church", "Maritime Museum"],
                    "best_time": "November to February"
                },
                {
                    "name": "Yelagiri",
                    "description": "Lesser-known hill station",
                    "attractions": ["Jalagamparai Falls", "Nature Park", "Telescope House"],
                    "best_time": "November to February"
                }
            ]
        }
    },
    "West Bengal": {
        "banner_image": "https://images.unsplash.com/photo-1558431382-27e303142255?w=1200",
        "overview": {
            "capital": "Kolkata",
            "best_time": "October to March",
            "known_for": ["Cultural Heritage", "Sundarbans", "Tea Gardens", "Durga Puja"],
            "languages": ["Bengali", "English", "Hindi"],
            "climate": "Tropical with hot summers and mild winters",
            "geography": "Varied landscape from mountains to mangroves"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 20500000, "foreign": 400000, "total": 20900000, "growth": 16.8},
                {"year": 2021, "domestic": 17500000, "foreign": 300000, "total": 17800000, "growth": 20.5},
                {"year": 2020, "domestic": 14500000, "foreign": 200000, "total": 14700000, "growth": -27.2}
            ],
            "monthly_distribution": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "visitors": [270000, 250000, 220000, 170000, 140000, 130000, 150000, 180000, 210000, 260000, 280000, 270000],
                "occupancy_rate": [85, 82, 72, 62, 52, 48, 58, 68, 78, 88, 92, 85]
            },
            "impact_metrics": {
                "revenue_cr": 16800,
                "revenue_growth": 20.5,
                "employment": 340000,
                "employment_growth": 15.8,
                "hotels": 2300,
                "hotels_growth": 10.8,
                "avg_stay": 4.5,
                "stay_duration_change": 0.7
            }
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Rabindra Sangeet", "description": "Songs composed by Rabindranath Tagore"},
                {"name": "Kantha Stitch", "description": "Traditional embroidery"},
                {"name": "Patachitra", "description": "Scroll painting"}
            ],
            "festivals": [
                {"name": "Durga Puja", "month": "September-October", "description": "Biggest festival of Bengal"},
                {"name": "Poush Mela", "month": "December", "description": "Cultural fair in Shantiniketan"},
                {"name": "Gangasagar Mela", "month": "January", "description": "Religious gathering"}
            ],
            "cuisines": [
                {"name": "Bengali Fish Curry", "description": "Traditional fish preparation"},
                {"name": "Mishti Doi", "description": "Sweet yogurt"},
                {"name": "Rosogolla", "description": "Syrupy dessert dumplings"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Darjeeling",
                    "description": "Queen of the Hills",
                    "attractions": ["Tiger Hill", "Tea Gardens", "Toy Train"],
                    "best_time": "March to May, October to December"
                },
                {
                    "name": "Sundarbans",
                    "description": "World's largest mangrove forest",
                    "attractions": ["Tiger Reserve", "Mangrove Forest", "River Cruise"],
                    "best_time": "October to March"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Mayapur",
                    "description": "ISKCON headquarters",
                    "attractions": ["ISKCON Temple", "Ganga Ghat", "Chandrodaya Temple"],
                    "best_time": "October to March"
                },
                {
                    "name": "Mandarmani",
                    "description": "Beach destination",
                    "attractions": ["Beach Drive", "Red Crabs", "Sunrise Point"],
                    "best_time": "October to February"
                }
            ]
        }
    },
    "Ladakh": {
        "banner_image": "https://images.unsplash.com/photo-1589793907316-f94025b46850?w=1200",
        "overview": {
            "capital": "Leh",
            "best_time": "June to September",
            "known_for": ["Buddhist Monasteries", "High Altitude Lakes", "Adventure Sports", "Unique Culture"],
            "languages": ["Ladakhi", "Hindi", "English"],
            "climate": "Cold desert with extreme temperatures",
            "geography": "High altitude desert with mountains and valleys"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 850000, "foreign": 150000, "total": 1000000, "growth": 25.5},
                {"year": 2021, "domestic": 650000, "foreign": 100000, "total": 750000, "growth": 35.2},
                {"year": 2020, "domestic": 450000, "foreign": 50000, "total": 500000, "growth": -45.8}
            ],
            "monthly_distribution": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "visitors": [5000, 3000, 2000, 15000, 80000, 150000, 180000, 200000, 150000, 80000, 10000, 5000],
                "occupancy_rate": [20, 15, 10, 40, 75, 90, 95, 98, 90, 70, 25, 20]
            },
            "impact_metrics": {
                "revenue_cr": 2500,
                "revenue_growth": 28.5,
                "employment": 50000,
                "employment_growth": 15.8,
                "hotels": 450,
                "hotels_growth": 12.5,
                "avg_stay": 7.2,
                "stay_duration_change": 1.2
            }
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Thangka Painting", "description": "Buddhist religious scroll paintings"},
                {"name": "Ladakhi Music", "description": "Traditional music with surna and daman"},
                {"name": "Wood Carving", "description": "Intricate wooden architectural details"}
            ],
            "festivals": [
                {"name": "Hemis Festival", "month": "June-July", "description": "Largest monastic festival"},
                {"name": "Losar", "month": "February", "description": "Ladakhi New Year"},
                {"name": "Ladakh Festival", "month": "September", "description": "Cultural showcase"}
            ],
            "cuisines": [
                {"name": "Thukpa", "description": "Noodle soup with vegetables"},
                {"name": "Butter Tea", "description": "Traditional salty tea with yak butter"},
                {"name": "Skyu", "description": "Traditional pasta dish"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Pangong Lake",
                    "description": "High altitude salt water lake",
                    "attractions": ["Blue Waters", "Sunrise Views", "Camping"],
                    "best_time": "May to September"
                },
                {
                    "name": "Nubra Valley",
                    "description": "Desert valley with sand dunes",
                    "attractions": ["Diskit Monastery", "Camel Safari", "Hot Springs"],
                    "best_time": "June to September"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Hanle",
                    "description": "Dark sky sanctuary",
                    "attractions": ["Observatory", "Star Gazing", "Ancient Monastery"],
                    "best_time": "May to October"
                },
                {
                    "name": "Sham Valley",
                    "description": "Cultural trek route",
                    "attractions": ["Ancient Villages", "Apricot Orchards", "Monasteries"],
                    "best_time": "June to September"
                }
            ]
        }
    },
    "Andaman and Nicobar Islands": {
        "banner_image": "https://images.unsplash.com/photo-1589381855733-01bb36156da9?w=1200",
        "overview": {
            "capital": "Port Blair",
            "best_time": "October to May",
            "known_for": ["Pristine Beaches", "Water Sports", "Colonial History", "Marine Life"],
            "languages": ["Hindi", "Bengali", "Tamil", "English"],
            "climate": "Tropical with moderate temperatures",
            "geography": "Archipelago of 572 islands"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 580000, "foreign": 120000, "total": 700000, "growth": 22.8},
                {"year": 2021, "domestic": 450000, "foreign": 90000, "total": 540000, "growth": 28.5},
                {"year": 2020, "domestic": 350000, "foreign": 50000, "total": 400000, "growth": -38.5}
            ],
            "monthly_distribution": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "visitors": [80000, 75000, 70000, 60000, 40000, 30000, 25000, 30000, 45000, 70000, 85000, 90000],
                "occupancy_rate": [95, 92, 88, 80, 65, 50, 45, 48, 70, 85, 98, 98]
            },
            "impact_metrics": {
                "revenue_cr": 1800,
                "revenue_growth": 25.5,
                "employment": 35000,
                "employment_growth": 12.8,
                "hotels": 280,
                "hotels_growth": 15.5,
                "avg_stay": 6.5,
                "stay_duration_change": 0.8
            }
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Nicobari Dance", "description": "Traditional tribal dance"},
                {"name": "Shell Craft", "description": "Ornaments made from seashells"},
                {"name": "Karen Weaving", "description": "Traditional textile weaving"}
            ],
            "festivals": [
                {"name": "Island Tourism Festival", "month": "January", "description": "Cultural showcase"},
                {"name": "Beach Festival", "month": "April", "description": "Water sports and activities"},
                {"name": "Food Festival", "month": "December", "description": "Local cuisine celebration"}
            ],
            "cuisines": [
                {"name": "Seafood Curry", "description": "Fresh seafood in coconut curry"},
                {"name": "Fish BBQ", "description": "Grilled fresh catch"},
                {"name": "Coconut Prawn", "description": "Local specialty"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Havelock Island",
                    "description": "Famous for Radhanagar Beach",
                    "attractions": ["Radhanagar Beach", "Scuba Diving", "Elephant Beach"],
                    "best_time": "October to May"
                },
                {
                    "name": "Cellular Jail",
                    "description": "Historic colonial prison",
                    "attractions": ["Light and Sound Show", "Museum", "Freedom Fighter Gallery"],
                    "best_time": "Year round"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Barren Island",
                    "description": "Only active volcano in South Asia",
                    "attractions": ["Volcano Viewing", "Scuba Diving", "Marine Life"],
                    "best_time": "December to March"
                },
                {
                    "name": "Ross Island",
                    "description": "Former British settlement",
                    "attractions": ["Colonial Ruins", "Deer Park", "Light and Sound Show"],
                    "best_time": "October to May"
                }
            ]
        }
    },
    "Madhya Pradesh": {
        "banner_image": "https://images.unsplash.com/photo-1624956319777-d656ad1f1151?w=1200",
        "overview": {
            "capital": "Bhopal",
            "best_time": "October to March",
            "known_for": ["Wildlife", "Temples", "Heritage Sites", "Tribal Culture"],
            "languages": ["Hindi", "Bundeli", "Malvi"],
            "climate": "Subtropical with hot summers and mild winters",
            "geography": "Central Indian plateau with forests"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 18500000, "foreign": 350000, "total": 18850000, "growth": 16.5},
                {"year": 2021, "domestic": 15800000, "foreign": 250000, "total": 16050000, "growth": 19.2},
                {"year": 2020, "domestic": 13200000, "foreign": 150000, "total": 13350000, "growth": -29.5}
            ],
            "monthly_distribution": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "visitors": [260000, 240000, 210000, 160000, 130000, 120000, 140000, 170000, 200000, 250000, 270000, 260000],
                "occupancy_rate": [85, 82, 72, 62, 52, 48, 58, 68, 78, 88, 92, 85]
            },
            "impact_metrics": {
                "revenue_cr": 14500,
                "revenue_growth": 19.5,
                "employment": 280000,
                "employment_growth": 14.8,
                "hotels": 1900,
                "hotels_growth": 9.8,
                "avg_stay": 4.8,
                "stay_duration_change": 0.6
            }
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Gond Art", "description": "Traditional tribal art form"},
                {"name": "Mandana", "description": "Wall and floor paintings"},
                {"name": "Maach Theater", "description": "Traditional theater form"}
            ],
            "festivals": [
                {"name": "Khajuraho Dance Festival", "month": "February", "description": "Classical dance festival"},
                {"name": "Tansen Music Festival", "month": "December", "description": "Classical music festival"},
                {"name": "Lokrang", "month": "January", "description": "Folk arts festival"}
            ],
            "cuisines": [
                {"name": "Bhutte Ka Kees", "description": "Spiced grated corn"},
                {"name": "Dal Bafla", "description": "Wheat dumplings with dal"},
                {"name": "Poha", "description": "Flattened rice breakfast dish"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Khajuraho",
                    "description": "UNESCO World Heritage temples",
                    "attractions": ["Western Group Temples", "Light Show", "Archaeological Museum"],
                    "best_time": "October to March"
                },
                {
                    "name": "Bandhavgarh",
                    "description": "Famous tiger reserve",
                    "attractions": ["Tiger Safari", "Ancient Fort", "Bird Watching"],
                    "best_time": "October to June"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Chanderi",
                    "description": "Historic textile town",
                    "attractions": ["Chanderi Fortress", "Weaving Centers", "Jain Temples"],
                    "best_time": "October to March"
                },
                {
                    "name": "Orchha",
                    "description": "Medieval city",
                    "attractions": ["Orchha Fort", "Chaturbhuj Temple", "River Rafting"],
                    "best_time": "October to March"
                }
            ]
        }
    },
    "Puducherry": {
        "banner_image": "https://images.unsplash.com/photo-1582636714834-5db0b9b6e6f0?w=1200",
        "overview": {
            "capital": "Puducherry",
            "best_time": "October to March",
            "known_for": ["French Architecture", "Beaches", "Spiritual Tourism", "French Cuisine"],
            "languages": ["Tamil", "French", "English", "Telugu"],
            "climate": "Tropical with warm temperatures",
            "geography": "Coastal region with French colonial heritage"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 1800000, "foreign": 200000, "total": 2000000, "growth": 18.5},
                {"year": 2021, "domestic": 1500000, "foreign": 150000, "total": 1650000, "growth": 22.2},
                {"year": 2020, "domestic": 1200000, "foreign": 100000, "total": 1300000, "growth": -35.5}
            ],
            "monthly_distribution": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "visitors": [220000, 200000, 180000, 150000, 120000, 100000, 110000, 130000, 160000, 200000, 220000, 210000],
                "occupancy_rate": [90, 85, 80, 70, 60, 55, 58, 65, 75, 85, 92, 88]
            },
            "impact_metrics": {
                "revenue_cr": 3500,
                "revenue_growth": 20.5,
                "employment": 45000,
                "employment_growth": 12.8,
                "hotels": 350,
                "hotels_growth": 8.5,
                "avg_stay": 3.8,
                "stay_duration_change": 0.5
            }
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Bharatanatyam", "description": "Classical dance form"},
                {"name": "Terracotta Work", "description": "Traditional pottery and sculptures"},
                {"name": "Shell Craft", "description": "Decorative items from seashells"}
            ],
            "festivals": [
                {"name": "Mascarade", "month": "March-April", "description": "French-style carnival"},
                {"name": "Villianur Temple Festival", "month": "May-June", "description": "Traditional temple car festival"},
                {"name": "International Yoga Festival", "month": "January", "description": "Yoga and wellness celebration"}
            ],
            "cuisines": [
                {"name": "French-Tamil Fusion", "description": "Unique blend of French and Tamil cuisine"},
                {"name": "Seafood Specialties", "description": "Fresh coastal preparations"},
                {"name": "Creole Cuisine", "description": "Indo-French fusion dishes"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "French Quarter",
                    "description": "Heritage area with French architecture",
                    "attractions": ["Promenade Beach", "Aurobindo Ashram", "French Colonial Buildings"],
                    "best_time": "October to March"
                },
                {
                    "name": "Paradise Beach",
                    "description": "Pristine beach with water sports",
                    "attractions": ["Boating", "Beach Activities", "Sunset Views"],
                    "best_time": "October to March"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Arikamedu",
                    "description": "Ancient Roman trading center",
                    "attractions": ["Archaeological Site", "Ancient Port", "Museum"],
                    "best_time": "November to February"
                },
                {
                    "name": "Yanam",
                    "description": "Former French colony",
                    "attractions": ["Godavari River", "French Heritage", "Local Markets"],
                    "best_time": "October to March"
                }
            ]
        }
    },
    "Sikkim": {
        "banner_image": "https://images.unsplash.com/photo-1626621934191-583e3268dfb3?w=1200",
        "overview": {
            "capital": "Gangtok",
            "best_time": "March to May, October to December",
            "known_for": ["Monasteries", "Mountain Views", "Adventure Sports", "Organic Farming"],
            "languages": ["Nepali", "Sikkimese", "Hindi", "English"],
            "climate": "Alpine in higher regions, subtropical in lower regions",
            "geography": "Mountainous terrain with valleys and glaciers"
        },
        "tourism_stats": {
            "yearly_stats": [
                {"year": 2022, "domestic": 1500000, "foreign": 150000, "total": 1650000, "growth": 20.5},
                {"year": 2021, "domestic": 1200000, "foreign": 100000, "total": 1300000, "growth": 25.2},
                {"year": 2020, "domestic": 950000, "foreign": 50000, "total": 1000000, "growth": -42.5}
            ],
            "monthly_distribution": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "visitors": [120000, 100000, 180000, 200000, 180000, 80000, 60000, 70000, 150000, 200000, 180000, 130000],
                "occupancy_rate": [75, 70, 85, 90, 85, 50, 45, 48, 80, 92, 88, 78]
            },
            "impact_metrics": {
                "revenue_cr": 2800,
                "revenue_growth": 22.5,
                "employment": 40000,
                "employment_growth": 15.8,
                "hotels": 420,
                "hotels_growth": 12.5,
                "avg_stay": 5.5,
                "stay_duration_change": 0.8
            }
        },
        "cultural_info": {
            "art_forms": [
                {"name": "Thangka Painting", "description": "Buddhist scroll painting"},
                {"name": "Carpet Weaving", "description": "Traditional Sikkimese patterns"},
                {"name": "Wood Carving", "description": "Religious and decorative items"}
            ],
            "festivals": [
                {"name": "Losar", "month": "February-March", "description": "Tibetan New Year"},
                {"name": "Saga Dawa", "month": "May-June", "description": "Buddhist festival"},
                {"name": "Pang Lhabsol", "month": "August", "description": "Mountain worshipping festival"}
            ],
            "cuisines": [
                {"name": "Momos", "description": "Traditional dumplings"},
                {"name": "Thukpa", "description": "Noodle soup"},
                {"name": "Gundruk", "description": "Fermented leafy vegetable"}
            ]
        },
        "destinations": {
            "popular": [
                {
                    "name": "Nathula Pass",
                    "description": "Indo-China border pass",
                    "attractions": ["Mountain Views", "Snow Experience", "Tsomgo Lake"],
                    "best_time": "May to October"
                },
                {
                    "name": "Pelling",
                    "description": "View point for Kanchenjunga",
                    "attractions": ["Pemayangtse Monastery", "Kanchenjunga Falls", "Ruins of Rabdentse"],
                    "best_time": "September to May"
                }
            ],
            "hidden_gems": [
                {
                    "name": "Dzongu",
                    "description": "Lepcha reserve",
                    "attractions": ["Traditional Villages", "Organic Farms", "River Teesta"],
                    "best_time": "March to May"
                },
                {
                    "name": "Yumthang Valley",
                    "description": "Valley of Flowers",
                    "attractions": ["Hot Springs", "Flower Meadows", "River Valley"],
                    "best_time": "March to June"
                }
            ]
        }
    }
}

def get_state_data(state_name: str) -> Dict[str, Any]:
    """Get all data for a specific state"""
    return STATES_DATA.get(state_name, {})

def get_all_states() -> List[str]:
    """Get list of all available states"""
    return list(STATES_DATA.keys())

def get_state_overview(state_name: str) -> Dict[str, Any]:
    """Get overview data for a specific state"""
    state_data = STATES_DATA.get(state_name, {})
    return state_data.get("overview", {})

def get_tourism_stats(state_name: str) -> Dict[str, Any]:
    """Get tourism statistics for a specific state"""
    state_data = STATES_DATA.get(state_name, {})
    return state_data.get("tourism_stats", {"yearly_stats": []})

def get_cultural_info(state_name: str) -> Dict[str, Any]:
    """Get cultural information for a specific state"""
    state_data = STATES_DATA.get(state_name, {})
    return state_data.get("cultural_info", {})

def get_destinations(state_name: str) -> Dict[str, Any]:
    """Get destination information for a specific state"""
    state_data = STATES_DATA.get(state_name, {})
    return state_data.get("destinations", {"popular": [], "hidden_gems": []}) 