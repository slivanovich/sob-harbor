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
Stefan Effenberg: Stefan Effenberg (] ; born 2 August 1968) is a retired German footballer who last managed SC Paderborn.  A midfielder, he possessed leadership skills, fantastic passing range, powerful shooting ability, physical strength, but also a fearsome and controversial character.

2002–03 VfL Wolfsburg season: VfL Wolfsburg finished 8th in Bundesliga, qualifying for the UEFA Intertoto Cup.  The club got into the spotlight signing Bayern Munich star Stefan Effenberg, who finished his career with a season in the Volkswagen-owned club.  Elsewhere, Martin Petrov and Tomislav Marić had successful seasons, being pivotal in the European qualification.

Stefan Ritter: Stefan Ritter (born (1998--)13 1998 ) is a Canadian male track cyclist, representing Canada at international competitions.  He won the bronze medal at the 2016 Pan American Track Cycling Championships in the 1 km time trial and in the team sprint.  Ritter is the current (2016) UCI junior world champion in the 1 kilometer time trial.

Augustine of Canterbury: Augustine of Canterbury (born first third of the 6th century – died probably 26 May 604) was a Catholic Benedictine monk who became the first Archbishop of Canterbury in the year 597.  He is considered the "Apostle to the English" and a founder of the Catholic Church in England.

1991–92 A.C. Fiorentina season: Associazione Calcio Fiorentina failed to take off under former Brazilian national team coach Sebastião Lazaroni, and ended the season in 12th place.  The result prompted president Cecchi Gori to sign German starlet Stefan Effenberg among others for the coming season, also replacing Lazaroni with Luigi Radice.  The most significant event in Fiorentina's season was the arrival of Argentinian striker Gabriel Batistuta, who was to become Fiorentina's all-time topscorer during his nine years at the club.

List of Lab Rats characters: "Lab Rats", also known as "Lab Rats: Bionic Island" for its fourth season, is an American television sitcom that premiered on February 27, 2012, on Disney XD.  It focuses on the life of teenager Leo Dooley, whose mother, Tasha, marries billionaire genius Donald Davenport.  He meets Adam, Bree, and Chase, three bionic superhumans, with whom he develops an immediate friendship.  It should be noted that the names of the Lab Rats imply that they were originally known as subjects A, B, C and D. Adam was born first, then Bree, then Chase, and finally Daniel.

Donald &amp; Deborah Ritter: Donald and Deborah Ritter are fictional characters from Marvel Comics.  They are the twin children of Thena, leader of the Eternals, and Kro, sometime leader of the race of Deviants.  The Ritter twins were created by Roy Thomas, Dann Thomas and Mark Texeira.  The twins first appeared in the one-shot special "Eternals: The Herod Factor".

Thomas Ritter: Thomas Ritter (born 10 October 1967 in Görlitz) is a retired German footballer.  He played one game for Germany on 13 October 1993 in a friendly against Uruguay, as a substitute for Stefan Effenberg.

Wale Adebanwi: Professor Wale Adebanwi, (born 1969), is a Nigerian - born first Black African Rhodes Professor at Oxford University

Despoina: In Greek mythology, Despoina, Despoena or Despoine, was the daughter of Demeter and Poseidon and sister of Arion.  She was the goddess of mysteries of Arcadian cults worshipped under the title "Despoina", "the mistress" alongside her mother Demeter, one of the goddesses of the Eleusinian mysteries.  Her real name could not be revealed to anyone except those initiated to her mysteries.  Pausanias spoke of Demeter as having two daughters; Kore being born first, then later Despoina.  With Zeus being the father of Kore, and Poseidon as the father of Despoina.  Pausanias made it clear that Kore is Persephone, though he wouldn't reveal Despoina's proper name.

Question: Who was born first, Thomas Ritter or Stefan Effenberg?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a_name": {
      "type": "string",
      "description": "The name of the first person being compared."
    },
    "person_a_birth_date": {
      "type": "string",
      "description": "The birth date of the first person (YYYY-MM-DD format if possible)."
    },
    "person_b_name": {
      "type": "string",
      "description": "The name of the second person being compared."
    },
    "person_b_birth_date": {
      "type": "string",
      "description": "The birth date of the second person (YYYY-MM-DD format if possible)."
    },
    "first_born_person_name": {
      "type": "string",
      "description": "The name of the person who was born first."
    }
  },
  "required": [
    "person_a_name",
    "person_a_birth_date",
    "person_b_name",
    "person_b_birth_date",
    "first_born_person_name"
  ],
  "additionalProperties": false
}
