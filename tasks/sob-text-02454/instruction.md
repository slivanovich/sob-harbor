{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Wounded Table: The Wounded Table (\"La mesa herida\" in Spanish) is an oil painting by Mexican artist Frida Kahlo.  Although lost in 1955, three photos of this painting were taken between 1940 and 1944.  The painting was first displayed in January 1940 at the International Surrealism Exhibit at Inés Amor's Gallery of Mexican Art in Mexico City, and a replica is currently displayed in the Kunstmuseum Gehrke-Remund, Baden-Baden, Germany.  The painting was last exhibited in Warsaw in 1955.\n\nLa Lecture: La Lecture (or Reading) is a painting by Spanish artist Pablo Picasso completed in January 1932.  The oil painting depicts Picasso's mistress and muse, Marie-Thérèse Walter, asleep with a book upon her lap.  The painting led to the breakup of Picasso's marriage to Olga Khokhlova after she saw it at a retrospective exhibition and realised that the facial features were not her own.  The painting went to auction in 1989 and in 1996, where it failed to sell.  In January 2011, it was announced that \"La Lecture\" would be going to auction on 8 February.  The painting, which had not been seen in Europe since the exhibition, was then displayed at Sotheby's in Paris.\n\nFuneral Procession (painting): Funeral Procession is the name of a painting by Ellis Wilson, which went from obscurity to notoriety in 1985, when it was featured heavily in the plot of a season 2 episode of the hit TV series \"The Cosby Show\".  In the episode, Mrs. Huxtable wins the painting at an auction and pays $11,000 for it.  She states that the painting was made by her \"great-uncle Ellis\".  At the end of the episode, Dr. Huxtable hangs the painting over the family's living room mantle, where it would stay for the remainder of the eight-season series.  In real life, the painting is displayed as part of the Aaron Douglas Collection at the Amistad Research Center at Tulane University in New Orleans, Louisiana.  Ellis Wilson was born on April 20, 1899 in Mayfield, Kentucky, and died on either January 1 or 2, 1977.  In real life, the most he ever got for one of his paintings was about $300.\n\nShepherd with a Flute: Shepherd with a flute is a painting produced around 1508 by Giorgione, now in the Royal Collection and shown at Hampton Court Palace.\n\nLinda Obermoeller: Linda Obermoeller (March 4, 1941 - January 1, 1990) was an American painter known for her watercolor portraits.  During her career she worked with watercolor and pencil.  She died at age 48.  At the time of her death was displaying her work at the Harris Gallery in Houston, Texas and she had a painting displayed at the Watercolor USA Honor Society Watercolor Now II, a national juried exhibition, in which her watercolor, “Still Life with Trout”, won first place posthumously (1990).\n\nHampton Court Palace: Hampton Court Palace is a royal palace in the borough of Richmond upon Thames, London, England, 11.7 mi south west and upstream of central London on the River Thames.  Building of the palace began in 1515 for Cardinal Thomas Wolsey, a favourite of King Henry VIII.  In 1529, as Wolsey fell from favour, the King seized the palace for himself and later enlarged it.  Along with St James's Palace, it is one of only two surviving palaces out of the many owned by King Henry VIII.\n\nPerkins House (DeKalb, Mississippi): The Perkins House in Dekalb, Mississippi is a historic structure listed on the National Register of Historic Places in 1994 for its architectural significance as a mid-nineteenth century example of a vernacular middle-class farmhouse as well as the artistic significance of the ornamental painting displayed throughout the interior of the house.  The Perkins House was originally built around 1870, and the artwork was added in the 1890s.  The house was originally located on Murphy Hardy Rd, northwest of its junction with Mississippi Highway 493 but was moved to its current location on Townsend Road in 2012 after being purchased by new owners.\n\nTom Mauchahty-Ware: Tom Mauchahty-Ware (March 21, 1949 – November 3, 2015) was a Kiowa-Comanche musician.  He was known for his work playing the Native American flute, and has been a successful Indian dancer, and has sung in a popular blues band.  He was also a skilled traditional artist: painting, sculpting, making flutes, bead working, and feather working.  He was a descendent of the famous Kiowa flutist, Belo Cozad, and made two commercial recordings, \"Flute Songs of the Kiowa and Comanche\" (1978) and \"The Traditional and Contemporary Indian Flute of Tom Mauchahty Ware\" (1983).\n\nA Palace Concert: A Palace Concert () is a Chinese Tang Dynasty silk painting showing ten court ladies and two standing servant maidens around a large rectangular table.  Some court ladies are depicted drinking tea, while others drink wine.  The four women at the far end are presumably responsible for playing music and livening up the mood.  The musical instruments depicted, from left to right, are bamboo pipes, guqin, pipa and flute.  One of the servant maidens plays a clapper to maintain beat.  A small dog is depicted under the table.  The artist and the precise year of the painting are unknown.  The painting is housed in the National Palace Museum in Taipei, Taiwan.\n\nInvestiture of Zimri-Lim: The Investiture of Zimri-Lim is a large colorful mural discovered at the Royal Palace of the ancient city-state of Mari in eastern Syria.  The fresco, which dates back to the 18th century BC, depicts Zimri-Lim, king of Mari, receiving the symbols of rule (a ring and a staff) from the goddess Ishtar.  The painting was discovered \"in situ\" on its original wall located opposite the grand doorway to the podium which leads to the throne room of the palace.  It was discovered by French archaeologist André Parrot during excavations at Mari in 1935–1936.  The painting is now displayed at the Musée du Louvre in Paris, France.\n\nQuestion: Shepherd with a flute is a painting displayed in a palace in what country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"painting_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the painting.\"\n    },\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who created the painting.\"\n    },\n    \"display_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the palace or venue where the painting is displayed.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of location where the painting is displayed (e.g., 'palace').\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the display location is situated.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the painting is displayed, serving as the direct answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"painting_title\",\n    \"artist_name\",\n    \"display_location\",\n    \"answer_country\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "painting_title": {
        "type": "string",
        "description": "The title of the painting."
      },
      "artist_name": {
        "type": "string",
        "description": "The name of the artist who created the painting."
      },
      "display_location": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the palace or venue where the painting is displayed."
          },
          "type": {
            "type": "string",
            "description": "The type of location where the painting is displayed (e.g., 'palace')."
          },
          "country": {
            "type": "string",
            "description": "The country where the display location is situated."
          }
        },
        "required": [
          "name",
          "type",
          "country"
        ],
        "additionalProperties": false
      },
      "answer_country": {
        "type": "string",
        "description": "The country where the painting is displayed, serving as the direct answer to the question."
      }
    },
    "required": [
      "painting_title",
      "artist_name",
      "display_location",
      "answer_country"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
