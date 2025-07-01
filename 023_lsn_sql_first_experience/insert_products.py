import sqlite3

products = [
    # Pistols
    ("Colt M1911", "Classic US semi-auto pistol", 1.1, 799, "8.5 in", ".45 ACP", "50 m", "USA", 1),
    ("Glock 17", "Modern Austrian 9mm pistol", 0.9, 599, "8.0 in", "9x19mm", "50 m", "Austria", 1),
    ("Makarov PM", "Soviet military sidearm", 0.73, 499, "6.3 in", "9x18mm", "50 m", "USSR", 1),
    ("SIG Sauer P226", "German police/military pistol", 0.96, 899, "7.7 in", "9x19mm", "50 m", "Germany", 1),
    ("Walther P38", "WW2 era German pistol", 0.96, 650, "8.5 in", "9x19mm", "50 m", "Germany", 1),
    ("Tokarev TT-33", "Soviet military pistol", 0.85, 475, "7.6 in", "7.62x25mm", "50 m", "USSR", 1),
    ("Beretta 92FS", "Modern Italian sidearm", 0.95, 780, "8.5 in", "9x19mm", "50 m", "Italy", 1),
    ("CZ 75", "Czech double-action pistol", 1.0, 740, "8.1 in", "9x19mm", "50 m", "Czech Republic", 1),
    ("FN Herstal FNX-45", "US tactical .45 pistol", 1.2, 980, "8.6 in", ".45 ACP", "50 m", "USA", 1),
    ("Steyr M9-A1", "Modern Austrian polymer pistol", 0.82, 690, "7.4 in", "9x19mm", "50 m", "Austria", 1),

    # Submachine Guns
    ("PPSh-41", "High rate Soviet SMG", 5.4, 1200, "33.9 in", "7.62x25mm", "150 m", "USSR", 2),
    ("MP40", "WW2 German SMG", 4.0, 2000, "24.8 in", "9x19mm", "100-150 m", "Germany", 2),
    ("Thompson M1A1", "WW2 US SMG", 4.8, 1800, "32 in", ".45 ACP", "150 m", "USA", 2),
    ("Uzi", "Compact Israeli SMG", 3.5, 1000, "18.5 in", "9x19mm", "100 m", "Israel", 2),
    ("MP5", "Modern German SMG", 2.5, 2500, "19.3 in", "9x19mm", "200 m", "Germany", 2),
    ("Sterling L2A3", "British SMG, post-WW2", 2.7, 1200, "27.4 in", "9x19mm", "100 m", "UK", 2),
    ("MAC-10", "Compact US machine pistol", 2.9, 850, "10.5 in", ".45 ACP", "75 m", "USA", 2),
    ("PPS-43", "WW2 Soviet SMG", 3.7, 700, "24 in", "7.62x25mm", "150 m", "USSR", 2),
    ("Beretta M12", "Italian police SMG", 3.6, 1100, "17.5 in", "9x19mm", "150 m", "Italy", 2),
    ("FN P90", "Bullpup personal defense weapon", 3.0, 2700, "20.8 in", "5.7×28mm", "200 m", "Belgium", 2),

    # Assault Rifles
    ("AK-47", "Legendary Soviet assault rifle", 4.3, 1500, "34.3 in", "7.62x39mm", "350 m", "USSR", 3),
    ("M16A2", "Standard US military rifle", 3.8, 1700, "39.6 in", "5.56x45mm", "500 m", "USA", 3),
    ("FN FAL", "Battle rifle used by NATO forces", 4.45, 2100, "43 in", "7.62x51mm", "600 m", "Belgium", 3),
    ("StG 44", "First modern assault rifle from WW2", 5.2, 3000, "37 in", "7.92×33mm Kurz", "300 m", "Germany", 3),
    ("AK-74", "Improved Soviet rifle with smaller caliber", 3.3, 1600, "37.1 in", "5.45x39mm", "500 m", "USSR", 3),
    ("HK G36", "Modern German assault rifle", 3.6, 2800, "39.3 in", "5.56x45mm", "600 m", "Germany", 3),
    ("Steyr AUG", "Austrian bullpup rifle", 3.6, 2750, "31.1 in", "5.56x45mm", "500 m", "Austria", 3),
    ("L85A2", "British standard issue rifle", 4.2, 2650, "30.9 in", "5.56x45mm", "400 m", "UK", 3),
    ("FAMAS F1", "French bullpup assault rifle", 3.8, 2500, "29.9 in", "5.56x45mm", "300 m", "France", 3),
    ("Galil ACE", "Modernized Israeli AK-variant", 3.7, 2900, "36.2 in", "7.62x39mm", "400 m", "Israel", 3),

    # Machine Guns
    ("PKM", "Soviet general-purpose machine gun", 7.5, 3200, "46 in", "7.62x54mmR", "1000 m", "USSR", 4),
    ("M60", "US machine gun used since Vietnam War", 10.5, 3500, "42.4 in", "7.62x51mm", "1100 m", "USA", 4),
    ("MG42", "High-rate German WW2 machine gun", 11.5, 4500, "48.4 in", "7.92x57mm", "1200 m", "Germany", 4),
    ("RPD", "Light Soviet squad machine gun", 6.6, 2700, "40.2 in", "7.62x39mm", "800 m", "USSR", 4),
    ("M249 SAW", "US light machine gun for infantry", 7.5, 3800, "40.7 in", "5.56x45mm", "700 m", "USA", 4),
    ("MG3", "Modernized MG42 used by Bundeswehr", 11.6, 4700, "48.4 in", "7.62x51mm", "1200 m", "Germany", 4),
    ("Type 95 LMG", "Chinese light machine gun", 3.4, 2600, "36.2 in", "5.8x42mm", "800 m", "China", 4),
    ("Bren Mk II", "British WW2 light machine gun", 10.2, 4000, "45.5 in", ".303 British", "600 m", "UK", 4),
    ("FN Minimi", "Belgian version of M249", 7.1, 3900, "39.4 in", "5.56x45mm", "800 m", "Belgium", 4),
    ("KORD", "Heavy Russian MG, successor to NSV", 25.5, 5500, "63 in", "12.7x108mm", "2000 m", "Russia", 4),

    # Sniper Rifles
    ("Dragunov SVD", "Semi-auto sniper rifle by USSR", 4.3, 4200, "48.2 in", "7.62x54mmR", "800 m", "USSR", 5),
    ("M24 SWS", "US Army standard bolt-action sniper rifle", 5.4, 4600, "43 in", "7.62x51mm", "800 m", "USA", 5),
    ("Mauser 86SR", "German precision sniper rifle", 6.1, 5200, "46.3 in", "7.62x51mm", "900 m", "Germany", 5),
    ("Barrett M82", "Heavy semi-auto sniper rifle", 14.0, 9000, "57 in", "12.7x99mm (.50 BMG)", "1800 m", "USA", 5),
    ("Blaser R93 Tactical", "German modular sniper rifle", 5.7, 7300, "45 in", "7.62x51mm", "1000 m", "Germany", 5),
    ("T-5000", "Russian precision sniper rifle", 6.5, 8000, "47 in", "7.62x51mm", "1200 m", "Russia", 5),
    ("Accuracy International AXMC", "British sniper rifle with interchangeable barrels", 6.9, 9600, "47.2 in",
     ".338 Lapua Magnum", "1500 m", "UK", 5),
    ("Remington MSR", "US modular sniper rifle", 6.8, 9800, "46 in", ".338 Lapua Magnum", "1500 m", "USA", 5),
    ("Steyr SSG 69", "Classic Austrian sniper rifle", 4.1, 5200, "44 in", "7.62x51mm", "800 m", "Austria", 5),
    ("VSS Vintorez", "Suppressed Soviet sniper rifle", 2.6, 4800, "35.2 in", "9x39mm", "400 m", "USSR", 5)
]

conn = sqlite3.connect("gunstore.db")
cursor = conn.cursor()

cursor.executemany("""
    INSERT INTO products (
        name, description, weight, price, length,
        caliber, effective_range, country_of_origin, category_id
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", products)

conn.commit()
conn.close()

print("✅ Products inserted successfully.")
