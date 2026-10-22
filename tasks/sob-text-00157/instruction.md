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
Klaus Weber: Klaus Weber (5 April 1936 – 8 August 2016) was a German scientist who made many fundamentally important contributions to biochemistry, cell biology, and molecular biology, and was for many years the director of the Laboratory of Biochemistry and Cell Biology at the Max Planck Institute for Biophysical Chemistry in Göttingen, Germany.

BG Göttingen: BG Göttingen ("Basketballgemeinschaft Göttingen" – "Basketball Association Göttingen") is a German basketball club based in Göttingen, Germany.  In 2010, the club won the EuroChallenge against Krasnye Krylya Samara from Russia.  The team had played in Germany's second division nearly every season since its foundation up to the 2006–07 season, in which Göttingen played in the Basketball Bundesliga.

Lichtenberg's Avertissement: Lichtenberg's Avertissement, written by Georg Christoph Lichtenberg, is a poster intended to deter the citizens of Göttingen, Germany, from attending the performance of Jacob Philadelphia in 1777.  The performance was supposed to be an exhibition of scientific experiments; however, Lichtenberg considered it to be a magic show.  He was angered by the alleged deception and posted the following satire in order to persuade people to avoid the performance.  As a result of the extravagant claims that were posted, Philadelphia left Göttingen without giving any exhibitions.

Göttingen minipig: Göttingen Minipig (also known as the Göttinger or Goettingen Minipig) is a breed of miniature swine developed specifically for use in biomedical research.  The Göttingen Minipig is a member of the species Sus scrofa domestica along with other domesticated swine.  The Göttingen Minipig is best known for its exceptionally small size and its very clean and well-characterized health status.  Development of this breed began in the late 1960s at the Institute of Animal Breeding and Genetics (Institut fϋr Tierzucht und Haustiergenetik) at the University of Göttingen, Germany, by crossbreeding the Minnesota minipig, the Vietnamese Potbelly Pig and the German Landrace pig.  Today the Göttingen Minipig is bred at four separate locations globally and is used in life-saving biomedical research all over the world.

Eva-Maria Neher: Dr. Eva-Maria Neher (née Ruhr, born 22 November 1950) is a German scientist in the fields of biochemistry and microbiology.  She founded the Göttingen Xlab and has been its Executive Director since 2000.  The Göttingen Xlab is an experimental laboratory for training young people from student to scientist level.  She is married to Erwin Neher who is a Nobel laureate for his Nobel Prize in Physiology or Medicine.  She is the recipient of many awards including the Lower Saxony State Prize.

Helmut Holzapfel: Helmut Holzapfel (born 1950 in Göttingen, Germany) is a German scientist.  He is Professor of Transportation Planning at University of Kassel, Germany.

Old Botanical Garden of Göttingen University: The Old Botanical Garden of Göttingen University (German: "Alter Botanischer Garten der Universität Göttingen" or "Alter Botanischer Garten Göttingen"), with an area of 4.5 hectares, is an historic botanical garden maintained by the University of Göttingen.  It is located in the "Altstadt" at Untere Karspüle 1, adjacent to the city wall, Göttingen, Lower Saxony, Germany, and open daily.

Göttingen Observatory: Göttingen Observatory ("Universitätssternwarte Göttingen" (Göttingen University Observatory) or "königliche Sternwarte Göttingen" (Royal Observatory Göttingen)) is a German astronomical observatory located in Göttingen, Lower Saxony, Germany.

Jens Reich: Jens Georg Reich (born 26 March 1939 in Göttingen) is a German scientist and a member of the German Ethics Council.  He has become famous as a civil rights campaigner in the last decade of the GDR times.

Georg Christoph Lichtenberg: Georg Christoph Lichtenberg (1 July 1742 – 24 February 1799) was a German scientist, satirist, and Anglophile.  As a scientist, he was the first to hold a professorship explicitly dedicated to experimental physics in Germany.  Today, he is remembered for his posthumously published notebooks, which he himself called "Sudelbücher", a description modelled on the English bookkeeping term "scrapbooks", and for his discovery of the strange tree-like electrical discharge patterns now called Lichtenberg figures.

Question: Lichtenberg's Avertissement, is a poster intended to deter the citizens of Göttingen, Germany, from attending the performance of Jacob Philadelphia in 1777, it was written by which German scientist, satirist, and Anglophile?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the author."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions or roles of the author."
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "work_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the work."
        },
        "purpose": {
          "type": "string",
          "description": "The stated purpose of the work."
        }
      },
      "required": [
        "title",
        "purpose"
      ],
      "additionalProperties": false
    },
    "event_details": {
      "type": "object",
      "properties": {
        "event_performer": {
          "type": "string",
          "description": "The name of the performer whose event the work was intended to deter."
        },
        "event_year": {
          "type": "integer",
          "description": "The year the event was supposed to take place."
        },
        "event_location": {
          "type": "string",
          "description": "The location where the event was supposed to take place."
        }
      },
      "required": [
        "event_performer",
        "event_year",
        "event_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "author_details",
    "work_details",
    "event_details"
  ],
  "additionalProperties": false
}
