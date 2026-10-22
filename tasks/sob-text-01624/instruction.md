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
M. Night Shyamalan: Manoj Nelliyattu "M. Night" Shyamalan ( ; ; "Maṉōj Nelliyāṭṭu Śyāmaḷaṉ"; Tamil: மனோஜ் நெல்லியட்டு ஷியாமளன் ; Malayalam: മനോജ് നെല്ലിയാട്ട് ശ്യാമളന്‍ born 6 August 1970) is an Indian American film director, screenwriter, author, producer, and actor known for making movies with contemporary supernatural plots and surprise endings.  His most well-received films include the supernatural horror thriller "The Sixth Sense" (1999), the superhero drama thriller "Unbreakable" (2000), and the science fiction thriller "Signs" (2002).  Afterwards, Shyamalan released a series of poorly received but sometimes financially successful movies, including the historical drama-horror film "The Village" (2004), the fantasy film "Lady in the Water" (2006), the disaster film "The Happening" (2008), the film adaptation of "The Last Airbender" (2010), and the science-fiction film "After Earth" (2013).  Following the financial failure of "After Earth," Shyalaman's career was revived with the release of the found footage horror "The Visit" (2015) and the psychological horror "Split" (2016), the latter of which is set in the same universe as his previous film "Unbreakable".  He is also known for producing "Devil" (2010), as well as being instrumental in the creation of the Fox science fiction series "Wayward Pines.

Howard Blumenthal: Howard Blumenthal is an American television and new media producer, author, educator, and executive.  Born and raised in New York City and nearby suburbs, he is the son of author and Concentration producer Norm Blumenthal, and the grandson of radio and music retailer Harry Blumenthal.  He is best known as the co-creator and producer of the Peabody Award winning PBS series, "Where in the World Is Carmen Sandiego? "

Sam Mercer: Sam Mercer is a producer of many Hollywood films, including several projects directed by M. Night Shyamalan such as "Signs", "Lady in the Water" and "Unbreakable", as well as other films like "Van Helsing" and "Things We Lost in the Fire".  His career started during the early 1980s as a location manager and later advanced to a producer and executive producer.  He also produced the M. Night Shyamalan films "The Happening" and "The Last Airbender".

Norm Green: Norm Green (born November 3, 1956 as Norman Green) is an American director and executive producer.

Signs (film): Signs is a 2002 American science fiction horror film written and directed by M. Night Shyamalan and executive produced by Shyamalan, Frank Marshall, Kathleen Kennedy and Sam Mercer.  A joint collective effort to commit to the film's production was made by Blinding Edge Pictures and The Kennedy/Marshall Company.  It was commercially distributed by Touchstone Pictures theatrically, and by Touchstone Home Entertainment in home media format.  Its story focuses on a former Episcopal priest named Graham Hess, played by Mel Gibson, who discovers a series of crop circles in his cornfield.  Hess slowly discovers that the phenomena are a result of extraterrestrial life.  It also stars Joaquin Phoenix, Rory Culkin, and Abigail Breslin.  "Signs" explores faith, kinship, and extraterrestrials.

Greg Brooker (screenwriter): Greg Brooker is an American screenwriter, best known for co-writing the screenplay of "Stuart Little" with M. Night Shyamalan.

India-West: India-West, also known as "India-West Publications, Inc.", is among the leading Indian newspapers in the United States of America which report on issues pertaining to the Indian American population of the United States, with special emphasis on California.  It focuses on issues that relate to, or affect the Indian American community.  Its head office is located in San Leandro, California, in the San Francisco Bay Area.  It also operates a Los Angeles bureau (based in Artesia, California) and bureau in Mumbai, India.  Its weekly circulation is approximately 25,000.  India-West launched a new Web portal Nov. 7, 2011.  The Web portal is the primary go-to source site for all things pertaining to the global Indian community.  It is currently ranked highest among websites of Indian American newspapers by Alexa.  India-West is represented in India by Shemak Acidwalla of MediaLink/MediaMate and the International Media Representation wing of the Times of India group for the purpose of advertising.

Blinding Edge Pictures: Blinding Edge Pictures is an American film production company, founded in 2000 by M. Night Shyamalan, which is known for producing films written and directed by Shyamalan like "Unbreakable" (2000), "Signs" (2002), "The Village" (2004), "The Happening" (2008), "After Earth" (2013), "The Visit" (2015) and "Split" (2017).  In 2015, the company released its first television series "Wayward Pines".

Praying with Anger: Praying with Anger is a 1992 Indian-American drama film, known for M. Night Shyamalan who made his directorial debut, produced, wrote and starred in the film.  It is about a young Indian American's return to India.  To date, the film has been shown primarily at film festivals and never received a wide release for mainstream distribution.  It has gradually developed a cult following as a work exploring the clash of Western values with those of the Indian subcontinent.

The Village (2004 film): The Village is a 2004 American psychological horror film, written, produced, and directed by M. Night Shyamalan, and starring Joaquin Phoenix, Adrien Brody, Bryce Dallas Howard, William Hurt, Sigourney Weaver, and Brendan Gleeson.  The film is about a village whose inhabitants live in fear of creatures inhabiting the woods beyond it referred to as "Those We Don't Speak Of."  Like other films written and directed by Shyamalan from the same time period, "The Village" has a twist ending.

Question: What occupation do American producer Norm Green and Indian American screenwriter M. Night Shyamalan share?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "shared_occupation": {
      "type": "string",
      "description": "The occupation shared by the individuals."
    },
    "occupation_category": {
      "type": "string",
      "description": "A broader category for the shared occupation."
    },
    "individuals": {
      "type": "array",
      "description": "Details of the individuals sharing the occupation.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the individual."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "shared_occupation",
    "occupation_category",
    "individuals"
  ],
  "additionalProperties": false
}
