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
Der Hölle Rache kocht in meinem Herzen: "Der Hölle Rache kocht in meinem Herzen " ("Hell's vengeance boils in my heart"), commonly abbreviated "Der Hölle Rache ", is an aria sung by the Queen of the Night, a coloratura soprano part, in the second act of Mozart's opera "The Magic Flute" ("Die Zauberflöte ").  It depicts a fit of vengeful rage in which the Queen of the Night places a knife into the hand of her daughter Pamina and exhorts her to assassinate Sarastro, the Queen's rival, on pain of denying and cursing Pamina if she does not comply.

Karl Erb: Karl Erb (13 July 1877 – 13 July 1958) was a German tenor vocalist who made his career first in opera and then in oratorio and lieder recital.  He excelled in all these genres, and before 1920 gave classic performances of key roles in modern works, and created lead roles in those of Hans Pfitzner.  He was the first husband of Maria Ivogün and was considered by many the ideal Evangelist in the "St Matthew Passion" of Johann Sebastian Bach.

Martín Garatuza: Martín Garatuza (born 1601, Puebla, Mexico) was a famous trickster whose frauds and escapes became legendary in colonial New Spain and whose name has passed into Spanish language, folklore and literature.

Asia Argento: Asia Argento [pronounced "ah-see-ah ar-jen-toe] (born Aria Maria Vittoria Rossa Argento; 20 September 1975) is an Italian actress, singer, model, and director.  Argento is best known for the role of Yelena in the action film "xXx", the first installment in the "xXx" franchise.

List of rulers of Ife: The Ooni of Ile-Ife (Ọọ̀ni of Ilè-Ifẹ̀) is the traditional ruler of Ile-Ife.  This Nigerian town is seen as the cradle of the Yoruba people.  The Ooni dynasties go back hundreds of years.  Because the oral tradition was only recently transcribed, there are several detailed lists that contradict each other.  Nevertheless, some key figures are common to all of them.  All the Ooni are traced down to Oduduwa, who is seen as the ancestral father of all the Yoruba people.  Ooni Oranmiyan, who is said to have lived between 1200 and 1300 A.D, became legendary for his role in creating many new towns.  One of his sons, Eweka, became the first Oba of Benin.  Another son, Ajaka, became the first Alaafin of Oyo.  Another, Osile, of Oke-Ona Egba.  Ooni Lajamisan, another descendant of Oranmiyan is often said to have opened the modern Ife history.

Three Guardsmen: The Three Guardsmen is the name popularized in Old West literature describing three lawmen who became legendary in their pursuit of many outlaws of the late 19th century.  Deputy U.S. Marshals Bill Tilghman (1854–1924), Chris Madsen (1851–1944), and Heck Thomas (1850–1912) were "The Three Guardsmen", working under U.S. Marshal Evett "E.D." Nix.

Maria Ivogün: Maria Ivogün (18 November 1891, Budapest – 3 October 1987, Beatenberg, Switzerland) was a distinguished soprano singer of Hungarian origin.  She was especially an outstanding interpreter of the works of Mozart: her recording of the aria of the Queen of the Night ("Die Zauberflöte") became legendary.

Malkotsis: Malkotsis is the trade name for "Technica S. Malkotsis A.E.", which has historically been the most important Greek engine manufacturer, surpassing several engine (mostly diesel and semi-diesel) manufacturers that flourished in Greece in the 1920s and (mostly) 1930s, like "Dimadis-Kanakis" in Volos, "Peteinaris" in Kalamata, "Sideris", "BIO", and others in Athens, etc.  Located in Piraeus, before World War II "Malkotsis" produced various types of industrial machinery.  After the war it produced industrial machinery for several Greek companies, but it progressively focused almost entirely on diesel engines, soon becoming the largest company in its field.  "Malkotsis" engines found use in a variety of industrial applications, while its boat engine models became legendary for their reliability.  A series of electric motors was produced as well.  Its "EM" Diesel series (designed in collaboration with a British consulting firm) included engines specifically designed for powering of vehicles and was employed in "Malkotsis's" own farm tractor models ("Malkotsis EM-2" and "EM-4") introduced in 1959.  The tractors were produced for only a few years, due to lack of funding and other problems related to a complete lack of state support.  The company faced financial problems later, due to competition from cheaper imports, and was acquired in 1991 by Drakos-Polemis A.E., a pump manufacturing company which used all "Malkotsis" infrastructure for its production purposes.

José Félix Aldao: José Félix Esquivel y Aldao (1785 - 1845) was an Argentine Dominican friar who became a General and then the undisputed Federist "caudillo" of Mendoza Province.  His ability as a soldier and his cruelty became legendary.  The largely fictionalized biography that Domingo Faustino Sarmiento wrote fed his legend.

Sophonisba: Sophonisba (also Sophonisbe, Sophoniba; in Punic, 𐤑𐤐𐤍𐤁𐤏𐤋 Ṣap̄anbaʿal) (fl.  203 BC) was a Carthaginian noblewoman who lived during the Second Punic War, and the daughter of Hasdrubal Gisco Gisgonis (son of Gisco).  In an act that became legendary, Sophonisba poisoned herself rather than be humiliated in a Roman triumph.

Question: What is name of the daughter depicted in the aria Maria Ivogün became legendary for?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "aria_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The full title of the aria."
        },
        "opera": {
          "type": "string",
          "description": "The opera from which the aria originates."
        },
        "character_singing": {
          "type": "string",
          "description": "The character who sings the aria."
        }
      },
      "required": [
        "title",
        "opera",
        "character_singing"
      ],
      "additionalProperties": false
    },
    "legendary_singer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the singer whose recording became legendary."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the singer."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "daughter_depicted": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the daughter depicted in the aria."
        },
        "relationship_to_character": {
          "type": "string",
          "description": "The relationship of the daughter to the character singing the aria."
        }
      },
      "required": [
        "name",
        "relationship_to_character"
      ],
      "additionalProperties": false
    },
    "question_answer": {
      "type": "string",
      "description": "The direct answer to the question: the name of the daughter."
    }
  },
  "required": [
    "aria_details",
    "legendary_singer",
    "daughter_depicted",
    "question_answer"
  ],
  "additionalProperties": false
}
