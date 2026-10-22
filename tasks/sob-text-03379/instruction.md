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
St. Vladimir's Cathedral (St. Petersburg): The Prince St. Vladimir's Cathedral (Russian: Князь-Владимирский Собор ), formally "the Cathedral of St. Equal to the Apostles Prince Vladimir" (собор Святого равноапостольного князя Владимира) is a Russian Orthodox Cathedral in Saint Petersburg, Russia.  It is located on Blokhin Street in the Petrogradsky District of the city across the Malaya Neva from the Spit of Vasilevsky Island, in close proximity to the Sportivnaya metro station.

Khilkov: Khilkoff or Khilkov (Russian: Хилков ) is a Rurikid princely family descending from sovereign rulers of Starodub-on-the-Klyazma.  The descendant of the Great Prince Vladimir Svyatoslavich, the Christianizer of Russia, Prince Ivan Vsevolodovich,(c. 958 – 15 July 1015) received from his brother, the Great Prince Yaroslav Vsevolodovich, the appanage of Starodub, and this originated the Princes of Starodub; those who later had the Ryapolovskaya volost took the name Prince Ryapolovsky in the sixteenth century, for an unknown reason, the Ryapolovskys changed their name: the older branch to Khilkoff, and the younger to Tatev.

Vladimir Petrovich Dolgorukov: Prince Vladimir Petrovich Dolgorukov (Russian: Владимир Петрович Долгоруков; 19 April 1773 – 24 November 1817) was a Russian army officer who rose to the rank of major general.  He was the eldest of the three sons born to the generalPrince Peter Petrovich Dolgorukov (Vladimir's younger brothers Peter and Mikhail were also generals), whilst his own son was the historian and journalist Pyotr Vladimirovich Dolgorukov.

Grand Duke of Vladimir: The Grand Duke of Vladimir was a prince during the Kievan Rus' and after its collapse.  He ruled territory approximately bounded by the Volga, Oka and Northern Dvina rivers.  Its capital was Vladimir during 1157-1238.  Vladimir city was founded by a Kievan prince Vladimir Monomakh in 1108 and was destroyed by a Mongol invasion in 1238.  The second important city was Suzdal', also destroyed by Mongols.  The Grand Duke ("Velikii Kniaz", Great Prince) Yuri Dolgorukii (Yuri "Long-arms"), the seventh son of Vladimir Monomakh, began the lineage of Suzdal' and Vladimir-Suzdal' great princes.  Vladimir-Suzdal' began the next consolidation of Russian lands, completed by Muscovy, which grew from within Vladimir-Suzdal.

Barbara (Yakovleva): Varvara Alexeyevna Yakovleva (Russian: Варвара Алексеевна Яковлева ; died July 18, 1918), called Nun Barbara (Russian: Инокиня Варвара ), was a Russian Orthodox nun in the convent of Grand Duchess Elizabeth Fyodorovna.  She was killed by the Bolsheviks along with the grand duchess and Prince Ioann Konstantinovich of Russia, Prince Konstantin Konstantinovich of Russia, Prince Igor Konstantinovich of Russia, Grand Duke Sergei Mikhailovich of Russia, Fyodor Remez, Grand Duke Sergei's secretary, and Prince Vladimir Pavlovich Paley at Alapaevsk.

Kurya (khan): Kurya (Ukrainian: Куря, Pecheneg: Kürä) was the name of a Pecheneg prince and khan who allied with Svyatoslav I of Kiev in his campaigns in the Balkans.  Later, after Svyatoslav's defeat by the Byzantine Empire, Kurya ambushed and killed the Kievan king at Khortitsa.  According to the "Chronicle of Bygone Years", Kurya had Svyatoslav's skull made into a goblet (a known practice in Eurasian nomadic cultures for brave foes), and gilded.  Dates of his rule are unknown, but he was no longer khan somewhere around 988 CE, being succeeded by Metiga.  It is also possible that he was the leader of the Pechenegs in the 968 siege of Kiev, but since a starting date is unknown, it is almost impossible to tell (and it could have been any of several other Pecheneg princes).  Kurya appears as a villain in the 2006 animated film "Prince Vladimir".

Russian submarine Knyaz Vladimir: Knyaz Vladimir (Russian: АПЛ "Knyaz Vladimir" - Prince Vladimir, previously expected - "Svyatitel Nikolai" - Saint Nicholas) is a Russian ballistic missile submarine and lead ship of the fifth generation Project 955A Borei II-class (sometimes marked as Project 955U) based on fourth generation Project 955 Borei-class submarines.

Master Jiang and the Six Kingdoms: Master Jiang and the Six Kingdoms () is an upcoming Chinese animated fantasy action adventure wuxia film.  The film is currently in production and was scheduled to be released in 2016.  The Film release date has been changed to 2018.  The film is mainly a traditionally-animated feature film and it has some computer animation in it.

Prince Vladimir (film): Prince Vladimir (Russian: Кня́зь Влади́мир , Knyaz Vladimir) is a 2006 Russian traditionally-animated feature film.  It is loosely based on the story of prince Vladimir the Fair Sun, who converted Kievan Rus' (a predecessor state of Russia, Ukraine, and Belarus) to Christianity in the late 10th century.  The film tells a romanticized version of the story, adapted for children and filled with fantasy elements.

Church Statute of Prince Yaroslav: Church Statute of Prince Yaroslav ("Russian: Церковный Устав князя Ярослава ") is a source of church law in Old Rus', defined legal authority of church by the prince (knyaz), his administration and churchmen.  Yaroslav's Statute was a short legal code, regulated relationship between the church and the state, including demarcation of jurisdiction between church and princely courts, index of persons within the church jurisdiction, rules of family law (family law belonged to church jurisdiction) and sanctions against moral violation.  The statute was written at the 11th-12th century and remaked during 13th-16th centuries, in Old Church Slavonic and Old Russian.  It was one of the first church sources of Old Russian Law.  Church Statute of Prince Vladimir and other Old Russian princely statutes served to closely purposes.  But church jurisdiction was expanded in comparison with Vladimir's Statute.  A part of the lawsuits in the Yaroslav's Statute was referred to the church jurisdiction, and a part - to joint jurisdiction of the church and the prince.  One of the sources of the statute was Byzantine law, including Nomocanon.

Question: Who allied with the Pecheneg prince who appears as a villain in a 2006 Russian traditionally-animated feature film loosely based on the story of prince Vladimir the Fair Sun?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the animated feature film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre"
      ],
      "additionalProperties": false
    },
    "villain_character": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the villain character in the film."
        },
        "title_or_role": {
          "type": "string",
          "description": "The title or role of the villain (e.g., prince, khan)."
        },
        "ethnicity_or_group": {
          "type": "string",
          "description": "The ethnic group or people the villain belongs to."
        }
      },
      "required": [
        "name",
        "title_or_role",
        "ethnicity_or_group"
      ],
      "additionalProperties": false
    },
    "ally_of_villain": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the individual who allied with the villain."
        },
        "role_or_title": {
          "type": "string",
          "description": "The role or title of the ally."
        },
        "alliance_purpose": {
          "type": "string",
          "description": "The purpose or context of the alliance."
        }
      },
      "required": [
        "name",
        "alliance_purpose"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_details",
    "villain_character",
    "ally_of_villain"
  ],
  "additionalProperties": false
}
