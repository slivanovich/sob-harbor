{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nElektra (opera): Elektra, Op.  58, is a one-act opera by Richard Strauss, to a German-language libretto by Hugo von Hofmannsthal, which he adapted from his 1903 drama \"Elektra\".  The opera was the first of many collaborations between Strauss and Hofmannsthal.  It was first performed at the Dresden State Opera on 25 January 1909.  It was dedicated to his friends Natalie and Willy Levin.\n\nZauvijek volim te: \"Zauvijek volim te\" (Cyrillic: Заувијек волим те, English translation: \"I Love You Forever\") is a song performed by Stefan Filipović, and was the Montenegrin entry for the Eurovision Song Contest 2008.  It was performed first in the first semi-final on May 20, 2008 but failed to make it to the final.  It got 23 points in total (12 from Bosnia and Herzegovina, 10 from Slovenia and 1 point from San Marino), which was enough only for a 14th place.The 10 and 12 points given make this song the best Montenegrin entry so far.\n\nIt's Too Soon to Know: \"It's Too Soon to Know\" is an American doo-wop ballad by Deborah Chessler (1923-2012), performed first by The Orioles.  It was number one on the American Rhythm and blues charts in November 1948.  It is considered by some to be the first \"rock and roll\" song, and described by others as \"the first rhythm and blues vocal group harmony recording\".\n\nDio, come ti amo: \"Dio, come ti amo\" (English translation: \"God, How I Love You\") was performed first time as duo by Domenico Modugno and Gigliola Cinquetti in San Remo Festival, 1966.  Later it was the Italian entry in the Eurovision Song Contest 1966, performed in Italian by Domenico Modugno.\n\nSweetwater (band): Sweetwater was an American rock band originally from Los Angeles, California.  They were the act scheduled to open the Woodstock Festival in 1969; however, due to being stopped by the police on their way to the festival, folksinger Richie Havens' trio (Daniel Ben Zebulon, percussion, Paul \"Deano\" Williams, guitar, backing vocals) performed first.  Sweetwater performed next, becoming the first band to perform at the festival.\n\nSemi-opera: The terms \"semi-opera\", \"dramatic[k] opera\" and \"English opera\" were all applied to Restoration entertainments that combined spoken plays with masque-like episodes employing singing and dancing characters.  They usually included machines in the manner of the restoration spectacular.  The first examples were the Shakespeare adaptations produced by Thomas Betterton with music by Matthew Locke.  After Locke's death a second flowering produced the semi-operas of Henry Purcell, notably \"King Arthur\" and \"The Fairy-Queen\".  Semi-opera received a deathblow when the Lord Chamberlain separately licensed plays without music and the new Italian opera.\n\nGanglionectomy: A ganglionectomy, also called a gangliectomy, is the surgical removal of a ganglion.  The removal of a ganglion cyst usually requires a ganglionectomy.  Such cysts usually form on the hand, foot or wrist and may cause pain or impair body function.  Aspiration of the cyst and steroid injections are typically performed first.  If they fail, the cyst is excised under local, regional or even general anesthetic.  Ganglionectomies are also performed for other reasons, such as the treatment of chronic pain.\n\nThe Fairy-Queen: The Fairy-Queen (1692; Purcell catalogue number Z.629) is a masque or semi-opera by Henry Purcell; a \"Restoration spectacular\".  The libretto is an anonymous adaptation of William Shakespeare's wedding comedy \"A Midsummer Night's Dream\".  First performed in 1692, \"The Fairy-Queen\" was composed three years before Purcell's death at the age of 35.  Following his death, the score was lost and only rediscovered early in the twentieth century.\n\nTe Siento: \"Te Siento\" (English: I Feel You) is a song performed by reggaeton duo Wisin & Yandel.  The song is taken from Wisin & Yandel's re-release studio album \"Evolution\".  It was released as the third single on December 15, 2009.  On November 5, 2009 a part of the song was performed first time on the Latin Grammy Awards 2009 along with \"Abusadora\", using a short intro-video to perform.\n\nOlive Gilbert: Olive Sarah Gilbert (22 November 1898 – 19 February 1981) was a British singer and actress, who, in a career spanning seven decades, performed first in opera and then in many of Ivor Novello's musicals in London's West End.\n\nQuestion: Which opera was performed first, The Fairy-Queen or Elektra?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"earlier_performance_entity\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the entity that was performed first.\"\n        },\n        \"first_performance_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year of the first performance of the earlier entity.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"first_performance_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"later_performance_entity\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the entity that was performed later.\"\n        },\n        \"first_performance_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year of the first performance of the later entity.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"first_performance_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"comparison_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A summary statement indicating which entity was performed first.\"\n    }\n  },\n  \"required\": [\n    \"earlier_performance_entity\",\n    \"later_performance_entity\",\n    \"comparison_summary\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "earlier_performance_entity": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the entity that was performed first."
          },
          "first_performance_year": {
            "type": "integer",
            "description": "The year of the first performance of the earlier entity."
          }
        },
        "required": [
          "title",
          "first_performance_year"
        ],
        "additionalProperties": false
      },
      "later_performance_entity": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the entity that was performed later."
          },
          "first_performance_year": {
            "type": "integer",
            "description": "The year of the first performance of the later entity."
          }
        },
        "required": [
          "title",
          "first_performance_year"
        ],
        "additionalProperties": false
      },
      "comparison_summary": {
        "type": "string",
        "description": "A summary statement indicating which entity was performed first."
      }
    },
    "required": [
      "earlier_performance_entity",
      "later_performance_entity",
      "comparison_summary"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
