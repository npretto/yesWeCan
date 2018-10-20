myAwesomeServerLessDb = {
    "Aerosols": "Recycling Centre",
    "Agrochemicals": "Recycling Centre",
    "Aluminium cans": "Yellow container",
    "Aluminium foil": "Yellow container",
    "Animal faeces": "Grey container",
    "Batteries": "Recycling Centre",
    "Bread": "Brown container",
    "CD": "Recycling Centre",
    "Cables": "Recycling Centre",
    "Car batteries": "Recycling Centre",
    "Cardboard": "Blue container",
    "Cigarette butts": "Grey container",
    "Clean polystyrene": "Recycling Centre",
    "Cleaning products": "Recycling Centre",
    "Clothes": "Recycling Centre",
    "Clothing accessories": "Punt verd",
    "Coffee capsules": "Recycling Centre",
    "Coffee grounds": "Brown container",
    "Containers": "Recycling Centre",
    "Corks": "Brown container",
    "Cosmetics": "Recycling Centre",
    "Cotton": "Grey container",
    "Cuttings and garden waste": "Recycling Centre",
    "DVD": "Recycling Centre",
    "Dried flowers": "Brown container",
    "Eggshells": "Brown container",
    "Electrical items": "Recycling Centre",
    "Electronics": "Recycling Centre",
    "Engine oil": "Recycling Centre",
    "Envelopes": "Blue container",
    "Expanded polystyrene trays": "Yellow container",
    "Fibrocement with asbestos": "Recycling Centre (only Vall d' Hebron).",
    "Filters for vehicles": "Recycling Centre",
    "Fish": "Brown container",
    "Fluorescent lights": "Recycling Centre",
    "Footwear": "Recycling Centre",
    "Fridges": "Recycling Centre",
    "Fruit": "Brown container",
    "Furniture": "Recycling Centre",
    "Glass bottles": "Green container",
    "Glass containers": "Green container",
    "Glues": "Recycling Centre",
    "Hair": "Grey container",
    "Herbicides": "Recycling Centre",
    "Ink": "Recycling Centre",
    "Large home appliances": "Recycling Centre",
    "Large pieces of cardboard": "Recycling Centre",
    "Large plastic water bottles": "Yellow container",
    "Lead": "Recycling Centre",
    "Leftovers of meat": "Brown container",
    "Light bulbs": "Recycling Centre",
    "Machines": "Recycling Centre",
    "Magazines": "Blue container",
    "Mattresses": "Recycling Centre",
    "Metal bottle lids": "Yellow container",
    "Metal bottle tops": "Yellow container",
    "Mirrors": "Recycling Centre",
    "Monitors": "Recycling Centre",
    "Napkins stained with oil": "Brown container",
    "Nappies": "Grey container",
    "Newspapers": "Blue container",
    "Notebooks without metal spiral": "Blue container",
    "Nuts": "Brown container",
    "Paints": "Recycling Centre",
    "Paper": "Brown container",
    "Paper bags": "Blue container",
    "Paper towels": "Brown container",
    "Pens": "Grey container",
    "Pesticides": "Recycling Centre",
    "Plastic Buckets": "Recycling Centre",
    "Plastic bags": "Yellow container",
    "Plastic wrap": "Yellow container",
    "Rubble": "Recycling Centre",
    "Sanitary towels": "Grey container",
    "Scrap metal": "Recycling Centre",
    "Seafood": "Brown container",
    "Sheet glass": "Recycling Centre",
    "Small tires": "Recycling Centre",
    "Solvents": "Recycling Centre",
    "Sprays": "Recycling Centre",
    "Stainless steel": "Recycling Centre",
    "Staple-free teabags": "Brown container",
    "Steel cans": "Yellow container",
    "Television sets": "Recycling Centre",
    "Tetra paks": "Yellow container",
    "Thermometers": "Recycling Centre",
    "Toner cartridges": "Recycling Centre",
    "Used Cardboard": "Brown container",
    "Used kitchen oil": "Recycling Centre",
    "Used pencils": "Grey container",
    "Varnishes": "Recycling Centre",
    "Vegetables": "Brown container",
    "Videotapes": "Recycling Centre",
    "Windows": "Recycling Centre",
    "Wood": "Recycling Centre",
    "Wrapping paper": "Blue container",
    "Writing paper": "Blue container",
    "Yogurt pots": "Yellow container"
}

def getBin(item):
    if item in myAwesomeServerLessDb:
        return list(myAwesomeServerLessDb.keys()).index(item)
    else:
        return 9999