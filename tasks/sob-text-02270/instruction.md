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
Pork Pie (film): Pork Pie is a 2017 comedy road movie written and directed by New Zealander Matt Murphy and produced by Tom Hern.  The film is a remake of 1981 movie "Goodbye Pork Pie", the first New Zealand film to win a substantial local audience.  The remake stars Dean O'Gorman, James Rolleston and Ashleigh Cummings as a trio of accidental outlaws who travel the length of New Zealand in a stolen yellow New Mini.  The film was scored by Jonathan Crayford

No Right Turn: No Right Turn is an independently produced feature film from Denmark directed by David Noel Bourke.  It stars Laura Bach, Sira Stampe, Tao Hildebrand and Lars Lippert.

Niels Arden Oplev: Niels Arden Oplev (] ) (born 26 March 1961) is a writer-director from Denmark.

Billa (2009 film): Billa is a 2009 Indian Telugu-language action thriller film directed by Meher Ramesh.  Prabhas plays the lead role, where he plays dual roles of the characters Billa and Swami Ranga, with Anushka Shetty and Namitha playing the heroines.  The film, which began in October 2008, released in April 2009.  It is a remake of the 2007 Tamil film of the same name.  This is the second Telugu remake of the 1978 Hindi movie "Don" after the 1979 N.T.R. starrer "Yugandhar".  Actress Jayasudha has a guest role as Janaki in this film, while in "Yugandhar" she played Anuskha's role.  The film had several changes to suit the audience.  The film recorded as "Hit" at the box office.  This film is dubbed in Hindi under the title "The Return of Rebel 2" by Goldmines Telefilms in 2017.

Flatliners: Flatliners is a 1990 American science fiction psychological horror film directed by Joel Schumacher, produced by Michael Douglas and Rick Bieber, and written by Peter Filardi.  It stars Kiefer Sutherland, Julia Roberts, William Baldwin, Oliver Platt, and Kevin Bacon.  The film is about five medical students who attempt to find out what lies beyond death by conducting clandestine experiments that produce near-death experiences.  The film was shot on the campus of Loyola University (Chicago) between October 1989 and January 1990, and was nominated for an Academy Award for Best Sound Editing in 1990 (Charles L. Campbell and Richard C. Franklin).  The film was theatrically released on August 10, 1990, by Columbia Pictures.  A remake, directed by Danish filmmaker Niels Arden Oplev, was released in September 2017.

Flatliners (2017 film): Flatliners is a 2017 American science fiction psychological horror film directed by Niels Arden Oplev and written by Ben Ripley.  The film is a remake of the 1990 film of the same name, and stars Ellen Page, Diego Luna, Nina Dobrev, James Norton, Kiersey Clemons and Kiefer Sutherland (who also starred in the original), and follows five young medical students who attempt to conduct experiments that produce near-death experiences. Sony Pictures released the film in the United States on September 29, 2017.

Death Wish (2017 film): Death Wish is an upcoming American vigilante action film directed by Eli Roth, a remake of the 1974 film of the same name which starred Charles Bronson in the lead, based on the 1972 novel written by Brian Garfield.  The remake will star Bruce Willis as main character Paul Kersey, and is scheduled to be released on November 22, 2017, by Metro-Goldwyn-Mayer.

Brothers (2009 film): Brothers is a 2009 American psychological war drama film and a remake of Susanne Bier's Danish film "Brødre" (2004), which takes place in Afghanistan and Denmark.  The film stars Tobey Maguire, Jake Gyllenhaal, and Natalie Portman, and is directed by Jim Sheridan.  Both films take inspiration from Homer's epic poem, the "Odyssey".  The film received a mixed to positive response and grossed $43 million.  Tobey Maguire received particular praise for his performance and received a Golden Globe nomination for Best Actor in a Motion Picture Drama for his performance.

The Legend of the Condor Heroes (2017 TV series): The Legend of the Condor Heroes is a 2017 Chinese television series adapted from Louis Cha's novel of the same title and a remake of the 1983 Hong Kong television series based on the same novel.  The series was directed by Jeffrey Chiang and starred Yang Xuwen, Li Yitong, Chen Xingxu and Meng Ziyi in the lead roles.  It started airing on Dragon TV in mainland China on 9 January 2017, and on TVB Jade in Hong Kong on 8 May 2017.

Udaharanam Sujatha: Udaharanam Sujatha (English: "Example Sujatha") is a 2017 Malayalam movie, starring Manju Warrier in the lead.  The film is directed by debutant Phantom Praveen.  The film is produced by Martin Prakkat ad Joju George.  This is the remake of the Tamil film Amma Kanakku, which itself is a remake of the Hindi film Nil Battey Sannata.  Udaharanam Sujatha is a musical film . The film has about 7 songട including 1 Promo Song sung by Suresh Thampanor . The Songട are well placed along with the flow of the story .

Question: Which writer-director from Denmark directed a remake of Flatliners in 2017?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the director."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the director."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the individual."
        }
      },
      "required": [
        "name",
        "nationality",
        "profession"
      ],
      "additionalProperties": false
    },
    "film_remake": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film remake."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film remake."
        },
        "original_film_title": {
          "type": "string",
          "description": "The title of the original film that was remade."
        }
      },
      "required": [
        "title",
        "release_year",
        "original_film_title"
      ],
      "additionalProperties": false
    },
    "relationship": {
      "type": "string",
      "description": "Describes the relationship between the director and the film."
    }
  },
  "required": [
    "director",
    "film_remake",
    "relationship"
  ],
  "additionalProperties": false
}
