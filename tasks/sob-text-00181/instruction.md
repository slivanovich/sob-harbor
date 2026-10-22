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
Aklan River: Aklan River is the longest river in the province of Aklan, Philippines and the third longest river in Panay Island, with a total length of 71 km.  ( 44 mi ), only Panay River in Capiz and Jalaur River in Iloilo has longer.  Aklan River drainage basin is the third largest in Panay.  The river source started in the Central Panay Mountain Range in western portion of Capiz on Tapaz area, and the river travel toward north from Tapaz to the mountainous western portion of Jamindan, Capiz, and changing its direction toward northeast to the town of Libacao, Aklan.  Traverses through to the municipalities of Madalag, Malinao, Banga, Lezo, Numancia, and Kalibo before emptying to its mouth into Sibuyan Sea.  It is located in the province of Aklan, Western Visayas, Philippines.  The name of the river is where the term Aklan came from, and is derived from the word "akae", which means to boil or to froth.  Because of the swiftness of the river current, the water of the Aklan river seems to boil or froth.  Akean therefore means "where there is boiling or frothing".

Mount Lupa: Mount Lupa ( ) is a flat-topped, ice-covered mountain, over 1,625 m high, standing between Romulus Glacier and Martin Glacier close east-southeast of Black Thumb and 5 nmi east of the head of Rymill Bay, on the west coast of Graham Land, Antarctica.  It was first roughly surveyed in 1936 by the British Graham Land Expedition under John Rymill.  It was resurveyed in 1948–49 by the Falkland Islands Dependencies Survey who applied the name.  This mountain lies near the heads of Romulus and Remus Glaciers, and the name derives from the mythological story of the she-wolf (Lupa) which fed the twins Romulus and Remus after they had been thrown into the Tiber.

Romulus (donkey): Romulus is the world's tallest living donkey, as certified by the Guinness World Records.  He is just over 2 2/3 times as tall as Kneehi, the Guinness World Record holder for shortest donkey.  He is owned by Phil and Cara Barker Yellott of Adrian, Michigan.  Romulus is an American Mammoth Jackstock gelding.  Romulus has a brother Remus, who is just 2 inch shorter.

Darling River: The Darling River is the third longest river in Australia, measuring 1472 km from its source in northern New South Wales to its confluence with the Murray River at Wentworth, New South Wales.  Including its longest contiguous tributaries it is 2844 km long, making it the longest river system in Australia.

Kings of Alba Longa: The kings of Alba Longa, or Alban kings (Latin: "reges Albani"), were a series of legendary kings of Latium, who ruled from the ancient city of Alba Longa.  In the mythic tradition of ancient Rome, they fill the 400-year gap between the settlement of Aeneas in Italy and the founding of the city of Rome by Romulus.  It was this line of descent to which the Julii claimed kinship.  The traditional line of the Alban kings ends with Numitor, the grandfather of Romulus and Remus.  One later king, Gaius Cluilius, is mentioned by Roman historians, although his relation to the original line, if any, is unknown; and after his death, a few generations after the time of Romulus, the city was destroyed by Tullus Hostilius, the third King of Rome, and its population transferred to Alba's daughter city.

Velabrum: The Velabrum is the low valley in the city of Rome that connects the Forum with the Forum Boarium, and the Capitoline Hill with the western slope of the Palatine Hill.  Before the construction of the Cloaca Maxima, which probably follows the course of an ancient stream, the area was a swamp.  Ancient authorities state that in this marshy area the roots of a fig tree "(Ficus Ruminalis)" caught and stopped the basket carrying Romulus and Remus as it floated along on the Tiber current.  The place therefore has a high symbolic significance.

Celer (builder): According to Ovid's description of the founding of Rome by Romulus (Fasti IV.809 ff.) , Celer was the name of an otherwise unknown foreman, appointed by Romulus to oversee the building of Rome's first walls.  Ovid, perhaps in part to exonerate the emperor Augustus' great forefather, relates how it was actually this foreman Celer (not Romulus) who struck down Remus for jumping over the wall in its early stages in an act of mockery towards his brother's attempt to fortify the new city.  Romulus is portrayed by the poet as putting on a brave front at Remus' funeral, stoically suppressing his tears and grief in order to be a role model for his people.  Ovid relates the account in connection with his description of the Roman festival of Parilia (April 21).  Ovid also provides additional allusions to Celer's killing of Remus further on in the "Fasti", in connection with festival of Lemuria (Fasti V - May 9).

Romulus and Remus (Rubens): Romulus and Remus is a painting by the Flemish artist Peter Paul Rubens.  It is housed in the Pinacoteca Capitolina in Rome, Italy.  It depicts the brothers Romulus and Remus being cared for by a wolf.  The painting also shows the god of the Tiber river sitting on his urn, a woodpecker that watched over the twins to bring them food, and a shepherd discovering the infants.

Tiber: The Tiber ( , Latin "Tiberis", Italian "", ] ) is the third-longest river in Italy, rising in the Apennine Mountains in Emilia-Romagna and flowing 406 km through Tuscany, Umbria and Lazio, where it is joined by the river Aniene, to the Tyrrhenian Sea, between Ostia and Fiumicino.  It drains a basin estimated at 17375 km2 .  The river has achieved lasting fame as the main watercourse of the city of Rome, founded on its eastern banks.

Romulus and Remus: In Roman mythology, Romulus and Remus are twin brothers, whose story tells the events that led to the founding of the city of Rome and the Roman Kingdom by Romulus.  The killing of Remus by his brother, and other tales from their story, have inspired artists throughout the ages.  Since ancient times, the image of the twins being suckled by a she-wolf has been a symbol of the city of Rome and the Roman people.  Although the tale takes place before the founding of Rome around 750 BC, the earliest known written account of the myth is from the late 3rd century BC.  Whether the twins' myth was an original part of Roman myth or a later development is a subject of ongoing debate.

Question: What is the longest river in Italy that carried Romulus and Remus on its current?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "river_name": {
      "type": "string",
      "description": "The name of the river."
    },
    "country": {
      "type": "string",
      "description": "The country where the river is located."
    },
    "length_km": {
      "type": "integer",
      "description": "The total length of the river in kilometers."
    },
    "rank_in_country": {
      "type": "integer",
      "description": "The river's rank by length within its country."
    },
    "association_with_romulus_remus": {
      "type": "string",
      "description": "How the river is associated with Romulus and Remus."
    }
  },
  "required": [
    "river_name",
    "country",
    "length_km",
    "rank_in_country",
    "association_with_romulus_remus"
  ],
  "additionalProperties": false
}
