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
Thomas Schumacher: Thomas Schumacher is a theatrical producer, currently president of Disney Theatrical Group, the theatrical production arm of The Walt Disney Company.

James Byng: James Byng (born 1985) is an English actor and vocalist.  Acting since the age of ten, James made his West End debut in the title role of "Oliver! " at the London Palladium.  He played the same role in the national tour of "Oliver!"  and at the Royal Charity Gala "Hey!  Mr. Producer", honoring theatrical producer Cameron Mackintosh at the Lyceum Theatre on 8 June 1998.  Byng also played Gavroche in "Les Misérables" at the Palace Theatre.  From 2007 to 2008 he was seen on stage at the Theatre Royal, Drury Lane, first playing various ensemble roles and then taking over the part of Frodo Baggins in Matthew Warchus' theatrical adaption of "The Lord of the Rings".  In 2008-09 Byng appeared in the role of John Darling in the musical "Peter Pan" at the West Yorkshire Playhouse in Leeds.  He just finished a tour with the West Yorkshire Playhouse production of "The History Boys" by Alan Bennet, in which he played Posner.  From September until November 2010 Byng was on tour with a production of "Carrie's War" in the role of Nick Willow.  After performing in "Secret Cinema - Back to the Future" he can currently be seen in "The Grimm Tales" at The Bargehouse at Oxo Tower Wharf.

Jonas Hurst: Jonas Hurst is a British singer, television presenter, trainer and theatrical producer.  He performed on "Minipops" and in the 1986 movie "Absolute Beginners" (credited as "Jonas").  He is the son of producer Mike Hurst.  Together with television presenter Sally Gray he runs a company called Presenters Inc, specializing in television presenter training and is a theatrical producer running The Hurst Children’s Theatre Group in Harpenden.  Together with Adrian Plunkett he forms a band called Jonas and Plunkett.  Jonas has six siblings and is a father of three.

Oscar Hammerstein II: Oscar Greeley Clendenning Hammerstein II ( ; July 12, 1895 – August 23, 1960) was an American librettist, theatrical producer, and (usually uncredited) theatre director of musicals for almost forty years.  Hammerstein won eight Tony Awards and two Academy Awards for Best Original Song.  Many of his songs are standard repertoire for vocalist's and jazz musicians.  He co-wrote 850 songs.  Hammerstein was the lyricist and playwright in his partnerships; his collaborators wrote the music.  Hammerstein collaborated with numerous composers, such as Jerome Kern, with whom he wrote "Show Boat", Vincent Youmans, Rudolf Friml, Richard A. Whiting and Sigmund Romberg; but he is best known for his collaborations with Richard Rodgers, as the duo Rodgers and Hammerstein which include "Oklahoma! ", "Carousel", "South Pacific", "The King and I", and "The Sound of Music".

Sunny (1941 film): Sunny is a 1941 film American film directed by Herbert Wilcox.  It was adapted by Sig Herzig from the Jerome Kern-Oscar Hammerstein II musical play "Sunny".  It stars Anna Neagle, Ray Bolger, John Carroll, Edward Everett Horton, Grace Hartman, Paul Hartman, Frieda Inescort, and Helen Westley.

Michael Reno: Michael Reno is an American composer, arranger, orchestrator, and theatrical producer who is a frequent collaborator of theatrical entrepreneur Peter Schneider.

Cameron Mackintosh: Sir Cameron Anthony Mackintosh (born 17 October 1946) is a British theatrical producer notable for his association with many commercially successful musicals.  At the height of his success in 1990, he was described as being "the most successful, influential and powerful theatrical producer in the world" by the "New York Times".  He is the producer of shows such as "Les Misérables", "The Phantom of the Opera", "Mary Poppins", "Oliver! ", "Miss Saigon" and "Cats.

Scott Sanders (producer): Scott Sanders (born 1957) is an American television producer, film producer and theatrical producer.  He is best known for the theatrical musical version of Alice Walker’s novel "The Color Purple", of which he was Lead Producer along with Oprah Winfrey, Quincy Jones, and Harvey Weinstein, for producing "Elaine Stritch: at Liberty" and the 2012 revival of the musical "Evita", and for his work on numerous musical and theatrical productions.

Philip Michael Faraday: Philip Michael Faraday (1 January 1875 – 6 February 1944) was an English lawyer, surveyor, composer, organist and theatrical producer.  He composed one of the last Savoy operas, staged several long-running shows in the West End of London, and wrote a book about local taxation that was for many years the standard work on the subject.  After sustaining financial losses on shows that he produced in the 1910s, Faraday declared bankruptcy in 1914.  In later years, however, he rebuilt his fortune through his legal and valuation work and resumed theatrical production.

Herman Shumlin: Herman Shumlin (December 6, 1898, Atwood, Colorado – June 4, 1979, New York City) was a prolific Broadway theatrical director and theatrical producer beginning in 1927 with the play "Celebrity" and continuing through 1974 with a short run of "As You Like It", notably with an all male cast.  He was also the director of two movies, including "Watch on the Rhine" (1943), which he first directed and produced on Broadway in 1941.

Question: Which theatrical producer co-created both "Sunny" and "Oklahoma!"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "producer_name": {
      "type": "string",
      "description": "The name of the theatrical producer."
    },
    "producer_role": {
      "type": "string",
      "description": "The primary role of the individual as a producer."
    },
    "co_created_works": {
      "type": "array",
      "description": "A list of works co-created by the producer.",
      "items": {
        "type": "string"
      }
    },
    "work_details": {
      "type": "array",
      "description": "Details about each co-created work, including collaborators and roles.",
      "items": {
        "type": "object",
        "properties": {
          "work_title": {
            "type": "string",
            "description": "The title of the co-created work."
          },
          "collaborator_name": {
            "type": "string",
            "description": "The name of the primary collaborator for this specific work."
          },
          "collaboration_type": {
            "type": "string",
            "description": "The type of work resulting from the collaboration (e.g., musical play, musical)."
          },
          "producer_contribution_role": {
            "type": "string",
            "description": "The specific role of the producer in the creation of this work (e.g., lyricist, playwright)."
          }
        },
        "required": [
          "work_title",
          "collaborator_name",
          "collaboration_type",
          "producer_contribution_role"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "producer_name",
    "producer_role",
    "co_created_works",
    "work_details"
  ],
  "additionalProperties": false
}
