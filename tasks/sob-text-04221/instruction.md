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
Bianca Chiminello: Bianca Chiminello (born 5 September 1976) is an Australian model and actress best known for her role as "Jenavian Charto" on the television series "Farscape".  Chiminello's breakout film performance is in the December 2008 release of David Fincher's "The Curious Case of Benjamin Button", starring Brad Pitt and Cate Blanchett.  Chiminello plays Blanchett's best friend.

Dastak (1996 film): Dastak (English: Knock) is a 1996 Hindi language Indian feature film directed by Mahesh Bhatt, starring Sushmita Sen in her debut film supported by Mukul Dev with Sharad Kapoor as the psychopath.

On Deadly Ground: On Deadly Ground is a 1994 environmental action-adventure film, directed, co-produced by and starring Steven Seagal, and co-starring Michael Caine, Joan Chen, and John C. McGinley, R. Lee Ermey.  It is, to date, Seagal's only directorial effort, and features a minor appearance by Billy Bob Thornton in one of his early roles.

Fight Club (disambiguation): Fight Club is a 1999 film directed by David Fincher and starring Brad Pitt, Edward Norton, and Helena Bonham Carter.  "Fight Club" may also refer to:

Seven (1995 film): Seven (sometimes stylized as SE7EN) is a 1995 American neo-noir crime thriller film directed by David Fincher and starring Brad Pitt, Morgan Freeman, Gwyneth Paltrow, John C. McGinley, R. Lee Ermey, and Kevin Spacey.  The film was based on a screenplay by Andrew Kevin Walker.  It tells the story of David Mills (Pitt), a young detective who is partnered with the retiring William Somerset (Freeman) and soon tasked with tracking down a serial killer (Spacey) who uses the seven deadly sins as tropes in his murders.

Austin Powers in Goldmember: Austin Powers in Goldmember is a 2002 American spy action comedy film.  It is the third and final installment of the "Austin Powers" trilogy starring Mike Myers in the title role.  The film was directed by Jay Roach, and co-written by Mike Myers and Michael McCullers.  Myers also plays the roles of Dr. Evil, Goldmember, and Fat Bastard.  The movie co-stars Beyoncé in her theatrical film debut, as well as Robert Wagner, Seth Green, Michael York, Verne Troyer, Michael Caine, Mindy Sterling and Fred Savage.  There are a number of cameo appearances including Steven Spielberg, Kevin Spacey, Britney Spears, Quincy Jones, Tom Cruise, Danny DeVito, Katie Couric, Gwyneth Paltrow, John Travolta, Nathan Lane, and The Osbournes.

Biwi No.1: Biwi No.1 (English: Wife No. 1 ) is a 1999 Indian Hindi comedy film directed by David Dhawan.  It stars Salman Khan, Karisma Kapoor, Sushmita Sen, Anil Kapoor and Tabu.  Saif Ali Khan has a special appearance.  It is remake of the 1995 Tamil film "Sathi Leelavathi".  The plot has inspired the 2005 comedy hit Kannada movie "Rama Shama Bhama" starring Kamal Hassan, Ramesh Aravind, Urvashi and Daisy Bopanna.  Biwi No.1 was the third title in the No. 1 (film series) directed by David Dhawan and starring Karisma Kapoor after "Coolie No.1" (1995) and "Hero No. 1" (1997).  It is also the only one of the three not to feature Govinda in the leading role.  Salman Khan replaced Govinda who had a disagreement with Sushmita Sen on the set and walked out of the film.

Interpretations of Fight Club: The 1999 American film "Fight Club", directed by David Fincher and starring Brad Pitt, Edward Norton, and Helena Bonham Carter, presents social commentary about consumerist culture, especially the feminization of American culture and its effects on masculinity.  The film has been the source of critical analysis.  Academics Jans B. Wager describes the film as retro-noir, while Keith Gandal defines it as a "slumming trauma".  Cultural critics Henry Giroux and Imre Szeman assert that "Fight Club" focuses too much on consumerist culture as society's problem.  Academic Robert von Dassanowsky describes "Fight Club" as an examination of European fascism.

Nirbaak: Nirbaak (English: Speechless ) (2015) is an Indian Bengali Drama film directed by Srijit Mukherji, starring Sushmita Sen, Jisshu Sengupta, Ritwick Chakraborty and Anjan Dutt.  As of August 2014, the shooting of the film is complete.  This is the first Bengali film for Sushmita Sen. The film was released in Kolkata on 1 May 2015 and 15 May 2015 across rest of India.

Samay: When Time Strikes: Samay: When Time Strikes is a 2003 thriller movie starring Sushmita Sen, and Sushant Singh.  It was inspired from Hollywood movie Se7en starring Morgan Freeman and Brad Pitt.

Question: Which thriller movie starring Sushmita Sen, and Sushant Singh was based on a film directed by David Fincher and starring Brad Pitt, Morgan Freeman, Gwyneth Paltrow, John C. McGinley, R. Lee Ermey, and Kevin Spacey?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "thriller_movie": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        },
        "genre": {
          "type": "string"
        },
        "main_actors": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "title",
        "release_year",
        "genre",
        "main_actors"
      ],
      "additionalProperties": false
    },
    "inspired_by_movie": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        },
        "director": {
          "type": "string"
        },
        "main_actors": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "title",
        "release_year",
        "director",
        "main_actors"
      ],
      "additionalProperties": false
    },
    "relationship_type": {
      "type": "string",
      "description": "Describes how the thriller movie relates to the inspired-by movie."
    }
  },
  "required": [
    "thriller_movie",
    "inspired_by_movie",
    "relationship_type"
  ],
  "additionalProperties": false
}
