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
Bahrain Pearling Trail: The Bahrain Pearling Trail or Bahrain Pearling Pathway is a serial cultural heritage site inscribed on the UNESCO World Heritage List in 2012.  It consists of 3 oyster beds in the Bahrain northern waters, a segment of the coast and the seafront Bu Mahir fortress in the southern tip of Muharraq, and 17 buildings in Muharraq historical town connected by a 3.5 km visitor pathway.  The Site was inscribed as a UNESCO World Heritage Site on June 30, 2012 and is Bahrain's second World Heritage Site after the Bahrain Fort.

List of World Heritage Sites in Western Asia: The UNESCO (United Nations Educational, Scientific and Cultural Organization) has designated 82 World Heritage Sites in 18 countries (also called "state parties") of Western Asia: Armenia, Azerbaijan, Bahrain, Cyprus, Georgia, Iran, Iraq, Israel, Jordan, Lebanon, Oman, Palestine, Saudi Arabia, Syria, Turkey, United Arab Emirates, Qatar and Yemen.  While Egypt is partially in Western Asia, it's World Heritage Sites are listed under Africa instead.  One site is located in Jerusalem.  Kuwait is the only country in the region that does not have any World Heritage Sites.  Arabian Oryx Sanctuary was designated as a World Heritage Site of Oman in 1994 but was delisted in 2007.  As the protected area was reduced by 90% as a result of Oman's decision, UNESCO delisted the site.

Manovo-Gounda St. Floris National Park: Manovo-Gounda St. Floris National Park is a national park and UNESCO World Heritage Site located in the Central African Republic prefecture Bamingui-Bangoran, near the Chad border.  It was inscribed to the list of World Heritage Sites in 1988 as a result of the diversity of life present within it.  Notable species include black rhinoceroses, elephants, Sudan cheetahs, leopards, red-fronted gazelles, and buffalo, giraffes, lions; a wide range of waterfowl species also occurs in the northern floodplains.  The site is under threat due to its rare wildlife dying and animals species being wiped out.  The western black rhinoceros that was indigenous to the Central African Republic has gone extinct in 2011.  The site was added to the List of World Heritage in Danger after reports of illegal grazing and poaching by heavily armed hunters, who may have harvested as much as 80% of the park's wildlife.  The shooting of four members of the park staff in early 1997 and a general state of deteriorating security brought all development projects and tourism to a halt.  The government of the Central African Republic proposed to assign site management responsibility to a private foundation.  The preparation of a detailed state of conservation report and rehabilitation plan for the site was recommended by the World Heritage Committee at its 1998 session.  People are working on breeding programs to revive the natural wildlife.

Wet Tropics of Queensland: The Wet Tropics of Queensland World Heritage Site consists of approximately 8,940 km² of Australian wet tropical forests growing along the north-east Queensland portion of the Great Dividing Range.  The Wet Tropics of Queensland meets all four of the criteria for natural heritage for selection as a World Heritage Site.  World Heritage status was declared in 1988.  The Wet Tropics were added to the Australian National Heritage List in May 2007.

Białowieża Forest: Białowieża Forest (Belarusian: Белавежская пушча, "Biełaviežskaja Pušča" ; Polish: "Puszcza Białowieska"   ] ; Russian: Беловежская пуща, "Belovezhskaya Pushcha" ) is one of the last and largest remaining parts of the immense primeval forest that once stretched across the European Plain.  The forest is home to 800 European bison, Europe's heaviest land animal.  UNESCO’s Man and the Biosphere Programme (MAB) designated the Polish Biosphere Reserve "Białowieża " in 1976 and the Belarusian Biosphere Reserve "Belovezhskaya Puschcha " in 1993.  In 2015, the Belarusian Biosphere Reserve occupied the area of 216,200 ha , subdivided into transition, buffer and core zones.  The forest has been designated a UNESCO World Heritage Site and an EU Natura 2000 Special Area of Conservation.  The World Heritage Committee by its decision of June 2014 approved the extension of the UNESCO World Heritage site “Belovezhskaya Pushcha/Białowieża Forest, Belarus, Poland”, which became “Białowieża Forest, Belarus, Poland”.  It straddles the border between Poland (Podlaskie Voivodeship) and Belarus (Brest and Grodno "voblast "s), and is 70 km north of Brest, Belarus and 62 km southeast of Białystok, Poland.  The Białowieża Forest World Heritage site covers a total area of 141,885 ha .

Waldschlösschen Bridge: The Waldschlösschen Bridge (German: Waldschlößchenbrücke or Waldschlösschenbrücke ) is a road bridge across the Elbe river in Dresden.  The bridge was intended to remedy inner-city traffic congestion.  Its construction was highly controversial, as the Dresden Elbe Valley had been declared a UNESCO World Heritage Site and UNESCO expressed strong concerns against the bridge, noting its intent to withdraw the World Heritage title if the bridge were built.  As a result of this project, the Dresden Elbe Valley was listed in 2006 as an "Endangered World Heritage Site" (one of two in Europe, the Medieval Monuments in Kosovo being the other one), and in 2009 became only the second World Heritage Site to be de-listed.

Nouakchott: Nouakchott ( ; ] ; Arabic: نواكشوط‎ ‎ "Nuwākshūṭ ", originally derived from Berber Nawākšūṭ, "place of the winds") is the capital and largest city of Mauritania.  It is one of the largest cities in the Sahara.  The city also serves as the administrative and economic centre of Mauritania.

Banc d'Arguin National Park: The Banc d'Arguin National Park (Arabic: حوض أركين‎ ‎ ) of Bay of Arguin lies in Western Africa on the west coast of Mauritania between Nouakchott and Nouadhibou.  The World Heritage Site is a major breeding site for migratory birds, including flamingos, broad-billed sandpipers, pelicans and terns. Much of the breeding is on sand banks including the islands of Tidra, Niroumi, Nair, Kijji and Arguim.  The surrounding waters are some of the richest fishing waters in western Africa and serve as nesting grounds for the entire western region.

Wandu: Wandu, called Hwando in Korean, was the second capital of the Goguryeo kingdom.  The remains of the mountain fortress are part of the UNESCO World Heritage Site Capital Cities and Tombs of the Ancient Koguryo Kingdom.  It is located 2.5 kilometers west of Ji'an, Jilin province in Northeast China, near the North Korean border.  It is part of the UNESCO World Heritage Site Capital Cities and Tombs of the Ancient Koguryo Kingdom, together with nearby Guonei City and the Wunü Mountain City.

Cornwall and West Devon Mining Landscape: The Cornwall and West Devon Mining Landscape is a World Heritage Site which includes select mining landscapes in Cornwall and West Devon in the south west of England.  The site was added to the World Heritage List during the 30th Session of the UNESCO World Heritage Committee in Vilnius, July 2006.  Following plans in 2011 to restart mining at South Crofty, and to build a supermarket at Hayle Harbour, the World Heritage Committee drafted a decision in 2014 to put the site on the List of World Heritage in Danger, but this was rejected at the 38th Committee Session at Doha, Qatar (July 2014), in favour of a follow-up Reactive Monitoring Mission.

Question: What country houses a capital that is one of the largest cities in the Saraha and is also home to The World Heritage Site?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_name": {
      "type": "string",
      "description": "The name of the country."
    },
    "capital_city": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the capital city."
        },
        "description": {
          "type": "string",
          "description": "A description of the capital city's significance, specifically its size relative to the Sahara."
        }
      },
      "required": [
        "name",
        "description"
      ],
      "additionalProperties": false
    },
    "world_heritage_sites": {
      "type": "array",
      "description": "A list of World Heritage Sites located in the country.",
      "items": {
        "type": "object",
        "properties": {
          "site_name": {
            "type": "string",
            "description": "The name of the World Heritage Site."
          },
          "location_description": {
            "type": "string",
            "description": "A brief description of the site's location or key features."
          }
        },
        "required": [
          "site_name",
          "location_description"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "country_name",
    "capital_city",
    "world_heritage_sites"
  ],
  "additionalProperties": false
}
