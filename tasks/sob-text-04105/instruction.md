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
Bayt Dajan: Bayt Dajan (Arabic: بيت دجن‎ , "Bayt Dajan " ‎ ; Hebrew: בית דג'אן‎ ‎ ), also known as Dajūn, was a Palestinian Arab village situated approximately 6 km southeast of Jaffa.  It is thought to have been the site of the biblical town of Beth Dagon, mentioned in the Book of Joshua and in ancient Assyrian and Ancient Egyptian texts.

Bayt Nabala: Bayt Nabala or Beit Nabala was a Palestinian Arab village in the Ramle Subdistrict in Palestine that was destroyed during the 1948 Arab–Israeli War.  The village was in the territory allotted to the Arab state under the 1947 UN Partition Plan.  Its population in 1945, before the war, was 2,310.

Samson: Samson ( ; Hebrew: שִׁמְשׁוֹן,  "Shimshon ",  "Šimšôn " , meaning "man of the sun") was the last of the judges of the ancient Israelites mentioned in the Book of Judges in the Hebrew Bible (chapters 13 to 16) and one of the last of the leaders who "judged" Israel before the institution of the monarchy.  He is sometimes considered to be an Israelite version of the popular Middle Eastern Heracles figure.

Bayt Nuba: Bayt Nuba (Arabic: بيت نوبا‎ ‎ ) was a Palestinian Arab village, located halfway between Jerusalem and al-Ramla.  Historically identified with the biblical city of Nob mentioned in the Book of Samuel, that association has been eschewed in modern times.  The village is mentioned in extrabiblical sources including the writings of 5th-century Roman geographers, 12th-century Crusaders and a Jewish traveller, a 13th-century Syrian geographer, a 15th-century Arab historian, and Western travellers in the 19th century.  Depopulated by Israeli forces during the 1967 war, it was subsequently leveled by military engineers using controlled explosions, and the Israeli settlement of Mevo Horon was established on its lands in 1970.

Bayt 'Itab: Bayt ʿIṭāb (Arabic: بيت عطاب‎ ‎ ) was a Palestinian Arab village located in the Jerusalem Subdistrict.  The village is believed to have been inhabited since biblical times.  An ancient tunnel which led to the village spring is associated with story of Samson.  Prior to, during, and after its incorporation into Crusader fiefdoms in the 12th century, its population was Arab.  Sheikhs from the Lahham family clan, who were associated with the Qays tribo-political faction, ruled the village during Ottoman era.  In the 19th century, this clan controlled 24 villages in the vicinity.  The homes were built of stone.  The local farmers cultivated cereals, fruit trees and olive groves and some engaged in livestock breeding.

Majdal Yaba: Majdal Yaba (Arabic: مجدل يابا‎ ‎ ) was a Palestinian Arab village in the Ramle Subdistrict, located 18.5 km northeast of Ramla and 4 km east of Jaffa.  A walled city stood at the same site as early as 3000 BCE, and Majdal Yaba is first mentioned by the name Aphek in Egyptian Execration texts dating to the 19th century BCE.  In the Bible's Old Testament, Aphek is described as a city conquered from the Canaanites by the Israelites, who then lost it to the Philistines.  It is also mentioned in extrabiblical Babylonian and Assyrian texts as a Philistine stronghold.  Under Roman rule, the city was known as Antipatris and the Crusaders, who built a fort there, renamed it Mirabel.  During the Islamic period it became known as Majdal Yaba.  For a short time under Ottoman rule, its name was changed from Majdal Yaba to Majdal Sadiq and then back again.

Zayta, Hebron: Zayta (Arabic: زيْتا‎ ‎ "Zaytā") was a Palestinian Arab village in the Hebron Subdistrict in Mandate Palestine.  During Crusader rule in Palestine, the village is mentioned as forming part of the landholdings of the Order of St. John.  At the time of the rule of the Ottoman Empire, according to the 1596 census, Zayta had a population of 165.  Mentioned by Western travellers to the region in the 19th century, it is described by one as, "a picturesque Arab village"; by 1945, its population was 330 inhabitants.

Bayt Tima: Bayt Tima (Arabic: بيت طيما‎ ‎ ) was a Palestinian Arab village in the Gaza Subdistrict, located 21 km northeast of Gaza and some 12 km from the coastline.  It was situated in flat terrain on the southern coastal plain of Palestine.  Bayt Tima was depopulated during the 1948 Arab-Israeli War.  Its population in 1945 was 1,060.

Lajjun: Lajjun (Arabic: اللجّون‎ ‎ , "al-Lajjûn") was a Palestinian Arab village located 16 km in Mandatory Palestine, northwest of Jenin and 1 km south of the remains of the biblical city of Megiddo.  Named after an early Roman legion camp in Syria Palaestina province called "Legio", predating the village at that location, Lajjun's history of habitation spanned some 2,000 years.  Under Abbasid rule it was the capital of a subdistrict, during Mamluk rule it served as an important station in the postal route, and during Ottoman rule it was the capital of a district that bore its name.  After the collapse of the Ottoman Empire towards the end of World War I, Lajjun and all of Palestine was placed under the administration of the British Mandate.  The village was depopulated during the 1948 Arab-Israeli War, when it was captured by Israel.  Most of its residents subsequently fled and settled in the nearby town of Umm al-Fahm.

Kafr 'Inan: Kafr ʿInān (Arabic: كفر عنان‎ ‎ ), was a Palestinian Arab village in the Acre Subdistrict around 33 km east of Acre.  Until 1949, it was an Arab village built over the ruins of ancient Kfar Hananya.  Archaeological surveys indicate the village was founded in the early Roman period, and was inhabited through the Byzantine period.  It was resettled in the Middle Ages and the modern era.

Question: Bayt ʿIṭāb, was a Palestinian Arab village located in which Subdistrict, an ancient tunnel which led to the village spring is associated with story of Samson, who was the last of the judges of the ancient Israelites mentioned in the Book of Judges in the Hebrew Bible (chapters 13 to 16) and one of the last of the leaders who "judged" Israel before the institution of the monarchy?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "village_name": {
      "type": "string",
      "description": "The name of the Palestinian Arab village."
    },
    "location": {
      "type": "object",
      "properties": {
        "subdistrict": {
          "type": "string",
          "description": "The subdistrict where the village was located."
        }
      },
      "required": [
        "subdistrict"
      ],
      "additionalProperties": false
    },
    "historical_figures_associated": {
      "type": "array",
      "description": "A list of historical figures associated with the village.",
      "items": {
        "type": "object",
        "properties": {
          "figure_name": {
            "type": "string",
            "description": "The name of the historical figure."
          },
          "association_details": {
            "type": "string",
            "description": "Details of the figure's association with the village."
          },
          "figure_description": {
            "type": "string",
            "description": "A description of the historical figure's role or significance."
          },
          "source_of_information": {
            "type": "object",
            "properties": {
              "book": {
                "type": "string",
                "description": "The book where information about the figure is found."
              },
              "chapters": {
                "type": "string",
                "description": "The specific chapters in the book."
              }
            },
            "required": [
              "book",
              "chapters"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "figure_name",
          "association_details",
          "figure_description",
          "source_of_information"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "village_name",
    "location",
    "historical_figures_associated"
  ],
  "additionalProperties": false
}
