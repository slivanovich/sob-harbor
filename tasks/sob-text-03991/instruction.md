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
Truus Schröder-Schräder: Truus Schröder-Schräder (1889-1985) was a Dutch socialite and trained pharmacist who was closely involved with avant-garde artists and architects of the De Stijl movement.  Gerrit Rietveld and her built a house for her and her three children — the Rietveld Schröder House — which is today a UNESCO World Heritage Site.

Aubette (building): Aubette is a historical building on Place Kléber in Strasbourg, France.  It was built by Jacques-François Blondel in 1765–1772.  Between 1926 and 1928 it was redecorated by Sophie Taeuber-Arp, Jean Arp and De Stijl artist Theo van Doesburg.  The work of the three artists had been called "the Sistine Chapel of abstract art".

Film Guild Cinema: The Film Guild Cinema was a movie house designed by notable architectural theoretician and De Stijl member, Frederick Kiesler.  It was located at 52 W. 8th St. in Greenwich Village, New York City.  It was built in 1929.  It was renamed the 8th Street Playhouse a year later.

Robert van 't Hoff: Robert van 't Hoff (November 5, 1887 – April 25, 1979), born Robbert van 't Hoff, was a Dutch architect and furniture designer.  His "Villa Henny", designed in 1914, was one of the earliest modernist houses and one of the first to be built out of reinforced concrete.  From 1917 he was an influential member of the "De Stijl" movement.

Rietveld Schröder House: The Rietveld Schröder House (Dutch: "Rietveld Schröderhuis" ) (also known as the Schröder House) in Utrecht (Prins Hendriklaan 50) was built in 1924 by Dutch architect Gerrit Rietveld for Mrs. Truus Schröder-Schräder and her three children.

De Stijl: De Stijl ( ; ] ), Dutch for "The Style", also known as neoplasticism, was a Dutch artistic movement founded in 1917 in Leiden.  The De Stijl consisted of artists and architects.  In a narrower sense, the term "De Stijl" is used to refer to a body of work from 1917 to 1931 founded in the Netherlands.  Proponents of De Stijl advocated pure abstraction and universality by a reduction to the essentials of form and colour; they simplified visual compositions to vertical and horizontal, using only black, white and primary colors.

César Domela: César Domela (15 January 1900 – 30 December 1992) was a Dutch sculptor, painter, photographer, and typographer, and a key member of the De Stijl movement.

Joseph Csaky: Joseph Csaky (also written Josef Csàky, Csáky József, József Csáky and Joseph Alexandre Czaky) (18 March 1888 – 1 May 1971) was a Hungarian avant-garde artist, sculptor, and graphic artist, best known for his early participation as a sculptor in the Cubist movement.  Joseph Csaky was one of the first sculptors in Paris to apply the principles of pictorial Cubism to his art.  A pioneer of modern sculpture, Csaky is among the most important sculptors of the early 20th century.  He was an active member of the Section d'Or group between 1911 and 1914, and closely associated with De Stijl and Purism throughout the 1920s.

Jack Curtis Dubowsky: Jack Curtis Dubowsky is an American composer who has scored independent feature films and composed music for television, advertising, and concert performance.  His music has been performed by the San Francisco Choral Artists, the Lesbian/Gay Chorus of San Francisco, the Snopea Chamber Ensemble, the Organic Sound Experiment, and many others.  He has received grants from Meet the Composer (1998), the Zellerbach Family Fund (1997), and the Friends of the San Francisco Public Library (1997), and a "Special Recognition of a Score" jury award from the Fire Island Gay and Lesbian Film Festival (2002) for his work on the film "Under One Roof".  Dubowsky works through his music house, De Stijl Music.

Gerrit Rietveld: Gerrit Thomas Rietveld (] ; 24 June 1888 – 25 June 1964) was a Dutch furniture designer and architect.  One of the principal members of the Dutch artistic movement called De Stijl, Rietveld is famous for his Red and Blue Chair and for the Rietveld Schröder House, which is a UNESCO World Heritage Site.

Question: What is the name of the house built in 1924 by a principal member of the De Stijl?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "house_name": {
      "type": "string",
      "description": "The name of the house."
    },
    "year_built": {
      "type": "integer",
      "description": "The year the house was built."
    },
    "architect": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the architect."
        },
        "de_stijl_role": {
          "type": "string",
          "description": "The architect's role within the De Stijl movement."
        }
      },
      "required": [
        "name",
        "de_stijl_role"
      ],
      "additionalProperties": false
    },
    "location": {
      "type": "string",
      "description": "The city where the house is located."
    },
    "is_unesco_world_heritage_site": {
      "type": "boolean",
      "description": "Indicates if the house is a UNESCO World Heritage Site."
    }
  },
  "required": [
    "house_name",
    "year_built",
    "architect",
    "location",
    "is_unesco_world_heritage_site"
  ],
  "additionalProperties": false
}
