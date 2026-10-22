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
David Bohm: David Joseph Bohm FRS (December 20, 1917 – October 27, 1992) was an American scientist who has been described as one of the most significant theoretical physicists of the 20th century and who contributed unorthodox ideas to quantum theory, neuropsychology and the philosophy of mind.

David Peat: David Peat (22 March 1947 – 16 April 2012) was an award-winning Scottish documentary-maker, cinematographer and photographer.

Ignite the Genius Within: Ignite The Genius Within is a multi-media creativity book co-authored by author and journalist Christopher Lee Nutter and EMDR therapist Dr. Christine Ranck.  It was published by Dutton Penguin in March, 2009 (ISBN  ).  The book uses visuals with audio stimulus created by Dr. David Grand derived from EMDR trauma therapy to the end of enhancing creativity.  It was endorsed by performance artist Laurie Anderson and actress / playwright Sarah Jones (stage actress).

Imagine: How Creativity Works: Imagine: How Creativity Works is the third non-fiction book by Jonah Lehrer, published in 2012.  It explores brain science, and creativity and its social aspects.  By July 2012, the book had been recalled by its publisher due to factual inaccuracies.

David M. Levinson: David Matthew Levinson (born 1967) is an American civil engineer and transportation analyst, currently a professor at the University of Minnesota, where he holds the RP Braun/CTS Chair in Transportation.  He has authored or co-authored 4 books, edited 3 collected volumes, and authored or co-authored over 100 peer-reviewed articles on various aspects of transportation.  His most widely cited works are on transportation accessibility and on the travel time budget.  He has developed models of the co-evolution of transport and land use systems, demonstrating mutual causality empirically.  He is a founder of the World Society for Transport and Land Use Research.  In 1995 he was awarded the Charles Tiebout prize in Regional Science by the Western Regional Science Association, and in 2004, the CUTC-ARTBA New Faculty Award.  His travel behavior research was featured in the book "Traffic" by Tom Vanderbilt.

Science, Order, and Creativity: Science, Order, and Creativity is a book by theoretical physicist David Bohm and physicist and writer F. David Peat.  It was originally published 1987 by Bantam Books, USA, then 1989 in Great Britain by Routledge.  The second edition, published in 2000 after Bohm`s death, comprises a new foreword by Peat as well as an additional introductory chapter, in which a fictitious dialogue between Bohm and Peat serves to introduce the reader to the context and topics of the book.

Seven Life Lessons of Chaos: Seven Life Lessons of Chaos: Spiritual Wisdom From the Science of Change is a book by Western Connecticut State University English Professor John Briggs and Physicist F. David Peat (who also co-authored "Turbulent Mirror").  Originally published in 1999 by Harper Collins, the book consists of 175 pages plus notes and an index (ISBN  , OCLC 38206755  ).

Big Banana Feet: Big Banana Feet is a 1976 comedy documentary film following Billy Connolly on his 1975 tour of Ireland.  The film was directed by Murray Grigor and David Peat, and was made in two days.

Pari Center for New Learning: The Pari Center for New Learning is a non-profit educational center located in the village of Pari in Civitella Paganico of the Province of Grosseto, Italy.  The center was directed by F. David Peat, who co-authored the book "Science, Order, and Creativity" with theoretical physicist David Bohm.  The center has hosted, with the support of its renowned "fellows" from academia and the arts, the academy "Accademia dei Pari".  It hosts international conferences on the role of trust and ethics in the world of economics and business, and conferences on the relationship between religion and science.

Pan Wenshi: ​Pan Wenshi(潘文石) is Peking University professor.  His research works on giant panda, white-headed langur and Chinese white dolphin in the last 36 years are internationally recognized contributions.  Pan had authored and co-authored 40 – 50 treatises published on various domestic and international journals including National Geographic and Nature and he is renowned for his academic achievements on researching the 3 near-extinct contemporary species.  In his book The Natural Refuge of Giant Panda at Qinling (秦嶺大熊猫的自然庇護所) co-authored with postgraduates under his supervision, researchers and other collaborators, Pan put forward for the first time arguments supporting “giant pandas in Qinling can survive living in natural conditions” which was acclaimed by international peers to be “significant contribution to the biological theory of giant panda”.  Following that in his book Chance for Continual Survival (繼績生存的機會) Pan commented that “since the cause leading to the near-extinct of giant panda was human error, it must require human to rectify their acts in order giant pandas could have a chance for continual survival”.  In the book The White Dolphins of Qinzhou (欽州的白海豚) Prof. Pan and his co-authors unveiled that Chinese white dolphin appeared in Beibu Gulf only from 6000 years ago and that in the Beibu Gulf population is preserved an ancient and rare genotype that is so far never found in populations in other territorial waters.  In the book he as well suggested that the social developments of Qinzhou must be planned to optimize a win-win situation between its economy and nature conservation for that is the only way to achieve sustainable development.  The Natural History of White-headed Langur (白頭葉猴自然史) is a live record of researches in wilderness.  When Prof. Pan went into the Nongguan Mountains he noticed there the sustenance environment was almost totally devastated and that “human was suffering more miserably than the langurs there”.  In view of which he suggested “the core issue of nature conservation in Nongguan Mountains is to improve the living conditions of the people there.  Only after people’s lives been improved could white-headed langur conservation be anticipated”.  20 years practice of his words has proved his foresight; during the period the white-headed langur population in Nongguan Mountains has increased from the initial of about 100 individuals to about 820 individuals, and the people there have as well gradually improved their livings to well-off standard. <br>

Question: What was the nationality of the person F. David Peat co-authored the book "Science, Order, and Creativity" with?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the book."
        },
        "co_authors": {
          "type": "array",
          "description": "A list of co-authors for the book.",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the author."
              },
              "role": {
                "type": "string",
                "description": "The role of the author in the book (e.g., 'primary author', 'co-author')."
              },
              "nationality": {
                "type": "string",
                "description": "The nationality of the author."
              }
            },
            "required": [
              "name",
              "role",
              "nationality"
            ],
            "additionalProperties": false
          }
        }
      },
      "required": [
        "title",
        "co_authors"
      ],
      "additionalProperties": false
    },
    "person_questioned": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person whose nationality is being asked."
        },
        "relationship_to_book": {
          "type": "string",
          "description": "The person's relationship to the book (e.g., 'co-author')."
        }
      },
      "required": [
        "name",
        "relationship_to_book"
      ],
      "additionalProperties": false
    },
    "answer_nationality": {
      "type": "string",
      "description": "The nationality of the person in question."
    }
  },
  "required": [
    "book_details",
    "person_questioned",
    "answer_nationality"
  ],
  "additionalProperties": false
}
