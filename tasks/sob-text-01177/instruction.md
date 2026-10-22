Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Ito-Balmond Serpentine Pavilion: The Ito-Balmond Serpentine Pavilion is a structure designed by Cecil Balmond and Toyo Ito and originally built for the Serpentine Gallery Pavilion programme in London's Kensington Gardens, Hyde Park, in 2002 and now part of a restaurant in southern France.  It focuses on modern and contemporary art.  Each year the Serpentine Gallery builds a temporary structure for the summer in its grounds, and projects are led by director Julia Peyton-Jones.  The Ito-Balmond Serpentine Pavilion has been hailed as one of the most successful temporary pavilions to date.  Jonathan Glancey, architecture critic for the UK's "The Guardian", called it "one of the most exquisite and revolutionary buildings of recent times."  The design is based on an algorithm designed by Balmond.  "Although fun to look at, this structure was rooted in complex geometry…the pavilion had no façade and no hidden structural frame behind it… what you saw was 100% pure structure, its holistic beauty like that of a crystal or a snowflake."  Balmond was awarded the Gengo Matsui Prize for the pavilion, one of the highest awards for engineering given in Japan.  The pavilion now serves as the beach club restaurant of a luxury hotel in Le Beauvallon, across the bay from Saint-Tropez in southern France.  Ito and Balmond have since collaborated on the Taichung Opera House in Taiwan.

Via Napoli Pizzeria e Ristorante: Via Napoli Pizzeria e Ristorante is one of two restaurants in the Italy Pavilion at Epcot's World Showcase at Walt Disney World Resort in Florida.  Via Napoli is one of two Epcot eateries operated by the Patina Restaurant Group, the other being Tutto Italia Ristorante.  The menu is curated by chef Joachim Splichal.  The restaurant was inspired by the dining/architecture trademarks of Naples and Florence, with the house speciality being Neapolitan pizza.  The restaurant trio of brick ovens are named Vesuvius, Etna, and Stromboli.

Pavilion Mountain: Pavilion Mountain is a mountain in the Marble Range in the South Cariboo region of the South-Central Interior of British Columbia, Canada, located northeast of the ranching and First Nations community of Pavilion and to the north of Marble Canyon and immediately south of Kelly Lake, which is the focus of Downing Provincial Park.  The term Pavilion Mountain is also used to refer to the historic ranch and associated rangeland on the "bench" on the mountain's southwestern side, and also to the road which traverses that benchland and the mountain's western shoulder and is the route of the Old Cariboo Road.  The switchback descent from the summit of the road was known as the Rattlesnake Grade and was an infamous stretch of the old wagon road.  From a junction at the road-summit, a road leads east along the spine of the mountain to the peak, which is the site of a microwave relay and former fire lookout.  The mountain's only named subpeak, Mount Carson, at 2005 metres (6578 ft, prominence: 120 m), is southeast of the fire lookout and is named for the original owner of the ranch and was briefly misapplied as the name of Pavilion Mountain.  Robert Carson was one of the first settlers in the region and whose sons later became prominent MLAs and provincial cabinet ministers.  The north wall of Marble Canyon is essentially the southeast buttress of Pavilion Mountain.

Teppan Edo: Teppan Edo is one of three restaurants in the Japan Pavilion at Epcot's World Showcase at Walt Disney World Resort in Florida.  Teppan Edo is a teppanyaki-style restaurant, meaning the food is cooked right in front of you at the table.  The restaurant is directly above, and connected to, the Mitsukoshi department store.  The decor and theming is intended to reflect the "vivaciousness" of the Edo period.  Foods that are cooked on the table are steaks, chicken, shrimps, scallops, and vegetables. Select sushi rolls, miso soup, edamame, and tempura is offered as an appetizer, and various ice cream flavors, as well as mousses are options for dessert.  Kids meal are served in monorail-shaped boxes.

Germany Pavilion at Epcot: The Germany Pavilion is a German-themed pavilion that is part of the World Showcase, within Epcot at Walt Disney World in Orlando, Florida, United States.  Its location is between the Chinese and Italian pavilions.

Probka Restaurant Group: Probka Restaurant Group (Russian Cyrillic: ресторанная группа Пробка) is a restaurant group that was founded by Aram Mnatsakanov in 2001 with the establishment of the wine bar, Probka (English translation: wine bottle cork), and the Italian restaurant, Il Grappolo, in St. Petersburg.  It now consists of nine Italian restaurants and one Russian restaurant which are spread all over St. Petersburg.  It consists of Ryba Na Dache, Probka, Mozzarella Bar, Gusto and Il Grappolo restaurants among others.  The Probka restaurant network consists of a strict Italian cuisine.  Although this is the case, the group is experimenting with Asian cuisine as well.  To date there are three restaurants with the name "Mozzarella Bar," the last one having been opened in February 2010.  These restaurants are among the most successful and popular in St. Petersburg.  Probka has become a very influential group in the Russian restaurant industry with mainly Italian cuisine.

Hollywood &amp; Vine (restaurant): Hollywood & Vine (formerly Hollywood & Vine Cafeteria of the Stars) is a restaurant located next to the 50's Prime Time Café in Disney's Hollywood Studios, one of the four main theme parks at Walt Disney World.  This restaurant is one of only five restaurants in park that recommend or require advance reservations, the others being the Hollywood Brown Derby, Mama Melrose's Ristorante Italiano, the 50's Prime Time Café, and the Sci-Fi Dine-In Theater Restaurant.  Both beer and wine are served at Hollywood & Vine.  Hollywood & Vine is one of three restaurants in the park that offer early entry into the show "Fantasmic! " Prior to 1998, the restaurant was called Hollywood & Vine Cafeteria; "of the Stars" was added to the name that year in recognition of the restaurant's newly instituted star-themed character meals.  In 2003, there were twenty character meals offered at Walt Disney World, during which actors portraying various Disney characters would interact with guests while they ate at the parks' restaurants, and Disney was in the process of increasing the presence of costumed characters in the parks at the time.  Nonetheless, Minnie Mouse character meals held at Hollywood & Vine were discontinued that year, and Robert Johnson of the "Orlando Sentinel" partially attributed this cancellation to competition from the Sci-Fi Dine-In, which he said "almost always has a line of customers waiting."  Hollywood & Vine had resumed its Minnie Mouse character meals by 2005.  By 2012, the character meals had been changed to be Playhouse Disney-themed.  By 2015, the Playhouse Disney characters had been switched out for Disney Junior characters.  During "Star Wars" Weekends, the restaurant offers Jedi Mickey's "Star Wars" Dine, a character meal with "Star Wars"-themed decorations, music, and food.

Royal Pavilion Tavern: The Royal Pavilion Tavern, commonly known as the Pavilion Tavern or Pav Tav, is a pub in the centre of Brighton, part of the English coastal city of Brighton and Hove.  Its original name of the Royal Pavilion Hotel indicates its original role; now it is one of the seaside resort's oldest surviving pubs.  Converted from a house in the early 19th century, it was also used as a court for several years.  Prominent local architect Amon Henry Wilds was responsible for its redesign as a hotel and inn.  English Heritage has listed the building at Grade II for its architectural and historical importance, and it stands within a conservation area.

Restaurant Marrakesh: Restaurant Marrakesh is one of three restaurants in the Morocco Pavilion at Epcot's World Showcase at Walt Disney World Resort in Florida.  The restaurant serves from a menu of Moroccan and other Arabian dishes for both lunch and dinner.  Select dishes include both chicken and seafood pastilla, harira, a variety of couscous and kebabs, fish tajine, merguez, and semolina pasta.

Biergarten Restaurant: Biergarten Restaurant is one of two restaurants in the Germany Pavilion at Epcot's World Showcase at Walt Disney World Resort in Florida.  The restaurant is styled as a typical Bavarian village, replete with the flags of every German state, numerous facades, and a running watermill.  The table features long communal benches for seating, as well as a band playing German folk music.  The restaurant is buffet-style, offering such dishes as schnitzel, bratwurst, kielbasa, rouladen, spatzle, sauerkraut, sauerbraten, cucumber salad, and strudel.

Question: What is the name of the German-themed pavilion in which Biergarten Restaurant is one resturant it

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "pavilion_name": {
      "type": "string",
      "description": "The name of the German-themed pavilion."
    },
    "pavilion_theme": {
      "type": "string",
      "description": "The theme of the pavilion."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "park_name": {
          "type": "string",
          "description": "The name of the theme park where the pavilion is located."
        },
        "world_showcase_area": {
          "type": "string",
          "description": "The specific area within the park where the pavilion is located."
        }
      },
      "required": [
        "park_name",
        "world_showcase_area"
      ],
      "additionalProperties": false
    },
    "restaurants_info": {
      "type": "object",
      "properties": {
        "total_restaurants_in_pavilion": {
          "type": "integer",
          "description": "The total number of restaurants in the pavilion."
        },
        "featured_restaurant": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the featured restaurant."
            },
            "style": {
              "type": "string",
              "description": "The dining style of the featured restaurant."
            }
          },
          "required": [
            "name",
            "style"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "total_restaurants_in_pavilion",
        "featured_restaurant"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "pavilion_name",
    "pavilion_theme",
    "location_details",
    "restaurants_info"
  ],
  "additionalProperties": false
}
