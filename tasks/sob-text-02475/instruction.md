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
Hubert Léonard: Hubert Léonard (7 April 1819 – 6 May 1890) was a famous Belgian violinist, born at Liège.  His earliest preparatory training was given by a prominent teacher of the time, August Rouma, after which he entered the Paris Conservatoire in 1836.  There he studied for three years under François Antoine Habeneck.  In 1844 he started his extended tours which established his reputation as one of the greatest of virtuosos. From 1848 to 1867 he held the position of principal professor of violin playing at the Brussels Conservatoire, having succeeded the celebrated Charles de Bériot.  Owing to ill health, he resigned and settled in Paris, where he spent the rest of his life, and where he gave lessons.  Among his notable students were Alfred De Sève, Martin Pierre Marsick, Henri Marteau, Henry Schradieck, and César Thomson.  He wrote a significant pedagogical work entitled "Ecole Léonard".

Peter de Ru: Peter de Ru is a photographer born 1946 in Oostkapelle in The Netherlands.  In 1969 he moved to Sweden.  After language studies at the Göteborg University he moved to Stockholm and entered the renowned Fotoskolan (Photo School) under Christer Strömholm where he studied 1971 to 1974.  He is married to the Swedish artist Susann Wallander.  Peter de Ru is represented at several state institutions like the Swedish Radio, the Nobel Museum, the Karolinska Hospital, and since 2011 at the National Museum in Stockholm (the Swedish State portrait gallery at Gripsholm).

Peter de Sève: Peter de Sève is an American artist who has worked in the illustration and animation fields.  He has drawn many covers for the magazine "The New Yorker".  As a character designer, he worked on the characters of "A Bug's Life", "Finding Nemo", "Robots", the four "Ice Age" films (including Scrat), and on the main animal character E.B. (voiced by Russell Brand) in the 2011 Easter themed comedy film "Hop".  Most recently, he designed the characters for "Arthur Christmas", for which he was nominated for Annie Award.  He received the National Cartoonists Society Magazine Illustration Award for 2000.  He is part of the Directors Collective Hornet Incorporated company.

Alfred De Sève: Alfred De Sève (May or June 1858 – 25 November 1927) was a Canadian violinist, composer, and music educator.  His compositional output includes works for violin and piano, solo piano, and orchestra; many of which were published by Arthur P. Schmidt and Charles H. Ditson.

Fyre: Fyre, formerly de Jong Explorer, is a cross-platform tool for producing artwork based on histograms of iterated chaotic functions.  It implements the Peter de Jong map in a fixed function pipeline through either a GTK GUI frontend, or a command line facility for easier rendering of high-resolution, high quality images.  The program was renamed from de Jong Explorer to Fyre simply because "<nowiki>'It wasn't taken yet'</nowiki>" and so that in the future, it could support more functions than just the standard Peter de Jong map.  Fyre features a sidebar on the left to which the user can input the required variables and on the right is displayed the result of the equation.

Peter de Koning: Peter de Koning (born 13 October 1960, Vlaardingen) is a Dutch singer.  In 1995 he had a big hit with the single, "Het is altijd lente in de ogen van de tandarts-assistente" written by Jan Rooymans.  It was written as part of his final exam at Rotterdam Conservatory.  It reached #5 in the Dutch Singles Chart.  He followed that up with the album "De avonturen van Peter de Koning"

Peter de Rivaux: Peter de Rivaux or Peter de Rivalis (died 1262) was an influential Poitevin courtier at the court of Henry III of England.  He was related to Peter des Roches, being a nephew (or possibly a son).

Jacques de Sève: Jacques de Sève (fl.  1742 - 1788) was a French illustrator.

Oscar Martel: Oscar Martel (February 1848 – 1924) was a renowned Canadian violinist and violin teacher.  Born in L'Assomption, Quebec, he received his earliest violin instruction from his grandfather, Pierre Martel.  He then studied at the Collège de L'Assomption and at the Royal Conservatory of Liège.  He taught at both the New England Conservatory and at the Chicago Musical College.  His notable pupils included Eugène Chartier and Alfred De Sève.  He died in Chicago.

Arthur Christmas: Arthur Christmas is a 2011 British-American 3D computer animated Christmas comedy film, produced by Aardman Animations and Sony Pictures Animation as their first collaborative project.  The film was released on 11 November 2011, in the UK, and on 23 November 2011, in the USA.

Question: When was "Arthur Christmas", the film that Peter de Sève designed the characters for, released in the US?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "character_designer": {
      "type": "string",
      "description": "The name of the artist who designed the characters for the film."
    },
    "release_information": {
      "type": "object",
      "properties": {
        "release_year": {
          "type": "integer",
          "description": "The year the film was released."
        },
        "usa_release_date": {
          "type": "string",
          "description": "The specific release date of the film in the USA."
        },
        "uk_release_date": {
          "type": "string",
          "description": "The specific release date of the film in the UK."
        }
      },
      "required": [
        "release_year",
        "usa_release_date",
        "uk_release_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "character_designer",
    "release_information"
  ],
  "additionalProperties": false
}
