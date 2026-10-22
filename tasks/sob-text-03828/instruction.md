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
Lois Greenfield: Lois Greenfield (born April 18, 1949) is an American photographer best known for her unique approach to photographing the human form in motion.  Born in NYC, she attended Hunter College Elementary School, the Fieldston School, and Brandeis University.  She majored in Anthropology and expected to become an ethnographic filmmaker but instead she became a photojournalist for local Boston newspapers.  She traveled around the world on various assignments as a photojournalist but her career path changed in the mid 1970s when she was assigned to shoot a dress rehearsal for a dance concert.  She has since specialized in photographing dancers not in performance, but in her photo studio as part of her exploration of the expressive potential of movement.  She has created countless classic images for the world’s most well known dance companies such as Alvin Ailey, Martha Graham, Merce Cunningham, Paul Taylor, Bill T. Jones/Arnie Zane Dance Company, and American Ballet Theatre.  Her work has been published in countless periodicals, and has been exhibited in museums and galleries around the world.  Based in New York City, she gives workshops and lectures in schools around the world.

Bill T. Jones: Bill T. Jones (born February 15, 1952) is an American artistic director, choreographer and dancer.  Jones has received numerous awards for his work and is the co-founder of the Bill T. Jones/Arnie Zane Dance Company.  He is Artistic Director of New York Live Arts, the company's home base, which hosts an annual curated season of performances and a range of other activities.

Janet Lilly: Janet Lilly (born August 15, 1957) is an American modern dancer and choreographer.  She was a principal dancer for Bill T. Jones and Arnie Zane's company from 1983–1991.  She currently serves as the Director of the UNCG College of Visual and Performing Arts, School of Dance at the University of North Carolina at Greensboro.  From 2012–2014 she the president of the Board of Directors of Iyengar Yoga National United States Association.

New York Live Arts: New York Live Arts [Live Arts] is a movement-focused arts organization in New York City that serves as the home of the Bill T. Jones/Arnie Zane Dance Company.  Its activities encompass commissioning, producing, and presenting works of dance, performance and music, together with allied education programming and services for artists.  Live Arts is located in New York City’s Chelsea neighborhood.  Its building features a 184-seat theater, rehearsal studios and offices.  The organization was formed in 2011 when Dance Theater Workshop [DTW] and the Bill T. Jones/Arnie Zane Dance Company merged.

Arnie Zane: Arnie Zane (September 26, 1948 – March 30, 1988) was an American photographer, choreographer, and dancer.  He is best known as the co-founder and co-artistic director of the Bill T. Jones/Arnie Zane Dance Company.

Arthur Aviles: Arthur Avilés (born 1963) is an American Bessie Award-winning dancer and choreographer of Puerto Rican descent.  Avilés was born in Queens, New York, and raised in Long Island and the Bronx.  He graduated from Bard College, a liberal arts college in Annandale-on-Hudson, New York.  After graduating from Bard, he became a member of the Bill T. Jones/Arnie Zane Dance Company, and toured internationally with the company for eight years 1987 to 1995.

Germaul Barnes: Germaul Barnes was born June 2, 1971 in Phoenix, Arizona where he studied at The Center of Performing Arts at South Mountain High School, Phoenix School of Ballet and Ballet Arizona.  Currently living in Brooklyn, New York and is the founder and artistic director of Viewsic Dance, a dance organization dedicated to the development of local and international contemporary dancers.  He continued his dance training at the University of the Arts-Philadelphia.  In the early part of his career, he performed with Bill T. Jones/Arine Zane Dance Company where he received the 2003 BESSIES -New York and Performance Award, Cleo Parker Robinson Dance Ensemble, Jose Tmim, Movement Source Dance Company, Group Motions Dance Company, Pacific Conservatory Theatre and as guest performer with numerous ballet and contemporary dance company worldwide.  He formed Viewsic Dance-VD (formerly Viewsic Expressions) in 1993 and has since created over 50 works for this project-by-project company.

Ronald K. Brown: Dancer and choreographer Ronald K. Brown founded the dance company Evidence in New York in 1985.  Brown's work incorporates modern dance, Senegalese Sabar and other West African movement vocabularies, Afro-Caribbean dance, and contemporary urban dance from around the world.  He has choreographed numerous works for his own company, as well as for Philadanco, Alvin Ailey American Dance Theater, the Jacob's Pillow Dance Festival, the Maimouna Keita West African Dance Company, and many others.  Brown has received numerous awards, including a Guggenheim Fellowship, a Bessie Award, a Black Theater Alliance Award, and an Audelco Award for the choreography of Regina Taylor's musical Crowns.  He has also been a guest artist at The Sharon Disney Lund School of Dance at CalArts.  He studied dance with Mary Anthony.

Bill T. Jones/Arnie Zane Dance Company: The Bill T. Jones/Arnie Zane Dance Company is an American dance company based out of Harlem in New York City.  Founded in 1983 by Bill T. Jones and Arnie Zane, the company made its debut performance at the Brooklyn Academy of Music with the world premiere of "Intuitive Momentum" with lauded drummer Max Roach.  The company has since drawn international acclaim, performing in more than 200 cities in 30 countries.

Helen Thorington: Helen Louise Thorington (born November 16, 1928 in Philadelphia, PA) is an American sound artist and writer.  She is also the founder of New Radio and Performing Arts (1981), a nonprofit organization based in New York City; the founder and executive producer of "New American Radio" (1987-1998); and the founder and co-director of Turbulence.org (1996-).  Thorington began composing in 1977; her first works were aired on National Public Radio on such programs as "Options", "Voices in the Wind", and "All Things Considered".  In 1978, she began composing music for dance, collaborating with Bill T. Jones, Arnie Zane, and Lois Welk.  She has performed nationally, including at Kennedy Center, Jacob's Pillow, Dance Theatre Workshop, and The Kitchen.  Thorington began creating Internet art in the mid-1990s, co-producing several multimedia, hypertext narratives and networked performances that culminated in an installation of the seminal work, "Adrift", at The New Museum in 2001.

Question: Who has received numerous awards for his work and is the co-founder of the Bill T. Jones/Arnie Zane Dance Company, and had the president of the Board of Directors of Iyengar Yoga National United States Association From 2012–2014 as a principal dancer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "identified_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person identified."
        },
        "is_co_founder_of_company": {
          "type": "boolean",
          "description": "Indicates if the person is a co-founder of the specified dance company."
        },
        "has_received_numerous_awards": {
          "type": "boolean",
          "description": "Indicates if the person has received numerous awards for their work."
        }
      },
      "required": [
        "name",
        "is_co_founder_of_company",
        "has_received_numerous_awards"
      ],
      "additionalProperties": false
    },
    "dance_company_details": {
      "type": "object",
      "properties": {
        "company_name": {
          "type": "string",
          "description": "The name of the dance company co-founded by the identified person."
        },
        "co_founders": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of co-founders of the dance company."
        }
      },
      "required": [
        "company_name",
        "co_founders"
      ],
      "additionalProperties": false
    },
    "related_dancer_details": {
      "type": "object",
      "properties": {
        "dancer_name": {
          "type": "string",
          "description": "The name of the principal dancer related to the identified person."
        },
        "role_in_company": {
          "type": "string",
          "description": "The role of the dancer in the company (e.g., principal dancer)."
        },
        "company_danced_for": {
          "type": "string",
          "description": "The name of the company the dancer performed for."
        },
        "presidency_details": {
          "type": "object",
          "properties": {
            "organization": {
              "type": "string",
              "description": "The name of the organization where the dancer held a presidency."
            },
            "start_year": {
              "type": "integer",
              "description": "The start year of the presidency."
            },
            "end_year": {
              "type": "integer",
              "description": "The end year of the presidency."
            }
          },
          "required": [
            "organization",
            "start_year",
            "end_year"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "dancer_name",
        "role_in_company",
        "company_danced_for",
        "presidency_details"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "identified_person",
    "dance_company_details",
    "related_dancer_details"
  ],
  "additionalProperties": false
}
