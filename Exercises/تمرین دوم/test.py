
import pandas as pd
import random

# لیست نام‌های واقعی گیاهان (650 نام منحصر به فرد)
plant_names = [
    "Aloe Vera", "Basil", "Cactus", "Daisy", "Eucalyptus", "Fern", "Geranium",
    "Hibiscus", "Ivy", "Jasmine", "Kale", "Lavender", "Mint", "Narcissus",
    "Orchid", "Peony", "Quince", "Rose", "Sunflower", "Tulip", "Umbrella Plant",
    "Violet", "Wisteria", "Xerophyte", "Yarrow", "Zinnia", "Acacia", "Bamboo",
    "Cedar", "Daffodil", "Elm", "Freesia", "Gardenia", "Hydrangea", "Juniper",
    "Kiwi", "Lemon Balm", "Magnolia", "Nutmeg", "Olive", "Pine", "Quillwort",
    "Rhubarb", "Sage", "Thyme", "Uva-Ursi", "Verbena", "Willow", "Xylosma",
    "Yew", "Zucchini", "Anthurium", "Begonia", "Camellia", "Dandelion",
    "Elderberry", "Foxglove", "Gladiolus", "Heliotrope", "Impatiens", "Jackfruit",
    "Kiwi", "Lily", "Marigold", "Nasturtium", "Oleander", "Pansy", "Quinoa",
    "Raspberry", "Snapdragon", "Tarragon", "Ulex", "Verbena", "Watermelon",
    "Yucca", "Zamia", "Azalea", "Bluebell", "Chrysanthemum", "Dahlia", "Epiphyllum",
    "Fuchsia", "Gloxinia", "Honeysuckle", "Ixora", "Jasmine", "Kudzu", "Lavatera",
    "Mistletoe", "Nymphaea", "Oxalis", "Pothos", "Quassia", "Rudbeckia", "Scaevola",
    "Tithonia", "Ursinia", "Viburnum", "Walnut", "Xanthium", "Yew", "Zantedeschia",
    "Amaranth", "Buttercup", "Cypress", "Delphinium", "Euphorbia", "Forsythia",
    "Goldenrod", "Hawthorn", "Indian Pink", "Juniper", "Kiwi", "Lobelia", "Maranta",
    "Nicotiana", "Onion", "Phlox", "Queen Anne's Lace", "Rutabaga", "Salvia",
    "Tuberose", "Umbrella Tree", "Venus Flytrap", "Walnut", "Xeranthemum",
    "Yam", "Zebra Plant", "Asparagus", "Begonia", "Carnation", "Dracaena",
    "Eustoma", "Fatsia", "Gerbera", "Hibiscus", "Inula", "Jacobinia", "Kaffir Lily",
    "Lobelia", "Magnolia", "Nasturtium", "Orchid", "Primrose", "Quaking Grass",
    "Rhododendron", "Schlumbergera", "Tussock", "Ulex", "Verbena", "Wisteria",
    "Xerophyllum", "Yellow Bells", "Zebra Plant", "Acanthus", "Bougainvillea",
    "Caladium", "Dahlia", "Echinacea", "Fuchsia", "Gaillardia", "Helenium",
    "Ipomoea", "Jasmine", "Kniphofia", "Lavatera", "Monarda", "Nandina",
    "Osmunda", "Petunia", "Quillwort", "Rosemary", "Stachys", "Tithonia",
    "Ursinia", "Vinca", "Wisteria", "Xeranthemum", "Yucca", "Zantedeschia",
    "Aconitum", "Bleeding Heart", "Chicory", "Dianthus", "Eupatorium", "Feverfew",
    "Gentian", "Hellebore", "Iberis", "Jonquil", "Knautia", "Liatris", "Mallow",
    "Nicotiana", "Oregano", "Paeonia", "Quassia", "Red Hot Poker", "Sea Holly",
    "Teasel", "Umbrella Plant", "Vetch", "Woodruff", "Xanthosoma", "Yarrow", "Zenobia",
    "Alyssum", "Borage", "Coreopsis", "Diascia", "Euryops", "Fennel", "Globeflower",
    "Helichrysum", "Incarvillea", "Jacaranda", "Kangaroo Paw", "Lupine", "Maranta",
    "Nemesia", "Osteospermum", "Pennisetum", "Quassia", "Ragwort", "Solomon's Seal",
    "Thalictrum", "Ursinia", "Verbascum", "Water Hyacinth", "Xylobium", "Yam", "Zephyranthes",
    "Amaryllis", "Bromeliad", "Croton", "Dicentra", "Echeveria", "Fritillaria",
    "Gypsophila", "Heliconia", "Ixia", "Kochia", "Lobularia", "Mimosa", "Nephrolepis",
    "Oenothera", "Papaver", "Quisqualis", "Radermachera", "Scabiosa", "Thunbergia",
    "Uvularia", "Veronica", "Wax Plant", "Xyris", "Yucca", "Zamia", "Achillea",
    "Bellflower", "Camellia", "Dianella", "Enkianthus", "Filipendula", "Geum",
    "Holly", "Iris", "Jaboticaba", "Kolkwitzia", "Lonicera", "Mahonia", "Nemophila",
    "Osteospermum", "Paeonia", "Quercus", "Ranunculus", "Santolina", "Torenia",
    "Urceolina", "Vaccinium", "Weigela", "Xanthisma", "Yucca", "Zephyranthes",
    "Anemone", "Bougainvillea", "Ceratostigma", "Dodecatheon", "Erigeron", "Forsythia",
    "Gazania", "Hibiscus", "Ipheion", "Jasminum", "Kniphofia", "Lagerstroemia",
    "Mandevilla", "Nepeta", "Oxalis", "Passiflora", "Quince", "Rhodanthemum", "Streptocarpus",
    "Tacca", "Urginia", "Veronica", "Windflower", "Xerosicyos", "Yucca", "Zelkova",
    "Aster", "Begonia", "Calibrachoa", "Doronicum", "Euphorbia", "Francoa",
    "Gomphrena", "Helenium", "Ixia", "Jatropha", "Kalanchoe", "Leontopodium",
    "Myrtus", "Nolana", "Oxalis", "Pelargonium", "Quercus", "Rosa", "Sisyrinchium",
    "Trollius", "Utricularia", "Viola", "Wahlenbergia", "Xylosma", "Yucca", "Zostera"
]

# print(len(plant_names))

# بررسی و اطمینان از اینکه لیست حداقل 650 نام دارد
if len(plant_names) < 335:
    additional_names = [f"Plant_{i}" for i in range(len(plant_names), 335)]
    plant_names.extend(additional_names)

# انتخاب 650 نام گیاه منحصر به فرد
selected_plant_names = random.sample(plant_names, 335)

# تابع تولید داده‌ها
def generate_data(rows, plant_names):
    data = []
    for plant_name in plant_names:
        sea_irrigation_cost = random.choice([None] + [round(random.uniform(6, 9), 2) for _ in range(9)])
        ocean_irrigation_cost = round(random.uniform(6, 9), 2)
        oxygen_requirement = random.choices(range(30, 91), weights=[1 if 65 <= x <= 78 else 0.5 for x in range(30, 91)])[0]
        ph_preference = random.choices(range(0, 15), weights=[1 if 6 <= x <= 8 else 0.5 for x in range(0, 15)])[0]
        data.append([plant_name, sea_irrigation_cost, ocean_irrigation_cost, oxygen_requirement, ph_preference])
    return data

# ایجاد دیتا
rows = 335
columns = ["نام گیاه", "هزینه آبیاری گیاه در دریا", "هزینه آبیاری گیاه در اقیانوس", "مقدار اکسیژن لازم برای گیاه", "ph مورد علاقه گیاه"]
data = generate_data(rows, selected_plant_names)

# ایجاد DataFrame
df = pd.DataFrame(data, columns=columns)

# ذخیره به فایل اکسل
df.to_excel("plants_data.xlsx", index=False)

print("فایل اکسل با موفقیت ایجاد شد!")

