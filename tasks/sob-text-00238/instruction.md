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
Ballet Manila: Ballet Manila is a classical ballet institution and dance company in the Philippines.  It currently highlights more than fifty highly trained dancers in the highly rigorous Russian (Vaganova) method of classical ballet.  Locally the company has performed in 47 cities holding more than 4,100 performances.  The company has done tours in Asia, Europe and North America, where it has held more than 140 performances.  The company is most notable for its in-house creative director, principal dancer and prima ballerina Lisa Macuja-Elizalde.  Along with Ballet Philippines and the Philippine Ballet Theatre, Ballet Manila is one of the three major ballet companies in the Philippines.  It regularly holds its performances at the Aliw theater and Star Theater, which are both located within Star City at Pasay City.  The concept of a ballet company by the dancers, of the dancers and for the dancers was the idea of Lisa Macuja-Elizalde when she, along with ballet master Osias Barroso and ten other dancers established Ballet Manila in 1995.

Elza Leimane: Elza Leimane (born 2 July 1984) is a Latvian ballet dancer.  She graduated from the Riga Choreography School in 2001 and has been a member of the Latvian National Ballet Company since her graduation.  She has been a principal dancer with the company since 2004.  Elza has had additional ballet training from the Paris Conservatoire (1999), Anaheim Ballet summer courses, USA (1999), International Batrolin Ballet seminar (2002 and 2003), Vienna Conservatory summer courses (2000), the St Petersburg Ballet Company, Maryinsky Theatre and Hamburg Ballet.  She was a member of the European Youth Ballet in 2000, 2001 and 2004.

Irek Mukhamedov: Irek Mukhamedov OBE (born March 8, 1960 in Kazan, USSR), is a Soviet-born ballet dancer of Tatar origin who has danced with the Bolshoi Ballet & the Royal Ballet He trained at the Moscow Choreographic Institute under the guidance of Alexander Prokofiev between 1970 and 1978.  Upon graduation he joined the Classical Ballet Company, where he spent three years touring around the world.  It was with this company that he first danced Romeo, a role that was to become one of his most acclaimed.  In 1981 he won the Grand Prix and Gold Medal at the International Ballet Competition in Moscow and was immediately invited to join the Bolshoi Ballet as a principal dancer, where he not only became Grigorovich's favourite danseur but went to become the youngest man ever to dance the leading role in "Spartacus".  After leaving the Soviet Union, he became a Senior Principal Dancer with the Royal Ballet in London, remaining with the company for many years and dancing lead roles in the classic ballets as well as the English repertoire.

Carolina Ballet: Carolina Ballet is a ballet company founded in 1997 which performs primarily in Raleigh, North Carolina and throughout the state.  It has toured to New York City, Hungary and China.  Robert Weiss, the artistic director, danced for George Balanchine for sixteen years at New York City Ballet and attained the rank of principal dancer.  Lynne Taylor-Corbett is principal guest choreographer.  One of Carolina Ballet's most popular performances, The Nutcracker, is performed annually.  Carolina Ballet currently has about 35 dancers.

Alicia Markova: Dame Alicia Markova DBE (1 December 1910 – 2 December 2004) was an English ballerina and a choreographer, director and teacher of classical ballet.  Most noted for her career with Sergei Diaghilev's Ballets Russes and touring internationally, she was widely considered to be one of the greatest classical ballet dancers of the twentieth century.  She was the first British dancer to become the principal dancer of a ballet company and, with Dame Margot Fonteyn, is one of only two English dancers to be recognised as a prima ballerina assoluta.  Markova was a founder dancer of the Rambert Dance Company, The Royal Ballet and American Ballet Theatre, and was co-founder and director of the English National Ballet.

Anna Antonicheva: Anna Antonicheva (Russian: Анна Анатольевна Антоничева ) is a ballerina and People's Artist of Russia, who was a principal dancer of Bolshoi Ballet.

Michele Wiles: Michele Wiles is an American ballet dancer.  She was a principal dancer with American Ballet Theatre from 2005 - 2011.  In 2011, she left ABT to form the independent classical ballet company Ballet Next with former New York City Ballet principal dancer Charles Askegard.

Johan Kobborg: Johan Kobborg (born 5 June 1972) is a Danish ballet dancer, choreographer, director and visual artist.  He is most noted as a ballet dancer, having been a principal dancer with both the Royal Danish Ballet and the Royal Ballet in London, as well as making guest appearances with other ballet companies.  Following his departure from the Royal Ballet in 2013, he became the director of the Romanian National Ballet Company.

Bolshoi Ballet: The Bolshoi Ballet is an internationally renowned classical ballet company, based at the Bolshoi Theatre in Moscow, Russian Federation.  Founded in 1776, the Bolshoi is among the world's oldest ballet companies.  It only achieved worldwide acclaim, however, in the early 20th century when Moscow became the capital of Soviet Russia.  Along with the Mariinsky Ballet in Saint Petersburg, the Bolshoi is recognised as one of the foremost ballet companies in the world.

César Morales (dancer): César Morales Anderson (born 17 November 1978) is a Chilean ballet dancer who, as of February 2014, is a principal dancer with the Birmingham Royal Ballet.  Born in Rancagua, Chile, César Morales began dancing at the age of eleven at the Ballet School of the Municipal Theatre of Santiago, where he trained for three years before being offered a scholarship by Ben Stevenson to train at the academy of Houston Ballet.  He returned to Santiago at the age of fifteen to complete his training and Ivan Nagy offered him a contract to join the Ballet de Santiago.  After a year in the Corps de Ballet, he was promoted to soloist and a year later to principal dancer immediately after his first performance of "Swan Lake".  Morales danced with the Ballet de Santiago until 2003, when he moved to Paris to work as a freelance guest artist, dancing in Paris, Slovenia and the Czech Republic.  He went on to join the English National Ballet in 2004, was Principal Guest Artist with Vienna Staatsoper in 2006 and then joined the Birmingham Royal Ballet in 2008.

Question: What year was the ballet company founded in which Anna Antonicheva was a principal dancer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "principal_dancer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the principal dancer."
        },
        "role": {
          "type": "string",
          "description": "The role of the dancer in the company."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "ballet_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the ballet company."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the ballet company was founded."
        }
      },
      "required": [
        "name",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "question_answer": {
      "type": "integer",
      "description": "The founding year of the ballet company where the principal dancer performed."
    }
  },
  "required": [
    "principal_dancer",
    "ballet_company",
    "question_answer"
  ],
  "additionalProperties": false
}
