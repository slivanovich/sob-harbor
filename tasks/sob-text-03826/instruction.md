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
Margarita Magaña: Margarita Magaña (] ; born Margara Magaña Jiménez on July 25, 1979 in Mexico City, D.F., Mexico) is a Mexican actress and model, best known for her roles in the Mexican television series "Al diablo con los guapos", "Un gancho al corazón", and "Teresa".

Toluca: Toluca ] , officially called Toluca de Lerdo ] , is the state capital of State of Mexico as well as the seat of the Municipality of Toluca.  It is the center of a rapidly growing urban area, now the fifth largest in Mexico.  It is located 63 km west-southwest of Mexico City, about 40 minutes by car to the western edge of the city.  According to the 2010 census, the city of Toluca has a population of 819,561.  The city is the fifth largest in Mexico in population.  The municipality of Toluca, along with thirteen other municipalities, make up the metropolitan population of 1,775,337 in Greater Toluca as of 2009 , making it the fifth most populous metropolitan area in Mexico.

Mayrín Villanueva: Mayrín Villanueva (born Mayrín Villanueva Ulloa on October 8, 1970, in Toluca, México, Mexico) is a Mexican actress and model.

Universidad Autónoma del Estado de México: The Universidad Autónoma del Estado de México (UAEM) (Autonomous University of Mexico State) is a public university in the State of Mexico, Mexico.  It is the largest university institution in the state with over 84,500 students, with its central campus located in the state capital of Toluca.  Formalised as a university under the UAEM name in 1956, the institution traces its origins back to 1828 with the foundation Instituto Literario del Estado de México, in the former state capital of Tlalpan.  In 1943 the institution was augmented to become the Instituto Científico y Literario de Toluca (ICLA), and thirteen years later obtaining its present name and institutional status.  The UAEM has graduated many notable alumni, the best-known is the artist Mariana Galán.

Adriana Nieto: Adriana Nieto (born Adriana Nieto Villanueva on March 13, 1978) is a semi-retired Mexican actress.

Altaír Jarabo: Altaír Jarabo (born Altaír Jarabo García on August 7, 1986, in Mexico City, Mexico) is a Mexican actress and fashion model.  Best known for co-starring in antagonistic roles in Mexican telenovelas such as "Súbete A Mi Moto" (2002), "Inocente de Ti" (2004), "Código Postal" (2006), "Pecados Ajenos" (2007), "Al Diablo con los Guapos" (2007), "En Nombre del Amor (2008)", "Mi pecado (2009)", "Llena de amor (2010)", "Abismo de pasión (2012)" and "Mentir para vivir (2013)" and recently "Que te perdone Dios (2015)".

Galilea Montijo: Galilea Montijo (born Martha Galilea Montijo Torres on June 5, 1973 in Guadalajara, Jalisco, Mexico) is a Mexican actress, comedian, model and TV presenter.  She currently hosts "Hoy", a morning show of Televisa that airs on Mondays through Fridays in Mexico (on Canal de las Estrellas) and in the United States (on Univision).  Montijo hosted the talent-reality show "Pequeños Gigantes", which was a success in Mexico and in the United States (again shown by Univision) in its 1st and 2nd editions (2011 and 2012 respectively).  In 2014, she hosted "Va Por Ti" - a co-production of Univision and Televisa that first aired on Univision, beating the competition in the ratings.  In 2015, she hosts "Me Pongo De Pie" that will air in Mexico and United States.

Danny Villanueva: Daniel Dario Villanueva (November 5, 1937 – June 18, 2015) was an American football professional player, television and Major League Soccer executive.  Villanueva was a placekicker and punter who played in the National Football League (NFL) for the Los Angeles Rams and the Dallas Cowboys.  Villanueva, who was of Mexican American descent, played college football at New Mexico State University.

Angélica Vale: Angélica Vale (born Angélica María Vale Hartman on November 11, 1975 in Mexico City, Mexico) is a Mexican actress, singer, and comedian known also as the daughter of Angélica María, "La Novia de Mexico" (Mexico's Sweetheart), and as the daughter of comedian Raúl Vale.  She has been working as an actress for almost 30 years, but achieved fame in 2006 when she became the protagonist of "La Fea Más Bella" ("The Prettiest Ugly Girl"), a Mexican telenovela, with her real-life mother.  She starred in the webnovela "No me hallo" as Luchita Guerra a young woman with a big dream of becoming a singer.  Early in 2012, Vale was a team captain on the Mexican TV Show "Parodiando", of Televisa network.

Una familia con suerte: Una familia con suerte (A Fortunate Family) is a Mexican telenovela produced by Juan Osorio for Televisa.  It is based on the Argentinean telenovela "Los Roldán".  Luz Elena Gonzalez, Mayrín Villanueva and Arath De La Torre star as the main protagonists.  while Sergio Sendel, Daniela Castro, Cecilia Galliano with the special participations of the first actors María Rubio, Enrique Rocha and Patricia Reyes Spíndola stars as the main antagonists.  "Una familia con suerte" won 4 awards in Premios TVyNovelas: Best young lead actor, best male & female revelation, and best musical theme.

Question: Mayrín Villanueva is a Mexican actress and model from what state capital of the State of Mexico?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The full name of the actress."
    },
    "profession": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The professions of the actress."
    },
    "birth_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the actress was born."
        },
        "state": {
          "type": "string",
          "description": "The state where the actress was born."
        },
        "country": {
          "type": "string",
          "description": "The country where the actress was born."
        },
        "is_state_capital": {
          "type": "boolean",
          "description": "Indicates if the birth city is a state capital."
        }
      },
      "required": [
        "city",
        "state",
        "country",
        "is_state_capital"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "profession",
    "birth_location"
  ],
  "additionalProperties": false
}
