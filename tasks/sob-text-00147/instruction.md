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
Mak's Noodle: Mak's Noodle () is a traditional Cantonese restaurant in Central, Hong Kong, specialising in wonton noodles.

Canadian cuisine: Canadian cuisine varies widely depending on the regions of the nation.  The three earliest cuisines of Canada have First Nations, English, Scottish and French roots, with the traditional cuisine of English Canada closely related to British cuisine, while the traditional cuisine of French Canada has evolved from French cuisine and the winter provisions of fur traders.  With subsequent waves of immigration in the 19th and 20th century from Central, Southern, and Eastern Europe, South Asia, East Asia, and the Caribbean, the regional cuisines were subsequently augmented.

Regional cuisine: Regional cuisine is cuisine based upon national, state or local regions.  Regional cuisines may vary based upon food availability and trade, varying climates, cooking traditions and practices, and cultural differences.  One noteworthy definition is based upon "traditional cuisine": "A traditional cuisine is a coherent tradition of food preparation that rises from the daily lives and kitchens of a people over an extended period in a specific region of a country, or a specific country, and which, when localized, has notable distinctions from the cuisine of the country as a whole."  Regional food preparation traditions, customs and ingredients often combine to create dishes unique to a particular region.  Regional cuisines are often named after the geographic areas or regions that they originate from.

Nicaraguan cuisine: Nicaraguan cuisine includes a mixture of indigenous cuisine, Spanish cuisine and Creole cuisine.  Despite the blending and incorporation of pre-Columbian and Spanish-influenced cuisine, traditional cuisine differs on the Pacific coast from the Caribbean coast.  While the Pacific coast's main staple revolves around local fruits and corn, the Caribbean coast's cuisine makes use of seafood and coconut.

Russian cuisine: Russian cuisine is a collection of the different cooking traditions of the Russian people.  The cuisine is diverse, with Northern European, Central European, Central Asian, Siberian, East Asian and Middle Eastern influences as Russia is by area the largest country in the world.  Russian cuisine derives its varied character from the vast and multi-cultural expanse of Russia.  Moreover, it is necessary to divide Russian traditional cuisine and Soviet cuisine, which has its own peculiarity.  Its foundations were laid by the peasant food of the rural population in an often harsh climate, with a combination of plentiful fish, pork, poultry, caviar, mushrooms, berries, and honey.  Crops of rye, wheat, barley and millet provided the ingredients for a plethora of breads, pancakes, pies, cereals, beer and vodka.  Soups and stews are centered on seasonal or storable produce, fish and meats.  Such food remained the staple for the vast majority of Russians well into the 20th century.

Cantonese cuisine: Cantonese cuisine (廣東菜), also known as Yue cuisine or Guangdong cuisine, refers to the cuisine of China's Guangdong Province, particularly the provincial capital, Guangzhou (Canton).  It is one of the Eight Culinary Traditions of Chinese cuisine.  Its prominence outside China is due to the large number of emigrants from Guangdong.  Chefs trained in Cantonese cuisine are highly sought after throughout China.  When Westerners speak of Chinese food, they usually refer to Cantonese cuisine.

Macedonian cuisine: Macedonian cuisine (Macedonian: Македонска кујна , "Makedonska kujna"), an aspect of Balkan cuisine, is the traditional cuisine of the Macedonia.  It reflects Mediterranean and Middle Eastern influences and shares characteristics of other Balkan cuisines.  The relatively warm climate of the country provides excellent growth conditions for a variety of vegetables, herbs and fruits.  Macedonian cuisine is also noted for the diversity and quality of its dairy products, wines, and local alcoholic beverages, such as rakija.

Levantine cuisine: Levantine cuisine is the traditional cuisine of the Levant, known in Arabic as the Bilad ash-Sham and Mashriq, which covers a large area of the Eastern Mediterranean.  It continues to carry an influentially mainstream character in a majority of the dishes today.  It is found in the modern states of Jordan, Lebanon, Israel, Palestine, Syria, and parts of southern Turkey near Adana, Gaziantep, and Antakya (the former Vilayet of Aleppo).  In the broader family of Mediterranean cuisine, Cypriot cuisine also has strong Levantine influences.

List of Russian restaurants: This is a list of notable Russian restaurants.  Russian cuisine is a collection of the different cooking traditions of the Russian people.  Russian cuisine derives its varied character from the vast and multi-cultural expanse of Russia.  Moreover, it is necessary to divide Russian traditional cuisine and Soviet cuisine, which has its own peculiarity.  Its foundations were laid by the peasant food of the rural population in an often harsh climate, with a combination of plentiful fish, poultry, game, mushrooms, berries, and honey.  Crops of rye, wheat, barley and millet provided the ingredients for a plethora of breads, pancakes, cereals, beer and vodka.  Soups and stews full of flavor are centered on seasonal or storable produce, fish and meats.

Mughlai cuisine: Mughlai cuisine consists of dishes developed in Medieval India at the centers of the Mughal Empire.  It represents a combination of the cooking style and recipes of Central Asia and North India.  The Mughlai cooking styles is used in the traditional cuisine of North India (especially Uttar Pradesh and Delhi), the Indian city of Hyderabad and the Pakistani city of Karachi (particularly among Muhajir migrants from India).  The cuisine is strongly influenced by Central Asian cuisine, the region where the Turco-Mongol Mughal rulers originally hailed from, and it has in turn strongly influenced the regional cuisines of modern India, Pakistan and Bangladesh.

Question: The traditional cuisine Mak's Noodle is located where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "restaurant_name": {
      "type": "string",
      "description": "The name of the restaurant."
    },
    "restaurant_type": {
      "type": "string",
      "description": "The type of restaurant, e.g., traditional, modern."
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the restaurant is located."
        },
        "region_or_country": {
          "type": "string",
          "description": "The region or country where the restaurant is located."
        }
      },
      "required": [
        "city",
        "region_or_country"
      ],
      "additionalProperties": false
    },
    "specialty_cuisine": {
      "type": "string",
      "description": "The specific cuisine or dish the restaurant specializes in."
    }
  },
  "required": [
    "restaurant_name",
    "restaurant_type",
    "location",
    "specialty_cuisine"
  ],
  "additionalProperties": false
}
